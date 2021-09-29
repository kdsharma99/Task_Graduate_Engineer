import pygame 
import random
import os


# os.environ['SDL_VIDEO_CENTERED'] = '1'
# pygame.mixer.init()
pygame.init()
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
WIDTH=750
HEIGHT=450
gameover=False
# goimg=pygame.image.load("images/game_over.jpg")
# goimg=pygame.transform.scale(goimg,(100,50)).convert_alpha()
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game Task")
pygame.display.update()
star=pygame.image.load("star.png")
star=pygame.transform.scale(star,(70,70)).convert_alpha()
def button(gameWindow, position, text, size, colors="white on blue"):
    fg, bg = colors.split(" on ")
    font = pygame.font.SysFont("Arial", size)
    text_render = font.render(text, 1, fg)
    x, y, w , h = text_render.get_rect()
    x, y = position
    # pygame.draw.line(gameWindow, (150, 150, 150), (x, y), (x + w , y), 5)
    # pygame.draw.line(gameWindow, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    # pygame.draw.line(gameWindow, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    # pygame.draw.line(gameWindow, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(gameWindow, bg, (x, y, w , h))
    # print(gameWindow.blit(text_render, (x, y)))
    return gameWindow.blit(text_render, (x, y)) 
def show(text,color,x,y,size):
    font = pygame.font.SysFont("Arial",size)
    show_score=font.render(text,True,color)
    gameWindow.blit(show_score,[x,y])
def welcome():
    exit_game=False
    while not exit_game:
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
        # gameWindow.blit(bgimg,(0,0))
        show("Welcome to Game Task",white,140,20,55)
        show("Developed By Kushal Sharma (KD)",white,200,120,28)
        show("Press enter to continue",white,130,280,55)
        pygame.display.update()

