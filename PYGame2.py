import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Set Title
pygame.display.set_caption("🌈My Game🌞")

# FPS
clock = pygame.time.Clock()


Background = pygame.image.load(
    "C:/Users/melis/OneDrive/바탕 화면/독학실습/Py_Game2/Background.png")

character = pygame.image.load(
    "C:/Users/melis/OneDrive/바탕 화면/독학실습/Py_Game2/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2)-(character_width/2)
character_y_pos = (screen_height-character_height)


to_x = 0
character_speed = 10

running = True

while running:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width

    screen.blit(Background(0, 0))
    screen.blit(character(character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()
