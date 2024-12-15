import random
import string
from hangman_visual import lives_visual_dict
from words import words


def get_valid_word(words):
    word = random.choice(words)                                                                                     #Randomly chooses word from our words in words.py
    while "-" in word or " " in words:                                                                              #if this choosen word consist of " " or "-" we will take another word with the help of this line
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)                                                                                     #Choose random word from word list
    word_letters = set(word)                                                                                         #Letter used to make that valid word
    alphabet = set(string.ascii_uppercase)                                                                           # string ascii_uppercase will give the uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
    used_letters = set()                                                                                             #set that consist all used words that used by user during playing HANGMAN
    
    lives = 7                                                                                                        #We have 7 trailers

    #Getting User Input
    while lives > 0 and len(word_letters) > 0:                                                                       #This loops will work only if we have "lives>0" and "lenght(word_letter)>0", both true
        #Letters used  
        # " ".join("a", "b", "c") = A B C 
        print("You have",lives,"lives left and you have used letter: ", " ".join(used_letters))

        #What current word is (ie R - B B I T)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(lives_visual_dict[lives])
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(" ")

            else:
                lives = lives - 1
                print("\nYour letter ",user_letter,"is not in word")

        elif user_letter in used_letters:
            print("You are using ",user_letter," 2nd time")

        else:
            print("You entered something wrong")

    if lives == 0:
        print("You have",lives,"lives left and you have used letter: ", " ".join(used_letters))
        print(lives_visual_dict[lives])                                                                              #When suiciding hangman has lives = 0 he will die
        print("You died, sorry. The word was", word)

    else:
        print("Wow, you guessed our whole word ie ", word, "!!!")                                                    #This line comes when you will win ie you guessed all letters in randomly choosen one


if __name__ == "__main__":
    hangman()