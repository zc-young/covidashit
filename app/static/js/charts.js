let chartTrendOptions = {
    chart: {
        type: 'line',
        zoomType: 'x'
    },
    title: title,
    xAxis: xAxis,
    yAxis: yAxis,
    series: series,
    tooltip: {
        crosshairs: {
            width: 1,
            color: 'gray',
            dashStyle: 'ShortDashDot'
        },
        shared: true,
        split: false,
        enabled: true
    },
    exporting: {
        buttons: {
            linScale: {
                text: 'Lin',
                onclick: function () {
                    this.yAxis[0].update({
                        type: 'linear'
                    });
                }
            },
            logScale: {
                text: 'Log',
                onclick: function () {
                    this.yAxis[0].update({
                        type: 'logarithmic'
                    });
                }
            },
        }
    },
    subtitle: subtitle,
    credits: credits,
    plotOptions: {
        series: {
            visible: false
        }
    }
}

let chartIacopoOptions = {
    chart: {
        type: 'scatter',
        zoomType: 'x'
    },
    legend: {
        enabled: false
    },
    title: title,
    subtitle: subtitle,
    xAxis: scatterXAxis,
    yAxis: scatterYAxis,
    plotOptions: {
        scatter: {
            marker: {
                radius: 3,
                states: {
                    hover: {
                        enabled: true,
                        lineColor: 'rgb(100,100,100)'
                    }
                }
            },
            states: {
                hover: {
                    marker: {
                        enabled: false
                    }
                }
            },
        }
    },
    tooltip: {
        crosshairs: {
            width: 1,
            color: 'gray',
            dashStyle: 'ShortDashDot'
        },
        shared: true,
        split: false,
        enabled: true
    },
    exporting: {
        buttons: {
            linScale: {
                text: 'Lin',
                onclick: function () {
                    this.yAxis[0].update({
                        type: 'linear'
                    });
                }
            },
            logScale: {
                text: 'Log',
                onclick: function () {
                    this.yAxis[0].update({
                        type: 'logarithmic'
                    });
                }
            },
        }
    },
    series: [scatterData],
    credits: credits
}

let chartTrend = Highcharts.chart('chart-trend', chartTrendOptions);

$(document).ready(function () {
    if (!window.location.href.includes("provinces")) {
        $("#chart-iacopo").highcharts(chartIacopoOptions);
    }
});

function dataTypeSelector(value) {
    if (value !== "default") {
        for (let i = 0; i < chartTrend.series.length; i++) {
            if (chartTrend.series[i].name === value) {
                chartTrend.series[i].show()
            } else {
                chartTrend.series[i].hide()
            }
        }
    }
}

function playBCR(bcr_id) {
    $('#loadBCRButtonLoader' + bcr_id).removeAttr('hidden')
    $('#loadBCRButton' + bcr_id).attr('hidden', true)
    $.ajax({
        url: '/api/bcr/' + bcr_id,
        method: 'get',
        success: function (response) {
            console.log(response)
            if (response["status"] === "ok") {
                $("#bcrCard" + bcr_id).append(response["html_str"])
                $("#bcrts" + bcr_id).append(response["ts"]).removeAttr('hidden')
            }
            else {
                $("#bcrCard" + bcr_id).append(response["error"])
                $("#bcrts" + bcr_id).append(response["error"]).removeAttr('hidden')
            }
            $("#loadBCRButtonLoader" + bcr_id).attr("hidden", true)
        }
    })
}

let totPosStrIT = "Totale Positivi";
let totPosStrEN = "Total Positive";
(function ($) {
    "use strict";
    $(function () {
        for (let i = 0; i < series.length; i++) {
            if (series[i].name === totPosStrEN || series[i].name === totPosStrIT) {
                chartTrend.series[i].show()
            }
        }
    })
})(jQuery);
