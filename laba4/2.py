import pygame
from pygame.draw import *
from random import choice, randint

"""Блок настроек игры"""

"""Параметры экрана"""
WIDTH, HEIGHT = 800, 600
FPS = 60
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

"""Блок используемых компонентов в игры"""

"""Функция по созданию шаров, готовых к изменениям в соответсвтии с задачей игры"""
def new_ball(screen):
    r = randint(30, 50)
    x = randint(100, WIDTH - r)
    y = randint(100, HEIGHT - r)
    color = choice(COLORS)  # случайный цвет из списка COLORS
    vx = randint(-25, 25)  # случайная скорость по  X
    vy = randint(-25, 25)  # случайная скорость по  Y
    return {'x': x, 'y': y, 'r': r, 'vx': vx, 'vy': vy, 'color': color}  # в качетсве результата выполнения функциии возвращаем словарь
"""Функция по проверке попадания в шарик"""
def is_inside_ball(ball_x, ball_y, ball_r, click_x, click_y):
    distance = ((click_x - ball_x) ** 2 + (click_y - ball_y) ** 2) ** 0.5
    return distance <= ball_r
"""Функция игры"""
def game(screen, clock, finished, balls):  # передача параметров 
    score = 0
    while not finished:
        """Блок технических составляющих игры"""
        screen.fill(BLACK) # Отрисовка шариков
        for ball in balls:
            circle(screen, ball['color'], (ball['x'], ball['y']), ball['r'])
        pygame.display.update() # Обновление экрана ,делает измененя видимыми для пользователя
        clock.tick(FPS) # Управление частотой кадров

        """Блок обработки событий в функциии"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                print("total score:",score)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("click")
                click_x, click_y = pygame.mouse.get_pos()
                """проверка на попадание курсора в область каждого шара"""
                for ball in balls:
                    if is_inside_ball(ball['x'], ball['y'], ball['r'], click_x, click_y):
                        print("bdish")
                        balls.remove(ball) # удаление шарика из списка
                        balls.append(new_ball(screen)) # Добавление нового шарика в другом месте
                        score += 1

        """Обновление координат шариков при их столкновение с границами экрана"""
        for ball in balls: # запускаем шарики в движение
            ball['x'] += ball['vx']
            ball['y'] += ball['vy']
            """Реализация отскока в случайную сторону с разной скоростью( углубленная реализация фактора непредсказуемости)"""
            if ball['x'] < ball['r']: # слева
                ball['x'] = ball['r'] + 1
                ball['vx'] = randint(1, 25) if ball['vx'] < 0 else randint(-25, -1)  
                ball['vy'] = randint(1, 25) if ball['vy'] < 0 else randint(-25, -1)
            elif ball['x'] > WIDTH - ball['r']: # справа
                ball['x'] = WIDTH - ball['r'] - 1
                ball['vx'] = randint(-25, -1) if ball['vx'] > 0 else randint(1, 25)
                ball['vy'] = randint(-25, -1) if ball['vy'] > 0 else randint(1, 25) 

            if ball['y'] < ball['r']: # сверху
                ball['y'] = ball['r'] + 1
                ball['vx'] = randint(1, 25) if ball['vx'] < 0 else randint(-25, -1)
                ball['vy'] = randint(1, 25) if ball['vy'] < 0 else randint(-25, -1) 
            elif ball['y'] > HEIGHT - ball['r']: # снизу 
                ball['y'] = HEIGHT - ball['r'] - 1
                ball['vx'] = randint(-25, -1) if ball['vx'] > 0 else randint(1, 25)
                ball['vy'] = randint(-25, -1) if ball['vy'] > 0 else randint(1, 25)  

def main():
    pygame.init() # Инициализация pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("colorful balls")
    
    clock = pygame.time.Clock() # Создание объекта clock для управления fps
    finished = False
    
    balls = [new_ball(screen) for i in range(17)] # Создание списка шаров
    game(screen, clock, finished, balls)
    pygame.quit()

main()
