import os
import fileinput
import pygame
import random

from Game.Bricks import *
from Game.Shared import *

# generic Level class. Defines the components of a level, reads the level dat file

class Level:

    def __init__(self, game):
        self.__game = game
        self.__bricks = []
        self.__amountOfBricksLeft = 0
        self.__currentLevel = 0

    def getBricks(self):
        return self.__bricks

    def getAmountOfBricksLeft(self):
        return self.__amountOfBricksLeft

    def brickHit(self):
        self.__amountOfBricksLeft -= 1

    def loadNextLevel(self):
        self.__currentLevel += 1
        fileName = os.path.join("Assets", "Levels", "level" +str(self.__currentLevel) + ".dat")

        if not os.path.exists(fileName):
            self.loadRandom()

        else:
            self.load(self.__currentLevel)

    def loadRandom(self):

        self.__bricks = []

        x, y = 0, 0

        maxBricks = int(GameConstants.SCREEN_SIZE[0] / GameConstants.BRICK_SIZE[0])
        rows = random.randint(2, 8)

        # define the different bricks (tiles). Labelled as 1, 2, 3, etc... Must then define Sprite and Render. Also append total brick count (not always useful)
        amountOfSuperPowerBricks = 0
        for row in range(0, rows):
            for brick in range(0, maxBricks):
                brickType = random.randint(0, 5) # 0 = Null Brick
                if brickType == 1 or amountOfSuperPowerBricks >= 2:
                    brick = Brick([x, y], pygame.image.load(GameConstants.SPRITE_BRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif brickType == 2:
                    brick = SpeedBrick([x, y], pygame.image.load(GameConstants.SPRITE_SPEEDBRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                    amountOfSuperPowerBricks += 1

                elif brickType ==  3:
                    brick = LifeBrick([x, y], pygame.image.load(GameConstants.SPRITE_LIFEBRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                    amountOfSuperPowerBricks += 1

                elif brickType == 4:
                    brick = SuperBrick([x, y], pygame.image.load(GameConstants.SPRITE_SUPERBRICK), self.__game) # need a new sprite for superbrick
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 2

                elif brickType == 5:
                    brick = BallBrick([x, y], pygame.image.load(GameConstants.SPRITE_BALLBRICK), self.__game) # need a new sprite for superbrick
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                    amountOfSuperPowerBricks += 1

                x += GameConstants.BRICK_SIZE[0]

            x = 0
            y += GameConstants.BRICK_SIZE[1]

    def load(self, level):
        self.__currentLevel = level
        self.__bricks = []

        x, y = 0, 0
        
        # define the different bricks (tiles). Labelled as 1, 2, 3, etc... Must then define Sprite and Render. Also append total brick count (not always useful)

        for line in fileinput.input(os.path.join("Game", "Assets", "Levels", "level" + str(level) + ".dat")):
            for currentBrick in line:
                if currentBrick == "1":
                    brick = Brick([x, y], pygame.image.load(GameConstants.SPRITE_BRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif currentBrick == "2":
                    brick = SpeedBrick([x, y], pygame.image.load(GameConstants.SPRITE_SPEEDBRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif currentBrick == "3":
                    brick = LifeBrick([x, y], pygame.image.load(GameConstants.SPRITE_LIFEBRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif currentBrick == "4":
                    brick = SuperBrick([x, y], pygame.image.load(GameConstants.SPRITE_SUPERBRICK), self.__game) # need a new sprite for superbrick
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 2
                    
                elif currentBrick == "5":
                    brick = BallBrick([x, y], pygame.image.load(GameConstants.SPRITE_BALLBRICK), self.__game) # need a new sprite for superbrick
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                x += GameConstants.BRICK_SIZE[0]

            x = 0
            y += GameConstants.BRICK_SIZE[1]




