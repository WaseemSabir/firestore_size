# firestore_size
[![Tests](https://github.com/WaseemSabir/firestore_size/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/WaseemSabir/firestore_size/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Python library to calculate the approximate size of a firestore document. This can be used for firebase storage cost analysis, among other things.

## Installation
```bash
pip install firestore_size
```

## Usage
```bash
from firestore_size.calculate import document_size

# initialize firebase and firestore client

collection = db.collection("data")
doc = collection.doc(id).get()
data = doc.to_dict()

doc_size = document_size(data)
print("Doc Size is ", doc_size)
```

## How it calculates?

Checkout how the size of firestore docs is calculated in [documentation](https://firebase.google.com/docs/firestore/storage-size#document-name-size). 

Brief description is
- Array -	The sum of the sizes of its values
- Boolean -	1 byte
- Bytes -	Byte length
- Date and time -	8 bytes
- Floating-point number -	8 bytes
- Geographical point - 16 bytes
- Integer -	8 bytes
- Map	- The size of the map, calculated the same way as document size
- Null -	1 byte
- Reference	- The document name size
- Text string -	Number of UTF-8 encoded bytes + 1


## What is not included?

Does not take into account the name of a document, check [docs on how it's calculated.](https://firebase.google.com/docs/firestore/storage-size#document-name-size)

Does not take into account indexing. Indexes can be disabled - [docs](https://firebase.google.com/docs/firestore/query-data/index-overview?authuser=0#single-field_index_exemptions) - to free up more space. 

## How to contribute?

Create issues for any bugs caught. Fork the repo to your account and send pull request with your changes.

Run tests using
```bash
python3 setup.py pytest
```
