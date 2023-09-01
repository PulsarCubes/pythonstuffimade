import sys, pygame, time 

pygame.init()
pygame.font.init
start_time = 0
testvar=0
clicks=0
black = (0,0,0)
green = (51, 204, 51)
i = 0
size = width, height = 800, 600

font = pygame.font.SysFont(None, 25)

screen = pygame.display.set_mode(size)

screen.fill((51, 204, 51))

click = pygame.image.load("cube.jpg")

clickrect = click.get_rect()

screen.blit(click, clickrect)
pygame.display.flip()

while True:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if pygame.Rect.collidepoint(clickrect, x,y) == True:
                 while clicks==0:
                    start_time=time.time()
                    clicks+=1
                    i+=1
                 while (i < 12):
                    
                     
                     end_time=time.time()-start_time
                     
                     text = font.render(str(end_time), True, black)
                     screen.blit(text, ( 600,300 ) )
                     i+=1
                 
              
                 text = font.render(str(clicks), True, black)
                 screen.blit(text, ( 600,400 ) )
                 clicks=clicks+1
            pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONUP:
          screen.blit(click, clickrect)
        pygame.display.flip()

        if event.type == pygame.QUIT: sys.exit()

