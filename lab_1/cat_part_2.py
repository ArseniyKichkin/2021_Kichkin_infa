import pygame
import math
import pygame.draw as draw


# !!! PLEASE WHEN RUNNING THIS PROGRAM PRESS ANY KEY SEVERAL TIMES

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))

# colors
gray = (128, 128, 128)
brown = (0, 100, 0)
lightBlue = (176, 196, 222)
white = (255, 255, 255)
pink = (255, 192, 203)
red = (220, 20, 60)
orange = (255, 0, 0)
catColor = (255, 99, 71)


def draw_window():
    """
    This function draws the background
    :return:
    """
    draw.rect(screen, (0, 128, 0), (0, 300, 900, 400), 0)  # frame
    draw.rect(screen, white, (270, 15, 225, 275), 10)  # frame
    draw.rect(screen, white, (270, 15, 112, 105), 10)  # frame
    draw.rect(screen, lightBlue, (274, 19, 108, 101), 0)  # outdoors
    draw.rect(screen, white, (384, 15, 112, 105), 10)  # frame
    draw.rect(screen, lightBlue, (388, 19, 108, 101), 0)  # outdoors
    draw.rect(screen, white, (378, 120, 10, 175), 0)  # frame
    draw.rect(screen, lightBlue, (274, 125, 106, 163))  # outdoors
    draw.rect(screen, lightBlue, (388, 125, 108, 163))  # outdoors


def draw_screamer():
    """
    This function draws a terrifying cat
    :return:
    """

    # background
    draw.rect(screen, (0, 0, 0), (0, 0, 500, 700))

    # face
    draw.circle(screen, (255, 0, 0), (250, 350), 200)

    # mouth
    draw.arc(screen, (0, 0, 0), (110, 280, 280, 250), -3.1415, 0.03, 5)
    draw.line(screen, (0, 0, 0), (110, 405), (390, 405), 5)
    a = 128
    b = 5

    # teeth
    draw.polygon(screen, (255, 255, 255), ((b + 110, a + 280), (b + 140, a + 340), (b + 155, a + 280),
                                           (b + 165, a + 355), (b + 180, a + 280), (b + 200, a + 390),
                                           (b + 230, a + 280), (b + 250, a + 390), (b + 275, a + 280),
                                           (b + 285, a + 385), (b + 300, a + 280), (b + 330, a + 350),
                                           (b + 350, a + 280), (b + 360, a + 335), (b + 380, a + 280)))

    # eyes
    draw.circle(screen, (240, 240, 240), (250 - 80, 350 - 60), 50)
    draw.circle(screen, (240, 240, 240), (250 + 80, 350 - 60), 50)

    # ears
    draw.polygon(screen, (255, 0, 0), ((80, 300), (80, 100), (190, 180)))
    draw.polygon(screen, (255, 0, 0), ((500 - 80, 300), (500 - 80, 100), (500 - 190, 180)))

    # pupils
    draw.ellipse(screen, (0, 0, 0), (160, 240, 20, 100))
    draw.ellipse(screen, (0, 0, 0), (320, 240, 20, 100))

    # moustache
    draw.line(screen, (240, 100, 100), (120, 390), (10, 390), 5)
    draw.line(screen, (240, 100, 100), (100, 350), (20, 300), 5)
    draw.line(screen, (240, 100, 100), (100, 380), (10, 360), 5)
    draw.line(screen, (240, 100, 100), (500 - 120, 390), (500 - 10, 390), 5)
    draw.line(screen, (240, 100, 100), (500 - 100, 350), (500 - 20, 300), 5)
    draw.line(screen, (240, 100, 100), (500 - 100, 380), (500 - 10, 360), 5)


def draw_lamp():
    draw.rect(screen, (0, 0, 0), (250, 0, 5, 10))
    draw.circle(screen, (249, 229, 38), (252, 30), 20)


def night():
    """
    This function sets night_mode
    :return:
    """
    night_mode = pygame.Surface((500, 700))
    night_mode.fill((1, 0, 0))
    night_mode.set_colorkey((0, 0, 0))
    night_mode.set_alpha(220)
    screen.blit(night_mode, (0, 0))
    

