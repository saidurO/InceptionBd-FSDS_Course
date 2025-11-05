# Get balance and withdrawal amount
balance = float(input("Enter your account balance: "))
withdraw = float(input("Enter withdrawal amount: "))

# Validate transaction
if withdraw > balance:
    print("Insufficient Balance")
else:
    balance -= withdraw
    print("Transaction Successful")
    print("Remaining Balance:", balance)
