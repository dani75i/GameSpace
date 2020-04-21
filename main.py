import pygame
import random

from missile import MissilePalyer
from obstacle import Obstacle
from player import Player
from text import Text

pygame.init()

# Constantes
NUMBER_OBSTACLES = 20
SIZE_FENETRE_X = 840
SIZE_FENETRE_Y = 900

# Variables
list_briques = []
list_briques_rect = []
list_missiles = []
continuer = 1
killplayer = False
start = False
x = 0
y = 0
y2 = - SIZE_FENETRE_Y

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((SIZE_FENETRE_X, SIZE_FENETRE_Y))

# Definition du background
background = pygame.image.load("images/space.png")
background = pygame.transform.scale(background, (SIZE_FENETRE_X, SIZE_FENETRE_Y))

# Definition du menu
menu = pygame.image.load("images/instruction.PNG")
menu = pygame.transform.scale(menu, (300, 200))

# Instanciation de la classe Player
player = Player()

# Instanciation de la classe Text
text = Text()

# Instanciation de la classe Obstacle
for i in range(NUMBER_OBSTACLES):
    obstacle = Obstacle(random.randint(0, SIZE_FENETRE_X - 50), random.randint(0, 100))
    list_briques.append(obstacle)
    list_briques_rect.append(obstacle.rect)

# Son
# son = pygame.mixer.Sound("songs/Game.wav")

while continuer:

    # MOVING BACKGROUND
    y += 1
    y2 += 1

    fenetre.blit(background, (x, y))
    fenetre.blit(background, (x, y2))

    if y > SIZE_FENETRE_Y:
        y = -SIZE_FENETRE_Y
    if y2 > SIZE_FENETRE_Y:
        y2 = -SIZE_FENETRE_Y

    if not start:
        fenetre.blit(menu, (270, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                start = True

            elif event.key == pygame.K_b:
                missile = MissilePalyer(player.rect.x, player.rect.y)
                list_missiles.append(missile)

    if start:

        # Test si le vaisseau existe
        if not killplayer:
            fenetre.blit(player.image, (player.rect.x, player.rect.y))
        else:
            fenetre.blit(text.end_message(), text.textRect)

        # Générer de nouveaux obstacles
        # if len(list_briques) == NUMBER_OBSTACLES - 1:
        #     for i in range(2):
        #         obstacle = Obstacle(random.randint(100, 700), random.randint(0, 100))
        #         list_briques.append(obstacle)
        #         list_briques_rect.append(obstacle.rect)

        #########################
        ####  OBSTACLE PART  ####
        #########################
        for obstacle in list_briques:
            fenetre.blit(obstacle.image, (obstacle.rect.x, obstacle.rect.y))
            if obstacle.rect.colliderect(player.rect) != 1:
                obstacle.move_forward()
            else:
                obstacle.move_forward()
                killplayer = True

        ########################
        ####  MISSILE PART  ####
        ########################
        for missile in list_missiles:
            fenetre.blit(missile.image, (missile.rect.x, missile.rect.y))
            missile.launch_missile()

        # Destroy missile if is not into the screen
        for missile in list_missiles:
            if missile.rect.y < 0:
                list_missiles.remove(missile)

        # Test collision entre le joueur et les briques
        for missile in list_missiles:
            if missile.rect.collidelist(list_briques_rect) != -1:
                index = missile.rect.collidelist(list_briques_rect)
                list_briques.remove(list_briques[index])
                list_briques_rect.remove(list_briques_rect[index])
                list_missiles.remove(missile)
                break

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and player.rect.x + player.rect.width < SIZE_FENETRE_X:
            player.move_right()

        elif keys[pygame.K_LEFT] and player.rect.x > 0:
            player.move_left()

        elif keys[pygame.K_UP] and player.rect.y > 0:
            if player.rect.collidelist(list_briques_rect) == -1:
                player.move_up()

        elif keys[pygame.K_DOWN] and player.rect.y + player.rect.height < SIZE_FENETRE_Y:
            player.move_down()

    # Rafraichissement
    pygame.display.flip()
