import firebase_admin
from firebase_admin import credentials, firestore, storage

cred=credentials.Certificate('E:\\Programing\\ML\\PI\\path\\to\\serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'countingcars-4a603.appspot.com'
})
db = firestore.client()
bucket = storage.bucket()
blob = bucket.blob('file/laporan.csv')
outfile='E:\\Programing\\ML\\PI\\data_csv\\laporan.csv'
blob.upload_from_filename(outfile)

print("Upload Berhasil")