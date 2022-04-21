let url = `ws://${window.location.host}/ws/streams/`
const socket = new WebSocket(url);

socket.onmessage = function (e) {
    const data = JSON.parse(e.data);

    if (data.type === "streams") {
        let streamsList = document.getElementById('streams_list');
        streamsList.innerHTML = "";

        data.message.forEach((e) => {
            streamsList.insertAdjacentHTML('beforeend', `
                <div class="col-12 col-md-6 col-lg-4 p-2">
                    <div class="card">
                        <a class="position-relative" href="${e.url}" target=”_blank”>
                            <img src="${e.thumbnail_url}" class="card-img-top" alt="...">
                            <span class="m-2 position-absolute bottom-0 start-0 badge bg-dark">
                                ${e.viewer_count}
                                <span class="visually-hidden">viewer count</span>
                            </span>
                        </a>
                        <div class="card-body">
                            <h5 class="card-title text-truncate">${e.title}</h5>
                            <p class="card-text text-truncate">${e.user_name}</p>
                            <span class="badge bg-secondary">tag</span>
                        </div>
                    </div>
                </div>
            `);
        });
    }
};