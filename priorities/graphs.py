import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

#connect to database
cred = credentials.Certificate("C:/Users/18DMartin.ACC/OneDrive - Longford and Westmeath Education and Training Board/daniels school computer/Documents/FireBaseLCCS/lc-cs-test-4caf6-firebase-adminsdk-mon19-6d2a4177ae.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://lc-cs-test-4caf6-default-rtdb.europe-west1.firebasedatabase.app/'})


"""
#existantaccount = False
#what account they would like to see
#while existantaccount == False:
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
        print("time is:", k)
        for k2,v2 in v.items():
            if k2 == "weight":
                print(k2, "is:",v2,"kg")
            elif k2 == "duration":
                print(k2, "is: ",v2,"minutes")
            elif k2 == "calories":
                print(k2,"burnt is:",v2)
            else:
                print(k2, "is:",v2) 
        print("\n")



X_axis = []
Y_axis = []
colour = 0
repeat = 0
times = 1


#allows user to determine how many dates they would like to see for the graph by using a while loop
    #isolates reps and weight.
while repeat != 1:
    chosendate = input("what workout would you like to see: ")
   # if chosendate == "":
    reverteddate = datetime.strptime(chosendate, "%Y-%m-%d %H:%M:%S")
    reverteddate = reverteddate.timestamp()
    reverteddate = int(reverteddate)
    reverteddate = str(reverteddate)
    
    #isolates reps and weight.
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
























"""
### what if question
whatifrepeat = 0
while whatifrepeat != 1:
    whatif = input("What what if question would you like one, two or none: ")
    whatif = whatif.lower()
    if whatif == "one":
        lastXaxis = []
        lastYaxis = []
        print("You are comparing the last workout of two accounts\n")

        accountuser1 = input("What is your first account name: ") #1708354895
        accountuser1 = accountuser1.lower()

        ref1 = db.reference().child(accountuser1)
        account1 = ref1.get()
        #print(account1)
        repscounts1 = []
        weightcounts1 = []
        user1color = 0
        
        for k, v in account1.items():
            if k == 'Gender':
                print('')
            else:
                date = int(k)
                k = datetime.fromtimestamp(date)
                print("time is:", k)
                
                for k2,v2 in v.items():
                    if k2 == 'reps':
                        print(k2, "completed was:",v2)
                        lastXaxis.append(v2)
                            
                    elif k2 == 'weight':
                        print(k2, "was:",v2, "kg")
                        lastYaxis.append(float(v2))# + "kg")
                
            print("\n")    
            user1color = user1color + 1
        
        sumofuser1reps = sum(lastXaxis)
        sumofuser1weight = sum((lastYaxis))


        
       
        accountuser2 = input("What is your second account name: ") #1708354895
        accountuser2 = accountuser2.lower()
        user2color = 0
        
        ref2 = db.reference().child(accountuser2)
        account2 = ref2.get()
        #print(account2)
        repscounts2 = []
        weightcounts2 = []
        
        for k, v in account2.items():
            if k == 'Gender':
                print('')
            else:
                date = int(k)
                k = datetime.fromtimestamp(date)
                print("time is:", k)
                
                for k2,v2 in v.items():
                    if k2 == 'reps':
                        print(k2, "completed was:",v2)
                        lastXaxis.append(v2)
                            
                    elif k2 == 'weight':
                        print(k2, "was:",v2, "kg")
                        lastYaxis.append(float(v2))# + "kg")
                        
            print("\n")   
            user2color = user2color + 1
       
        
        sumofuser2reps = (sum(lastXaxis) - sumofuser1reps)
        sumofuser2weight = (sum(lastYaxis) - sumofuser1weight)
        positions = range(len(lastYaxis))
        whatifrepeat = 1
        c = []
        x = 0
        
        while x != user1color:
            c.append('red')
            x = x + 1

        x = 0
        while x != user2color:
            c.append('yellow')
            x = x + 1
            
        
        print("The total reps",accountuser1,"completed was",sumofuser1reps,"reps at an total weight of",sumofuser1weight, "kg over",user1color,"workouts.")
        print("The average rep",accountuser1,"completed was",(sumofuser1reps/user1color),"reps at an average weight of",(sumofuser1weight/user1color),"kg.")
        print("The model predicted that if",accountuser1,"stays at their current pace after 10 workouts they will do",(sumofuser1reps/user1color)* 10,"total reps at a total weight of",(sumofuser1weight/user1color) * 10,"kg.")
        
        print("\n")
        print("The total reps",accountuser2,"completed was",sumofuser2reps,"reps at an total weight of",sumofuser2weight, "over",user2color,"workouts.")
        print("The average rep",accountuser2,"completed was",(sumofuser2reps/user1color),"reps at an average weight of",(sumofuser2weight/user1color),"kg.")
        print("The model predicted that if",accountuser1,"stays at their current pace after 10 workouts they will do",(sumofuser2reps/user1color)* 10,"total reps at a total weight of",(sumofuser2weight/user1color) * 10,"kg")
 
 
 
        print("\n")
        print(accountuser1, "is the colour red")
        print(accountuser2, "is the colour yellow")
        plt.xticks(positions, lastXaxis)
        plt.bar(positions, lastYaxis, color = c)
        #plt.xticks(positions, lastXaxis)
        plt.title(accountuser1 + " vs " + accountuser2)
        plt.xlabel('Reps')
        plt.ylabel('Weight')
        plt.show()
 
        print("\n")
        print(accountuser1, "is the colour red")
        print(accountuser2, "is the colour yellow")
                
                
                # Bring some raw data.
        # In my original code I create a series and run on that,
        # so for consistency I create a series from the list.
        freq_series = pd.Series(lastYaxis)

        x_labels = positions

        # Plot the figure.
        plt.figure(figsize=(12, 8))
        ax = freq_series.plot(kind="bar")
        ax.set_title("Amount Frequency")


        ax.set_xlabel("Amount ($)")
        ax.set_ylabel("Frequency")




        rects = ax.patches



        for rect, positions in zip(rects, positions):
            height = rect.get_height()
            ax.text(
                rect.get_x() + rect.get_width() / 2, height - 5, positions, ha="center", va="bottom"
            )

        plt.show()

                
                
                
                
                
                        




        print("\n")
        print(accountuser1, "is the colour red")
        print(accountuser2, "is the colour yellow")
        plt.bar(positions, lastYaxis, color = c)
        #plt.xticks(positions, lastXaxis)
        plt.title(accountuser1 + " vs " + accountuser2)
        plt.xlabel('Reps')
        plt.ylabel('Weight')
        plt.show()
        """        
        ax = freq_series.plot(kind="bar")
        rects = ax.patches



                    
                    
                    
                     
                if (lastweight1 > lastweight2) and (lastreps1 > lastreps2):
            print(accountuser1, "has more weight and reps")
            print(accountuser2, "has less weight and reps")
        
        elif (lastweight1 < lastweight2) and (lastreps1 < lastreps2):
            print(accountuser1, "has less weight and reps")
            print(accountuser2, "has more weight and reps")
           
        elif (lastweight1 < lastweight2) and (lastreps1 > lastreps2):
            print(accountuser1, "has less weight and more reps")
            print(accountuser2, "has more weight and less reps")
            
        elif (lastweight1 > lastweight2) and (lastreps1 < lastreps2):
            print(accountuser1, "has more weight and less reps")
            print(accountuser2, "has less weight and more reps")
            
        elif (lastweight1 == lastweight2) and (lastreps1 > lastreps2):
            print(accountuser1, "has equal weight and more reps")
            print(accountuser2, "has equal weight and less reps")
            
        elif (lastweight1 == lastweight2) and (lastreps1 < lastreps2):
            print(accountuser1, "has equal weight and less reps")
            print(accountuser2, "has equal weight and more reps")         
        
        elif (lastweight1 > lastweight2) and (lastreps1 == lastreps2):
            print(accountuser1, "has more weight and equal reps")
            print(accountuser2, "has less weight and equal reps")         
        
        elif (lastweight1 < lastweight2) and (lastreps1 == lastreps2):
            print(accountuser1, "has less weight and equal reps")
            print(accountuser2, "has more weight and equal reps")   
            
        elif (lastweight1 == lastweight2) and (lastreps1 == lastreps2):
            print(accountuser1, "and", accountuser2, "are completely equal")
           
        plt.bar(lastXaxis, lastYaxis, color = c)
        plt.title(accountuser1 + " vs " + accountuser2)
        plt.xlabel('Reps')
        plt.ylabel('Weight')
        plt.show()
        """










        
    elif whatif == "two":
        calsBurnt1 = []
        timeused1 = []
        calsBurnt2 = []
        timeused2 = []
        print("You are comparing the last calorie per minute burned of two accounts\n")
        accountuser1 = input("What is your first account name: ") #1708354895
        accountuser1 = accountuser1.lower()
        
        #accountuser2 = input("What is your second account name") #1708354895
       # accountuser2 = accountuser2.lower()
        
        ref1 = db.reference().child(accountuser1)
        account1 = ref1.get()
        
        for k, v in account1.items():
            if k == 'Gender':
                print('')
            else:
                date = int(k)
                k = datetime.fromtimestamp(date)
                print("time is:", k)
                
                for k2,v2 in v.items():
                    if k2 == 'calories':
                        print(k2, "burnt is:",v2)
                        calsBurnt1.append(v2)
                            
                    elif k2 == 'duration':
                        print(k2, "is:",v2, "minutes")
                        timeused1.append(v2)
                
                print("\n")

            
            
            

        
        accountuser2 = input("What is your second account name: ") #1708354895
        accountuser2 = accountuser2.lower()
        
        ref2 = db.reference().child(accountuser2)
        account2 = ref2.get()
        
        for k, v in account2.items():
            if k == 'Gender':
                print("")   
            else:
                date = int(k)
                k = datetime.fromtimestamp(date)
                print("time is: ", k)
                
                for k2,v2 in v.items():
                    if k2 == 'calories':
                        print(k2, "burnt is: ",v2)
                        calsBurnt2.append(v2)
                    elif k2 == 'duration':
                        print(k2, "is: ",v2, "minutes")
                        timeused2.append(v2)
                            
                print("\n")
                
                
        
        #print(calsBurnt1, accountuser1,"cals")
        

        
        lenghtuser1 = len(timeused1)
        length1=[]
        while lenghtuser1 != 0:
            length1.append(lenghtuser1)
            lenghtuser1 = lenghtuser1 - 1
            
        length1.reverse()
        #print(length1, accountuser1,"workouts")

        lenghtuser2 = len(timeused2)
        length2=[]
        while lenghtuser2 != 0:
            length2.append(lenghtuser2)
            lenghtuser2 = lenghtuser2 - 1
        
        #print(calsBurnt2,accountuser2,"cals")
        length2.reverse()
        #print(length2, accountuser2,"workouts")
        

        print(accountuser1, "has burnt a total of",sum(calsBurnt1), "over", len(length1), "workouts.")
        print(accountuser2, "has burnt a total of",sum(calsBurnt2), "over", len(length2), "workouts.")
        print("\n")
        
        plt.plot(length1, calsBurnt1, marker='o',label = accountuser1)
        plt.plot(length2, calsBurnt2, marker='o',label = accountuser2)
        plt.title(accountuser1 + " vs " + accountuser2, fontsize=14)
        plt.xlabel('workout', fontsize=14)
        plt.ylabel('cals burnt', fontsize=14)
        plt.grid(True)
        plt.legend()
        plt.show()
        
        
        predictedcals1 = (sum(calsBurnt1) / len(length1))
        print(accountuser1, "is predicted to burn a total of total of",(predictedcals1 * 10),"calories in the next 10 workouts")
        predictedcals2 = (sum(calsBurnt2) / len(length2))
        print(accountuser2, "is predicted to burn a total of total of",(predictedcals2 * 10),"calories in the next 10 workouts")
        whatifrepeat = 1 
        
    elif whatif == "none":
        print("thats ok.")
        whatifrepeat = 1 

    else:
        print("try again")
        whatifrepeat = 0

    """

        #
        #ref2 = db.reference().child(accountuser2)
        #account2 = ref2.get()
        

































    if whatif == "one":
        lastXaxis = []
        lastYaxis = []
        print("You are comparing the last workout of two accounts\n")

        accountuser1 = input("What is your first account name: ") #1708354895
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
        print(lastreps1, "is how many reps",accountuser1,"completed.")
        
        ref1 = db.reference().child(accountuser1).child(lastwork1).child("weight")
        lastweight1 = ref1.get()
        lastweight1 = float(lastweight1)
        print(lastweight1,"kg is the weight",accountuser1,"used.")
        print(accountuser1,"is the colour red.\n")
        
        
        lastXaxis.append(lastreps1)
        lastYaxis.append(lastweight1)

        
       
        accountuser2 = input("What is your second account name: ") #1708354895
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
        print(lastreps2,"is how many reps",accountuser2,"completed.")
        
        ref2 = db.reference().child(accountuser2).child(lastwork2).child("weight")
        lastweight2 = ref2.get()
        lastweight2 = float(lastweight2)
        print(lastweight2,"kg is the weight",accountuser2,"used.")
        print(accountuser2,"is the colour yellow.\n")

        lastXaxis.append(lastreps2)
        lastYaxis.append(lastweight2)
        c = ['red', 'yellow']
        #print(lastXaxis)
        #print(lastYaxis)
            
        plt.bar(lastXaxis, lastYaxis, color = c)
        plt.title(accountuser1 + " vs " + accountuser2)
        plt.xlabel('Reps')
        plt.ylabel('Weight')
        plt.show()
        



















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

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        whatif = whatif.lower()
    if whatif == "one":
        lastXaxis = []
        lastYaxis = []
        print("You are comparing the last workout of two accounts\n")

        accountuser1 = input("What is your first account name: ") #1708354895
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
        print(lastreps1, "is how many reps",accountuser1,"completed.")
        
        ref1 = db.reference().child(accountuser1).child(lastwork1).child("weight")
        lastweight1 = ref1.get()
        lastweight1 = float(lastweight1)
        print(lastweight1,"kg is the weight",accountuser1,"used.")
        print(accountuser1,"is the colour red.\n")
        
        
        lastXaxis.append(lastreps1)
        lastYaxis.append(lastweight1)
       
        accountuser2 = input("What is your second account name: ") #1708354895
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
        print(lastreps2,"is how many reps",accountuser2,"completed.")
        
        ref2 = db.reference().child(accountuser2).child(lastwork2).child("weight")
        lastweight2 = ref2.get()
        lastweight2 = float(lastweight2)
        print(lastweight2,"kg is the weight",accountuser2,"used.")
        print(accountuser2,"is the colour yellow.\n")

        lastXaxis.append(lastreps2)
        lastYaxis.append(lastweight2)
        c = ['red', 'yellow']
        #print(lastXaxis)
        #print(lastYaxis)
            
            
            
            
        if (lastweight1 > lastweight2) and (lastreps1 > lastreps2):
            print(accountuser1, "has more weight and reps")
            print(accountuser2, "has less weight and reps")
        
        elif (lastweight1 < lastweight2) and (lastreps1 < lastreps2):
            print(accountuser1, "has less weight and reps")
            print(accountuser2, "has more weight and reps")
           
        elif (lastweight1 < lastweight2) and (lastreps1 > lastreps2):
            print(accountuser1, "has less weight and more reps")
            print(accountuser2, "has more weight and less reps")
            
        elif (lastweight1 > lastweight2) and (lastreps1 < lastreps2):
            print(accountuser1, "has more weight and less reps")
            print(accountuser2, "has less weight and more reps")
            
        elif (lastweight1 == lastweight2) and (lastreps1 > lastreps2):
            print(accountuser1, "has equal weight and more reps")
            print(accountuser2, "has equal weight and less reps")
            
        elif (lastweight1 == lastweight2) and (lastreps1 < lastreps2):
            print(accountuser1, "has equal weight and less reps")
            print(accountuser2, "has equal weight and more reps")         
        
        elif (lastweight1 > lastweight2) and (lastreps1 == lastreps2):
            print(accountuser1, "has more weight and equal reps")
            print(accountuser2, "has less weight and equal reps")         
        
        elif (lastweight1 < lastweight2) and (lastreps1 == lastreps2):
            print(accountuser1, "has less weight and equal reps")
            print(accountuser2, "has more weight and equal reps")   
            
        elif (lastweight1 == lastweight2) and (lastreps1 == lastreps2):
            print(accountuser1, "and", accountuser2, "are completely equal")
            
        plt.bar(lastXaxis, lastYaxis, color = c)
        plt.title(accountuser1 + " vs " + accountuser2)
        plt.xlabel('Reps')
        plt.ylabel('Weight')
        plt.show()
        

    """
