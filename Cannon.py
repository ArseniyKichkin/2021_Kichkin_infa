from random import randrange as rnd, choice
import math
import time
import pygame
import numpy
import pygame.draw as draw

tank_image = pygame.image.load("tank.jpg")  # В репозиторий загружена картинка с именем "tank.jpg".
# Перед запуском программы скачайте её и добавьте в ту же папку, откуда запускается код.
LEVEL = 2
TARGETS_QUANTITY = 3
DARK_GREEN = (1, 51, 33)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BEIGE = (245, 245, 220)
COLORS = [RED, BLUE, CYAN, YELLOW, GREEN, MAGENTA]
SLEEP = 3
FPS = 60
POINTS = 0

pygame.init()
screen = pygame.display.set_mode((1000, 600))
screen.fill(BEIGE)


class Shell(object):
    def __init__(self, x=0, y=0):
        """
        Конструктор класса Shell
        Arguments:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.acceleration = 1
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.color = choice(COLORS)

    def set_coordinates(self):
        """
        отрисовка снаряда
        return:
        """
        draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        """
        Анимация движения снаряда по параболе
        """
        if self.x + self.r >= 1000 or self.x - self.r <= 0:
            self.vx *= -0.8
        if self.y + self.r >= 600 or self.y - self.r <= 0:
            self.vy *= -0.8
        self.vy += self.acceleration
        self.vx -= 0.01 * self.vx
        self.x += self.vx
        self.y += self.vy

    def check_for_collision(self, obj):
        """
        Проверка сталкивалкивания данного обьекта с целью, описываемой в обьекте obj.
        Arguments:
            obj: Обьект, с которым проверяется столкновение.
        return: Возвращает True в случае столкновения мяча и цели. В противном случае - False.
        """
        if ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5 <= self.r + obj.r:
            return True
        else:
            return False


class Cannon(object):
    """
    класс Cannon
    """

    def __init__(self):
        """
        коструктор для класса Cannon
        """
        self.f2_power = 8
        self.f2_on = 0
        self.an = 1
        self.x = rnd(50, 1000)
        self.y = rnd(50, 580)
        self.x_gun = 0
        self.y_gun = 0
        self.speed = 3

    def start_fire(self):
        """
        начало стрельбы
        return:
        """
        self.f2_on = 1

    def end_fire(self, event):
        """
        Выстрел снарядом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global Shells, strike
        x, y = event.pos
        strike += 1
        new_shell = Shell(self.x_gun, self.y_gun)
        if x - new_shell.x == 0:
            self.an = math.pi
        else:
            self.an = math.atan(abs(y - new_shell.y) / abs(x - new_shell.x))
        new_shell.vx = numpy.sign(x - self.x) * self.f2_power * math.cos(self.an)
        new_shell.vy = numpy.sign(y - self.y) * self.f2_power * math.sin(self.an)
        Shells += [new_shell]
        self.f2_on = 0
        self.f2_power = 8

    def aim(self):
        """
        Прицеливание.
        Зависит от положения мыши.
        """
        x, y = pygame.mouse.get_pos()
        if x - self.x == 0:
            self.an = math.pi
        else:
            self.an = math.atan(abs(y - self.y) / abs(x - self.x))
        self.x_gun = self.x + numpy.sign(x - self.x) * max(self.f2_power, 20) * math.cos(self.an)
        self.y_gun = self.y + numpy.sign(y - self.y) * max(self.f2_power, 20) * math.sin(self.an)
        pygame.draw.line(screen, BLACK, (self.x, self.y), (self.x_gun, self.y_gun), 7)

    def power_up(self):
        """
        усиление Cannon спустя время
        return:
        """
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1

    def cannon_ride(self):
        """
        передвижение Cannon
        return:
        """
        if pygame.key.get_pressed()[pygame.K_w]:
            self.y += -self.speed
        if self.y > 585:
            self.y = 585
        if self.y < 10:
            self.y = 10
        else:
            if pygame.key.get_pressed()[pygame.K_s]:
                self.y += self.speed
        if pygame.key.get_pressed()[pygame.K_a]:
            self.x += -self.speed
        if self.x > 980:
            self.x = 980
        if self.x < 20:
            self.x = 20
        else:
            if pygame.key.get_pressed()[pygame.K_d]:
                self.x += self.speed
        screen.blit(tank_image, (self.x - 20, self.y - 10))


