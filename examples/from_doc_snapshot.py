from firebase_admin import credentials, firestore, initialize_app
from firestore_size.calculate import document_size

# See more at: https://firebase.google.com/docs/admin/setup#initialize_the_sdk
app = initialize_app()
db = firestore.client()

collection_name = "data"  # collection name here
collection = db.collection(collection_name)
doc = collection.doc(id).get()
doc_size = document_size(doc.to_dict())

print(f"doc with id {doc.id} has size {doc_size}")
