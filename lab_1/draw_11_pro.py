import pygame
import math
import pygame.draw as draw

pygame.init()

screen = pygame.display.set_mode((800, 1200))


def yurt(x1, y1, length, height):
    """
    функция рисует юрту заданных размеров в заданном месте
    :param x1: координата по х верхнего левого угла прямоугольника, в который будет вписана юрта
    :param y1: координата по у верхнего левого угла прямоугольника, в который будет вписана юрта
    :param length: ширина юрты
    :param height: высота юрты, умноженная на 2
    :return: функция ничего не возвращает
    """
    draw.ellipse(screen, (230, 230, 230), (x1, y1, length, height))
    draw.arc(screen, (0, 0, 0), (x1, y1, length, height), math.pi * 2, math.pi, 3)
    draw.rect(screen, (255, 255, 255), (x1, y1 + height / 2, length, height / 2))
    draw.line(screen, (0, 0, 0), (x1, y1 + height / 2), (x1 + length, y1 + height / 2), 1)
    x2 = x1 + length / 8
    xx2 = x2 - x1 - length / 2
    l2 = length / 2
    y2 = -(height / 2) * math.sqrt(1 - (xx2 ** 2) / (l2 ** 2)) + y1 + height / 2
    draw.arc(screen, (0, 0, 0), (x2, y2 - 5, 0.75 * length, 10), math.pi, math.pi * 2, 2)
    x3 = x1 + length / 32
    xx3 = x3 - x1 - length / 2
    y3 = -(height / 2) * math.sqrt(1 - (xx3 ** 2) / (l2 ** 2)) + y1 + height / 2
    draw.arc(screen, (0, 0, 0), (x3, y3 - 5, 0.9375 * length, 10), math.pi, math.pi * 2, 2)
    x4 = x1 + length / 4
    xx4 = x4 - x1 - length / 2
    y4 = -(height / 2) * math.sqrt(1 - (xx4 ** 2) / (l2 ** 2)) + y1 + height / 2
    draw.arc(screen, (0, 0, 0), (x4, y4 - 5, 0.5 * length, 10), math.pi, math.pi * 2, 2)
    draw.line(screen, (0, 0, 0), (x3 + length / 5, y3), (x1 + length / 5, y1 + height / 2), 1)
    draw.line(screen, (0, 0, 0), (x3 + 2 * length / 5, y3), (x1 + 3 * length / 7, y1 + height / 2), 1)
    draw.line(screen, (0, 0, 0), (x3 + 3 * length / 5, y3), (x1 + 4 * length / 6, y1 + height / 2), 1)
    draw.line(screen, (0, 0, 0), (x3 + 4 * length / 5, y3), (x1 + 7 * length / 8, y1 + height / 2), 1)
    draw.line(screen, (0, 0, 0), (x2 + length / 4, y2), (x3 + 2 * length / 7, y3 + 5), 1)
    draw.line(screen, (0, 0, 0), (x2 + 4 * length / 7, y2), (x3 + 5 * length / 7, y3 + 5), 1)
    draw.line(screen, (0, 0, 0), (x4 + length / 10, y4), (x2 + length / 8, y2 + 5), 1)
    draw.line(screen, (0, 0, 0), (x4 + length / 4, y4), (x2 + 3 * length / 7, y2 + 5), 1)
    draw.line(screen, (0, 0, 0), (x4 + 5 * length / 11, y4), (x2 + 8 * length / 12, y2 + 5), 1)
    draw.line(screen, (0, 0, 0), (x1 + length / 2, y1), (x4 + 4 * length / 12, y4 + 5), 1)


