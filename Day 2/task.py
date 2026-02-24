print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
split = int(input("How many people to split the bill? "))
each_person = (total_bill * 0.12 + total_bill) / split
print(f"Each person should pay: ${each_person:.2f}")
