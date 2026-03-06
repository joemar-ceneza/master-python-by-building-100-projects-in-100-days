print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("Can ride")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    elif age >= 45 and age <= 55:
        bill = 0
    else:
        bill = 12
    photos = input("Do you want photos? yes or no: ")
    if photos == "yes":
        bill += 3

    print(f"The total bill is ${bill}")
else:
    print("Can't ride")
