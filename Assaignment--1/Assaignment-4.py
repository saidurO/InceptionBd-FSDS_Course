Age=int(input("Enter your age:"))
if Age<5:
    print('For you-"Ticket price is free"')

elif 5>=Age<=18:
    print("50% Discount")

elif Age>=60:
    print("30% Discount")

else:
    print("Full price")     