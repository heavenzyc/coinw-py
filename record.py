class Record :
    def __init__(self, board, latest_price, low, high, volume) :
        self.board = board
        self.latest_price = latest_price
        self.low = low
        self.high = high
        self.volume = volume

    def print_record(self):
        print('board=%s, latest_price=%s, low=%s, high=%s, volume=%s' %(self.board, self.latest_price, self.low, self.high, self.volume))