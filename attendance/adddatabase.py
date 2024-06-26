import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceaccountkey.json")
firebase_admin.initialize_app(cred,{
'databaseURL':'https://facerecognition-c23c5-default-rtdb.firebaseio.com/',

})
ref= db.reference('students')
data={
  "4": {
     "name":"Devika",
      "major": "cse",
      "starting year":2022,
      "standing" :"G",
      "total_attendance":6,
      "year":3,
      "last_attendance":"2024-06-12 00:54:34"
  },
"16": {
     "name":"Dhruv",
      "major": "ds",
      "starting year":2022,
      "standing" :" M",
      "total_attendance":3,
      "year":3,
      "last_attendance":"2024-06-12 00:50:34"
  },
"23": {
     "name":"yashaswi",
      "major": "datascience honors",
      "starting year":2022,
      "standing" :"G",
      "total_attendance":10,
      "year":3,
      "last_attendance":"2024-06-12 00:54:34"
  },
 "37":   {
"name":"nishtha",
      "major": "datascience honors",
      "starting year":2022,
      "standing" :"G",
      "total_attendance":10,
      "year":3,
      "last_attendance":"2024-06-12 00:54:34"
    }

}
for key,value in data.items():
    ref.child(key).set(value)