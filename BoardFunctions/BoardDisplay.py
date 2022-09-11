import pygame

from BoardFunctions.Board import Board

class BoardDisplay:
    width = 0
    height = 0
    board = None

    def __init__(self, board, width, height=8):
        assert board.size == width * height, 'board size ({0} does not meet given dimensions {1}x{2}'.format(board.size, width, height)
        self.width = width
        self.height = height
        self.board = board

    def drawBoard(self, screen, space, size):
        assert self.board, 'No board assigned'

        for i in range(self.width * self.height):
            if(i >= len(self.board.data)):
                print("index", i, "outside of data array bounds")
                return
            color = self.board.data[i]            
            row = self.getRow(i)
            col = self.getCol(i)

            if not self.board.data[i]: 
                continue
            pos = (col * space + space/2, row * space + space/2)
            pygame.draw.circle(screen, color, pos, size)

    def getRow(self, idx):
        return idx % self.height
    def getCol(self, idx):
        return idx // self.height