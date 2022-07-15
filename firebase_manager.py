import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from google.cloud import storage

from firebase_utils.constants import SKINCARE_BUCKET
import os

try:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(os.path.dirname(__file__), "firebase_credentials.json")
except:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join("./", "firebase_credentials.json")


cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

storage_client = storage.Client()
bucket = storage_client.get_bucket(SKINCARE_BUCKET)