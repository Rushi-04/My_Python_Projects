
import random
import hangman_art
from hangman_words import word_list

chosen_word = random.choice(word_list)
length_of_chosen_word = len(chosen_word)
end_of_game = False
lives = 6
guess_list = []

print(hangman_art.hangman_logo)

display = []
for letters in chosen_word:
    display.append("_")
print(display)

while not end_of_game:
    guess = input("Guess a letter:").lower()

    if guess not in guess_list:
        guess_list.append(guess)
        for position in range(len(chosen_word)):
            if guess == chosen_word[position]:
                display[position] = guess

        if guess not in display:
            lives -= 1
            print(hangman_art.stages[lives])
            print(f"{guess} is not in the word. You have lost a life.")

        print(display)

        if "_" not in display:
            end_of_game = True
            print("You Win")

        if lives == 0:
            end_of_game = True
            print("You Lose")

    else:
        print(f"You have already guessed {guess}")
        guess_list.append(guess)