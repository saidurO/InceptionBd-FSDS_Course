user_name=input("Enter User Name:")
password=int(input("Enter your password:"))

if user_name=='admin'and password==12345:
    print("Log in successfull!")

else:
    print("Invalid Credentials!")