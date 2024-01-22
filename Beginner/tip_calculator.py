print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10, 12, 15? "))
people = int(input("how many people to split the bill? "))

amount_of_payment = round(total_bill * ((tip+100)/100) / people,2)

print(f"Each person should pay {amount_of_payment}")