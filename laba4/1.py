import pygame
from pygame.draw import *
from random import choice, randint

"""Блок настроек игры"""

"""Параметры экрана"""
WIDTH, HEIGHT = 1200, 900
FPS = 10
BLACK = (0, 0, 0)
"""Цвета шаров"""
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


"""Блок используемых компонент в ф-и игры"""

"""Функция отвечающая за создание нового шара в рамках заданного пространства""" 
def new_ball(screen):
    r = randint(50, 80)
    x = randint(100, WIDTH - r)
    y = randint(100, HEIGHT - r)
    color = choice(COLORS)
    circle(screen, color, (x, y), r)
    return x, y, r

"""Функция по проверке попадания в шарик"""
def is_inside_ball(ball_x, ball_y, ball_r, click_x, click_y):
    distance = ((click_x - ball_x) ** 2 + (click_y - ball_y) ** 2) ** 0.5
    return distance <= ball_r

"""Функция реализации логики игры"""
def game(screen, clock, finished):
    score = 0 # Инициализация счетчика из задания
    """Блок обработки событий в ф-и"""
    while not finished:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                print("total score:",score)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Click!')
                click_x, click_y = pygame.mouse.get_pos() # Получение координат курсора мыши в момент клика
                if is_inside_ball(ball_x, ball_y, ball_r, click_x, click_y):
                    print("got")
                    score += 1
        """Блок интерактивных объектов функции""" 
        ball_x, ball_y, ball_r = new_ball(screen) # Cоздание нового шара
        pygame.display.update() # Обновление экрана
        screen.fill(BLACK)
        clock.tick(FPS) # Управление частотой кадров

"""Блок функции main реалищирующей самму игру"""
def main():
    pygame.init() # Инициализация pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Colorful Balls")

    clock = pygame.time.Clock() # Создание объекта для управления fps
    finished = False
    game(screen, clock, finished)  

    pygame.quit() # Завершение работы pygame

main()
