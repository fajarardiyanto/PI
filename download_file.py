import pyrebase
import firebase_admin
from firebase_admin import credentials

cred=credentials.Certificate('E:\\Programing\\ML\\MobilPI\\path\\to\\serviceAccountKey.json')
config = {
    "apiKey": "AIzaSyBzbmPBjwSwZgnhwEM76fM3XklCtM3lU5Q",
    "authDomain": "countingcars-4a603.firebaseapp.com",
    "databaseURL": "https://countingcars-4a603.firebaseio.com",
    "projectId": "countingcars-4a603",
    "storageBucket": "countingcars-4a603.appspot.com",
    "messagingSenderId": "691798674025"
}

firebase = pyrebase.initialize_app(config)

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
storage.child("file/laporan.csv").download("download_csv/laporan.csv")

print("Download Berhasil")