import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import matplotlib.pyplot as plt
from datetime import datetime

#connect to database
cred = credentials.Certificate("C:/Users/18DMartin.ACC/OneDrive - Longford and Westmeath Education and Training Board/daniels school computer/Documents/FireBaseLCCS/lc-cs-test-4caf6-firebase-adminsdk-mon19-6d2a4177ae.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://lc-cs-test-4caf6-default-rtdb.europe-west1.firebasedatabase.app/'})




#what account they would like to see
username = input("What is your account name: ") #1708354895
username = username.lower()

#access to user account
ref = db.reference().child(username)
results = ref.get()



repslist = []
weightlist = []
#pull account info.
for k, v in results.items():
    if k != "Gender":
        date = int(k)
        k = datetime.fromtimestamp(date)
        print("time is:", k)
        for k2,v2 in v.items():
            if k2 == "weight":
                print(k2, "is:",v2,"kg")
                weightlist.append(v2)
            elif k2 == "duration":
                print(k2, "is: ",v2,"minutes")
            elif k2 == "calories":
                print(k2,"burnt is:",v2)
            elif k2 == "reps":
                print(k2, "is:",v2)
                repslist.append(v2)
        print("\n")

ammountworkoutstest = len(repslist)
ammountworkout = []
length1=[]
while ammountworkoutstest != 0:
    ammountworkout.append(ammountworkoutstest)
    ammountworkoutstest = ammountworkoutstest - 1

ammountworkout.reverse
print(repslist,"is reps")
print(ammountworkout, "is which workout")
print(weightlist,"is weight")






"""
#makes graph.
plt.bar(repslist, ammountworkout, color = color1)
plt.title('total reps and weight')
plt.xlabel('Reps')
plt.ylabel('Weight')
plt.show()


"""





















