from ..Encodings import encodeURIComponentAll

HTTP_HOST_URL = "http://reflect.ahh.bet/#"
HTTPS_HOST_URL = "https://reflect.ahh.bet/#"


def https_host(src: str) -> str:
    """
    Takes an HTML source string, returns an HTTPS url.
    Hosts page on "https://reflect.ahh.bet/".
    Returns url of hosted page.
    """

    html = encodeURIComponentAll(src)
    return f"{HTTPS_HOST_URL}{html}"


def http_host(src: str) -> str:
    """
    Takes an HTML source string, returns an HTTPS url.
    Hosts page on "http://reflect.ahh.bet/".
    Returns url of hosted page.
    """
    html = encodeURIComponentAll(src)
    return f"{HTTP_HOST_URL}{html}"


__all__ = ["http_host", "https_host"]