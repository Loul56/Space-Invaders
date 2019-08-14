import pygame
from pygame.locals import 

class Score(pygame.sprite.Sprite):
    score_points = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 20)
        self.font.set_italic(1)
        self.color= Color('white')
        self.lastscore = -1
        self.update
        self.rect= self.image.get_rect().move(10, 450)
    
    def update(self):
        if self.score_points != self.lastscore:
            self.lastscore = self.score_points
            msg ="Score: %d" % self.score_points
            self.image = self.font.render(msg, 0, self.color)