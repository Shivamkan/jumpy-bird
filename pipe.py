from random import randint
import player
import pygame

from util import *


class pipe:
    def __init__(self, screen, player, width=500, height=500):
        self.movespeed = 2
        self.screen = screen
        self.PipeWidth = width / 6
        self.GapHeight = height / 5
        self.BottomTolerance = self.GapHeight * 2
        self.PipeHeight = (self.PipeWidth, (randint(int(self.GapHeight / 2), self.BottomTolerance) + 100))
        self.width = width
        self.height = height
        self.SpawnPipe()
        self.player = player
        self.pipelist = [self.top, self.bottom]

    def SpawnPipe(self):
        self.top = pygame.Rect((self.width, -100), (self.PipeHeight))
        self.bottom = pygame.Rect((self.width, self.top.height + self.GapHeight), (self.PipeWidth, self.height))
        # print("spawned")

    def MovePipe(self):
        self.top.x -= self.movespeed
        self.bottom.x -= self.movespeed
        # print("moving")

    def DrawPipe(self):
        pygame.draw.rect(self.screen, RGB("#00ff00"), self.top)
        pygame.draw.rect(self.screen, RGB("#00ff00"), self.bottom)
        # print("drawing")

    def addpoint(self):
        if self.top.x == 40 or self.top.x == 41:
            self.player.point += 1
            # print(self.player.point)
