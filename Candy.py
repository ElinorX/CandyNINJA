#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame, sys
import os
import random


# In[2]:


player_lives = 3  # chances 
score = 0  # initial value
# list to store image of candy and bomb
candy = ['C1', 'C2', 'C3', 'C4', 'C5','bomb']  


# In[3]:


WIDTH = 800
HEIGHT = 500
# how many frame per second you want the game to display
FPS = 12   
#define the size of Candy image
Candy_WIDTH, Candy_HEIGHT = 80, 80 
pygame.init()
# title
pygame.display.set_caption('Final Project Scaffold')  
# display window
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


# In[4]:


# define color 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BABY_BLUE = (137, 207, 250)


# In[5]:


# backgroud
background = pygame.transform.scale(pygame.image.load('Backgroud-1.jpeg'), (WIDTH, HEIGHT))
# font
font = pygame.font.Font(os.path.join(os.getcwd(), 'comic copy.ttf'), 42)  
score_text = font.render('Score : ' + str(score), True, (255, 255, 255))  


# In[6]:


# randomly generated candys' position and store the data
def generate_random_candy(candy):
    #candy_path = "images/" + candy + ".png"
    candy_path =  candy + ".png"
    data[candy] = {
        'img': pygame.transform.scale(pygame.image.load(candy_path),(Candy_WIDTH, Candy_HEIGHT)),
        # candy position 
        'x': random.randint(100, 500),  
        'y': 800,
        # speed 
        'speed_x': random.randint(-10, 10),  
        'speed_y': random.randint(-80, -60), 
        # avoid generating the candy outside of rectangle
        'throw': False, 
        't': 0,
        'hit': False,
    }
    # keep candy showing on the screen while the game is still running
    if random.random() >= 0.75:  
        data[candy]['throw'] = True
    else:
        data[candy]['throw'] = False


# In[7]:


# store the data
data = {}
for candy in candy:
    generate_random_candy(candy)


# In[8]:


def hide_cross_lives(x, y):
    gameDisplay.blit(pygame.image.load("white_lives copy.png"), (x, y))


# In[9]:


font_name = pygame.font.match_font('comic copy.ttf')


# In[10]:


# function to draw the text 
def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BABY_BLUE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)


# In[11]:


# function to display how many chances you have before game is over
def draw_lives(display, x, y, lives, image):
    for i in range(lives):
        img = pygame.image.load(image)
        img_rect = img.get_rect()
        img_rect.x = int(x + 35 * i)
        img_rect.y = y
        display.blit(img, img_rect)


# In[12]:


# function to draw the start and end of the game 
def show_gameover_screen():
    gameDisplay.blit(background, (0, 0))
    draw_text(gameDisplay, "CANDY NINJA!", 90, WIDTH / 2, HEIGHT / 4)
    if not game_over:
        draw_text(gameDisplay, "Score : " + str(score), 50, WIDTH / 2, HEIGHT / 2)
    draw_text(gameDisplay, "Press any key to start the game", 64, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


# In[13]:


first_round = True
# if the player cut 3 more bomb, game over, we end the loop
game_over = True  
# keep check the loop
game_running = True  
while game_running:
    if game_over:
        if first_round:
            show_gameover_screen()
            first_round = False
        game_over = False
        player_lives = 3
        draw_lives(gameDisplay, 690, 5, player_lives, 'white_lives copy.png')
        score = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    gameDisplay.blit(background, (0, 0))
    gameDisplay.blit(score_text, (0, 0))
    draw_lives(gameDisplay, 690, 5, player_lives, 'white_lives copy.png')
    for key, value in data.items():
        if value['throw']:
            # moving candy postition
            value['x'] += value['speed_x']  
            value['y'] += value['speed_y']  
            value['speed_y'] += (1 * value['t'])  
            value['t'] += 1
            if value['y'] <= 800:
                # display the candy
                gameDisplay.blit(value['img'], (value['x'], value['y']))  
            else:
                generate_random_candy(key)
                # get the position of mouse 
            current_position = pygame.mouse.get_pos()  
            if not value['hit'] and current_position[0] > value['x'] and current_position[0] < value['x'] + 60                     and current_position[1] > value['y'] and current_position[1] < value['y'] + 60:
                if key == 'bomb':
                    player_lives -= 1
                    if player_lives == 0:
                        hide_cross_lives(690, 15)
                    elif player_lives == 1:
                        hide_cross_lives(725, 15)
                    elif player_lives == 2:
                        hide_cross_lives(760, 15)
                    # end the game and go back to the original start window 
                    if player_lives < 0:
                        show_gameover_screen()
                        game_over = True
                    half_candy_path = "explosion copy.png"
                else:
                    # half_candy_path = "images/" + "half_" + key + ".png"
                    half_candy_path = key+ "_half" + ".png"
                value['img'] = pygame.transform.scale(pygame.image.load(half_candy_path),(Candy_WIDTH, Candy_HEIGHT))
                value['speed_x'] += 10
                if key != 'bomb':
                    score += 1
                score_text = font.render('Score : ' + str(score), True, (255, 255, 255))
                value['hit'] = True
        else:
            generate_random_candy(key)
    pygame.display.update()
    clock.tick(FPS)


# In[ ]:


pygame.quit()


# In[ ]:


# make sure we only running the game if we run the main function directly 
# not from other file 
if __name__ == "__main__":
    main()


# In[ ]:




