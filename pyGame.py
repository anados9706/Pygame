import pygame,sys,time
screen_width,screen_height = 800,800

from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
bg = pygame.image.load("black.bg.jpg")
bg = pygame.transform.scale(bg,(screen_width,screen_height))
path_1 = [((30,450),(200,300)),((30,450),(450,230)),((330,150),(150,500)),((330,150),(350,30)),((600,30),(80,150))]
path_2 = [((35,75),(720,120)),((35,75),(120,350)),((35,400),(340,100)),((290,285),(85,215)),((290,285),(465,70)),((700,285),(60,330)),((35,530),(700,85)),((35,530),(200,250)),((35,700),(730,80))]
path_3 = [((40,650),(700,70)),((40,550),(70,100)),((40,550),(680,60)),((660,450),(60,100)),((50,450),(660,50)),((50,350),(50,100)),((50,350),(650,50)),((650,300),(50,50)),((60,280),(640,35)),((60,250),(35,50)),((60,230),(600,35)),((640,190),(20,40)),((80,190),(570,20)),((80,170),(16,30)),((80,160),(570,16)),((638,140),(12,20)),((350,140),(300,12)),((350,120),(12,20)),((335,70),(50,50))]
sound = pygame.mixer.Sound("scream.wav")
run=True

pygame.mouse.set_pos((100,600))

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
            pygame.mouse.set_pos((50,700))
            print("false")

        screen.fill((0, 0, 0))
        screen.blit(bg,(0,0))
        if ((pygame.mouse.get_pos()[0]-615)**2+(pygame.mouse.get_pos()[1]-130)**2)<=100:
            Level_2()

        for x in path_1:
            pygame.draw.rect(screen,(0,255,255),x)
        pygame.draw.rect(screen,(255,48,48),x)
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
            pygame.mouse.set_pos((680,135))
            print("false")

        screen.fill((0, 0, 0))
        screen.blit(bg,(0,0))
        if ((pygame.mouse.get_pos()[0]-615)**2+(pygame.mouse.get_pos()[1]-130)**2)<=100:
            Level_3()

        for x in path_2:
            pygame.draw.rect(screen,(0,255,255),x)
        pygame.draw.rect(screen,(225,48,48),x)
        pygame.display.update()     


def Level_3():
    while run:
        clock.tick(15)
        for event in pygame.event.get():
            print(event)
        if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()   

        if any (b[0][0]<=pygame.mouse.get_pos()[0]<=b[1][0]+b[0][0] and b[0][1]<=pygame.mouse.get_pos()[1]<=b[1][1]+b[0][1] for b in path_3):
            print("true")
        else:
            pygame.mouse.set_pos((680,750))
            print("false")

        screen.fill((0, 0, 0))
        screen.blit(bg,(0,0))
        if ((pygame.mouse.get_pos()[0]-615)**2+(pygame.mouse.get_pos()[1]-130)**2)<=100:
            sound.play ()
            time.sleep(1)

        for x in path_3:
            pygame.draw.rect(screen,(0,255,255),x)
        pygame.draw.rect(screen,(225,48,48),x)
        pygame.display.update()     

Level_1()          