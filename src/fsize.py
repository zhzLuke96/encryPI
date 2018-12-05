import os
from copy import deepcopy
__all__ = ('file_size',)

__size_dict__ = ['Bytes', 'KB', 'MB', 'GB', 'TB']


def unit_pop(n):
    sd = deepcopy(__size_dict__)
    unit = sd.pop(0)
    while len(sd) != 0:
        if n >= 1024:
            n = round(n / 1024, 2)
            unit = sd.pop(0)
            print(n, unit)
        else:
            break
    return n, unit


def file_size(file_name):
    ts = os.path.getsize(file_name)
    n, unit = unit_pop(ts)
    return f'{n} {unit}'


if __name__ == '__main__':
    # print(unit_pop(1024))
    # print(unit_pop(102))
    # print(unit_pop(102400))
    # print(unit_pop(10240))
    # print(unit_pop(10240000))
    # print(unit_pop(10240000000))
    pass
