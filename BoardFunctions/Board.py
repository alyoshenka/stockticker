class Board:
    size = 0
    data = []
    """
        board data:
            [ None, Red, Red, Red, None, Green, ... ]
    """

    def __init__(self, size):
        self.size = size
        
        self.initData()

    def initData(self):
        self.data = [None for i in range(self.size)]

    def turnOn(self, idx, color=(255,255,255)):
        if idx >= len(self.data):
            print('index {0} out of bounds: size = {1}'.format(idx, self.size))
            return
        self.data[idx] = color

    def turnOff(self, idx):
        self.data[idx] = None

    def setColor(self, idx, color):
        self.turnOn(idx, color=color)