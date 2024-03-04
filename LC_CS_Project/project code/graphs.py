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


#pull account info.
for k, v in results.items():
    if k != "Gender":
        date = int(k)
        k = datetime.fromtimestamp(date)
        print("time is: ", k)
        for k2,v2 in v.items():
            if k2 == "weight":
                print(k2, "\tis: ",v2,"kg")
            else:
                print(k2, "\tis: ",v2) 
        print("\n")




X_axis = []
Y_axis = []
colour = 0
repeat = 0
times = 1

#isolates reps and weight.
while repeat != 1:
    chosendate = input("what workout would you like to see: ")
   # if chosendate == "none"
    reverteddate = datetime.strptime(chosendate, "%Y-%m-%d %H:%M:%S")
    reverteddate = reverteddate.timestamp()
    reverteddate = int(reverteddate)
    reverteddate = str(reverteddate)

    ref = db.reference().child(username).child(reverteddate).child("reps")
    reps = ref.get()
    reps = int(reps)
    ref = db.reference().child(username).child(reverteddate).child("weight")
    weight = ref.get()
    weight = float(weight)
    print("rep is",reps)
    print("weight is",weight,"kg")
    
#repeats the loop if user wants to.
    rerun = str(input("\nWould you like to add another set of reps and weights, yes or no: "))
    rerun = rerun.lower()
    if rerun == "yes":
        repeat = 0
    else:
        repeat = 1
    
#addes reps and weight to list for graph.
    X_axis.append(reps)
    color1 = 'green'
    Y_axis.append(weight)
    
    #print(X_axis)
    #print(Y_axis)
 

    #makes graph.
plt.bar(X_axis, Y_axis, color = color1)
plt.title('total reps and weight')
plt.xlabel('Reps')
plt.ylabel('Weight')
plt.show()

### what if question
whatif = input("What what if question would you like one, two or none")
whatif = whatif.lower()
if whatif == "one":
    lastXaxis = []
    lastYaxis = []
    print("You are comparing the last workout of two accounts\n")

    accountuser1 = input("What is your first account name") #1708354895
    accountuser1 = accountuser1.lower()

    ref1 = db.reference().child(accountuser1)
    account1 = ref1.order_by_key().limit_to_last(3).get()
    #print(account1)
    
    for k, v in account1.items():
        if k != "Gender":
            lastwork1 = k
    

            
            
    ref1 = db.reference().child(accountuser1).child(lastwork1).child("reps")
    lastreps1 = ref1.get()
    lastreps1 = int(lastreps1)
    print(lastreps1, "is how many reps",accountuser1,"completed")
    
    ref1 = db.reference().child(accountuser1).child(lastwork1).child("weight")
    lastweight1 = ref1.get()
    lastweight1 = float(lastweight1)
    print(lastweight1,"kg is the weight",accountuser1,"used\n")
    
    
    lastXaxis.append(lastreps1)
    lastYaxis.append(lastweight1)

    
   
    accountuser2 = input("What is your second account name") #1708354895
    accountuser2 = accountuser2.lower()
    
    ref2 = db.reference().child(accountuser2)
    account2 = ref2.order_by_key().limit_to_last(3).get()
    #print(account2)
    
    for k, v in account2.items():
        if k != "Gender":
            lastwork2 = k
    #print(lastwork2,"is the last time")
    
    ref2 = db.reference().child(accountuser2).child(lastwork2).child("reps")
    lastreps2 = ref2.get()
    lastreps2 = int(lastreps2)
    print(lastreps2,"is how many reps",accountuser2,"completed")
    
    ref2 = db.reference().child(accountuser2).child(lastwork2).child("weight")
    lastweight2 = ref2.get()
    lastweight2 = float(lastweight2)
    print(lastweight2,"kg is the weight",accountuser2,"used\n")

    lastXaxis.append(lastreps2)
    lastYaxis.append(lastweight2)
    #print(lastXaxis)
    #print(lastYaxis)
        
    plt.bar(lastXaxis, lastYaxis)
    plt.title(accountuser1 + " vs " + accountuser2)
    plt.xlabel('Reps')
    plt.ylabel('Weight')
    plt.show()
    


elif whatif == "two":
    print("You are comparing the last calorie per minute burned of two accounts")
    accountuser1 = input("What is your first account name") #1708354895
    accountuser1 = accountuser1.lower()
    
    #accountuser2 = input("What is your second account name") #1708354895
   # accountuser2 = accountuser2.lower()
    
    ref1 = db.reference().child(accountuser1)
    account1 = ref1.get()
    
    for k, v in results.items():
        date = int(k)
        k = datetime.fromtimestamp(date)
        print("time is: ", k)
        for k2,v2 in v.items():
                print(k2, "\tis: ",v2)
        print("\n")

    
    
    #ref2 = db.reference().child(accountuser2)
    #account2 = ref2.get()
    



















































"""  
### what if question
whatif = input("What what if question would you like one, two or none")
whatif = whatif.lower()
if whatif == "one":
    lastXaxis = []
    lastYaxis = []
    print("You are comparing the last workout of two accounts")

   accountuser1 = input("What is your first account name") #1708354895
    accountuser1 = accountuser1.lower()

    ref1 = db.reference().child(accountuser1)
    account1 = ref1.get()
    
    for k, v in account1.items():
        #print("time is: ", k)
        lastwork1 = k
    
    print(lastwork1,"is the last time", accountuser1,"worked out")
    
    ref1 = db.reference().child(accountuser1).child(lastwork1).child("reps")
    lastreps1 = ref1.get()
    lastreps1 = int(lastreps1)
    print(lastreps1)
    
    ref1 = db.reference().child(accountuser1).child(lastwork1).child("weight")
    lastweight1 = ref1.get()
    lastweight1 = float(lastweight1)
    print(lastweight1)
    lastXaxis.append(lastreps1)
    lastYaxis.append(lastweight1)

    
"""