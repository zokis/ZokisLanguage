# coding: utf-8
from zokis_VM import ZokisVM
from zokis_Interpreter import ZokisInterpreter

maps = {
    'map1': {
        '<<': 'N_IN',
        '%': 'MOD',
        '->!': 'JUMP_IF_FALSE',
        '~>': 'END',
        '$>>': 'C_OUT',
    }
}


def main(argv):
    code = open(argv[0]).read()

    if 'debug' in argv:
        debug = True
        argv.remove('debug')
    else:
        debug = False

    if len(argv) >= 2:
        _map = maps[argv[1]]
    else:
        _map = {}
    z_interpreter = ZokisInterpreter(code, _map=_map, vm=ZokisVM, debug=debug)
    z_interpreter.run()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
