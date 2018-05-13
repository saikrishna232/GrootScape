import pygame
import time
from random import randint,randrange

black=(0,0,0)
white=(255,255,255)
lavender=(150,33,194)
orange=(240,125,0)
red=(255,0,0)
green=(35,166,56)
yellow=(255,193,0)
pink=(249,3,117)
dgreen=(74,83,33)
brown=(203,176,118)

color_choice=[brown,red,green,yellow,pink]


pygame.init()


area_height=600
area_width=850

img_height=67
img_width=35

area=pygame.display.set_mode((area_width,area_height))
pygame.display.set_caption('Grootscape')
clock=pygame.time.Clock()



img=pygame.image.load('groot.png')


def scorecount(count):
    font=pygame.font.Font('freesansbold.ttf',30)
    text=font.render("Score: "+str(count),True,lavender)
    area.blit(text,[0,0])


def obstacles(choice,x_ob,y_ob,ob_width,ob_height,gap):
    pygame.draw.rect(area,choice,[x_ob,y_ob,ob_width,ob_height])
    pygame.draw.rect(area,choice,[x_ob,y_ob+ob_height+gap,ob_width,area_height])



def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN,pygame.KEYUP,pygame.QUIT]):
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type==pygame.KEYDOWN:
            continue

        return event.key

    return None

def makeobjs(text,font):
    textarea=font.render(text,True,orange)
    return textarea,textarea.get_rect()


def msgon(text):
    smalltext=pygame.font.Font('freesansbold.ttf',20)
    largetext=pygame.font.Font('freesansbold.ttf',120)

    titlearea,titlerec=makeobjs(text,largetext)
    titlerec.center=area_width/2,area_height/2
    area.blit(titlearea,titlerec)

    msgarea,msgrec=makeobjs('PreSs ANy KeY To CoNtiNUe!',smalltext)
    msgrec.center=area_width/2,((area_height/2)+100)
    area.blit(msgarea,msgrec)

    pygame.display.update()
    time.sleep(1)


    while replay_or_quit()==None:
       clock.tick()

    main()

def gameover():
    msgon('Crash!!!!!')

def groot(x,y,image):
    area.blit(img,(x,y))


def main():
    x=150
    y=200
    y_mov=0
    x_ob=area_width
    y_ob=0
    ob_width=75
    ob_height=randint(0,(area_height/2))
    gap=img_height*2.5
    ob_mov=4
    score=0
    choice=color_choice[randrange(0,len(color_choice))]

    game_status=True
    while game_status:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_status=False

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    y_mov=-5

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    y_mov=5

        y+=y_mov
        area.fill(black)
        groot(x,y,img)
        obstacles(choice,x_ob,y_ob,ob_width,ob_height,gap)
        x_ob-=ob_mov
        scorecount(score)


        if y>area_height-40 or y<0:
            gameover()

        if x_ob < (-1*ob_width):
            x_ob=area_width
            ob_height=randint(0,(area_height/2))
            choice=color_choice[randrange(0,len(color_choice))]
            score+=1


        if x+img_width>x_ob:
            if x<x_ob+ob_width:
                if y<ob_height:
                    if x-img_width<ob_width+x_ob:
                        gameover()


        if x+img_width>x_ob:
            if y+img_height>ob_height+gap:
                if x<ob_width+x_ob:
                    gameover()



        if 3 <= score < 5:
            ob_mov = 5
            gap = img_height * 2.4
        if 5 <= score < 8:
            ob_mov = 6
            gap = img_height *2.3
        if 8 <= score < 14:
            ob_mov = 7
            gap = img_height *2.2
        if 14 <= score < 20:
            ob_mov = 7
            gap = img_height *2.1




        pygame.display.update()
        clock.tick(60)


main()
pygame.quit()
quit()
