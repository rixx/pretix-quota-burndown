/*globals $, Morris, gettext*/
$(function () {
    $(".chart").css("height", "250px");
    new Morris.Area({
        element: 'quota_burndown_chart',
        data: JSON.parse($("#quota-data").html()),
        xkey: 'date',
        ykeys: ['available'],
        labels: [gettext('Quota availability')],
        smooth: false,
        resize: true,
        fillOpacity: 0.3,
        behaveLikeLine: true
    });
});
