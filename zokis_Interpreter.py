# coding: utf-8
from zokis_VM import ZokisVM


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
        if isinstance(code, basestring):
            self.__code = code.splitlines()
        elif hasattr(code, 'next'):
            self.__code = list(code)
        else:
            try:
                code[0]
            except IndexError:
                raise IndexError("Code must contain one or more lines")
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


class ZokisInterpreter(object):

    def __init__(self, code, _map={}, vm=ZokisVM, debug=False):
        self.__code = code
        self.map = _map
        self.vm = vm
        self.debug = debug

    def run(self):
        z_iter = iter(ZokisCode(self.__code))
        vm = self.vm(z_iter)
        while True:
            if self.debug:
                print vm._ZokisVM__stack
            try:
                linha = z_iter.next()
                if '#' in linha:
                    code, comment = linha.split('#', 1)
                    code = code.strip()
                else:
                    code = linha.strip()
            except StopIteration:
                break
            if code.isdigit():
                vm.PUSH(float(code))
            elif code:
                code = self.map.get(code, code)
                getattr(vm, code, vm.NOOP)()