def eskimo(x1, y1, length, height, hand):
    """"
        функция рисует эскимоса
        :param x1: координата по х верхнего левого угла прямоугольника, в который вписан эллипс - голова эскимоса
        :param y1: координата по y верхнего левого угла прямоугольника, в который вписан эллипс - голова эскимоса
        :param length: ширина головы эскимоса
        :param height: высота головы эскимоса
        :param hand: если данный параметр = 0, то эскимос держит палку в правой руке, иначе - в левой
        :return: функция ничего не возвращает
    """
    if hand == 0:
        draw.ellipse(screen, (149, 124, 110), (x1 - 0.3 * length, y1 + height, 0.55 * length, 0.25 * height))
        draw.line(screen, (0, 0, 0), (x1 - 0.25 * length, y1), (x1 - 0.25 * length, y1 + 2 * height), 1)
        tale = pygame.Surface((0.55 * length, 0.25 * height))
        tale.set_colorkey('BLACK')
        draw.ellipse(tale, (149, 124, 110), (0, 0, 0.5 * length, 0.25 * height))
        tale2 = pygame.transform.rotate(tale, 330)
        screen.blit(tale2, (x1 + 0.78 * length, y1 + 0.91 * height))
    else:
        draw.ellipse(screen, (149, 124, 110),
                     (x1 + 0.78 * length, y1 + 0.91 * height, 0.55 * length, 0.25 * height))
        draw.line(screen, (0, 0, 0), (x1 + 1.2 * length, y1), (x1 + 1.2 * length, y1 + 2 * height), 1)
        tale = pygame.Surface((0.55 * length, 0.25 * height))
        tale.set_colorkey('BLACK')
        draw.ellipse(tale, (149, 124, 110), (0, 0, 0.5 * length, 0.25 * height))
        tale2 = pygame.transform.rotate(tale, 30)
        screen.blit(tale2, (x1 - 0.3 * length, y1 + 0.9 * height))
    draw.ellipse(screen, (228, 222, 219), (x1, y1, length, height))
    draw.ellipse(screen, (149, 124, 110), (x1 - 0.1 * length, y1 + height / 2, 1.2 * length, 3 * height))
    draw.rect(screen, (255, 255, 255), (x1 - 0.1 * length, y1 + height * 2, 1.2 * length, 2 * height))
    draw.rect(screen, (111, 92, 82), (x1 + 0.35 * length, y1 + height / 2, 0.3 * length, 1.5 * height))
    draw.ellipse(screen, (149, 124, 110),
                 (x1 + 0.12 * length, y1 + 1.85 * height, 0.25 * length, 0.5 * height))
    draw.ellipse(screen, (149, 124, 110),
                 (x1 + 0.62 * length, y1 + 1.85 * height, 0.25 * length, 0.5 * height))
    draw.ellipse(screen, (149, 124, 110), (x1, y1 + 1.8 * height + 0.4 * height, 0.35 * length, 0.2 * height))
    draw.ellipse(screen, (149, 124, 110),
                 (x1 + 0.62 * length, y1 + 2.2 * height, 0.35 * length, 0.2 * height))
    draw.ellipse(screen, (175, 157, 146), (x1 + 0.1 * length, y1 + 0.1 * height, 0.8 * length, 0.8 * height))
    draw.ellipse(screen, (229, 218, 219), (x1 + 0.2 * length, y1 + 0.2 * height, 0.6 * length, 0.6 * height))
    draw.line(screen, (0, 0, 0), (x1 + 0.32 * length, y1 + 0.35 * height),
              (x1 + 0.42 * length, y1 + 0.4 * height), 2)
    draw.line(screen, (0, 0, 0), (x1 + 0.64 * length, y1 + 0.35 * height),
              (x1 + 0.54 * length, y1 + 0.4 * height), 2)
    draw.arc(screen, (0, 0, 0), (x1 + 0.3 * length, y1 + 0.5 * height, 0.4 * length, 0.4 * height),
             math.pi * 0.3, math.pi * 0.7,
             2)
    draw.rect(screen, (111, 92, 82), (x1 - 0.1 * length, y1 + 1.8 * height, 1.2 * length, 0.2 * length))


