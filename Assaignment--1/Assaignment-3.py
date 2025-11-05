Marks = int(input("Enter your marks:"))
if Marks >= 90 and Marks <= 100:
    print("Grade A+")
elif Marks>100:
    print("Invalid Marks")
elif Marks >= 80:
    print("Grade A")
elif Marks >= 70:
    print("Grade B")
elif Marks >= 60:
    print("Grade C")
else:
    print("You Failed")