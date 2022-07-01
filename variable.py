from string import ascii_lowercase as chars
from string import digits
from random import choice

class Variable:
    _length = 1
    _used = []

    def __new__(cls):
        while len([_var for _var in cls._used if len(_var) == cls._length]) == 26 * (36 ** (cls._length - 1)):
            cls._length += 1

        while True:
            _var_name = choice(chars)
            if cls._length > 1:
                for _ in range(cls._length - 1):
                    _var_name += choice(chars + digits)
            if _var_name not in cls._used:
                cls._used.append(_var_name)
                return _var_name
        

if __name__ == '__main__':
    step = 0
    try:
        while True:
            step += 1
            print(f'{step:>6}: {Variable()}')
    except KeyboardInterrupt:
        print(f'length of used: {len(Variable._used)}')
