// code based on
//https://github.com/tdiethe/flask-live-charts

// Author :  Juan Pablo Ramirez G
// Date : July 4, 2017

/**
 * Request data from the server, add it to the graph and set a timeout
 * to request again
 */

var chart;
function requestData() {
    $.ajax({
        url: '/live-data',
        success: function(point) {
            var series = chart.series[0],
                shift = series.data.length > 20; // shift if the series is
                                                 // longer than 20
                                                 //step between point to point

            // add the point
              chart.series[0].addPoint(point, true, shift);
              console.log(point)

            // call it again after one second
            setTimeout(requestData, 1000);
        },
        cache: false
    });
}

$(document).ready(function() {
  // show time in Colombia
  Highcharts.setOptions({
    global: {
        timezoneOffset: 5 * 60
    }
  });
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container',
            defaultSeriesType: 'spline',
            events: {
                load: requestData
            }
        },
        title: {
            text: 'Sensed Temperature in Medellin'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {

            min: 5, max: 40 ,
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Temperature',
                margin: 80
            }
        },
        series: [{
            name: 'Temperature',
            data: []
        }]
    });
});
