let url = `ws://${window.location.host}/ws/current-date/`
const socket = new WebSocket(url);

socket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    console.log('data: ', data)

    if (data.type === "current_date") {
        let currentDate = document.getElementById('current_date')
        current_date.innerHTML = `${data.message}`
    }
};