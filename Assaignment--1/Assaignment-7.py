color=input("Enter Signal Color:")

if color.lower() == 'red':
    print("Stop!")
elif color.lower()=='Yellow':
    print("Ready to go!")
elif color.lower()=='green':
    print("Go!")
else:
    print("Enter valid color!")        