
def Caloriecalc():
    maleorfemale = input(str("are you male or female")) #1708354895

    age = input(str("how old are you"))
    age = float(age)

    Bweight = input(str("What is your bodyweight in kgs"))
    Bweight = float(Bweight) 

    if maleorfemale == "male":
        METMale = 14.7-(0.11 * age)
        print("male MET is: ", METMale)
        caloriesPMin = (METMale * Bweight * 3.5) / 200
        print("male calories per minute is: ", caloriesPMin)
    else:
        METFemale = 14.7-(0.13 * age)
        print("female MET is: ", METFemale)
        caloriesPMin = (METFemale * Bweight * 3.5) / 200
        print("female calories per minute is: ", caloriesPMin)
        
    return caloriesPMin
        




