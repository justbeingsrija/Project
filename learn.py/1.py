import pygame
pygame.init()
grey=(119,118,110)
display_width=800
display_height=600
gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("car game")
clock=pygame.time.Clock()
backgroundpic=pygame.image.load("strip.jpg")
yellow_strip=pygame.image.load("yellow strip.jpeg")
white_strip=pygame.image.load("White strip.jpg")
carimg=pygame.image.load("Car.png")


def background():
    gamedisplay.blit(backgroundpic,(0,0))
    gamedisplay.blit(backgroundpic,(0,200))
    gamedisplay.blit(backgroundpic,(0,400))
    gamedisplay.blit(backgroundpic,(700,0))
    gamedisplay.blit(backgroundpic,(700,200))
    gamedisplay.blit(backgroundpic,(700,400))
    gamedisplay.blit(yellow_strip,(400,0))
    gamedisplay.blit(yellow_strip,(400,100))
    gamedisplay.blit(yellow_strip,(400,200))
    gamedisplay.blit(yellow_strip,(400,300))
    gamedisplay.blit(yellow_strip,(400,400))
    gamedisplay.blit(yellow_strip,(400,500))



def car(x,y):
    gamedisplay.blit(carimg,(x,y))

def game_loop():
    x=(display_width*0.45)
    y=(display_height*0.8)
    x_change=0

    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                bumped=True
        if event.type==pygame.KEYDOWN:
           if event.key==pygame.K_LEFT:
               x_change=-5
           if event.key==pygame.K_RIGHT:
               x_change=5
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                x_change=0

        x+=x_change
        gamedisplay.fill(grey)
        background()
        car(x,y)
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()
