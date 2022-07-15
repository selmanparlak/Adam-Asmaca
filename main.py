import random
from art import stages, logo
from words import word_list

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
blank = []

for _ in range(word_length):
    blank += "_"

while not game_is_finished:
    guess = input("Bir harf söyle: ").lower()

    if guess in blank:
        print(f" {guess} harfini zaten söylemiştin.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            blank[position] = letter
    print(f"{' '.join(blank)}")

    if guess not in chosen_word:
        print(f" {guess} harfi bu dünyada yer almıyor.Can kaybettin 💀")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("Kaybettin 😢")

    if "_" not in blank:
        game_is_finished = True
        print("Kazandın 😎")

    print(stages[lives])
