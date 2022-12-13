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


def _calculate_size(obj: any) -> int:

    if isinstance(obj, str):
        return _str_size(obj) + 1
    elif isinstance(obj, bool):
        return 1
    elif isinstance(obj, int) or isinstance(obj, float):
        return 8
    elif isinstance(obj, datetime):
        return 8

    return 0


def document_size(document: any) -> int:
    additional_document_size = (
        32  # https://firebase.google.com/docs/firestore/storage-size#document-name-size
    )
    return additional_document_size + _calculate_size(document)
