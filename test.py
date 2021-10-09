import pygame, random
from pygame import display, movie

#Colors
white = (255, 255, 255)
black = (255, 255, 255, 255)
red = (255, 0, 0)
food_size = 30
fps = 90

#Window Creation
x = pygame.init()
gamewindow = pygame.display.set_mode((900, 500))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()

pygame.mixer.init()

#Game Specific Veriables
exit_game = False
game_over = False

#Put text on screen
font = pygame.font.SysFont(None, 55)
def text_(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    gamewindow.blit(screen_text, (x,y))

#Create Snake
def plot_snake(snk_list):
    snake = pygame.image.load("Snake_35967.png")
    snake = pygame.transform.scale(snake, (40, 40))
    for x, y in snk_list:
        gamewindow.blit(snake, (x, y))
        # pygame.draw.rect(gamewindow, colour, [x, y, snake_size, snake_size])

#BackGround
bgimg = pygame.image.load("BackGround.jpg")
bgimg = pygame.transform.scale(bgimg, (900, 500)).convert_alpha()
wcimg = pygame.image.load("welcome.jpg")
wcimg = pygame.transform.scale(wcimg, (900, 500)).convert_alpha()
goimg = pygame.image.load("gameover.png")
goimg = pygame.transform.scale(goimg, (900, 500)).convert_alpha()

def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill(white)
        gamewindow.blit(wcimg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Game_Loop()
                    
        pygame.display.update()
        clock.tick(fps)
#Creating Game Loop
def Game_Loop():
    food = pygame.image.load("Food.png")
    food = pygame.transform.scale(food, (30, 30))
    exit_game = False
    game_over = False
    snake_length = 1
    int_velocity = 3
    snake_x = 100
    snake_y = 100
    velocity_x = 0
    velocity_y = 0
    snake_size = 30
    food_x = random.randint(0, 900)
    food_y = random.randint(0, 500)
    score = 0
    snk_list = []
    while not exit_game:
        if game_over:
            
            gamewindow.fill(white)
            gamewindow.blit(goimg, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Game_Loop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = +int_velocity
                        velocity_y = 0
                    
                    if event.key == pygame.K_LEFT:
                        velocity_x = -int_velocity
                        velocity_y = 0
                        
                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = +int_velocity
                        
                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -int_velocity

            snake_x += int(velocity_x)
            snake_y += int(velocity_y)

            if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8:
                pygame.mixer.music.load('beep.mp3')
                pygame.mixer.music.play()
                score+=10
                food_x = random.randint(0, 900)
                food_y = random.randint(0, 500)
                int_velocity += 0 
                snake_length += 2

            if snake_x >= 900:
                snake_x = 10
            if snake_x <= 0:
                snake_x = 900
            if snake_y > 500 or snake_y < 0:
                game_over = True
                pygame.mixer.music.load('explosion.wav')
                pygame.mixer.music.play()

            head = []
            head.append(snake_x)
            head.append(snake_y)
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('explosion.wav')
                pygame.mixer.music.play()
            else:
                snk_list.append(head)

            if len(snk_list) > snake_length:
                del snk_list[0]
                    
            gamewindow.fill(white)
            gamewindow.blit(bgimg, (0,0))
            text_("Score: "+str(score), red, 5, 5)
            plot_snake(snk_list)
            gamewindow.blit(food, (food_x, food_y))
            # (gamewindow, red, [food_x, food_y, food_size, food_size])
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()