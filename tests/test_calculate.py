from firestore_size.calculate import document_size


def test_document_size():
    additional_document_size = (
        32  # https://firebase.google.com/docs/firestore/storage-size#document-name-size
    )

    # check if basic document size is calculated correctly
    assert document_size({}) == additional_document_size
    assert document_size("abc") == additional_document_size + 4
    assert document_size(123) == additional_document_size + 8
    assert document_size(True) == additional_document_size + 1

    # check for diffrent types of strings
    assert document_size("åß∂ƒ") == additional_document_size + 10
    assert document_size("ثبهخنى") == additional_document_size + 13
    assert document_size("你好") == additional_document_size + 7
    assert document_size("ха ха...шутка что ли?") == additional_document_size + 36

    # check for None and None in list and dict
    assert document_size(None) == additional_document_size + 1
    assert document_size({"abc": None}) == additional_document_size + 5
    assert document_size(["abc", None]) == additional_document_size + 5