def draw_cat(x, y):
    """
    This function draws a cat, parameters determine where the left cat's ear is
    :param x:
    :param y:
    :return:
    """
    # body
    draw.ellipse(screen, catColor, (x - 22 + 53, y - 364 + 353, 320, 140))
    draw.ellipse(screen, (0, 0, 0), (x - 22 + 53, y - 364 + 353, 320, 140), 1)

    # front legs
    draw.ellipse(screen, catColor, (x - 22 + 43, y - 364 + 433, 28, 41))
    draw.ellipse(screen, (0, 0, 0), (x - 22 + 43, y - 364 + 433, 28, 41), 1)
    draw.ellipse(screen, catColor, (x - 22 + 70, y - 364 + 456, 70, 40))
    draw.ellipse(screen, (0, 0, 0), (x - 22 + 70, y - 364 + 456, 70, 40), 1)

    # head
    draw.circle(screen, catColor, (x - 22 + 75, y - 364 + 413), 50)
    draw.circle(screen, (0, 0, 0), (x - 22 + 75, y - 364 + 413), 50, 1)

    # ears
    draw.polygon(screen, pink, ((x - 22 + 22, y - 364 + 364), (x - 22 + 45, y - 364 + 373),
                                (x - 22 + 29, y - 364 + 391)))  # left ear
    draw.polygon(screen, red, ((x - 22 + 22, y - 364 + 364), (x - 22 + 45, y - 364 + 373),
                               (x - 22 + 29, y - 364 + 391)), 4)  # left ear
    draw.polygon(screen, pink, ((x - 22 + 113, y - 364 + 357), (x - 22 + 114, y - 364 + 382),
                                (x - 22 + 96, y - 364 + 368)))  # right ear
    draw.polygon(screen, red, ((x - 22 + 113, y - 364 + 357), (x - 22 + 114, y - 364 + 382),
                               (x - 22 + 96, y - 364 + 368)), 4)  # right ear

    # eyes
    draw.circle(screen, orange, (x - 22 + 54, y - 364 + 413), 17)  # left eye
    draw.circle(screen, orange, (x - 22 + 96, y - 364 + 413), 17)  # right eye

    # pupils
    draw.ellipse(screen, (0, 0, 0), (x - 22 + 56, y - 364 + 400, 4, 26))  # left pupil
    draw.ellipse(screen, (0, 0, 0), (x - 22 + 98, y - 364 + 400, 4, 26))  # right pupil

    # blick on left eye
    surface = pygame.Surface((10, 10))
    surface.fill(catColor)
    draw.ellipse(surface, (255, 255, 255), (x - 22 + 0, y - 364 + 0, 5, 10))
    a = pygame.transform.rotate(surface, 50)
    screen.blit(a, (x - 22 + 43, y - 364 + 397))
    draw.circle(screen, (0, 0, 0), (x - 22 + 54, y - 364 + 413), 17, 1)

    # blick on right eye
    surface1 = pygame.Surface((10, 10))
    surface1.fill(catColor)
    draw.ellipse(surface, (255, 255, 255), (x - 22 + 0, y - 364 + 0, 5, 10))
    b = pygame.transform.rotate(surface, 50)
    screen.blit(b, (x - 22 + 84, y - 364 + 397))
    draw.circle(screen, (0, 0, 0), (x - 22 + 96, y - 364 + 413), 17, 1)

    # nose
    draw.polygon(screen, pink, ((x - 22 + 70, y - 364 + 433), (x - 22 + 78, y - 364 + 433),
                                (x - 22 + 74, y - 364 + 438)))
    draw.polygon(screen, (0, 0, 0), ((x - 22 + 69, y - 364 + 432), (x - 22 + 79, y - 364 + 432),
                                     (x - 22 + 74, y - 364 + 440)), 1)

    # mouth
    draw.aaline(screen, (0, 0, 0), (x - 22 + 74, y - 364 + 440), (x - 22 + 74, y - 364 + 447))
    draw.arc(screen, (0, 0, 0), (x - 22 + 75, y - 364 + 444, 10, 6), math.pi, 0)
    draw.arc(screen, (0, 0, 0), (x - 22 + 65, y - 364 + 444, 10, 6), math.pi, 0)

    # tale
    surface_tail = pygame.Surface((200, 100))
    surface_tail.fill((0, 128, 0))
    surface_tail.set_colorkey(catColor)
    surface_tail.set_colorkey((0, 128, 0))
    draw.ellipse(surface_tail, catColor, (0, 0, 180, 60))
    draw.ellipse(surface_tail, (0, 0, 0), (0, 0, 180, 60), 1)
    c = pygame.transform.rotate(surface_tail, -30)
    screen.blit(c, (x - 22 + 280, y - 364 + 360))

    # back legs
    draw.circle(screen, catColor, (x - 22 + 340, y - 364 + 458), 42)
    draw.circle(screen, (0, 0, 0), (x - 22 + 340, y - 364 + 458), 42, 1)
    draw.ellipse(screen, catColor, (x - 22 + 362, y - 364 + 468, 28, 65))
    draw.ellipse(screen, (0, 0, 0), (x - 22 + 362, y - 364 + 468, 28, 65), 1)

    # moustache
    draw.arc(screen, (0, 0, 0), (x - 22 + 78, y - 364 + 428, 120, 50), math.pi/3, 5*math.pi/6)
    draw.arc(screen, (0, 0, 0), (x - 22 + 70, y - 364 + 434, 130, 50), math.pi/3, 4*math.pi/5.3)
    draw.arc(screen, (0, 0, 0), (x - 22 + 62, y - 364 + 440, 140, 50), math.pi/3, 4*math.pi/5.55)

    draw.arc(screen, (0, 0, 0), (x - 22 - 48, y - 364 + 425, 120, 50), math.pi/6, 5*math.pi/6)
    draw.arc(screen, (0, 0, 0), (x - 22 - 56, y - 364 + 430, 130, 50), math.pi/5.4, 5*math.pi/6)
    draw.arc(screen, (0, 0, 0), (x - 22 - 64, y - 364 + 435, 140, 50), math.pi/5.1, 5*math.pi/6)


def draw_ball():
    """
    This function draws klubok
    :return:
    """
    draw.circle(screen, gray, (300, 608), 40)
    draw.arc(screen, (0, 0, 0), (290, 598, 10, 30), 2*math.pi/3, 3*math.pi/1.8)
    draw.arc(screen, (0, 0, 0), (300, 595, 10, 35), 2*math.pi/3, 3*math.pi/1.8)


# set coordinates for cat
x = 22
y = 364

# initialize a counter
counter = 1

clock = pygame.time.Clock()

running = True

# program loop
while running:
    screen.fill(brown)
    clock.tick(FPS)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # changing a counter by keyboard
            if counter == 5:
                counter = 1
            else:
                counter += 1

    # condition for drawing screamer
    if counter % 5 == 0:
        draw_screamer()

    # drawing cat in house
    else:
        draw_window()
        # sometimes cat disappears
        if counter % 3 != 0 and counter % 4 != 0:
            draw_cat(x, y)
        draw_ball()
        draw_lamp()
        # condition for turning night_mode on
        if counter % 2 == 0:
            night()

    pygame.display.flip()

pygame.quit()
