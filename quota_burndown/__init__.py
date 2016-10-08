from django.apps import AppConfig
from pretix.base.plugins import PluginType


class QuotaBurndownApp(AppConfig):
    name = 'quota_burndown'
    verbose_name = "Quota Burndown"

    class PretixPluginMeta:
        name = 'Quota Burndown'
        author = 'Tobias Kunze'
        description = 'Shows burndown charts for quotas and tries availability predictions'
        visible = True
        version = '0.1'
        type = PluginType.ADMINFEATURE

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'quota_burndown.QuotaBurndownApp'
