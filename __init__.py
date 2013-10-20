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


if __name__ == '__main__':
    import sys
    code = open(sys.argv[1]).read()

    if len(sys.argv) >= 3:
        _map = maps[sys.argv[2]]
    else:
        _map = {}

    z_interpreter = ZokisInterpreter(code, _map=_map)
    z_interpreter.run()
