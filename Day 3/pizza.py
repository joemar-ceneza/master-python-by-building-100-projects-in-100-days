print("Welcome to Python Pizza Deliveries!")

small_pizza = 15
medium_pizza = 20
large_pizza = 25

total_bill = 0

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    total_bill = small_pizza
elif size == "M":
    total_bill = medium_pizza
elif size == "L":
    total_bill = large_pizza
else:
    print("Wrong input")

if pepperoni == "Y":
    if size == "S":
        total_bill += 2
    else:
        total_bill += 3

if extra_cheese == "Y":
    total_bill += 1

print(f"Your final bill is: ${total_bill}")
