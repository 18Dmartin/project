#sending temp to firebase
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial
import CaloriesandMet
import Gender
b = Gender.maleorfemale()
a = CaloriesandMet.Caloriecalc(b)




ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM14"
ser.open()

cred = credentials.Certificate("C:/Users/18DMartin.ACC/OneDrive - Longford and Westmeath Education and Training Board/daniels school computer/Documents/FireBaseLCCS/lc-cs-test-4caf6-firebase-adminsdk-mon19-6d2a4177ae.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://lc-cs-test-4caf6-default-rtdb.europe-west1.firebasedatabase.app/'})


#reference to db
ref = db.reference()
usernumber = input("\nWhat is your name: ") #1708354895
usernumber = usernumber.lower()

ref = db.reference().child(usernumber)
ref.update({'Gender':b})
times = str(int(time.time()))
ref = db.reference().child(usernumber).child(times)

#print(a)



weight = False
while weight == False:
    mb_weight_recived = (str(ser.readline().decode('utf-8')))
    if mb_weight_recived:
        
        print(mb_weight_recived,"kg")
        mb_weight_recived = mb_weight_recived.replace("\r\n","")
        ref = db.reference().child(usernumber).child(times)
        ref.update({'weight':mb_weight_recived})
        weight = True
x = 1       
rep = 0
tracking = True

if mb_weight_recived:
    t1 = int(time.time())
while tracking == True:
    mb_angle = (str(ser.readline().decode('utf-8')))
    #print(mb_angle)
    mb_angle = mb_angle.strip()
    #mb_angle = mb_angle[8:]
    mb_angle = int(mb_angle)
    if (x == 1 and mb_angle < -70 and mb_angle > -170 ):
        x = 2
    if (x == 2 and mb_angle < 150 and mb_angle > 0 ):
        x = 1
        rep = rep + 1
        print(rep)
        ref = db.reference().child(usernumber).child(times)
        ref.update({'reps':rep})
    if mb_angle == 900:
        tracking = False
if tracking == False:
    t2 = int(time.time())
    
totaltime = t2-t1
#print("time 1 is",t1)
#print("time 2 is",t2)

totaltime = float(totaltime)
totaltime = totaltime / 100
#print(totaltime, "seconds")

Cals = totaltime * a
print("\n",Cals," calsories burnt per minute for", totaltime,"minutes")
ref = db.reference().child(usernumber).child(times)
ref.update({'calories':Cals})
