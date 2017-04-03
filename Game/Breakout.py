import pygame

from Game import *
from Game.Scenes import *
from Game.Shared import GameConstants

# Define the Breakout Class
class Breakout:

    def __init__(self):
        self.__lives = 5
        self.__score = 0

        self.__level = Level(self)
        self.__level.load(0)
        #self.__level.loadRandom()

        # Here we define the middle of the pad to be used later.

        self.__pad = Pad((GameConstants.SCREEN_SIZE[0]/2,
                         GameConstants.SCREEN_SIZE[1] - GameConstants.PAD_SIZE[1]),
                         pygame.image.load(GameConstants.SPRITE_PAD) # Load PAD Sprite into memory
                         )
        self.__balls = [Ball((100, 400), pygame.image.load(GameConstants.SPRITE_BALL), self)]

        pygame.init() # init pygame
        pygame.mixer.init() # init audio mixer
        pygame.display.set_caption("FakeOut") # simply the window caption

        self.__clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE,  # set the display mode
                                              pygame.DOUBLEBUF, 32)

        pygame.mouse.set_visible(1)  # make the mouse invisible

        # declare our scenes (0 - 3 (4))

        self.__scenes = (
            PlayingGameScene(self),
            GameOverScene(self),
            HighscoreScene(self),
            MenuScene(self)
        )

        self.__currentScene = 3  # set the first scene (MenuScene.py)

        # load the game's sounds into the mixer.

        self.__sounds = (
            pygame.mixer.Sound(GameConstants.SOUND_FILE_GAMEOVER),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK_LIFE),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK_SPEED),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_WALL),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_PAD)
        )

    def start(self):
        while 1:
            self.__clock.tick(100)

            self.screen.fill((0, 0, 0))

            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get())
            currentScene.render()

            pygame.display.update()

    def changeScene(self, scene):
        self.__currentScene = scene

    def getLevel(self):
        return self.__level

    def getScore(self):
        return self.__score

    def increaseScore(self, score):
        self.__score += score

    def getLives(self):
        return self.__lives

    def getBalls(self):
        return self.__balls

    def getPad(self):
        return self.__pad

    def playSound(self, soundClip):
        sound = self.__sounds[soundClip]

        sound.stop()
        sound.play()

    def reduceLives(self):
        self.__lives -= 1

    def increaseLives(self):
        self.__lives += 1

    def reset(self):
        self.__lives = 5
        self.__score = 0
        self.__level.load(0)

Breakout().start()
