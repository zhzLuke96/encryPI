# https://math.stackexchange.com/questions/1817064/bbp-formula-for-e
import math

__all__ = ('get_byte',)


def series(idx):
    # 16^(id-k)/(8*k+m)
    __eps__ = 1e-17
    # 太小的过程就跳过，BBP不需要高精度小数
    s = .0
    # 小于index的part
    for k in range(idx):
        ak = (4 * k + 2) * math.factorial(2 * k)
        p = idx - k
        t = (4 ** p * (4 * k + 3)) % ak
        s = s + t / ak
        s = s - int(s)
    # idx到无穷的part
    for k in range(idx, idx + 100):
        ak = (4 * k + 2) * math.factorial(2 * k)
        p = idx - k
        t = (4 ** p * (4 * k + 3)) / ak
        if t < __eps__:
            break
        s = s + t
        s = s - int(s)
    return s


def half_byte(idx):
    pid = series(idx)
    pid = pid - int(pid) + 1
    y = abs(pid)
    return 4. * (y - math.floor(y))


def get_byte(idx):
    assert idx >= 0, 'value error'
    idx_t = idx * 4
    p1 = int(half_byte(idx_t))
    p2 = int(half_byte(idx_t + 1))
    p3 = int(half_byte(idx_t + 2))
    p4 = int(half_byte(idx_t + 3))
    return p1 << 6 | p2 << 4 | p3 << 2 | p4


if __name__ == '__main__':
    # for i in range(100):
    #     print(get_byte(i), end='-')
    # print(get_byte(0))
    # print(get_byte(2))
    pass
