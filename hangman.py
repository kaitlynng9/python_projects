import random

# selects a random word from text file
def get_word():
    words = []
    in_file = open ("C:\\Users\\Hp 840 G4\\Code Projects\\Hangman\\wordlist.txt", "r")
    for word in in_file:
        new_word = word.strip('\n')
        words.append(new_word)
    index = random.randint(0, len(words))
    return(words[index].lower())

# format print of blanks
def print_blanks(blanks):
    for blank in blanks:
        print(blank, end=' ')

# sets up blanks and fills them in while prompting user for letting guesses
def hangman(word):
    # print initial blanks
    blanks = []
    for letter in word:
        blanks.append('_')

    # break word into a list by letter
    word_letters = list(word)

    # store guessed letters here
    guessed = []
    wrong_guesses = 0
    correct = 0
    lives = 10

    # prompt user for letters
    while (wrong_guesses < 11) or (correct < len(word)): # max 10 guesses
        print('Guessed Letters:', guessed) # display guesses
        print('Word: ', end='')
        print_blanks(blanks)
        print('\n')
        print('Number of Lives Left:', lives)
        letter = input('Guess a letter:').lower()

        if letter not in guessed:
            guessed.append(letter)
            for i in range(len(word_letters)):
                if letter == word_letters[i]:
                    correct += 1
                    blanks[i] = letter
            if letter not in word_letters:
                wrong_guesses += 1
                lives -= 1

        print('\n')

        if correct == len(word) or wrong_guesses > 10:
            break

    if correct == len(word):
        print('Finished!\n', word)
    if wrong_guesses > 10:
        print('You Failed.')

def main():
    print('Starting Hangman game...\nYou have ten lives...\nCategory is...\nAnimals')
    rand_word = get_word()
    hangman(rand_word)
main()