import pygame


class Text:

    def __init__(self):
        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)
        self.font = pygame.font.Font('freesansbold.ttf', 42)
        self.message = ''
        self.text = self.font.render(self.message, True, self.green, self.blue)
        self.textRect = self.text.get_rect()
        self.textRect.center = (220, 350)

    def start_message(self):
        self.message = "CLICK TO B TO START"
        self.text = self.font.render(self.message, True, self.green, self.blue)
        return self.text

    def end_message(self):
        self.message = "GAME OVER"
        self.text = self.font.render(self.message, True, self.green, self.blue)
        return self.text
