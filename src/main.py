
from .cache import LRU

__all__ = ("encrypt", "decrypt")


@LRU(255)
def find(bt_idx, get_byte):
    assert isinstance(bt_idx, int), 'type error'
    idx = 0
    while True:
        tb = get_byte(idx)
        if tb == bt_idx:
            return idx
        idx += 1


def encrypt(bs, get_byte):
    assert isinstance(bs, bytes), 'type error'
    cipherls = []
    # bin ciphertext
    for tbin in bs:
        ct = find(tbin, get_byte)
        cipherls.append(ct)
    return dump(cipherls)


def decrypt(bts, get_byte):
    assert isinstance(bts, bytes), 'type error'
    idxs = dedump(bts)
    srctext = b''
    # bin src
    for tidx in idxs:
        src_b = get_byte(tidx)
        srctext += (src_b).to_bytes(1, 'big')
    return srctext


def dump(ls):
    ret = b''
    for i in ls:
        ret += (i).to_bytes(10, 'big')
    # clear b'\0'
    rret = b''
    last = None
    for i in ret:
        if last == 0 and i == 0:
            continue
        rret += (i).to_bytes(1, 'big')
        last = i
    if len(rret) != 0 and rret[0] == 0:
        rret = rret[1:]
    if len(rret) != 0 and rret[-1] == 0:
        rret = rret[:-1]
    return rret


def dedump(bts):
    if len(bts) == 0:
        return []
    ls = bts.split(b'\0')
    return [int.from_bytes(i, 'big') for i in ls]
