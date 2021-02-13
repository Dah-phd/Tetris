import random


class field:
    # block presets
    blocks = [
        {'1': (0, 4), '2': (1, 4), '3': (2, 4), '4': (3, 4)},
        {'1': (0, 4), '2': (1, 4), '3': (2, 4), '4': (2, 5)},
        {'1': (0, 5), '2': (1, 5), '3': (2, 4), '4': (2, 5)},
        {'1': (0, 4), '2': (1, 4), '3': (1, 5), '4': (2, 5)},
        {'1': (0, 5), '2': (1, 4), '3': (1, 5), '4': (2, 4)},
        {'1': (0, 4), '2': (0, 5), '3': (1, 4), '4': (1, 5)},
        {'1': (0, 4), '2': (1, 4), '3': (1, 5), '4': (2, 4)}
    ]

    def __init__(self):
        # base vars
        self.score = 0

    def start(self):
        self.board = [[0 for _ in range(10)] for _ in range(24)]
        self.alive = True
        self.block()

    def _burn(self):
        for row, t in enumerate(self.board[4:]):
            if all(t):
                self.board.pop(row)
                self.board.insert(0, [t for t in range(10)])
        return

    def prb(self):
        for n, row in enumerate(self.board):
            print(row, '<--ROW:', n)

    def _collison_bot(self):
        for val in self.falling.values():
            if val[0] == 23 or self.board[val[0]+1][val[1]] == 1:
                return True
            return False

    def _collison_left(self):
        for val in self.falling.values():
            if val[1] == 0 or self.board[val[0]][val[1]-1] == 1:
                return True
            return False

    def _collison_right(self):
        for val in self.falling.values():
            if val[1] == 9 or self.board[val[0]][val[1]+1] == 1:
                return True
            return False

    def move_left(self):
        if self._collison_left():
            return
        self._retire()
        for key, val in self.falling.items():
            self.falling[key] = (val[0], val[1]-1)
        self._set()
        return

    def move_right(self):
        if self._collison_right():
            return
        self._retire()
        for key, val in self.falling.items():
            self.falling[key] = (val[0], val[1]+1)
        self._set()
        return

    def block(self):
        if not any(self.board[:4]):
            pass
        else:
            self.falling = self.blocks[random.randint(0, 6)]
            self._set()
            return

    def _set(self):
        for cord in ['1', '2', '3', '4']:
            self.board[cord[0]][cord[1]] = 1
        return

    def _retire(self):
        for cord in ['1', '2', '3', '4']:
            self.board[cord[0]][cord[1]] = 0
        return

    def motion(self):
        if not self._collison_bot():
            self._retire()
            for key, val in self.falling.items():
                self.falling[key] = (val[0]+1, val[1])
            self._set()
        else:
            self.block()
