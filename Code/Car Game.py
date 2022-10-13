import pygame as pg
from pygame.locals import *
from sys import exit
import random

screen_size = width, height = (400,600)
road_w = (width/1.6)
roadmark_w = (width/40)
orient = False
   
pg.init()
pg.font.init()
screen = pg.display.set_mode(screen_size)
screen.fill((60,200,0))

font = pg.font.Font('freesansbold.ttf', 32)
text = font.render('Game Over', True, (0, 255, 200), (0, 0, 128))
text_loc = text.get_rect()
text_loc.center = 200,300

car = pg.image.load("1.png")
car = pg.transform.rotate(car,180)
car_loc = car.get_rect()
car_loc.center = 260,500

car2 = pg.image.load("2.png")
car2 = pg.transform.rotate(car2,180)
car_loc2 = car2.get_rect()
car_loc2.center = 140,100
clock = pg.time.Clock()

running = True
q = False
while running:

    pg.draw.rect(screen,
         (50,50,50),
         (width/5-5,0 , road_w, height))

    rect_1 = pg.draw.rect(screen,
             (255,240,60),
             (width/5+5,0 , roadmark_w, height))

    rect_2 = pg.draw.rect(screen,
             (255,240,60),
             (width-95,0 , roadmark_w, height))

    pg.draw.rect(screen,
             (255,255,255),
             (width/2 ,0 , roadmark_w, height))

    pg.display.set_caption("Car Game")
    
    screen.blit(car,car_loc)
    screen.blit(car2,car_loc2)
    ran = random.randint(0,1)
    car_loc2[1] += 5
    if car_loc2[1] >= height:
        car_loc2[1] = -200

        if ran == 0:
            car_loc2[0] = 230
        elif ran == 1:
            car_loc2[1] = 140
    

    for event in pg.event.get():
        if event.type == QUIT:
            running = False
            q = True
    
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                car_loc = car_loc.move([-110,0])
                
            if event.key == K_RIGHT:
                car_loc = car_loc.move([110,0])

            if event.type == K_a:
                running = True

    if car_loc.colliderect(car_loc2) == True:
        running = False
        screen.blit(text,text_loc)

    if car_loc.colliderect(rect_1):
        car_loc = 150

    if car_loc.colliderect(rect_2):
        car_loc = 250

    pg.display.update()
    clock.tick(60)

if q == True:
   pg.quit()
