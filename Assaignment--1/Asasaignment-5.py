Total_bill=int(input("Your Bill is:"))
if Total_bill<=1000:
    print("Your Bill is:",Total_bill,"tk")

else:
    print("Discount is:", Total_bill * 0.1, "tk")
    print("Your Bill is:", Total_bill - (Total_bill * 0.1), "tk")