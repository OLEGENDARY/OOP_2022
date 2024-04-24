import math
from random import choice, randint

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GRAY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
       
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
       
        # FIXED
        self.x += self.vx
        self.vy += 0.98
        self.y += self.vy


    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
     
        # FIXED
        distance = math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)
        return distance < self.r + obj.r


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GRAY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)

        x_end = int(20 + max(self.f2_power, 100) * math.cos(self.an))
        y_end = int(450 - max(self.f2_power, 100) * math.sin(self.an))

        
        new_ball.x = x_end
        new_ball.y = y_end

        new_ball.r += 5
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)

        self.f2_on = 0
        self.f2_power = 10


    def targetting(self, event):
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GRAY

    def draw(self):
        # FIXIT don't know how to do it
        x_end = int(20 + max(self.f2_power, 100) * math.cos(self.an))
        y_end = int(450 - max(self.f2_power, 100) * math.sin(self.an))
        pygame.draw.line(self.screen, self.color, [20, 450], [x_end, y_end] ,30)


    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GRAY


class Target:
    def __init__(self, screen, vx = 0 ,vy = 0 ):
        self.screen = screen
        self.new_target()
       
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)

    # FIXED

    def move(self):
        """
        self.x += self.vx
        """

        self.y += self.vy

        """
        if self.x < self.r or self.x + self.r > WIDTH:
            self.vx = -self.vx  
        """

        if self.y < self.r or self.y + self.r > HEIGHT:
            self.vy = -self.vy  


    def new_target(self): 

        x = self.x = randint(600, 780)
        y = self.y = randint(300, 550)
        r = self.r = randint(20, 50)
        color = self.color = choice(GAME_COLORS)

    def hit(self, points=1): 

        self.points += points

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)

targets = [Target(screen) for target in range(2)]

finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    
    for target in targets:
        target.draw()
        target.move()

    for b in balls:
        b.draw()
        b.move()

    

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    
    

    for target in targets:
        for b in balls:
            if b.hittest(target):  
                balls.remove(b)
                targets.remove(target)
                """
                balls.append(Ball(screen))
                """
                targets.append(Target(screen))
                break  
        gun.power_up()

    

    pygame.display.update()

pygame.quit()

