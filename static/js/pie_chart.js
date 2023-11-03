// custom.js
document.addEventListener('DOMContentLoaded', function () {
    var labels = {{ labels|tojson }};
    var values = {{ values|tojson }};

    // Initialize date pickers
    $('.datepicker').datepicker({
        format: 'yyyy-mm-dd',
        autoclose: true,
    });

    // Function to update the chart based on user input
    function updateChart() {
        var start_time = document.getElementById('start-time').value;
        var end_time = document.getElementById('end-time').value;

        if (start_time > end_time) {
            alert('Start date cannot be greater than end date.');
            return;
        }

        // Send an AJAX request to update_chart endpoint with new start and end times
        fetch('/update_chart', {
            method: 'POST',
            body: new URLSearchParams({ start_time, end_time }),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        })
            .then(response => response.json())
            .then(data => {
                labels = data[0];
                values = data[1];

                // Create the nested pie chart
                var data = [{
                    labels: labels,
                    values: values,
                    type: 'pie',
                }];

                Plotly.newPlot('nested-pie-chart', data);
            })
            .catch(error => console.error('Error:', error));
    }

    // Initialize the nested pie chart
    var data = [{
        labels: labels,
        values: values,
        type: 'pie',
    }];

    Plotly.newPlot('nested-pie-chart', data);

    // Attach event listener to the "Update Chart" button
    document.getElementById('update-chart').addEventListener('click', updateChart);
});
