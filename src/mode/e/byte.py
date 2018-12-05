# https://math.stackexchange.com/questions/1817064/bbp-formula-for-e
import math

__all__ = ('get_byte',)


def series(idx):
    # 16^(id-k)/(8*k+m)
    __eps__ = 1e-17
    s = .0
    for k in range(idx):
        ak = (4 * k + 2) * math.factorial(2 * k)
        p = idx - k
        t = (4 ** p * (4 * k + 3)) % ak
        s = s + t / ak
        s = s - int(s)
    for k in range(idx, idx + 100):
        ak = (4 * k + 2) * math.factorial(2 * k)
        p = idx - k
        t = (4 ** p * (4 * k + 3)) / ak
        if t < __eps__:
            break
        s = s + t
        s = s - int(s)
    return s


def quarter_byte(idx):
    pid = series(idx)
    pid = pid - int(pid) + 1
    y = abs(pid)
    return 4. * (y - math.floor(y))


def get_byte(idx):
    assert idx >= 0, 'value error'
    idx_t = idx * 4
    q1 = int(quarter_byte(idx_t))
    q2 = int(quarter_byte(idx_t + 1))
    q3 = int(quarter_byte(idx_t + 2))
    q4 = int(quarter_byte(idx_t + 3))
    return q1 << 6 | q2 << 4 | q3 << 2 | q4


if __name__ == '__main__':
    # for i in range(100):
    #     print(get_byte(i), end='-')
    # print(get_byte(0))
    # print(get_byte(2))
    pass
