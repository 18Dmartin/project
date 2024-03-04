
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial


#read data from microbit
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM12"
ser.open()

#connect to database
cred = credentials.Certificate("C:/Users/18DMartin.ACC/OneDrive - Longford and Westmeath Education and Training Board/daniels school computer/Documents/FireBaseLCCS/lc-cs-test-4caf6-firebase-adminsdk-mon19-6d2a4177ae.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://lc-cs-test-4caf6-default-rtdb.europe-west1.firebasedatabase.app/'})


#reference to db
ref = db.reference('workout')




ref = db.reference().child(str(int(time.time())))



#weight to database
weight = False
while weight == False:
    mb_weight_recived = (str(ser.readline().decode('utf-8')))
    if mb_weight_recived:
        print(mb_weight_recived, "kg")
        ref.update({'weight':mb_weight_recived})

        weight = True
        
        
#ref.update({str(int(time.time())):{ 'weight':mb_weight_recived,'reps':50}})

x = 1
rep = 0
while True:
    #strip any unneeded information from angle
    mb_angle = (str(ser.readline().decode('utf-8')))
    mb_angle = mb_angle.strip()
    mb_angle = int(mb_angle)
    
    #converts angles movement to reps
    if (x == 1 and mb_angle < -70 and mb_angle > -180 ):
        x = 2
    if (x == 2 and mb_angle < 180 and mb_angle > 0 ):
        x = 1
        int(rep) = rep + 1
        print(rep)
     
        ref.update({"Reps":rep})
        #print(mb_angle)

