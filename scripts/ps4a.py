# Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 10

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}



WORDLIST_FILENAME = "C:/Users/varsha/Canopy/scripts/words_1.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# Scoring a word

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    """
   
    score=0
    if len(word)>0:
        for i in word:
            score=score+int(SCRABBLE_LETTER_VALUES[i])
    score=score*len(word)
    if len(word)==n:
        score=score+50
    return score

def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    

def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
#  Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    """
    
    temp=hand.copy()
    for i in word:
        if i in temp.keys():
            if int(temp[i])>0:
                temp[i]=int(temp[i])-1
    return temp

#
# Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    """
    c=0
    if len(word)==0:
        return False
    for i in word:
        if i in hand.keys() and word.count(i)<=int(hand[i]) and word in wordList:
            c=c+1
    return c==len(word) and c<=sum(hand.values())    

#
# Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    """
    c=0
    for i in hand.keys():
        c=c+int(hand[i])
    return c

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      
    """
    totalscore=0
    while(calculateHandlen(hand)>0):
        c=calculateHandlen(hand)
        print "\r\n"
        print('Current Hand:  '), displayHand(hand)
        word=raw_input('Enter word, or a "." to indicate that you are finished: ')# BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
        if word=='.':
            print('Goodbye! Total score: '+str(totalscore)+' points.')
            break
        elif isValidWord(word, hand, wordList)==True:
            score=getWordScore(word, n)
            totalscore=totalscore+score
            hand=updateHand(hand,word)
            print('"'+str(word)+'" earned '+str(score)+' points. Total: '+str(totalscore)+' points')# Keep track of the total score
            if len(word)==c:
                print('')
                print('Run out of letters. Total score: '+str(totalscore)+' points.')
                break
        elif isValidWord(word, hand, wordList)==False:
            print('Invalid word, please try again.')

        
        
    
    


#
#  Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # TO DO ... <-- Remove this comment when you code this function
    hand=[]
    while True:
        c=raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if c=='n':
            hand=dealHand(HAND_SIZE)
            temp1=hand.copy()
            playHand(hand,wordList,HAND_SIZE)
        elif c=='r':
            if hand==[]:
                print('You have not played a hand yet. Please play a new hand first!')
            else:
                playHand(temp1,wordList,HAND_SIZE)
        elif c=='e':
            break
        else:
            print('Invalid command.')
            
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    
    hand=[]
    while True:
        c=raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if c=='n':
            hand=dealHand(HAND_SIZE)
            temp1=hand.copy()
            playHand(hand,wordList,HAND_SIZE)
        elif c=='r':
            if hand==[]:
                print('You have not played a hand yet. Please play a new hand first!')
            else:
                playHand(temp1,wordList,HAND_SIZE)
        elif c=='e':
            break
        else:
            print('Invalid command.')
            
            
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
