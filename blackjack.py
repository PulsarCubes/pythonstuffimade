#blackjack maybe
import random

#big note you still have so much work to do on this but it is not that hard to do. gl from ur past self <3
#add bets and maybe splits later for funzies?

#variables
run=1
aceValue = 11
#function timeee
def endgame():
    global run
    run = 0
    print(dealerHand)
    print(Hand)
    if dealerHand == 21 or Hand == 21:
        if dealerHand == Hand:
            print('dealer and you both had a blackjack! you tied')
        elif dealerHand == 21:
            print('dealer had a blackjack, you lost')
        else:
            print('you had a blackjack and won!')
    elif dealerHand > 21:
        print('dealer busted you win')
    elif dealerHand > Hand:
        print('dealer had greater hand you lose')
    elif dealerHand < Hand:
        print('you had greater hand and won')
    else:
        print('pulsar is a fucking idiot')
        
    
    #TODO make people bust and shit     
    
    
    '''if dealerHand > 21:
        print('dealer busted, you win!')
    elif dealerHand == 21 and Hand != 21:
        print('dealer got a blackjack, you lose')
    elif Hand == 21 and dealerHand != 21:
        print('you got a blackjack and won')'''
    
#hit stand system that is actually not terrible
def hitstand():
    hitStand = str(input("Do you want to hit or stand?" + '\n'))
    
    global Hand
    global startSecondCard
    global startFirstCard
    global run
    hitCard1int = 0
    hitCard2int = 0
    hit = 0 
    if hitStand == 'hit':
        print('You hit')
        hit=hit+1
        hitCard1 = random.choice(list(cards))
        hitCard2 = random.choice(list(cards))
        if hit==1:
            Hand = startFirstCard + "\n" + startSecondCard + "\n" + hitCard1
            hitCard1int = int((cards[str(hitCard1)]))
            print('Your new hand is'+'\n' +  Hand)
        elif hit==2:
            Hand = startFirstCard + "\n" + startSecondCard + "\n"  + hitCard1 + "\n" + hitCard2
            hitCard2int = int((cards[str(hitCard2)]))
            print('Your new hand is'+'\n' +  Hand)
        else:
            print('You drew 5 cards and won!')
            run=0
        
        
    elif hitStand == 'stand':
        print("You stood")
        Hand=int((cards[str(startFirstCard)])) + int((cards[str(startSecondCard)]))+hitCard1int+hitCard2int
        if Hand > 21:
            print('you busted')
            run = 0
        else: 
            endgame()
    else:
        print('Invalid input')


#cards list obviously
cards = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":aceValue}
#gives user a hand to play with
startFirstCard = random.choice(list(cards))
startSecondCard = random.choice(list(cards))
Hand = startFirstCard + "\n" + startSecondCard
print("Your hand is" + "\n" + Hand)
dealerVisible = random.choice(list(cards))
dealerHidden1 = random.choice(list(cards))
#TODO make this shit not suck maybe 
dealerHand=int((cards[str(dealerVisible)])) + int((cards[str(dealerHidden1)]))
while dealerHand < 17:
    #i know this next line is fucking braindead but i dont want to think of a better way
    dealerHand=dealerHand+int((cards[str(random.choice(list(cards)))]))
print("The dealer's visible card is" + "\n" + dealerVisible)

#gotta do the thing now
while run == 1:
    hitstand()