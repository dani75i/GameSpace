import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 10
        self.image = pygame.image.load("images/vaisseau.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 480 - self.rect.height

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity
