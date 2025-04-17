import pygame  # импортируем библиотеку pygame
from random import *

w = randint(1,100)
print(w)
class Food():
    def __init__(self, name_image, x, y):  # конструктор, создание свойств, self - ОБЪЕКТ
        self.image = pygame.image.load(name_image)  # создание картинки, ЭТО СВОЙСТВО
        self.rect = self.image.get_rect()  # создание прямямоугольника по границам картинки, ЭТО СВОЙСТВО
        self.rect.x = x  # координата x для картинки, ЭТО СВОЙСТВО
        self.rect.y = y # координата y для картинки, ЭТО СВОЙСТВО

    def draw_image(self):  # метод отрисовки картинки
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move_plate(self): #метод движения тарелки
        keys = pygame.key.get_pressed() #получение списка нажатых клавишь
        if keys[pygame.K_LEFT] == True:#если нажата клавиша влево
            self.rect.x -= 1
        if keys[pygame.K_RIGHT]:#если нажата клавиша вправо
            self.rect.x += 1

    def move_food(self):#метод движения eды
         self.rect.y += w

fon = Food("кухня.jpg", 0, 0)
pygame.init()  # обязательная команда
window_size = (1000, 750)  # размеры окна
screen = pygame.display.set_mode(window_size)  # создание экрана с размерами
plate = Food("plate.png", 300, 650)  # создание объекта класса Food
apple1= Food("яблоко.png", 200, randint(-1000,0))  # создание объекта класса Food
apple2 = Food("яблоко.png", 450, randint(-490,0))  # создание объекта класса Food
apple3 = Food("яблоко.png", 650, randint(-700,0))  # создание объекта класса Food
apple4 = Food("яблоко.png", 850,randint(-250,0) )  # создание объекта класса Food
apple5 = Food("яблоко.png", 50, randint(-1575,0))  # создание объекта класса Food
food_list = [apple1, apple2, apple3, apple4, apple5]
clock = pygame.time.Clock()  # создание игрового таймера

while True:  # игровой цикл
    clock.tick(20)  # 40фпс\с
    fon.draw_image()  # применение метода отрисовки к объекту класса Food
    for i in food_list:
        i.draw_image()
        i.move_food()

    plate.draw_image()  # применение метода отрисовки к объекту класса Food
    plate.move_plate()
    for event in pygame.event.get():  # проходимся по событиям
        if event.type == pygame.QUIT:  # если нажали на крестик
            pygame.QUIT()  # выход из игры
    pygame.display.update()# обновление содержимого экрана