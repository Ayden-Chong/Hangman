import random
import os
from hangman_images import starting_image, lives_images, lose_image, win_image
from hangman_strings import word_list

is_game_over = False
num_lives = len(lives_images) - 1

# Step 1: Print the starting_image onto console when we start the game

# Step 2: Choose a word from word_list to be mystery word for hangman game

# Step 3: Show clue to player

# Step 4: Get User to guess letter

# Step 5: Check if Letter guessed is in Mystery Word

# Step 6: Check if Letter guessed is not in Mystery Word

# Step 7: Check if Player won or lost

# Enclose Steps 4 to 7 in while loop so long as game is not over

print(starting_image)

word= word_list[random.randrange(0, len(word_list))]
word_length = len(word)
clue = []
for i in range(word_length):
  clue.append("_")
print(" ".join(clue))

while is_game_over == False:
  guess= input("Guess a letter: ").lower().strip()
  while not len(guess) == 1 or not guess.isalpha():
    guess=input("Please give a valid letter: ").lower().strip()
  os.system('cls');
  for index in range(word_length):
    letter = word[index]
    if letter == guess:
      clue[index] = letter
  print(" ".join(clue))
  
  if guess not in word: 
    print("Oops! You guessed a wrong letter!Losing a life.")
    num_lives-=1
  print(lives_images[num_lives])
  
  if not "_" in clue: 
    is_game_over=True
    print(win_image)
  
  if num_lives == 0: 
    is_game_over = True
    print(lose_image)
    print("Oh no! You ran out of lives! The word is {}".format(word))
  

  
