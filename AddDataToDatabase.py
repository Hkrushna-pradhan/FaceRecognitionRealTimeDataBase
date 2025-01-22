import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendacerealtime-48b7c-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "2104025":
        {
            "name": "Harekrushna pradhan",
            "Branch": "CSEDS",
            "semester": 6,
            "total_attendance": 7,
            "year": 3,
            "last_attendance_time": "2024-01-11 00:54:34"
        },
    "2104007":
        {
            "name": "Amit Ranjan Beura",
            "Branch": "CSEDS",
            "semester": 6,
            "total_attendance": 12,
            "year": 3,
            "last_attendance_time": "2024-01-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "Branch": "CSEDS",
            "semester": 6,
            "total_attendance": 7,
            "year": 3,
            "last_attendance_time": "2024-01-11 00:54:34"
        }
}


for key, value in data.items():
    ref.child(key).set(value)
