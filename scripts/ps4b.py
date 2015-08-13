from ps4a import *
import time
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    
    score1=0
    score=0
    Highestscoreword=''
    for word in wordList:
        if isValidWord(word, hand, wordList):
            score=getWordScore(word, n)
        if score>score1:
            Highestscoreword=word
            score1=score
    if len(Highestscoreword)>0:
        return Highestscoreword
    else:
        return None

        


#
#  Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    
    """
    
    totalcompscore=0
    while(calculateHandlen(hand)>0):
        c=calculateHandlen(hand)
        print "\r\n"
        print('Current Hand:  '), (displayHand(hand))
        compword=compChooseWord(hand, wordList, n)
        if compword!=None:
            compscore=getWordScore(compword, n)
            totalcompscore=totalcompscore+compscore
            print('"'+compword+'" earned '+str(compscore)+' points. Total: '+str(totalcompscore)+' points')
            hand=updateHand(hand,compword)
        else:
            break
    print('')
    print('Total score: '+str(totalcompscore)+' points.')

            
# Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    hand=[]
    while True:
        character=raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if character=='n':
            hand=dealHand(HAND_SIZE)
            temp1=hand.copy()
            while True:
                choice=raw_input('Enter u to have yourself play, c to have the computer play: ')
                if choice=='u':
                    playHand(hand,wordList,HAND_SIZE)
                    break
                elif choice=='c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print('Invalid command.')
                    break
        elif character=='r':
            if hand==[]:
                print('You have not played a hand yet. Please play a new hand first!')
            while True:
                choice=raw_input('Enter u to have yourself play, c to have the computer play: ')
                if choice=='u':
                    playHand(temp1,wordList,HAND_SIZE)
                    break
                elif choice=='c':
                    compPlayHand(temp1,wordList,HAND_SIZE)
                    break
                else:
                    print('Invalid command.')
                    break
        elif character=='e':
            break
        else:
            print('Invalid command.')
                
                
   
#
# Build data structures used for entire session and play game
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


