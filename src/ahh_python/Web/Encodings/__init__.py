from urllib.parse import quote as _quote
from urllib.parse import unquote as _unquote
from html import escape as he_encode
from html import unescape as he_decode


def encodeURIComponent(uriComponent):
    return _quote(uriComponent, safe="!'()*")


def encodeURIComponentAll(uriComponent):
    return _quote(uriComponent, safe="")


def decodeURIComponent(encodedURI):
    return _unquote(encodedURI)


__all__ = [
    "encodeURIComponent",
    "encodeURIComponentAll",
    "decodeURIComponent",
    "he_encode",
    "he_decode",
]
