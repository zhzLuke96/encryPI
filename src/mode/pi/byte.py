# https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula
import math

__all__ = ('get_byte',)


def series(m, idx):
    # 16^(id-k)/(8*k+m)
    __eps__ = 1e-17
    # 太小的过程就跳过，BBP不需要高精度小数
    s = .0
    # 小于index的part
    for k in range(idx):
        ak = 8 * k + m
        p = idx - k
        t = (16 ** p) % ak
        s = s + t / ak
        s = s - int(s)
    # idx到无穷的part
    for k in range(idx, idx + 100):
        ak = 8 * k + m
        p = idx - k
        t = (16 ** p) / ak
        if t < __eps__:
            break
        s = s + t
        s = s - int(s)
    return s


def get_byte(idx):
    assert idx >= 0, 'value error'
    s1 = series(1, idx)
    s2 = series(4, idx)
    s3 = series(5, idx)
    s4 = series(6, idx)
    pid = 4 * s1 - 2 * s2 - s3 - s4
    pid = pid - int(pid) + 1

    y = abs(pid)
    y = 16. * (y - math.floor(y))
    first = int(y)
    y = 16. * (y - math.floor(y))
    second = int(y)
    return first << 4 | second
