# coding: utf-8
version = '0.1'

import sys


class ZokisVM(object):

    def __init__(self, code):
        self.__code = code
        self.__stack = []

    def get_top_next(self):
        if len(self.__stack) < 2:
            raise IndexError("there is one or less elements in the stack to be returned, two elements are required")
        else:
            return self.__stack.pop(), self.__stack.pop()

    def get_top(self):
        if not self.__stack:
            raise IndexError("there is no element in the stack to be returned")
        else:
            return self.__stack.pop()

    def JUMP_IF_FALSE(self):
        """
        jumps to the specified
        line on 'top'
        if 'next' is false
        """
        top, next = self.get_top_next()
        if not next:
            self.__code.send(top-1)

    def JUMP(self):
        top = self.get_top()
        self.__code.send(top-1)

    def END(self):
        self.__code.send(self.__code.ultima_linha)

    def PUSH(self, n):
        self.__stack.append(n)

    def NOOP(self):
        return None

    def POP(self):
        if not self.__stack:
            raise IndexError("there is no element in the stack to be removed")
        else:
            self.__stack.pop()

    def LEN(self):
        self.__stack.append(len(self.__stack))

    def ADD(self):
        top, next = self.get_top_next()
        self.__stack.append(next + top)

    def SUB(self):
        top, next = self.get_top_next()
        self.__stack.append(next - top)

    def MULT(self):
        top, next = self.get_top_next()
        self.__stack.append(next * top)

    def DIV(self):
        top, next = self.get_top_next()
        self.__stack.append(next // top)

    def MOD(self):
        top, next = self.get_top_next()
        self.__stack.append(next % top)

    def NOT(self):
        top = self.get_top()
        self.__stack.append(int(not top))

    def GTR(self):
        top, next = self.get_top_next()
        self.__stack.append(int(next > top))

    def DUP(self):
        if not self.__stack:
            raise IndexError("there is no element in the stack to be duplicated")
        self.__stack.append(self.__stack[-1])

    def N_IN(self):
        n = int(raw_input("enter an integer: "))
        self.__stack.append(n)

    def C_IN(self):
        c = ord(raw_input("enter a character: "))
        self.__stack.append(c)

    def N_OUT(self):
        top = self.get_top()
        sys.stdout.write(str(top))

    def C_OUT(self):
        top = int(self.get_top())
        sys.stdout.write(chr(top))

    def SN_OUT(self):
        top = int(self.get_top())
        s = [chr(int(self.get_top())) for x in range(top)]
        sys.stdout.write((''.join(s))[::-1]+'\n')
