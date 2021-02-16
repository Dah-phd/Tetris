from os import path


class highscore:

    def __init__(self, base_name, name=None, high='max'):
        '''
        base name: the file to store the values (it will be txt always but you can use any extension).

        name: name of the player that is currently playing (or use later as self.name = 'myname').

        high: default is max so the higher the score the better.
        '''
        self.base_name = base_name
        self.name = name
        self.high = high
        self._check()

    def quarry(self):
        '''
        returns all scores from the database.

        RETURNS LIST OF TUPLES
        '''
        result = []
        for score in self._pull().split('-<>-'):
            if not score:
                return
            else:
                result.append(self._decode(score))
        if self.high == 'min':
            return sorted(result, key=lambda x: x[1])
        else:
            return sorted(result, key=lambda x: x[1], reverse=True)

    def new_score(self, value):
        self.value = value
        entry = self._encode()
        data = self._pull()
        if not data:
            data = entry
            self._save(data)
            return
        data = data+'-<>-'+entry
        self._save(data)
        return

    def _encode(self):
        value = str((self.value*5)/19+16)
        return value+'-'+self.name

    def _decode(self, encoded):
        value, name = encoded.split('-')
        value = ((float(value)-16)*19)/5
        return (name, int(value))

    def _pull(self):
        with open(self.base_name, 'r') as f:
            return f.read()

    def _save(self, data):
        with open(self.base_name, 'w') as f:
            f.write(data)
        return

    def _check(self):
        if path.isfile(self.base_name):
            return
        else:
            with open(self.base_name, 'x'):
                return
