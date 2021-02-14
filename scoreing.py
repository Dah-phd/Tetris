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

    def quarry(self, set_=10):
        '''
        returns the top 10 scores,
        the quarried results could be increase by ne set_= int,
        if set_ = -1 quarries all.

        RETURNS LIST OF TUPLES
        '''
        result = {}
        for score in self._pull().split('-<>-'):
            val, name = self._decode(score)
            result[name] = val
        if self.high == 'min':
            return sorted(result.items(), key=lambda x: x[1])[:set_]
        else:
            return sorted(result.items(), key=lambda x: x[1], reverse=True)[:set_]

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
        name = self.name.replace('-', '!').replace('a', '9847y4').replace(
            'o', '023y87t').replace('e', '87tsfuyg33').replace('u', 'vd98yvib2g').replace('i', 's98yqi3ulbg')
        return value+'-'+name

    def _decode(self, encoded):
        value, name = encoded.split('-')
        value = ((float(value)-16)*19)/5
        name = name.replace('!', '-').replace('9847y4', 'a').replace(
            '023y87t', 'o').replace('87tsfuyg33', 'e').replace('vd98yvib2g', 'u').replace('s98yqi3ulbg', 'i')
        return value, name

    def _pull(self):
        with open(self.base_name, 'r') as f:
            return f.read()

    def _save(self, data):
        with open(self.base_name, 'x') as f:
            f.write(data)
        return

    def _check(self):
        if path.isfile(self.base_name):
            return
        else:
            with open(self.base_name, 'x'):
                return
