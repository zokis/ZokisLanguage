class ZokisIterable(object):

    def __init__(self, code):
        self.__code = code
        self.linha_atual = 0
        self.ultima_linha = len(self.__code) - 1

    def next(self):
        if self.linha_atual <= self.ultima_linha:
            self.linha_atual += 1
            return self.__code[self.linha_atual - 1]
        else:
            raise StopIteration()

    def send(self, linha):
        self.linha_atual = linha
