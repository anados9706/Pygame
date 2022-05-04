import pygame,sys
screen_width,screen_height = 800,800
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
bg = pygame.image.load("black.bg.jpg")
bg = pygame.transform.scale(bg,(screen_width,screen_height))
path = [((0,400),(200,30)),((200,400),(30,200)),((200,600),(300,30)),((500,200),(30,430)),((500,200),(100,30)),((600,100),(30,130))]
run=True
pygame.mouse.set_pos((50,415))
clock = pygame.time.Clock()
font = pygame.font.Font(None,60)

while run:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()   

    if any (b[0][0]<=pygame.mouse.get_pos()[0]<=b[1][0]+b[0][0] and b[0][1]<=pygame.mouse.get_pos()[1]<=b[1][1]+b[0][1] for b in path):
        print("true")
    else:
        print("false")

    screen.blit(bg,(0,0))
    if ((pygame.mouse.get_pos()[0]-615)**2+(pygame.mouse.get_pos()[1]-130)**2)<=100:
        msg = font.render("WINNER",1,(255,255,0)) 
        screen.blit(msg,(300,100))

    for x in path:
        pygame.draw.rect(screen,(255,255,255),x)
    pygame.draw.circle(screen,(225,0,0),(615,130),10)
    pygame.display.update()     