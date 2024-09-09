import pygame
import sys
import random
pygame.init()

w, h, scl = 720, 720, 40
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("snake")


dir = (1, 0)
s = [(5, 5), (5, 4), (5, 3), (5, 2)]
food = [random.randint(0, int(w/scl))*scl, random.randint(0, int(h/scl))*scl]
grow = False
delay = 10
d = delay


def move(s, dir, delay, d, grow):
    delay -= .1
    if delay <= 0:
        if grow:
            if inbounds(dir, s):
                s.insert(0, (s[0][0]+dir[0], s[0][1]+dir[1]))
                grow = False
            else:
                print("haha fuck you")
                quit()
        else:
            del s[-1]
            s.insert(0, (s[0][0]+dir[0], s[0][1]+dir[1]))
        delay = d
    return s, delay, grow

def inbounds(dir, s):
    if (s[0][0]+dir[0] < w/scl and s[0][1]+dir[1] < w/scl) and (s[0][0]+dir[0] > 0 and s[0][1]+dir[1] > 0):
        return True
    else:
        return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            sys.exit()
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dir != (0, 1): dir = (0, -1)
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dir != (0, -1): dir = (0, 1)
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dir != (1, 0): dir = (-1, 0)
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dir != (-1, 0): dir = (1, 0)


    s, delay, grow = move(s, dir, delay, d, grow)
    if s[0][0]*scl == food[0] and s[0][1]*scl == food[1]:
        grow = True
        food[0], food[1] = random.randint(0, int(w/scl-1))*scl, random.randint(0, int(h/scl-1))*scl
        print("score:", len(s))
        print(food) 
    
    for i in range(len(s)-1):
        if s[0] == s[i+1]:
            print("haha fuck you")
            quit()
            sys.exit()
    
    for i in range(len(s)):
        pygame.draw.rect(screen, (0, 255, 0), (s[i][0]*scl+1, s[i][1]*scl+1, scl-2, scl-2))
    pygame.draw.rect(screen, (0, 200, 0), (s[0][0]*scl, s[0][1]*scl, scl, scl))
    pygame.draw.rect(screen, (255, 0, 0), (food[0]+1, food[1]+1, scl-1, scl-1))
    pygame.display.update()
