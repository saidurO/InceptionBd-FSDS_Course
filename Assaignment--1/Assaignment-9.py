
age = int(input("Enter your age: "))
qualification = input("Enter your qualification: ").lower()

if age >= 18 and qualification == "graduate":
    print("Eligible for Job")
else:
    print("Not Eligible")
