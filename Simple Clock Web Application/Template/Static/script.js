function updateTime() {
    fetch("/get_time")
        .then(response => response.json())
        .then(data => {
            document.getElementById("time").innerText = data.time;
        });
}

setInterval(updateTime, 1000);
updateTime();
