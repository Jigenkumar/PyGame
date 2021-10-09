import pygame

#Window Creation
x = pygame.init()
gamewindow = pygame.display.set_mode((900, 500))
pygame.display.set_caption("My Game")

#Game Specific Veriables

exit_game = False
game_over = False

#Creating Game Loop

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You pressed RIGHT aerrow key")
            if event.key == pygame.K_LEFT:
                print("You pressed LEFT aerrow key")
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_0:
                print("You pressed 0")
            if event.key == pygame.K_1:
                print("You pressed 1")

pygame.quit()
quit()