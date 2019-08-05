import pygame
import random
import os
pygame.mixer.init()

pygame.init()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
#creating window

screen_width=1000
screen_height=600
gamewindow=pygame.display.set_mode((screen_width,screen_height))
#Game title
pygame.display.set_caption("SnakeWithSaurabhSahu")
pygame.display.update()


bgimg=pygame.image.load("snake.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)



def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])
def plot_snake(gamewindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        gamewindow.fill((250,220,230))
        text_screen("***Welcome in saurabh's_snake game*** ",black,100,250)
        text_screen("Press SPACEBAR to play ", black, 250, 300)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:

                    pygame.mixer.music.load('back.mp3.mp3')
                    pygame.mixer.music.play()

                    gameloop()

        pygame.display.update()
        clock.tick(60)

# creating a game loop
def gameloop():
    # Game specific variables

    exit_game = False
    game_over = False
    velocity_x = 0
    velocity_y = 0
    init_velocity = 3
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2.5)
    score = 0
    # check if hiscore file not exist
    if(not os.path.exists("highscore.txt")):
        with open ("highscore.txt","w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore=f.read()

    snk_list = []
    snk_length = 1
    snake_x = 45
    snake_y = 55
    snake_size = 20

    fps = 60


    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))

            gamewindow.fill(white)
            text_screen("Game Over! Press ENTER to play again..",red,130,280)
            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    # if event.key==pygame.K_q:             cheat code  ---here by cheating i'm increasing our score
                    #     score+=5


            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y
            if abs(snake_x - food_x)<10and abs(snake_y - food_y)<10:
                score+=10

                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 3)
                snk_length+=5

                if score>int(highscore):
                    highscore=score


            gamewindow.fill(white)
            gamewindow.blit(bgimg,(0,0))
            text_screen("score: " + str(score)+"  highscore:"+str(highscore) ,red, 5,5)
            pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[ :-1]:
                game_over=True
                pygame.mixer.music.load('game_over.mp3.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height :
                game_over=True
                pygame.mixer.music.load('game_over.mp3.mp3')
                pygame.mixer.music.play()



            plot_snake(gamewindow,black,snk_list,snake_size)


        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()