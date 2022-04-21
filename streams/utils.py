def replace_stream_thumbnail_url(stream):
    stream["thumbnail_url"] = stream["thumbnail_url"].replace(
        "{width}x{height}", "440x248"
    )

    return stream


def set_stream_url(stream):
    stream["url"] = "https://www.twitch.tv/" + stream["user_login"]

    return stream


def set_stream_properties(stream):
    stream = replace_stream_thumbnail_url(stream)
    stream = set_stream_url(stream)

    return stream
