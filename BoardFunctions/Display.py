import pygame
from BoardFunctions import BoardDisplay

class Display:
    screen = None
    width = 0
    height = 0
    background = None
    board = None
    size = 0
    space = 0
    shouldExit = False
    boardDisplay = None

    def __init__(self, board, rows=8, cols=32, width=1600, height=400, background=(0, 20, 30), size=20, space=50):
        self.background = background
        self.width = width
        self.height = height
        self.board = board
        self.size = size
        self.space = space

        self.boardDisplay = BoardDisplay.BoardDisplay(board, cols, rows)       
        self.initPygame()

    def initPygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('stock board simulator')
        icon = pygame.image.load('./assets/images/wsb.png')
        pygame.display.set_icon(icon)

    def draw(self):
        self.screen.fill(self.background)
        self.boardDisplay.drawBoard(self.screen, self.space, self.size)

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.shouldExit = True       
        self.draw()
        pygame.display.update()
        return self.shouldExit
            
