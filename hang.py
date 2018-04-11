import random
import string

WORDLIST_FILENAME = "palavras.txt"

def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."

    inFile = open(WORDLIST_FILENAME, 'r', 0)# inFile: file
    line = inFile.readline()# line: string
    wordlist = string.split(line)# wordlist: list of strings

    print " ", len(wordlist), "words loaded."
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getGuessedWord():
    guessed = ''
    return guessed

def getAvailableLetters():

    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase
    return available

def initialMessage(secretWord):

    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'

def availableLetters(available, lettersGuessed):
    for letter in available:
        if letter in lettersGuessed:
            available = available.replace(letter, '')

    print 'Available letters', available

def result(secretWord, lettersGuessed):

    if isWordGuessed(secretWord, lettersGuessed) == True:
        print 'Congratulations, you won!'
    else:
        print 'Sorry, you ran out of attempts. The word was', secretWord, '.'

def checkGuessedLetter(letter, secretWord, lettersGuessed):

    guessed = getGuessedWord()
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_'
    return guessed

def gameEngine(attempts,lettersGuessed, secretWord):

    while isWordGuessed(secretWord, lettersGuessed) == False and attempts > 0:
        print 'You have ', attempts, 'attempts left.'

        available = getAvailableLetters()
        availableLetters(available, lettersGuessed)

        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:

            guessed = checkGuessedLetter(letter, secretWord, lettersGuessed)
            print 'Oops! You have already guessed that letter: ', guessed

        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = checkGuessedLetter(letter, secretWord, lettersGuessed)

            print 'Good guess: ', guessed
        else:
            attempts -=1
            lettersGuessed.append(letter)

            guessed = checkGuessedLetter(letter, secretWord, lettersGuessed)

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        result(secretWord, lettersGuessed)


def hangman(secretWord):

    attempts = 8
    lettersGuessed = []
    initialMessage(secretWord)
    gameEngine(attempts,lettersGuessed, secretWord)

secretWord = loadWords()
hangman(secretWord)
