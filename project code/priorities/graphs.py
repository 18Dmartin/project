import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import matplotlib.pyplot as plt
from datetime import datetime

#connect to database
cred = credentials.Certificate("C:/Users/18DMartin.ACC/OneDrive - Longford and Westmeath Education and Training Board/daniels school computer/Documents/FireBaseLCCS/lc-cs-test-4caf6-firebase-adminsdk-mon19-6d2a4177ae.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://lc-cs-test-4caf6-default-rtdb.europe-west1.firebasedatabase.app/'})


totalcaloriesburnt = []
totalrepscompleted = []
totaltimecompleted = []
totalweightcompleted = []
amountofworkouts = 0


accountuser1 = input("What is your account name: ") #1708354895
accountuser1 = accountuser1.lower()
ref1 = db.reference().child(accountuser1)
account1 = ref1.get()
while account1 == None:
    print("Could not find account please retry.\n")
    accountuser1 = input("What is your account name: ") #1708354895
    accountuser1 = accountuser1.lower()
    ref1 = db.reference().child(accountuser1)
    account1 = ref1.get()



for k, v in account1.items():
    if k == 'Gender':
        print('')
    else:
        date = int(k)
        k = datetime.fromtimestamp(date)
        amountofworkouts = amountofworkouts + 1
        #print("time is:", k)
                
        for k2,v2 in v.items():
            if k2 == 'calories':
                #int(v2)
                totalcaloriesburnt.append(v2)
                        
            elif k2 == 'reps':
                #int(v2)
                totalrepscompleted.append(v2)
                        
            elif k2 == 'duration':
                totaltimecompleted.append(v2)
                
            elif k2 == 'weight':
                totalweightcompleted.append(float(v2))
                
        #print("\n")





X_axis = []
Y_axis = ["average calories" , "average reps" ,"average weight", "average time"]

#total calories burnt
print("The total calories burnt is",sum(totalcaloriesburnt))
averagecalories = sum(totalcaloriesburnt)/amountofworkouts
X_axis.append(averagecalories)


#total reps completed

print("The total reps is",sum(totalrepscompleted))
averagereps = sum(totalrepscompleted)/amountofworkouts
X_axis.append(averagereps)


#total weight completed
print("The total weight is",sum(totalweightcompleted))
averageweight = sum(totalweightcompleted)/amountofworkouts
X_axis.append(averageweight)


#total time completed
#print(totaltimecompleted)
print("The total time is",sum(totaltimecompleted))
averagetime = sum(totaltimecompleted)/amountofworkouts
X_axis.append(averagetime)
        
singlecalPrep = sum(totalcaloriesburnt)/sum(totalrepscompleted)
#print(singlecalPrep,"\n")






plt.bar(Y_axis,X_axis)
plt.title('Average data for ' + accountuser1 ) ### to rename and add weight
plt.xlabel('Averages')
plt.ylabel('Weight')
plt.show()
        
print("The average calories per workout is",averagecalories)
#print(amountofworkouts)
 
 

 
 
 #####FIX SECTION######
print("\n")
TorF = True
increaseordecrease = input("Would you like to increase or decrease the amount of calories you want to burn, I/D: ")
increaseordecrease = increaseordecrease.lower()
percentage = input("By what percentage would you like to do this by e.g. 20:")
percentage = int(percentage)

        
while TorF == True:
    if increaseordecrease == "i" or "d" or "increase" or "decrease":
        if increaseordecrease == "i" or increaseordecrease == "increase":
            percentagelen = len(str(percentage))
            #print(percentagelen)
            percentage = percentage / 100
            #print(percentage)
            
            print("You are currently at",averagecalories)
            #print((averagecalories*percentage))
            totalcals = averagecalories + (averagecalories*percentage)
            print("You want to be here ",totalcals)
            finalreps = (totalcals/singlecalPrep)
            print("You need to do another",finalreps,"reps.")
            print("")
            TorF = False
            
        elif increaseordecrease == "d" or increaseordecrease == "decrease":
            percentagelen = len(str(percentage))
            #print(percentagelen)
            percentage = percentage / 100
            #print(percentage)
                    
                    
            print("You are currently at",averagecalories)
            #print((averagecalories*percentage))
            totalcals = averagecalories - (averagecalories*percentage)
            #print((averagecalories*percentage))
            #print(averagecalories)
            print("You want to be here ",totalcals)
            finalreps = (totalcals * singlecalPrep)
            print("You need to do",finalreps,"reps.")
            print("")
            TorF = False
            
        else:
            print("Could not understand please retry.\n")
            increaseordecrease = input("Would you like to increase or decrease the amount of calories you want to burn, I/D: ")
            increaseordecrease = increaseordecrease.lower()
            percentage = input("By what percentage would you like to do this by e.g. 20:")
            percentage = int(percentage)

#while 
           

"""      
       
       
if increaseordecrease == "i" or "d" or "increase" or "decrease":       
    if increaseordecrease == "i" or increaseordecrease == "increase":
        percentagelen = len(str(percentage))
        #print(percentagelen)
        percentage = percentage / 100
        #print(percentage)
                
                
        print("You are currently at",averagecalories)
        #print((averagecalories*percentage))
        wanttobe = averagecalories + (averagecalories/percentage)
        print("You want to be here ",wanttobe)
        overdoing = (wanttobe * singlecalPrep)
        print("You need to do another",overdoing,"reps.")
        print("")
                
                
                
                
                
                
    elif increaseordecrease == "d" or increaseordecrease == "decrease":
        percentagelen = len(str(percentage))
        #print(percentagelen)
        percentage = percentage / 100
        #print(percentage)
                
                
        print("You are currently at",averagecalories)
        #print((averagecalories*percentage))
        wanttobe = (averagecalories - averagecalories)*percentage
        print("You want to be here ",wanttobe)
        overdoing = (wanttobe * singlecalPrep)
        print("You are over doing it by",overdoing,"reps.")
        print("")
                    

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
        
        
        while account1 == None:
            print("Could not find account please retry.\n")
            accountuser1 = input("What is your account name: ") #1708354895
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
                print("Time is:", k)
                
                for k2,v2 in v.items():
                    if k2 == 'reps':
                        print(k2, "completed was:",v2)
                        lastXaxis.append(v2)
                            
                    elif k2 == 'weight':
                        print(k2, "was:",v2, "kg\n")
                        lastYaxis.append(float(v2))# + "kg")
                
                
            user1color = user1color + 1
        
        sumofuser1reps = sum(lastXaxis)
        sumofuser1weight = sum((lastYaxis))


        
       
        accountuser2 = input("What is your second account name: ") #1708354895
        accountuser2 = accountuser2.lower()
        user2color = 0
        
        ref2 = db.reference().child(accountuser2)
        account2 = ref2.get()
        
        
        while account2 == None:
            print("Could not find account please retry.\n")
            accountuser2 = input("What is your account name: ") #1708354895
            accountuser2 = accountuser2.lower()
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
                print("Time is:", k)
                
                for k2,v2 in v.items():
                    if k2 == 'reps':
                        print(k2, "completed was:",v2)
                        lastXaxis.append(v2)
                            
                    elif k2 == 'weight':
                        print(k2, "was:",v2, "kg\n")
                        lastYaxis.append(float(v2))# + "kg")
                        
            user2color = user2color + 1
       
        
        sumofuser2reps = (sum(lastXaxis) - sumofuser1reps)
        sumofuser2weight = (sum(lastYaxis) - sumofuser1weight)
        positions = range(len(lastYaxis))
        whatifrepeat = 1
        c = []
        x = 1
        
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
            

        """       
        x = positions
        y = lastYaxis     

        for i in range(len(x)):
            plt.text(i,y[i],y[i], ha = 'center')
         

            # creating data on which bar chart will be plot
        x = positions
        y = lastYaxis
             
            # making the bar chart on the data
        plt.bar(x, y, color = c)
             
            # calling the function to add value labels
        #addlabels(x, y)
             
            # giving title to the plot
        plt.title(accountuser1 + " vs " + accountuser2)
             
            # giving X and Y labels
        plt.xlabel('Reps')
        plt.ylabel('Weight')
        
        print("\n")
        print(accountuser1, "is the colour red")
        print(accountuser2, "is the colour yellow")
        
            # visualizing the plot
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
        
                
        while account1 == None:
            print("Could not find account please retry.\n")
            accountuser1 = input("What is your account name: ") #1708354895
            accountuser1 = accountuser1.lower()
            ref1 = db.reference().child(accountuser1)
            account1 = ref1.get()
        
        
        for k, v in account1.items():
            if k == 'Gender':
                print('')
            else:
                date = int(k)
                k = datetime.fromtimestamp(date)
                print("Time is:", k)
                
                for k2,v2 in v.items():
                    if k2 == 'calories':
                        print(k2, "burnt is:",v2)
                        calsBurnt1.append(v2)
                            
                    elif k2 == 'duration':
                        print(k2, "is:",v2, "minutes\n")
                        timeused1.append(v2)
                


            
            
            

        
        accountuser2 = input("What is your second account name: ") #1708354895
        accountuser2 = accountuser2.lower()
        
        ref2 = db.reference().child(accountuser2)
        account2 = ref2.get()
        
                
        while account2 == None:
            print("Could not find account please retry.\n")
            accountuser2 = input("What is your account name: ") #1708354895
            accountuser2 = accountuser2.lower()
            ref2 = db.reference().child(accountuser2)
            account2 = ref2.get()
            

        
        for k, v in account2.items():
            if k == 'Gender':
                print("")   
            else:
                date = int(k)
                k = datetime.fromtimestamp(date)
                print("Time is: ", k)
                
                for k2,v2 in v.items():
                    if k2 == 'calories':
                        print(k2, "burnt is: ",v2)
                        calsBurnt2.append(v2)
                    elif k2 == 'duration':
                        print(k2, "is: ",v2, "minutes\n")
                        timeused2.append(v2)
                            
                
                
                
        
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
        plt.xlabel('Workout', fontsize=14)
        plt.ylabel('Calories burnt', fontsize=14)
        plt.grid(True)
        plt.legend()
        plt.show()
        
        
        predictedcals1 = (sum(calsBurnt1) / len(length1))
        print(accountuser1, "is predicted to burn a total of total of",(predictedcals1 * 10),"calories in the next 10 workouts")
        predictedcals2 = (sum(calsBurnt2) / len(length2))
        print(accountuser2, "is predicted to burn a total of total of",(predictedcals2 * 10),"calories in the next 10 workouts")
        whatifrepeat = 1 
        
    elif whatif == "none":
        print("Thats ok.")
        whatifrepeat = 1 



