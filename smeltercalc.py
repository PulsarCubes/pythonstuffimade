import math
choice = (input('do you want to know how much iron you need or check with how many you have?\(type need or have\)\n'))
if choice == 'have':
    iron = int((input('how much iron do you have?\n')))
    #accounting for base cost
    iron = iron-20
    #rail cost calc
    iron = iron/15
    iron = iron/(2*6/16)
    #hopper cost

    #rounding
    ironfinal = math.floor(iron)
    print(ironfinal) 
elif choice == 'need':
    length=int(input('how long will it be/how many furnaces?' + '\n'))
    hc=length*15
    railcost=length*2*6/16
    preovr=railcost+hc+20
    ovr = math.ceil(preovr)
    print('you will need ' + str(ovr) + ' iron')
    stacksnorem = ovr // 64
    stacksrem = ovr % 64
    print('which is ' + str(stacksnorem) + ' stacks and ' + str(stacksrem))
    woodcost=length*24
    woodcost=woodcost+(length*2*1/16*0.5)
    #adding base chests and lever
    woodcost=woodcost+43
    math.ceil(woodcost)
    print('you will also need ' + str(woodcost) + ' wood')
    woodstacksnorem = woodcost // 64
    woodstacksrem = woodcost % 64
    math.ceil(woodstacksnorem)
    if woodstacksrem == 0:
        print('which is ' + str(woodstacksnorem) + ' stacks')
    elif woodstacksrem>0:
        print('which is ' + str(woodstacksnorem) + ' stacks and ' + str(woodstacksrem))
    else:
        print('pulsar fucked up lol')
else:
    print('invalid answer')


