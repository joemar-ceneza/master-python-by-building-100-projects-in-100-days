import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

list_of_index = [rock, paper, scissors]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
computer_choice = random.randint(0, len(list_of_index) - 1)

if user_choice < 0 or user_choice >= len(list_of_index) - 1:
    print("You typed an invalid number, you lose!")
else:
    print(list_of_index[user_choice])
    print(f"Computer choose: \n{list_of_index[computer_choice]}")
    if user_choice == computer_choice:
        print("It's a draw")
    elif user_choice == 0 and computer_choice == 1:
        print("You Lose")
    elif user_choice == 1 and computer_choice == 2:
        print("You Lose")
    elif user_choice == 2 and computer_choice == 1:
        print("You Lose")
    else:
        print("You Won")
