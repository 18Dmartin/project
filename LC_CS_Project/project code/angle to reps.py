#sending temp to firebase
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial
continueactivity = True

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM6"
ser.open()

cred = credentials.Certificate("C:/Users/18DMartin.ACC/OneDrive - Longford and Westmeath Education and Training Board/daniels school computer/Documents/FireBaseLCCS/lc-cs-test-4caf6-firebase-adminsdk-mon19-6d2a4177ae.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://lc-cs-test-4caf6-default-rtdb.europe-west1.firebasedatabase.app/'})


#reference to db
ref = db.reference()
ref.update({'angle':''})
"""
ref = db.reference().child('intensity rating')
userrating = input("How intensity do you want this work out to for 1 - 10:")
ref.update({'intensity rating': userrating})
"""
ref = db.reference().child('reps')
weight = False
while weight == False:
    mb_weight_recived = (str(ser.readline().decode('utf-8')))
    if mb_weight_recived:
        print("yikes")
        print("mb_weight_recived")
        weight = True
x = 1       
rep = 0
while True:
    mb_angle = (str(ser.readline().decode('utf-8')))
    mb_angle = mb_angle.strip()
    #mb_angle = mb_angle[8:]
    mb_angle = int(mb_angle)
    if (x == 1 and mb_angle < -70 and mb_angle > -180 ):
        x = 2
    if (x == 2 and mb_angle < 180 and mb_angle > 0 ):
        x = 1
        rep = rep + 1
        print(rep)
    #print(mb_angle)
    
