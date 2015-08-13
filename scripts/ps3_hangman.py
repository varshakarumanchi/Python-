# Hangman game

import random
import string

WORDLIST_FILENAME = "C:/Users/varsha/Canopy/scripts/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    count=0
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            count=count+1
    return count==len(secretWord)
            
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
   
    length=len(secretWord)
    string_return=''
    for i in range(length):
        if secretWord[i] in lettersGuessed:
            string_return=string_return+secretWord[i]
        else:
            string_return=string_return+'_'
    return string_return
    
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    string1=string.ascii_lowercase
    string2=''
    for i in range(len(string1)):
        if string1[i] in lettersGuessed:
            continue
        else:
            string2= string2+string1[i]
    return string2
    
def hangman(secretWord):
    
    
    #secretWord=chooseWord(wordlist)
    num_guesses=8
    char=''
    for i in range(len(secretWord)):
        string3='_'
    string5=''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+str(len(secretWord))+' letters long.')
    print('-------------')
    print('You have 8 guesses left.')
    print('Available letters: abcdefghijklmnopqrstuvwxyz')
    while char!=secretWord or num_guesses>=0:
        char=str(raw_input('Please guess a letter: '))
        char_inlower=char.lower()
        string5=string5+char_inlower
        if char_inlower in string5[:-1]:
            print("Oops! You've already guessed that letter: "+ string3)
        elif char_inlower in secretWord:
            string3=getGuessedWord(secretWord, string5)
            print('Good guess: '+string3)
            if(string3==secretWord):
                print('-------------')
                print('Congratulations, you won!')
                break
        else:
            print('Oops! That letter is not in my word:'+string3)
            num_guesses=num_guesses-1
            if num_guesses==0:
                print('-------------')
                print('Sorry, you ran out of guesses. The word was '+secretWord)
                break
        print('-------------')
        print('You have '+str(num_guesses)+' guesses left.')
        print('Available letters: '+getAvailableLetters(string5))
                   


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
