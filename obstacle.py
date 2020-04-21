import pygame
import random

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, posx, posy):
        super().__init__()
        self.velocity = 1
        self.posx = posx
        self.posy = posy
        self.image = pygame.image.load("images/asteroide.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = self.posx
        self.rect.y = self.posy
        self.origine_image = self.image
        self.angle = random.randint(0, 90)
        self.image = pygame.transform.rotate(self.image, self.angle)

    def move_forward(self):
        self.rect.y += self.velocity
        self.rotate()

    def rotate(self):
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
