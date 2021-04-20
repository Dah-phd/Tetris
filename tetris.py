import random


class engine:
    # block presets
    blocks = [
        {'1': (1, 4), '2': (2, 4), '3': (3, 4), '4': (4, 4)},
        {'1': (1, 4), '2': (2, 4), '3': (3, 4), '4': (3, 5)},
        {'1': (1, 5), '2': (2, 5), '3': (3, 4), '4': (3, 5)},
        {'1': (1, 4), '2': (2, 4), '3': (2, 5), '4': (3, 5)},
        {'1': (1, 5), '2': (2, 4), '3': (2, 5), '4': (3, 4)},
        {'1': (1, 4), '2': (1, 5), '3': (2, 4), '4': (2, 5)},
        {'1': (1, 4), '2': (2, 4), '3': (2, 5), '4': (3, 4)}
    ]

    def start(self):
        '''
        Builds the board, and starts the game, also restarts
        '''
        self.board = [[0 for _ in range(10)] for _ in range(25)]
        self.off = False
        self.alive = True
        self.score = 0
        self.que = random.randint(0, 6)
        self.block()

    def prb(self):
        '''
        Dev tool (not private) logs the current board
        '''
        for n, row in enumerate(self.board):
            print(row, '<--ROW:', n)

    def move_left(self):
        '''
        Moves the block left
        '''
        if self._collison_left() or self.off:
            return
        self._retire()
        for key, val in self.falling.items():
            self.falling[key] = (val[0], val[1]-1)
        self._set()
        return

    def move_right(self):
        '''
        Moves the block right
        '''
        if self._collison_right() or self.off:
            return
        self._retire()
        for key, val in self.falling.items():
            self.falling[key] = (val[0], val[1]+1)
        self._set()
        return

    def block(self):
        '''
        Generates new blocks
        '''
        self._burn()
        if 1 in self.board[4]:
            self.alive = False
            return
        self.falling = self.blocks[self.que].copy()
        self.que = random.randint(0, 6)
        self._set()
        self.off = False
        return

    def motion(self):
        '''
        Should be included in the main loop it moves the blocks
        '''
        if not self._collison_bot() and not self.off:
            self._retire()
            for key, val in self.falling.items():
                self.falling[key] = (val[0]+1, val[1])
            self._set()
            return
        self.off = True
        self.block()

    def flip(self):
        '''
        Looks ugly, I should try to optimize this monstrosity
        '''
        if self._is_square():
            return
            # check if it is square
        self._retire()
        base = self.falling['2']
        flipped = {}
        for key, val in self.falling.items():
            if key == '2':
                flipped[key] = base
                continue
            if val[0] == base[0]:
                flipped[key] = (val[0]-(val[1] - base[1]), base[1])
            elif val[1] == base[1]:
                flipped[key] = (base[0], val[1]-(base[0] - val[0]))
            else:
                if (val[0] > base[0] and val[1] > base[1]) or (val[0] < base[0] and val[1] < base[1]):
                    flipped[key] = (
                        val[0] + ((base[0]-val[0])*2),
                        val[1])
                else:
                    flipped[key] = (
                        val[0],
                        val[1] + ((base[1]-val[1])*2))
        for val in flipped.values():
            if val[1] < 0 or val[1] > 9 or self.board[val[0]][val[1]] == 1:
                self._set()
                return
        self.falling = flipped
        self._set()

    def _set(self):
        for cord in self.falling.values():
            self.board[cord[0]][cord[1]] = 1
        return

    def _retire(self):
        for cord in self.falling.values():
            self.board[cord[0]][cord[1]] = 0
        return

    def _is_square(self):
        if self.falling['1'][0] == self.falling['2'][0] and self.falling['3'][0] == self.falling['4'][0]:
            if self.falling['1'][1] == self.falling['3'][1] and self.falling['2'][1] == self.falling['4'][1]:
                return True
        return False

    def _burn(self):
        score = 0
        for num_row, row in enumerate(self.board[5:]):
            if all(row):
                self.board.pop(num_row+5)
                self.board.insert(5, [0 for _ in range(10)])
                score += 10
        if score > 20:
            self.score += score*3
        elif score > 10:
            self.score += score*2
        else:
            self.score += score
        return

    def _collison_bot(self):
        for val in self.falling.values():
            if val[0] == 24 or (self.board[val[0]+1][val[1]] == 1 and (val[0]+1, val[1]) not in self.falling.values()):
                return True
        return False

    def _collison_left(self):
        for val in self.falling.values():
            if val[1] == 0 or (self.board[val[0]][val[1]-1] == 1 and (val[0], val[1]-1) not in self.falling.values()):
                return True
        return False

    def _collison_right(self):
        for val in self.falling.values():
            if val[1] == 9 or (self.board[val[0]][val[1]+1] == 1 and (val[0], val[1]+1) not in self.falling.values()):
                return True
        return False
