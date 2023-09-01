run=1


while run==1:   
    preuwu=input('What would you like to uwuify?'+" (stop to end)" + '\n')
    if preuwu == 'stop' or preuwu == 'STOP' or preuwu == 'Stop':
        run=0
        break
    else:
        def uwumachine(preuwu):
            shit = "lr"
            for bad in shit:
                preuwu=preuwu.replace(bad, 'w')
            preuwu=preuwu+('~')
            print(preuwu)
    uwumachine(preuwu)
    
input('press enter to exit program')