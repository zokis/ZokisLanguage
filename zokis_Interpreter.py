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


class ZokisCode(object):

    def __init__(self, code):
        self.__code = code

    def __len__(self):
        return len(self.__code)

    def __iter__(self):
        return ZokisIterable(self)

    def __getitem__(self, linha):
        if linha <= len(self) - 1:
            self.linha_atual = int(linha + 1)
            return self.__code[self.linha_atual - 1]
        else:
            raise IndexError()
