import time
i=99
#while loop so it runs until it finishes
while i > 0:
    print(str(i) + ' bottles of beer on the wall')
    time.sleep(1)
    print(str(i) + ' bottles of beer')
    time.sleep(1)
    print('take one down pass it around')
    time.sleep(1)
    print(str(i-1) + ' bottles of beer on the wall')
    time.sleep(1)
    i=i-1

#condition for when it ends
print('no more bottles of beer on the wall')
time.sleep(1)
print('no more bottles of beer')
time.sleep(1)
print('go to the store and buy some more')
time.sleep(1)
print('99 bottles of beer on the wall')
