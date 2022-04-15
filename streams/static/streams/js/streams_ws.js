let url = `ws://${window.location.host}/ws/streams/`
const socket = new WebSocket(url);

socket.onmessage = function (e) {
    const data = JSON.parse(e.data);

    if (data.type === "streams") {
        let streamsList = document.getElementById('streams_list')
        streamsList.innerHTML = ""

        data.message.forEach((e) => {
            streamsList.insertAdjacentHTML('beforeend', `<p>${e.title}</p>`);
        });
    }
};