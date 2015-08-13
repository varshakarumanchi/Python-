'''you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
The computer makes guesses, and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's secret number!
'''
low=0
high=100
bisected_num=(low+high)/2
print('Please think of a number between 0 and 100!')
print('Is your secret number 50?')
while True:
    guess=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if guess=='h':
        high=bisected_num
    elif guess=='l':
        low=bisected_num
    elif guess=='c':
        break
    else:
        print('Sorry, I did not understand your input.')
    bisected_num=(low+high)/2
    print('Is your secret number '+str(bisected_num)+'?')
print('Game over. Your secret number was: '+str(bisected_num))
    
    
        