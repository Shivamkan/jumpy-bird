import pipe
import player
import pygame
import sys
import os
from util import *


class main:
    def __init__(self, width=500, height=500):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "500,30"
        pygame.init()
        self.PipeList = []
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.Clock = pygame.time.Clock()
        self.ground = pygame.Rect(0, height - 30, width, height)
        self.player = player.player(self.height)
        self.SpawnTime = 100000000
        self.font = pygame.font.SysFont(None, 100)
        self.font.set_bold(True)

    def draw(self):
        self.screen.fill((100, 100, 255))
        self.player.DrawPlayer(self.screen)
        self.DrawMap()

    def run(self):
        while True:
            self.Clock.tick(60)
            self.SpawnPipe()
            self.MyEvents()
            self.player.Fall()
            self.handleInput()
            self.draw()
            self.PipeUpdate()
            text = self.font.render(f"{self.player.point}", 1, (255, 255, 255))
            textpos = text.get_rect(centerx=int(self.screen.get_width() / 2),
                                              y=0)
            self.screen.blit(text, textpos)
            pygame.display.flip()

    def MyEvents(self):
        hitpipe = 0
        outofbound = 0
        if self.player.Birdrect.y <= -70:
            outofbound = 1
        for Pipe in self.PipeList:
            if self.player.Birdrect.collidelist(Pipe.pipelist) >= 0:
                hitpipe = 1
        if hitpipe == 1 or self.player.Birdrect.colliderect(self.ground) or outofbound == 1:
            self.player.FallSpeed = 0
            self.player.dead =1
            for event in self.event:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.player.Birdrect.y = int(self.height / 2 - 50)
                        self.player.FallSpeed = 0
                        self.player.dead = 0
                        self.PipeList = []
                        self.player.point = 0

    def handleInput(self):
        self.event = pygame.event.get()
        self.player.handleInput(self.event)
        for event in self.event:
            if event.type == pygame.QUIT:
                sys.exit()

    def DrawMap(self):
        pygame.draw.rect(self.screen, RGB("#002900ff"), self.ground)

    def SpawnPipe(self):
        if self.player.dead == 0:
            self.SpawnTime += 3
            if self.SpawnTime >= self.width:
                Pipe = pipe.pipe(self.screen, self.player, self.width, self.height)
                self.PipeList.append(Pipe)
                self.SpawnTime = 0

    def PipeUpdate(self):
        for Pipe in self.PipeList:
            Pipe.DrawPipe()
            if self.player.dead == 0:
                Pipe.MovePipe()
                Pipe.addpoint()


run = main(450, 650)
run.run()