def gameloop():
    exit_game=False
    gameover=False
    a=random.randint(0,1)
    b=random.randint(0,1)
    c=random.randint(0,1)
    d=random.randint(0,1)
    e=random.randint(0,1)
    f=random.randint(0,1)
    g=random.randint(0,1)
    h=random.randint(0,1)
    i=random.randint(0,1)
    s=a+b+c+d+e+f+g+h+i
    clock=pygame.time.Clock()
    start=1000
    score=0
    u=0
    a1=0
    a2=0
    a3=0
    a4=0
    a5=0
    a6=0
    a7=0
    a8=0
    a9=0
    while not exit_game:
        if gameover:
            gameWindow.fill(black)
            # gameWindow.blit(goimg,(0,0))
            # with open("Highscore.txt",'w') as f:
            #     f.write(str(highscore))
            show("Game Over!",red,230,170,55)
            show("Press Enter to continue",white,530,230,20)
            # show("Score:"+str(score),white,250,390,20)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        
                        gameloop()
        else:
            start-=1
            # print(start)
            for event in pygame.event.get():
                # print(event)
                if event.type==pygame.QUIT:
                    exit_game = True
                gameWindow.fill(white)
                # show("Score:"+str(score),black,70,400,55)
                
                # pygame.display.update()
                start-=1
                # print(a)
                show("Select matching number that corresponds to the number of stars displayed or",black,100,20,20)
                show("Select the pair of numbers that matches the count of stars within 10 secs",black,110,50,20)
                if a==1:
                    gameWindow.blit(star,(70,110))
                    
                if b==1:
                    gameWindow.blit(star,(120,110))
                    
                if c==1:
                    gameWindow.blit(star,(170,110))
                    
                if d==1:
                    gameWindow.blit(star,(70,160))
                    
                if e==1:
                    gameWindow.blit(star,(120,160))
                    
                if f==1:
                    gameWindow.blit(star,(170,160))
                    
                if g==1:
                    gameWindow.blit(star,(70,210))
                    
                if h==1:
                    gameWindow.blit(star,(120,210))
                    
                if i==1:
                    gameWindow.blit(star,(170,210))
                
                b0 = button(gameWindow, (500, 110), " 1 ", 30, "black on grey")
                b1 = button(gameWindow, (550, 110), " 2 ", 30, "black on grey")
                b2 = button(gameWindow, (600, 110), " 3 ", 30, "black on grey")
                b3 = button(gameWindow, (500, 160), " 4 ", 30, "black on grey")
                b4 = button(gameWindow, (550, 160), " 5 ", 30, "black on grey")
                b5 = button(gameWindow, (600, 160), " 6 ", 30, "black on grey")
                b6 = button(gameWindow, (500, 210), " 7 ", 30, "black on grey")
                b7 = button(gameWindow, (550, 210), " 8 ", 30, "black on grey")
                b8 = button(gameWindow, (600, 210), " 9 ", 30, "black on grey")
                if a1>=1:
                    b0 = button(gameWindow, (500, 110), " 1 ", 30, "white on grey")
                    button(gameWindow, (70, 300), " 1 ", 30, "black on grey")
                if a2>=1:
                    b1 = button(gameWindow, (550, 110), " 2 ", 30, "white on grey")
                    button(gameWindow, (120, 300), " 2 ", 30, "black on grey")
                if a3>=1:
                    b2 = button(gameWindow, (600, 110), " 3 ", 30, "white on grey")
                    button(gameWindow, (170, 300), " 3 ", 30, "black on grey")
                if a4>=1:
                    b3 = button(gameWindow, (500, 160), " 4 ", 30, "white on grey")
                    button(gameWindow, (220, 300), " 4 ", 30, "black on grey")
                if a5>=1:
                    b4 = button(gameWindow, (550, 160), " 5 ", 30, "white on grey")
                    button(gameWindow, (270, 300), " 5 ", 30, "black on grey")
                if a6>=1:
                    b5 = button(gameWindow, (600, 160), " 6 ", 30, "white on grey")
                    button(gameWindow, (320, 300), " 6 ", 30, "black on grey")
                if a7>=1:
                    b6 = button(gameWindow, (500, 210), " 7 ", 30, "white on grey")
                    button(gameWindow, (370, 300), " 7 ", 30, "black on grey")
                if a8>=1:
                    b7 = button(gameWindow, (550, 210), " 8 ", 30, "white on grey")
                    button(gameWindow, (420, 300), " 8 ", 30, "black on grey")
                if a9>=1:
                    b8 = button(gameWindow, (600, 210), " 9 ", 30, "white on grey")
                    button(gameWindow, (470, 300), " 9 ", 30, "black on grey")
                
                # pygame.display.update()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b0.collidepoint(pygame.mouse.get_pos()):
                        a1=a1+1
                        if a1 == 1:
                            u=u+1
                            if u==s:
                                score=score+1
                                gameloop()
                    
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        a2=a2+1
                        if a2==1:
                            u=u+2
                            if u==s:
                                score=score+1
                                gameloop()
                    if b2.collidepoint(pygame.mouse.get_pos()):
                        a3=a3+1
                        if a3==1:
                            u=u+3
                            if u==s:
                                score=score+1
                                gameloop()
                    if b3.collidepoint(pygame.mouse.get_pos()):
                        a4=a4+1
                        if a4==1:
                            u=u+4
                            if u==s:
                                score=score+1
                                gameloop()
                    if b4.collidepoint(pygame.mouse.get_pos()):
                        a5=a5+1
                        if a5==1:
                            u=u+5
                            if u==s:
                                score=score+1
                                gameloop()
                    if b5.collidepoint(pygame.mouse.get_pos()):
                        a6=a6+1
                        if a6==1:
                            u=u+6
                            if u==s:
                                score=score+1
                                gameloop()
                    if b6.collidepoint(pygame.mouse.get_pos()):
                        a7=a7+1
                        if a7==1:
                            u=u+7
                            if u==s:
                                score=score+1
                                gameloop()
                    if b7.collidepoint(pygame.mouse.get_pos()):
                        a8=a8+1
                        if a8==1:
                            u=u+8
                            if u==s:
                                score=score+1
                                gameloop()
                    if b8.collidepoint(pygame.mouse.get_pos()):
                        a9=a9+1
                        if a9==1:
                            u=u+9
                            if u==s:
                                score=score +1
                                gameloop()
            # show("Time remaining "+str(int(start/100))+" secs",white,370,350,20)
            show("Time remaining "+str(int(start/100))+" secs",black,370,350,20)
           
                
            
            
            pygame.display.update()
            if start <=0:
                gameover=True    
        pygame.display.update()
        clock.tick(100)
    pygame.quit()
    quit() 

welcome()