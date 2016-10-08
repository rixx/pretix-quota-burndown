from datetime import timedelta
import json

from django.db.models import Q
from django.dispatch import receiver
from django.template.loader import get_template

from pretix.base.models import Order, OrderPosition, Quota
from pretix.base.signals import order_paid, order_placed
from pretix.control.signals import quota_detail_html


@receiver(quota_detail_html, dispatch_uid='quota_burndown')
def quota_burndown(sender, quota, **kwargs):
    cache = sender.get_cache()
    date_list = cache.get('quotaburndown_data_{}'.format(quota.name)) or []

    if not date_list:
        qs = OrderPosition.objects\
            .filter(quota._position_lookup)\
            .order_by('order__datetime')

        if not qs.exists():
            return ''

        first_day = qs.first().order.datetime.date()
        last_day = qs.last().order.datetime.date()
        duration = last_day - first_day

        baseline = quota.count_blocking_vouchers()

        for date in (first_day + timedelta(n) for n in range(duration.days + 1)):
            date_list.append({
                'date': date.strftime('%Y-%m-%d'),
                'quota_used': qs.filter(
                    Q(Q(order__status=Order.STATUS_PAID) | Q(order__status=Order.STATUS_PENDING)) &
                    Q(order__datetime__lte=date)
                ).distinct().count() + baseline,
            })
        cache.set('quotaburndown_data_{}'.format(quota.name), date_list)

    template = get_template('quotaburndown/quota_detail.html')
    return template.render(context={'data': json.dumps(date_list)})


def clear_cache(sender, **kwargs):
    cache = sender.get_cache()
    for quota in Quota.objects.all().values_list('name', flat=True):
        cache.delete('quotaburndown_data_{}'.format(quota))

order_placed.connect(clear_cache)
order_paid.connect(clear_cache)
