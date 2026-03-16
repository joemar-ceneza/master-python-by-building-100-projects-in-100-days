import random
from hangman_words import word_list
from hangman_ascii import stages, logo

print(logo)
chosen_word = random.choice(word_list)
lives = len(stages)

display = "_" * len(chosen_word)
guessed_letters = set()

print("Word to guess: ", display)

while "_" in display and lives > 0:
    guess_letter = input("Guess a letter: ").lower()

    if guess_letter in guessed_letters:
        print("Your already guessed that letter.")
        continue

    guessed_letters.add(guess_letter)

    if guess_letter not in chosen_word:
        lives -= 1
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life.")

    display = ""
    for char in chosen_word:
        if char in guessed_letters:
            display += char
        else:
            display += "_"

    print(stages[lives - 1])
    print(f"***** Lives left: {lives}/{len(stages)} *****")
    print("Word to guess: ", display)

if "_" not in display:
    print("You won")
else:
    print("Game Over! The word was:", chosen_word)
