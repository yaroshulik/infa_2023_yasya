import pygame
from pygame.draw import *
# После импорта библиотеки, необходимо её инициализировать:
pygame.init()

# И создать окно:
FPS = 30
screen = pygame.display.set_mode((600, 400))
# здесь будут рисоваться фигуры
# ...
rect(screen, (204,255,255), (0, 0, 600, 175))
rect(screen, (102, 204, 0), (0, 175, 600, 225))
rect(screen, (153, 76, 0), (100, 150, 120, 90))
rect(screen, (0, 0, 0), (100, 150, 120, 90), 2)
polygon(screen, (255, 0, 0), [(100,150), (160,100),
                               (220,150), (100,150)])
polygon(screen, (0, 0, 0), [(100,150), (160,100),
                               (220,150), (100,150)], 2)
rect(screen, (0, 153, 153), (140, 175, 40, 30))
rect(screen, (255, 128, 0), (140, 175, 40, 30), 3)
circle(screen, (255, 255, 255), (200, 80), 30)
circle(screen, (0, 0, 0), (200, 80), 30, 1)
circle(screen, (255, 255, 255), (235, 80), 30)
circle(screen, (0, 0, 0), (235, 80), 30, 1)
circle(screen, (255, 255, 255), (275, 80), 30)
circle(screen, (0, 0, 0), (275, 80), 30, 1)
circle(screen, (255, 255, 255), (310, 80), 30)
circle(screen, (0, 0, 0), (310, 80), 30, 1)
circle(screen, (255, 255, 255), (290, 45), 30)
circle(screen, (0, 0, 0), (290, 45), 30, 1)
circle(screen, (255, 255, 255), (255, 45), 30)
circle(screen, (0, 0, 0), (255, 45), 30, 1)
circle(screen, (255, 255, 255), (220, 45), 30)
circle(screen, (0, 0, 0), (220, 45), 30, 1)

rect(screen, (0, 0, 0), (470.5, 158, 20, 70))
circle(screen, (15, 83, 14), (485, 75), 30)
circle(screen, (0, 0, 0), (485, 75), 30, 1)
circle(screen, (15, 83, 14), (450, 100), 30)
circle(screen, (0, 0, 0), (450, 100), 30, 1)
circle(screen, (15, 83, 14), (520, 100), 30)
circle(screen, (0, 0, 0), (520, 100), 30, 1)
circle(screen, (15, 83, 14), (485, 120), 30)
circle(screen, (0, 0, 0), (485, 120), 30, 1)
circle(screen, (15, 83, 14), (455, 140), 30)
circle(screen, (0, 0, 0), (455, 140), 30, 1)
circle(screen, (15, 83, 14), (505, 140), 30)
circle(screen, (0, 0, 0), (505, 140), 30, 1)

# после чего, чтобы они отобразились на экране, экран нужно обновить:
pygame.display.update()
clock = pygame.time.Clock()
finished = False
# Эту же команду нужно будет повторять, если на экране происходят изменения.

# Наконец, нужно создать основной цикл, в котором будут отслеживаться
# происходящие события.
# Пока единственное событие, которое нас интересует - выход из программы.
#while True:
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

#    for event in pygame.event.get():
 #       if event.type == pygame.QUIT:
  #          pygame.quit()
   #         exit()