def puts(x1, y1, length, height, angle):
    """"
        функция рисует ноги и хвост кота
        :param x1: координата по х верхнего левого угла прямоугольника, в который вписан эллипс - конечность кота
        :param y1: координата по н верхнего левого угла прямоугольника, в который вписан эллипс - конечность кота
        :param length: длина части тела
        :param height: ширина части тела
        :param angle: угол, на который нужно повернуть лапу.хвост(против часовой стрелки)
        :return: функция ничего не возвращает
    """
    tale = pygame.Surface((length, height))
    tale.set_colorkey('BLACK')
    draw.ellipse(tale, (204, 204, 204), (0, 0, length, height))
    tale2 = pygame.transform.rotate(tale, angle)
    screen.blit(tale2, (x1, y1))


def fish(x1, y1, length, height):
    """"
    функция рисует рыбу
    :param x1: координата х носа рыбы
    :param y1: координата у носа рыбы
    :param length: длина туловища рыбы
    :param height: ширина туловища рыбы
    :return: функция ничего не возвращает
    """
    draw.polygon(screen, (229, 75, 87),
                 [(x1 + 0.6 * length, y1 + 1.05 * height), (x1 + 0.9 * length, y1 + 1.05 * height),
                  (x1 + 0.8 * length, y1 + 1.45 * height),
                  (x1 + 0.9 * length, y1 + 1.6 * height), (x1 + 0.55 * length, y1 + 1.45 * height),
                  (x1 + 0.65 * length, y1 + 1.18 * height)])

    tale = pygame.Surface((2 * length, 2 * height))
    tale.set_colorkey('BLACK')
    a = []
    b = []
    g = int(length)
    for k in range(g):
        a.append((k, length + height - math.sqrt(
            (height ** 2 / 4 + length ** 2 / 4) ** 1 - (length / 2 - k) ** 2)))
        b.append((length - k,
                  length + math.sqrt((height ** 2 / 4 + length ** 2 / 4) ** 1 - (length / 2 - k) ** 2)))
    c = a + b
    draw.polygon(tale, (140, 175, 168), c)
    tale2 = pygame.transform.rotate(tale, 335)
    screen.blit(tale2, (x1, y1))
    draw.polygon(screen, (140, 175, 168),
                 [(x1 + 1.25 * length, y1 + 1.47 * height), (x1 + 1.65 * length, y1 + 1.47 * height),
                  (x1 + 1.45 * length, y1 + 1.72 * height)])
    draw.circle(screen, (103, 9, 251), (x1 + 0.559 * length, y1 + 1.218 * height), 0.08 * length)
    draw.circle(screen, (0, 0, 0), (x1 + 0.559 * length, y1 + 1.21 * height), 0.04 * length)


def clouds(x, color):
    """"
    функция рисует облака
    :param x: координата по x, с которой начинается отрисовка второго слева облака
    :param color: цвет облак
    :return: возвращаемого значения нет
    """
    draw.circle(screen, color, (x, 250), 40)
    draw.ellipse(screen, color, (x, 210, 150, 80))

    draw.rect(screen, color, (x - 200, 320, 100, 50))
    draw.circle(screen, color, (-192 + x, 330), 40)
    draw.ellipse(screen, color, (-162 + x, 310, 100, 60))

    draw.rect(screen, color, (250 + x, 300, 80, 30))
    draw.circle(screen, color, (258 + x, 290), 40)
    draw.ellipse(screen, color, (278 + x, 280, 90, 50))
    draw.ellipse(screen, color, (178 + x, 270, 130, 60))

    draw.circle(screen, color, (500 + x, 350), 50)
    draw.ellipse(screen, color, (500 + x, 332, 150, 80))
    draw.ellipse(screen, color, (410 + x, 342, 90, 70))