class Target(object):
    """
    Класс мишени первого типа
    """

    def __init__(self):
        """
        Инициализация новой цели.
        """
        self.x = rnd(50, 950)
        self.y = rnd(50, 560)
        self.r = rnd(2, 50)
        self.x_acceleration = choice([1, -1]) * rnd(1, 8)
        self.y_acceleration = choice([1, -1]) * rnd(1, 8)
        draw.circle(screen, RED, (self.x, self.y), self.r)

    def move(self):
        """
        Перемещение мишени 1 типа по прошествии единицы времени.
        """
        if self.y - self.r >= 580 or self.y + self.r <= 0:
            self.y_acceleration *= -1
        if self.x - self.r <= 0 or self.x + self.r >= 1000:
            self.x_acceleration *= -1
        self.y += self.y_acceleration
        self.x += self.x_acceleration

    def set_coordinates(self):
        """
        Отрисовка мишени 1 типа
        return:
        """
        draw.circle(screen, MAGENTA, (self.x, self.y), self.r)


class Square(Target):
    """
    Класс мишени второго типа, унаследованной от первого
    """

    def new_target(self):
        self.x = rnd(50, 950)
        self.y = rnd(50, 580)
        self.r = rnd(2, 50)
        self.x_acceleration = choice([-1, 1]) * rnd(1, 8)
        self.y_acceleration = choice([-1, 1]) * rnd(1, 8)

    def set_coordinates(self):
        """
        Отрисовка мишени второго типа
        return:
        """
        draw.rect(screen, RED, (self.x - self.r, self.y - self.r, 2 * self.r, 2 * self.r))

    def move(self):
        """
        Метод обеспечивает движение мишени 2 типа спустя время
        return:
        """
        if self.y < 10 or self.y > 580:
            self.y_acceleration *= -1
        if self.x + self.r < 0 or self.x - self.r >= 1000:
            self.x_acceleration *= -1
        self.x += self.x_acceleration
        self.y += self.y_acceleration


def collision_occurs():
    """
    Функция очищает поле и выводит надпись, когда все цели уничтожены
    return:
    """
    global strike, is_alive, POINTS, Shells, targets, squares, LEVEL
    if targets:
        pass
    else:
        if squares:
            pass
        else:
            screen.fill(BEIGE)
            text = font.render("Цели уничтожены за " + str(strike) + " выстрелов" + "." + " Уровень " + str(LEVEL)
                               + ".", True, BLACK)
            LEVEL += 1
            screen.blit(text, [100, 300])
            pygame.display.update()
            Shells = []
            is_alive = 0
            POINTS += 1


def targets_for_next_level():
    """
    Функция создает новые цели для новой игры
    return:
    """
    global targets, squares, TARGETS_QUANTITY
    for t in range(0, TARGETS_QUANTITY):
        targets.append(Target())
    for s in range(0, TARGETS_QUANTITY):
        squares.append(Square())


targets = []
squares = []
cannon = Cannon()
strike = 0
Shells = []
is_alive = 1
font = pygame.font.Font(None, 50)
pygame.display.update()
clock = pygame.time.Clock()


def new_game():
    """
    Main loop
    return:
    """
    global targets, is_alive, Shells, strike, FPS, clock, POINTS, SLEEP, cannon
    for target in targets:
        target.Target()
    for s in squares:
        s.new_target()
    targets_for_next_level()
    is_alive = 1
    cannon = Cannon()
    strike = 0
    Shells = []
    while is_alive == 1 or Shells:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cannon.start_fire()
            elif event.type == pygame.MOUSEBUTTONUP:
                cannon.end_fire(event)
        cannon.cannon_ride()
        cannon.aim()
        for target in targets:
            target.move()
            target.set_coordinates()
        for square in squares:
            square.move()
            square.set_coordinates()
        for shell in Shells:
            shell.move()
            shell.set_coordinates()
            for target in targets:
                if shell.check_for_collision(target):
                    Shells.remove(shell)
                    targets.remove(target)
                    collision_occurs()
            for square in squares:
                if shell.check_for_collision(square):
                    Shells.remove(shell)
                    squares.remove(square)
                    collision_occurs()
        text_score = font.render(str(POINTS), True, BLUE)
        screen.blit(text_score, [870, 30])
        pygame.display.update()
        cannon.power_up()
        screen.fill(BEIGE)
    time.sleep(SLEEP)
    new_game()


new_game()
