
def Caloriecalc(maleorfemale):
     MET = False
     while MET == False:  
       # maleorfemale = input(str("Are you male or female: ")) #1708354895
       # maleorfemale = maleorfemale.upper()
        
        age = input(str("How old are you: "))
        age = float(age)

        Bweight = input(str("What is your bodyweight in kgs:"))
        Bweight = float(Bweight) 

        if maleorfemale == "MALE":
           # METMale = 14.7-(0.11 * age)
            #print("male MET is: ", METMale)
            caloriesPMin = (4 * Bweight * 3.5) / 200
            print("male calories burnt per minute is: ", caloriesPMin)
            MET = True
            return caloriesPMin

        elif maleorfemale == "FEMALE":
            #METFemale = 14.7-(0.13 * age)
            #print("female MET is: ", METFemale)
            caloriesPMin = (4 * Bweight * 3.5) / 200
            print("female calories per minute is: ", caloriesPMin)
            MET = True
            return caloriesPMin
            
        else:
            print("Try again!")
            
            
        
            

"""

def Caloriecalc():
     MET = False
     while MET == False:  
        maleorfemale = input(str("Are you male or female: ")) #1708354895
        maleorfemale = maleorfemale.upper()
        
        age = input(str("How old are you: "))
        age = float(age)

        Bweight = input(str("What is your bodyweight in kgs:"))
        Bweight = float(Bweight) 

        if maleorfemale == "MALE":
            METMale = 14.7-(0.11 * age)
            print("male MET is: ", METMale)
            caloriesPMin = (METMale * Bweight * 3.5) / 200
            print("male calories per minute is: ", caloriesPMin)
            MET = True
            return caloriesPMin

        elif maleorfemale == "FEMALE":
            METFemale = 14.7-(0.13 * age)
            print("female MET is: ", METFemale)
            caloriesPMin = (METFemale * Bweight * 3.5) / 200
            print("female calories per minute is: ", caloriesPMin)
            MET = True
            return caloriesPMin
            
        else:
            print("Try again!")
"""      
        
            





