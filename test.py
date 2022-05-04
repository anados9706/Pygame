import pygame
import random
import time

pygame.init()
# all fonts used
font1 = pygame.font.SysFont("comicsansms", 49, True)
font2 = pygame.font.SysFont("comicsansms", 150, True)
font3 = pygame.font.SysFont("comicsansms", 28, True)

# creates the string that displays time
def get_time(hours,minutes,seconds):
    if len(str(hours)) > 1:
        a = str(hours)
    else:
        a = "0" + str(hours)

    if len(str(minutes)) > 1:
        b = str(minutes)
    else:
        b = "0" + str(minutes)

    if len(str(seconds)) > 1:
        c = str(seconds)
    else:
        c = "0" + str(seconds)

    return a + ":" + b + ":" + c

# creates the time counter
def draw_time(start_time,pause_time):
    hours = 0
    minutes = 0
    seconds = 0
    current_time = time.time() - pause_time - start_time
    if current_time > 3600:
        while True:
            if current_time - 3600 > 0:
                hours += 1
                current_time -= 3600
            else:
                while True:
                    if current_time - 60 > 0:
                        minutes += 1
                        current_time -= 60
                    else:
                        seconds += int(current_time)
                        break
                break

    else:
        while True:
            if current_time - 60 > 0:
                minutes += 1
                current_time -= 60
            else:
                seconds += int(current_time)
                break

    return [font1.render(get_time(hours, minutes, seconds), True, (0, 0, 0), (255, 255, 255)), get_time(hours, minutes, seconds)]

class cell:
    def __init__(self,up,down,left,right):
        self.visited = False
        self.walls = [up,down,left,right]

class labyrinth:
    # generates the maze
    def __init__(self,id):
        self.id = id
        self.walls = []
        self.maze_walls = []
        self.cells = []

        x = 0
        t = 0

        # creates all cell within the maze
        for f in range(22):
            for s in range(28):
                # if command makes sure no cellls are created where the clock is supposed to be
                if not (f in (0,1,2) and s > 20):
                    self.cells.append(cell((x + 8, t, 25, 8), (x + 8, t + 33, 25, 8), (x, t + 8, 8, 25), (x + 33, t + 8, 8, 25)))
                x += 33
            x = 0
            t += 33

        # generates maze using prim's algorithm
        for v in self.cells[0].walls:
            self.maze_walls.append(v)
            self.walls.append(v)

        self.cells[0].visited = True

        while len(self.walls) > 0:
            wall = random.choice(self.walls)
            # checks which cells are divided by the wall
            divided_cells = []
            for u in self.cells:
                if wall in u.walls:
                    divided_cells.append(u)

            if len(divided_cells) > 1 and (not ((divided_cells[0].visited and divided_cells[1].visited) or ((not divided_cells[0].visited) and (not divided_cells[1].visited)))):
                # checks which cells have been visited
                for k in divided_cells:
                    k.walls.remove(wall)

                    if k.visited == False:
                        k.visited = True

                    for q in k.walls:
                        if not q in self.walls:
                            self.walls.append(q)

                        if not q in self.maze_walls:
                            self.maze_walls.append(q)

                    if wall in self.maze_walls:
                        self.maze_walls.remove(wall)

            self.walls.remove(wall)

        for j in range(0,736,33):
            for i in range(0,951,33):
                self.maze_walls.append((i, j, 8, 8))

    # draws the maze
    def draw(self, goal):
        screen.fill((0, 0, 0))

        for k in self.maze_walls:
            pygame.draw.rect(screen, color, pygame.Rect(k[0],k[1],k[2],k[3]))

        pygame.draw.rect(screen, color, pygame.Rect(695, 0, 300, 105)) # clock background
        pygame.draw.rect(screen, (0, 255, 0), goal) # finish

id = 0
running = True
while running:
    screen = pygame.display.set_mode((930, 733))
    done = False
    color = (0, 128, 255) # color of the walls
    x = 16
    y = 16
    clock = pygame.time.Clock()
    start = time.time()
    id += 1
    maze = labyrinth(id)
    goal = pygame.Rect(899,701,25,25)
    victory = False
    speed = 4 # movement speed
    pause = False
    pause_time = 0 # time spent in pause menue

    while not done:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    if pause:
                        pause = False
                        pause_time += time.time() - pause_time_start
                    else:
                        pause = True
                        pause_time_start = time.time()

                if event.key == pygame.K_RETURN:
                    done = True

        if pause:
            screen.fill((0, 0, 0))
            pause_text = font2.render("PAUSE",True,(255,255,255))
            screen.blit(pause_text, (468 - (pause_text.get_width() // 2), 368 - (pause_text.get_height() // 2)))

        # the actual game
        if not victory and not pause:
            move_up = True
            move_down = True
            move_left = True
            move_right = True
            pressed = pygame.key.get_pressed()

            # movment
            if pressed[pygame.K_w] or pressed[pygame.K_UP]:
                # checks if their is a overlap with the wall
                for m in maze.maze_walls:
                    player = pygame.Rect(x, y - speed, 10, 10)
                    if player.colliderect(pygame.Rect(m[0],m[1],m[2],m[3])):
                        move_up = False
                        break
                if move_up:
                    y -= speed

            if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
                player = pygame.Rect(x, y + speed, 10, 10)
                for m in maze.maze_walls:
                    if player.colliderect(pygame.Rect(m[0],m[1],m[2],m[3])):
                        move_down = False
                        break
                if move_down:
                    y += speed

            if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
                player = pygame.Rect(x - speed, y, 10, 10)
                for m in maze.maze_walls:
                    if player.colliderect(pygame.Rect(m[0],m[1],m[2],m[3])):
                        move_left = False
                        break
                if move_left:
                    x -= speed

            if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
                player = pygame.Rect(x + speed, y, 10, 10)
                for m in maze.maze_walls:
                    if player.colliderect(pygame.Rect(m[0],m[1],m[2],m[3])):
                        move_right = False
                        break
                if move_right:
                    x += speed

            # checks if player has reached the goal
            if goal.colliderect((x, y, 10, 10)):
                victory = True

            # draws the screen
            maze.draw(goal)
            text = draw_time(start, pause_time)
            pygame.draw.rect(screen, (255, 100, 0), pygame.Rect(x,y,10,10))
            screen.blit(text[0], (700, 15))

        # victory screen
        if victory:
            screen.fill((0, 0, 0))
            time_text = font1.render("Time Taken: " + text[1],True,(255,255,255))
            victory_text = font2.render("VICTORY!",True,(255,255,255))
            reset = font3.render("(Press Enter to Start New Game)",True,(255,255,255))

            screen.blit(victory_text,(468 - (victory_text.get_width() // 2), 328 - (victory_text.get_height() // 2)))
            screen.blit(time_text, (468 - (time_text.get_width() // 2), (248 - (time_text.get_height() // 2)) + victory_text.get_height()))
            screen.blit(reset, (468 - (reset.get_width() // 2), (248 - (reset.get_height() // 2)) + victory_text.get_height() + time_text.get_height()))

        clock.tick(60)
        pygame.display.flip()