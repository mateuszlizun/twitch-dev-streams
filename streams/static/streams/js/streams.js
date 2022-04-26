let url = `ws://${window.location.host}/ws/streams/`;
const socket = new WebSocket(url);

let currentFilter = "";

socket.onmessage = function (e) {
    const data = JSON.parse(e.data);

    if (data.type == "streams") {
        let streamsList = document.getElementById('streams_list');
        streamsList.innerHTML = "";

        data.message.forEach((e) => {
            let tags = "";
            if (e.tags_names.length) {
                e.tags_names.forEach(t => tags += `<span class="badge bg-secondary">` + t + `</span>\n`);
            } else {
                tags = `<span class="badge"><span class="d-none">...</span></span>`;
            }

            streamsList.insertAdjacentHTML('beforeend', `
                <div data-title="${e.title}" data-tags="${e.tags_codes}"
                    class="col-12 col-md-6 col-lg-4 p-2 stream-container ${streamTagsIncludesFilter(e.tags_codes) ? `` : `d-none`}">
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
                            <p class="card-text text-truncate">${e.user_name}</p>`
                + tags
                + `</div>
                    </div>
                </div>
            `);
        });
    }
};

function streamTagsIncludesFilter(tags) {
    if (currentFilter == "all") {
        return true;
    }

    if (!tags.length) {
        return false;
    }

    return tags.includes(currentFilter);
}

function filterStreams(filter) {
    currentFilter = filter;
    let streams = document.getElementsByClassName('stream-container');

    [...streams].forEach(element => {
        element.classList.remove("d-none");

        if (!streamTagsIncludesFilter(element.dataset.tags)) {
            element.classList.add("d-none");
        }
    });
}