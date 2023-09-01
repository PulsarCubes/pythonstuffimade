import random
import time

run=1


while run==1:
    #taking and testing user inputs
    print('welcome to rock paper scissors')
    time.sleep(1)
    userinput=input('put in r, p, s, or stop\n')
    

    if not userinput in ['r','s','p', 'stop']:
        print('invalid input, only put r, p, s or stop')

    elif userinput == 'stop':
        run==0
        break
    elif run==1:
        time.sleep(0.5)
        print('rock')
        time.sleep(0.5)
        print('paper')
        time.sleep(0.5)
        print('scissors')
        time.sleep(0.5)
        print('shoot')
    ai=random.randint(1,3)
#making comparison easier
    if ai==1:
        ai='r'
    elif ai==2:
        ai='s'
    elif ai==3:
       ai='p'
    else:
        print('ai screwed up')
    #pretty bad code i probably could've used a function for, i guess wait for v2
    if userinput==ai:
        print('you tied!')
        continue
    elif ai=='r' and userinput=='s':
        print('you lose, rock smashes scissors!')
        continue
    elif ai=='s' and userinput=='p':
        print('you lose, scissors cut paper!')
        continue
    elif ai=='p' and userinput=='r':
        print('you lose, paper covers rock!')
        continue
    elif ai=='s' and userinput=='r':
        print('you win, rock smashes scissors!')
        continue
    elif ai=='r' and userinput=='p':
        print('you win, paper covers rock!')
        continue
    elif ai=='p' and userinput=='s':
        print('you win, scissors cut paper!')
        continue
    else:
        print('something went wrong')
        continue
print('see you later')
