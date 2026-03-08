import random

letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

random_password = []
for i in range(nr_letters):
    random_choice_letters = random.choice(letters)
    random_password.append(random_choice_letters)

for i in range(nr_numbers):
    random_choice_numbers = random.choice(numbers)
    random_password.append(random_choice_numbers)

for i in range(nr_symbols):
    random_choice_symbols = random.choice(symbols)
    random_password.append(random_choice_symbols)

full_random = random.sample(random_password, len(random_password))
final_random = "".join(full_random)
print(f"Your password is: {final_random}")
