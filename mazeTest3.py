import pygame,sys
screen_width,screen_height=800,800
pygame.init()
screen=pygame.display.set_mode((screen_width,screen_height))
bg = pygame.image.load("black bg.png")
by = pygame.transform.scale(bg,(screen_width,screen_height))
path=[((0,400),(20,300)),((200,400),(30,200)),((200,600),(300,30)),((500,300),(30,330)),((500,300),(250,30))]

while True:
    for event in pygame.event.net():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg,(0,0))
    for x in path:
        pygame.draw.rect(screen,(255,255,255),x)        

    pygame.display.update()       