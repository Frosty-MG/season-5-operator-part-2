hieght =float(input("enter your hieght in centimeter"))
weight=float(input("enter your weight in kg "))
bmi=weight/(hieght/100)**2
#if the bmi is less then 18.4 [ under wieght ] , if bmi is less then 24.9 [helthy ], if bmi is less then 29.9 , you r over wieght , else you are very obiese
if bmi <= 18.4:
    print("you are under weight") 
elif bmi <=24.9:
    print("you are healthy")    
elif bmi <=29.9:
    print("YOU ARE OVER WEIGHT!")
else:
    print("YOU ARE VERY OBIESE!!")

 