from Game.Bricks import Brick
from Game.Shared import *
from Game import *

class BallBrick(Brick):

    def __init__(self, position, sprite, game):
        super(BallBrick, self).__init__(position, sprite, game)

    def BallSpawn(self, position, sprite, game):
            self.__game = game
            self.__speed = 3
            self.__increment = [2, 2]
            self.__direction = [1, 1]
            self.__inMotion = 1
            super(self).__init__(position, GameConstants.BALL_SIZE, sprite)

    def isDestroyed(self):
        return self.__lives <= 0
