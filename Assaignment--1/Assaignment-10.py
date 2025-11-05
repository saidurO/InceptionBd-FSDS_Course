Unit=int(input("Enter your consumed unit:"))
if Unit<=100:
    print("Your Bill is 5 tk per unit:",Unit*5,"tk")
elif Unit<=200:
    print("Your Bill is 7 tk per unit:",Unit*7,"tk")
else:
    print("Your Bill is 10 tk per unit:",Unit*10,"tk")    