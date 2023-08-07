import random
import sys
import pygame
import time

def ball_animation():
    global ball_speed_x,ball_speed_y, player_score, opponent_score, score_time
    ball.x+=ball_speed_x
    ball.y+=ball_speed_y

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y*=-1
        ball_speed_y *= 1.0001

    if ball.left <=0:
        player_score+=1
        score_time=pygame.time.get_ticks()

    if ball.right >= width:
        opponent_score+=1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x*=-1
        ball_speed_x *= 1.0001


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= height:
        player.bottom = height
def opponent_animation():
    if opponent.top<ball.y:
        opponent.top+=opponent_speed
    if opponent.bottom>ball.y:
        opponent.bottom-=opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= height:
        opponent.bottom = height
def ball_restart():
    global ball_speed_y, ball_speed_x, score_time

    current_time=pygame.time.get_ticks()
    ball.center = (width / 2, height / 2)
    if current_time-score_time<700:
        number_3 = game_font.render("3",False, (255,0,0))
        screen.blit(number_3,(width/2-9, height/2+50))
    if 700 <current_time - score_time < 1400:
        number_2 = game_font.render("2", False, (255,0,0))
        screen.blit(number_2, (width / 2-9, height / 2+50))
    if 1400 < current_time - score_time < 2100:
        number_1 = game_font.render("1", False, (255,0,0))
        screen.blit(number_1, (width / 2 -9, height / 2+50))
    if current_time-score_time<2100:
        ball_speed_x, ball_speed_y=0,0
    else:
        ball_speed_y= random.choice((2, 3, 4))*random.choice((1,-1))
        ball_speed_x= random.choice((2, 3, 4))* random.choice((1, -1))
        score_time=None
#main window
pygame.init()
FPS = 120
clock = pygame.time.Clock()
width = 1280
height = 960
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PONG")
# -------------------------------------------

# game obj

ball = pygame.Rect(width/2-15,height/2-15 ,30,30)
player = pygame.Rect(width-20, height/2-70, 10,140)
opponent = pygame.Rect(10, height/2-70, 10,140)
bg_color=pygame.Color("gray12")
light_grey = (200,200,200)


#Game Var
ball_speed_x = random.choice((1,2, 3, 4, 5)) * random.choice((1, -1))
ball_speed_y = random.choice((2, 3, 4, 5)) * random.choice((1, -1))
player_speed=0
opponent_speed=5

#text var
player_score=0
opponent_score=0
game_font=pygame.font.Font('freesansbold.ttf',32)

#Score Timer
score_time=True

# Game loop
while True:
# Handling inuts
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 5
            if event.key == pygame.K_UP:
                player_speed -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 5
            if event.key == pygame.K_UP:
                player_speed += 5
        if player.top <= 0:
            player.top = 0
        if player.bottom >= height:
            player.top = height

#Game logic
    ball_animation()
    player_animation()
    opponent_animation()
#Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (width/2,0), (width/2,height))

    if score_time:
        ball_restart()

    player_text=game_font.render(f"{player_score}", False,light_grey)
    screen.blit(player_text,(660,470))
    opponent_text=game_font.render(f"{opponent_score}", False,light_grey)
    screen.blit(opponent_text,(600,470))


# updating window
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FPS)


# ----------------------------------------------