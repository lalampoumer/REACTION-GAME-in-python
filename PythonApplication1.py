import pygame
import time
import random
run=True
screen=pygame.display.set_mode((1000,1000))
timer=0
speed=60
rx=random.randint(100,900)
ry=random.randint(100,900)

scale_x=100
scale_y=100

start=True
speed_limit=17.5
color=(255,255,255)
get_time=False

fps=200
score=0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0,0,0))
    timer=timer+60/fps
    if speed > speed_limit:
        speed=speed-3/fps
    if speed <= speed_limit and scale_x > 75 :
        scale_x=scale_x-3/fps
        scale_y = scale_y - 3/fps
    if scale_x <= 75:
        speed_limit=840/fps

    if timer < speed:
        pygame.draw.rect(screen,color,(rx,ry,scale_x,scale_y))
    if timer > speed and start:
        rx = random.randint(100, 900)
        ry = random.randint(100, 900)
        start=False
    if timer > speed*2:
        timer=1
        color = (255, 255, 255)
        start=True
        get_time=True
    mouse_x,mouse_y=pygame.mouse.get_pos()
    if (mouse_x > rx and mouse_x < rx+scale_x) and (mouse_y > ry and mouse_y < ry+scale_y):
        color=(0,255,0)
        if get_time:
            get_time=False
            score = score + ((speed/timer*1000))/speed
            score=round(score)
            print(score)


    if (mouse_x > rx and mouse_x < rx+scale_x)==False and (mouse_y > ry and mouse_y < ry+scale_y)==False and (timer>speed) and color!=(0,255,0) :
        run=False

    pygame.display.update()
    time.sleep(1/fps)
