from datetime import datetime


def _str_size(s: str):
    s_size = len(s)

    i = s_size - 1
    while i >= 0:
        ascii_code = ord(s[i])

        if ascii_code > 0x7F and ascii_code <= 0x7FF:
            s_size += 1
        elif ascii_code > 0x7FF and ascii_code <= 0xFFFF:
            s_size += 2

        i -= 1

    return s_size


def _object_size(obj: any) -> int:
    if obj is None:
        return 1

    if hasattr(obj, "_bytes"):
        # is a Blob
        return len(obj._bytes)

    # check if obj is reference to another firestore snapshot document
    if hasattr(obj, "on_snapshot") and callable(obj.on_snapshot):
        return 16 + sum([len(segment) + 1 for segment in obj._key._path._segments])

    if isinstance(obj, list):
        return sum([_calculate_size(item) for item in obj])

    if isinstance(obj, set):
        return sum([_calculate_size(item) for item in obj])

    if isinstance(obj, tuple):
        return sum([_calculate_size(item) for item in obj])

    if isinstance(obj, dict):
        return sum(
            [
                _calculate_size(key) + _calculate_size(value)
                for key, value in obj.items()
            ]
        )

    if hasattr(obj, "_lat") or hasattr(obj, "latitude"):
        # is a GeoPoint
        return 16

    return 0


def _calculate_size(obj: any) -> int:

    if isinstance(obj, str):
        return _str_size(obj) + 1
    elif isinstance(obj, bool):
        return 1
    elif isinstance(obj, int) or isinstance(obj, float):
        return 8
    elif isinstance(obj, datetime):
        return 8
    else:
        return _object_size(obj)


def document_size(document: any) -> int:
    additional_document_size = (
        32  # https://firebase.google.com/docs/firestore/storage-size#document-name-size
    )
    return additional_document_size + _calculate_size(document)
