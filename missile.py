import pygame

class MissilePalyer(pygame.sprite.Sprite):

    def __init__(self, posx, posy):
        super().__init__()
        self.velocity = 10
        self.image = pygame.image.load("images/missile2.png")
        self.image = pygame.transform.scale(self.image, (20, 100))
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = posx + 40
        self.rect.y = posy - 45
        self.song = pygame.mixer.Sound("songs/shoot.wav")

    def launch_missile(self):
        self.rect.y -= self.velocity


class MissileEnemy(pygame.sprite.Sprite):

    def __init__(self, posx, posy):
        super().__init__()
        self.velocity = 10
        self.image = pygame.image.load("images/brique.jpg")
        self.image = pygame.transform.scale(self.image, (20, 100))
        self.image = pygame.transform.rotate(self.image, 180)
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

    def shoot(self):
        self.rect.y += self.velocity


