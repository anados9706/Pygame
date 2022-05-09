import pygame,sys
screen_width,screen_height = 800,800

pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
bg = pygame.image.load("black.bg.jpg")
bg = pygame.transform.scale(bg,(screen_width,screen_height))
path_1 = [((0,400),(200,30)),((200,400),(30,200)),((200,600),(300,30)),((500,200),(30,430)),((500,200),(100,30)),((600,100),(30,130))]
path_2 = [((0,400),(200,30)),((200,400),(30,200)),((200,600),(300,30)),((500,200),(30,430)),((500,200),(100,30)),((600,100),(30,130))]
path_3 = [((0,400),(200,30)),((200,400),(30,200)),((200,600),(300,30)),((500,200),(30,430)),((500,200),(100,30)),((600,100),(30,130))]
run=True

pygame.mouse.set_pos((50,415))

clock = pygame.time.Clock()
font = pygame.font.Font(None,60)

def Level_1():
    while run:
        clock.tick(15)
        for event in pygame.event.get():
            print(event)
        if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()   

        if any (b[0][0]<=pygame.mouse.get_pos()[0]<=b[1][0]+b[0][0] and b[0][1]<=pygame.mouse.get_pos()[1]<=b[1][1]+b[0][1] for b in path_1):
            print("true")
        else:
            pygame.mouse.set_pos((50,415))
            print("false")

        screen.fill((0, 0, 0))
        screen.blit(bg,(0,0))
        if ((pygame.mouse.get_pos()[0]-615)**2+(pygame.mouse.get_pos()[1]-130)**2)<=100:
            Level_2()

        for x in path_1:
            pygame.draw.rect(screen,(255,255,255),x)
        pygame.draw.circle(screen,(225,0,0),(615,130),10)
        pygame.display.update()     

def Level_2(): 
    while run:
        clock.tick(15)
        for event in pygame.event.get():
            print(event)
        if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()   

        if any (b[0][0]<=pygame.mouse.get_pos()[0]<=b[1][0]+b[0][0] and b[0][1]<=pygame.mouse.get_pos()[1]<=b[1][1]+b[0][1] for b in path_2):
            print("true")
        else:
            #pygame.mouse.set_pos((50,415))
            print("false")

        screen.fill((0, 0, 0))
        screen.blit(bg,(0,0))
        if ((pygame.mouse.get_pos()[0]-615)**2+(pygame.mouse.get_pos()[1]-130)**2)<=100:
            #Level_2()
            msg = font.render("you won!!",1,(255,255,0)) 
            screen.blit(msg,(300,100))


        for x in path_2:
            pygame.draw.rect(screen,(255,255,255),x)
        pygame.draw.circle(screen,(225,0,0),(615,130),10)
        pygame.display.update()     


#def Level_3():
   # while run:
        clock.tick(15)
        for event in pygame.event.get():
            print(event)
        if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()   

        if any (b[0][0]<=pygame.mouse.get_pos()[0]<=b[1][0]+b[0][0] and b[0][1]<=pygame.mouse.get_pos()[1]<=b[1][1]+b[0][1] for b in path_3):
            print("true")
        else:
            #pygame.mouse.set_pos((50,415))
            print("false")

        screen.fill((0, 0, 0))
        screen.blit(bg,(0,0))
        if ((pygame.mouse.get_pos()[0]-615)**2+(pygame.mouse.get_pos()[1]-130)**2)<=100:
            

        #for x in path_3:
            pygame.draw.rect(screen,(255,255,255),x)
        pygame.draw.circle(screen,(225,0,0),(615,130),10)
        pygame.display.update()     


Level_1()     
Level_2()     
#Level_3()     