def cat(x1, y1, length, height):
    """
    эта функция рисует кота
    :param x1: координата по х верхнего левого угла прямоугольника, в который вписан эллипс - тело кота
    :param y1: координата по y верхнего левого угла прямоугольника, в который вписан эллипс - тело кота
    :param length: длина туловища кота
    :param height: ширина туловища кота
    :return: функция ничего не возвращает
    """
    puts(x1 - 0.5 * length, y1 + 0.15 * height, 0.85 * length, 0.37 * height, 10)
    puts(x1 - 0.4 * length, y1 + 0.4 * height, 0.85 * length, 0.37 * height, 15)
    puts(x1 + 0.65 * length, y1 + 0.1 * height, 0.85 * length, 0.37 * height, 335)
    puts(x1 + 0.55 * length, y1 + 0.15 * height, 0.85 * length, 0.37 * height, 320)
    puts(x1 + 0.8 * length, y1 - 0.55 * height, 0.9 * length, 0.4 * height, 20)
    draw.ellipse(screen, (204, 204, 204), (x1, y1, length, height))
    fish(x1 - 0.5 * length, y1 - 1.5 * height, 0.4 * length, 1.3 * height)
    draw.ellipse(screen, (204, 204, 204), (x1 - 0.2 * length, y1 - 0.6 * height, 0.5 * length, 0.9 * height))
    draw.ellipse(screen, (255, 255, 255),
                 (x1 - 0.16 * length, y1 - 0.37 * height, 0.09 * length, 0.199 * height))
    draw.ellipse(screen, (0, 0, 0),
                 (x1 - 0.12 * length, y1 - 0.335 * height, 0.05 * length, 0.05 * length))
    draw.ellipse(screen, (255, 255, 255),
                 (x1 + 0.02 * length, y1 - 0.33 * height, 0.09 * length, 0.199 * height))
    draw.ellipse(screen, (0, 0, 0),
                 (x1 + 0.024 * length, y1 - 0.31 * height, 0.05 * length, 0.05 * length))
    draw.polygon(screen, (204, 204, 204),
                 [(x1 - 0.02 * length, y1 - 0.8 * height), (x1 - 0.09 * length, y1 - 0.55 * height),
                  (x1 + 0.07 * length, y1 - 0.5 * height)])
    draw.polygon(screen, (204, 204, 204),
                 [(x1 + 0.17 * length, y1 - 0.8 * height), (x1 + 0.06 * length, y1 - 0.55 * height),
                  (x1 + 0.2 * length, y1 - 0.5 * height)])
    draw.circle(screen, (0, 0, 0), (x1 - 0.04 * length, y1 - 0.03 * height), 0.025 * length)
    draw.polygon(screen, (255, 255, 255),
                 [(x1 - 0.16 * length, y1 + 0.11 * height), (x1 - 0.13 * length, y1 + 0.15 * height),
                  (x1 - 0.15 * length, y1 + 0.19 * height)])
    draw.polygon(screen, (255, 255, 255),
                 [(x1 - 0.07 * length, y1 + 0.238 * height), (x1 - 0.04 * length, y1 + 0.25 * height),
                  (x1 - 0.065 * length, y1 + 0.3 * height)])


FPS = 30


screen.fill("white")
draw.rect(screen, (220, 220, 220), (0, 0, 800, 500))

yurt(15, 470, 128, 112)
yurt(400, 500, 128, 112)
yurt(50, 450, 400, 350)
yurt(45, 600, 200, 175)
yurt(200, 650, 200, 175)

eskimo(590, 480, 55, 44, 0)
eskimo(720, 500, 55, 44, 0)
eskimo(650, 550, 55, 44, 0)
eskimo(500, 600, 55, 44, 1)
eskimo(590, 630, 55, 44, 1)
eskimo(700, 650, 55, 44, 0)
eskimo(490, 750, 55, 44, 1)
eskimo(600, 750, 130, 104, 0)

cat(0, 800, 120, 48)
cat(150, 1000, 120, 48)
cat(250, 859, 120, 48)

pygame.display.update()
clock = pygame.time.Clock()
finished = False


i = 0
coordinate = 140

while not finished:
    clock.tick(FPS)
    i += 1
    clouds(coordinate + (i - 1), (220, 220, 220))
    clouds(coordinate + i, (255, 255, 255))
    if coordinate + i > 930:
        clouds(coordinate - 750, (255, 255, 255))
        coordinate = coordinate - 750
        i = 0
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
