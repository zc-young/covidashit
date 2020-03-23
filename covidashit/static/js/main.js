let url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json";
$(document).ready(function () {
    $(chart_id).highcharts({
        chart: chart,
        title: title,
        xAxis: xAxis,
        yAxis: yAxis,
        series: series,
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
        subtitle: {
            text: ('Source: <a href="' + url + '">Protezione Civile</a>'),
            align: "left"
        },
        credits: {
            href: "https://fabriziomiano.github.io",
            text: "by Fabrizio Miano"
        },
    });
});
