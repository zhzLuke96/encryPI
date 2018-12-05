from collections import deque
__all__ = ('LRU',)


class LRU:
    __slots__ = ['size', 'cache', 'access']

    def __init__(self, maxsize=64):
        self.size = maxsize
        self.cache = dict()
        self.access = deque()

    @property
    def isFull(self):
        return len(self.cache) >= self.size

    def __put__(self, key, val):
        self.access.append(key)
        self.cache[key] = val
        if self.isFull:
            self.__popleft__()

    def __popleft__(self):
        k = self.access.popleft()
        del self.cache[k]

    def __index__(self, key):
        try:
            return self.access.index(key)
        except ValueError:
            return -1

    def __call__(self, fn):
        def warpper(*args):
            # just args[0]
            key = args[0]
            idx = self.__index__(key)
            if idx == -1:
                ret = fn(*args)
                self.__put__(key, ret)
            else:
                ret = self.cache[key]
            return ret
        return warpper
