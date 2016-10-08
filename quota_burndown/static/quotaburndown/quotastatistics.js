/*globals $, Morris, gettext*/
$(function () {
    $(".chart").css("height", "250px");
    new Morris.Area({
        element: 'quota_burndown_chart',
        data: JSON.parse($("#quota-data").html()),
        xkey: 'date',
        ykeys: ['quota_used'],
        labels: [gettext('Quota usage')],
        smooth: false,
        resize: true,
        fillOpacity: 0.3,
        behaveLikeLine: true
    });
});
