userrange = int(input('how high should the fizzbuzz go?'))

for i in range(1, userrange):
    
    if i % 15 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print ('buzz')
    else:
        print(i)
    i+=1
        
