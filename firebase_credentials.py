import os
CREDENTIALS_FIREBASE = {
    "type": "service_account",
    "project_id": os.environ['firebase_project_id'],
    "private_key_id": os.environ['firebase_private_key_id'],
    "private_key":os.environ['firebase_private_key'].replace('\\n', '\n'),
    "client_email": os.environ['firebase_client_email'],
    "client_id": os.environ['firebase_client_id'],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": os.environ['firebase_client_x509_cert_url'],
}
