#sending temp to firebase
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial
continueactivity = True

# connect to microbit
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM8"
ser.open()

#connect to database
cred = credentials.Certificate("C:/Users/18DMartin.ACC/OneDrive - Longford and Westmeath Education and Training Board/daniels school computer/Documents/FireBaseLCCS/lc-cs-test-4caf6-firebase-adminsdk-mon19-6d2a4177ae.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://lc-cs-test-4caf6-default-rtdb.europe-west1.firebasedatabase.app/'})

#reference to db
ref = db.reference()
ref.update({'angle':''})
ref = db.reference().child('angle')



prompt("hi")
rep = 0
while True:
    mb_angle = (str(ser.readline().decode('utf-8')))
    mb_angle = mb_angle.strip()
    #mb_angle = mb_angle[8:]
    mb_angle = int(mb_angle)
    if mb_angle < 0:
        mb_angle = mb_angle 
    print(mb_angle)

    #if mb_angle goes from 100 -> 120 = 1/2 rep
    if ((mb_angle >= 70 and mb_angle <=90) or (mb_angle <= 160 and mb_angle >=180)):
       rep =rep + .5
       print(rep)
