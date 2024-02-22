import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import matplotlib.pyplot as plt

#connect to database
cred = credentials.Certificate("C:/Users/18DMartin.ACC/OneDrive - Longford and Westmeath Education and Training Board/daniels school computer/Documents/FireBaseLCCS/lc-cs-test-4caf6-firebase-adminsdk-mon19-6d2a4177ae.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://lc-cs-test-4caf6-default-rtdb.europe-west1.firebasedatabase.app/'})


#what graph they would like to see
usernumber = input("what is your name") #1708354895
ref.update({usernumber:''})


#remove the reps and weight from the database
ref = db.reference().child(usernumber).child('Reps')
results = ref.get()
Reps = results
Reps = float(Reps)
print(Reps)

ref = db.reference().child(usernumber).child('weight')
results = ref.get()
weight = results
weight = weight.strip()
weight = float(weight)
print(weight)


Repstaken = [Reps]
TotalWeight = [int(weight)]

plt.bar(Repstaken, TotalWeight)
plt.title('total reps and weight')
plt.xlabel('Reps')
plt.ylabel('Weight')
plt.show()
