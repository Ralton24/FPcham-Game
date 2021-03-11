import random
import time

# Initial Step to Invite in the Game
print("\nWelcome to Hangman Game Create By Israel\n")
Name = input("Please Enter Your Name to Continue: ")
print("Welcome " + Name + "! Best Of Luck!")
time.sleep(2)
print("The Game is About to START" "\nLet Play HangMan")
time.sleep(3)


# Define The Main Function
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""


# A loop to re-execute the Game when the First Round Ends
def play_loop():
    global play_game
    play_game = input("Do You Want To Play Again? Y = yes, N = no \n")
    while play_game not in ["Y", "y", "N", "n"]:
        play_game = input("Do You Want To PLay Again? Y = yes, N = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("thanks For Playing! We Expect You Back Again")
        exit()


# Initialize all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + "Enter Your Guess: \n")
    guess = guess.strip()
    if guess in word:
        already_guessed.extnd([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("Try Another Letter Please.\n")
    else:
        count += 1
        if count == 1:
            time.sleep(2)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", already_guessed, word)
            play_loop()
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != limit:
        hangman()


main()
hangman()






