import random
userrange = int(input('how high do you want the numbers to go?\n'))
correctnum = random.randint(1,userrange)
guesscount = int(input('how many guesses do you want?\n'))


for i in range(guesscount):
    guess=int(input('Guess the number between 1 and ' + str(userrange)+'\n'))
    if guess==correctnum:
        print('You got it correct! the number was '+ str(correctnum))
        break
    elif guess>correctnum:
        print('the number is lower')
    elif guess<correctnum:
        print('the number is higher')
    else:
        print('invalid guess')
if guess==correctnum:
    print('congrats!')
else:
    print('sorry you ran out of guesses')
    
   

