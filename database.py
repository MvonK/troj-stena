import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'projectId': os.getenv('FIREBASE_PROJECT_ID'),
})

db = firestore.client()


def get_document(collection, document):
    return db.collection(collection).document(document).get()


def check_document(collection, document):
    if db.collection(collection).document(document).get().exists:
        return True
    return False


def load_to_map(collection, document, key, content):
    doc_ref = db.collection(collection).document(document)
    doc_ref.set({key: content}, merge=True)


def update_map(collection, document, key, field, content):
    doc_ref = db.collection(collection).document(document)
    doc_ref.update({f'{key}.{field}': content})


def remove_from_map(collection, document, key, field):
    doc_ref = db.collection(collection).document(document)
    doc_ref.update({f'{key}.{field}': firestore.DELETE_FIELD})


def load(collection, document, value):
    doc_ref = db.collection(collection).document(document)
    doc_ref.set(value)
