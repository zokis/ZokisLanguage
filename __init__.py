# coding: utf-8
from zokis_VM import ZokisVM
from zokis_Interpreter import ZokisInterpreter


if __name__ == '__main__':
    import sys
    code = open(sys.argv[1]).read()

    z_interpreter = ZokisInterpreter(code)
    z_interpreter.run()
