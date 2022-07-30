import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from firebase_credentials import CREDENTIALS_FIREBASE

cred = credentials.Certificate(CREDENTIALS_FIREBASE)
firebase_admin.initialize_app(cred)
db = firestore.client()


