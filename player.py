import pygame


class player:
    def __init__(self,height):
        self.FallSpeed = 0
        self.dead = 0
        self.point = 0
        self.Bird = pygame.image.load("bird.png")
        self.Birdrect = self.Bird.get_rect()
        self.Birdrect.x = 45
        self.Birdrect.y = height / 2 - 50

    def Fall(self):
        self.Birdrect.y += int(self.FallSpeed)
        self.FallSpeed += .2
        self.Birdrect.y = max(0,self.Birdrect.y)

    def Jump(self):
        self.FallSpeed = -7

    def handleInput(self, event):
        for event in event:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.Jump()

    def DrawPlayer(self, screen):
        screen.blit(self.Bird,self.Birdrect)
