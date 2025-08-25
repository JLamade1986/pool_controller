let phChart = new Chart(document.getElementById("chartPh"), {
    type: 'line',
    data: { labels: [], datasets: [{ label: 'pH', data: [], borderColor: 'blue' }] }
});

let orpChart = new Chart(document.getElementById("chartOrp"), {
    type: 'line',
    data: { labels: [], datasets: [{ label: 'ORP (mV)', data: [], borderColor: 'red' }] }
});

setInterval(() => {
    fetch("/api/data").then(r => r.json()).then(data => {
        document.getElementById("ph").innerText = data.ph;
        document.getElementById("orp").innerText = data.orp;
        document.getElementById("pump").innerText = data.pump ? "ON" : "OFF";

        let now = new Date().toLocaleTimeString();
        phChart.data.labels.push(now);
        phChart.data.datasets[0].data.push(data.ph);
        if (phChart.data.labels.length > 20) {
            phChart.data.labels.shift();
            phChart.data.datasets[0].data.shift();
        }
        phChart.update();

        orpChart.data.labels.push(now);
        orpChart.data.datasets[0].data.push(data.orp);
        if (orpChart.data.labels.length > 20) {
            orpChart.data.labels.shift();
            orpChart.data.datasets[0].data.shift();
        }
        orpChart.update();
    });
}, 5000);
