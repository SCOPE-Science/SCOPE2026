import sys
sys.path.insert(0, '.')
import numpy as np
from k3p_common import *

# Glove key: per leaf, sorted multiset of labels across factors, packed 8 bits/leaf.
def glove_keys(cols):
    L = G[cols]                       # M x d x 4
    S = np.sort(L, axis=1)            # sort along factor axis
    d = cols.shape[1]
    key = np.zeros(cols.shape[0], dtype=np.int64)
    for j in range(4):
        pack = np.zeros(cols.shape[0], dtype=np.int64)
        for t in range(d):
            pack = pack * 4 + S[:, t, j].astype(np.int64)
        key = key * 256 + pack
    return key


if __name__ == '__main__':
    mono2 = enum_monomials(2)
    k2 = glove_keys(mono2)
    u2, c2 = np.unique(k2, return_counts=True)
    print("quad: nblocks", len(u2), "sizes:", sorted(c2.tolist())[:20], "...",
          sorted(c2.tolist())[-10:], flush=True)
    mono3 = enum_monomials(3)
    k3 = glove_keys(mono3)
    u3, c3 = np.unique(k3, return_counts=True)
    print("cubic: nblocks", len(u3), "maxsize", int(c3.max()),
          "sizes>40:", int((c3 > 40).sum()), flush=True)
    mono4 = enum_monomials(4)
    k4 = glove_keys(mono4)
    u4, c4 = np.unique(k4, return_counts=True)
    print("quartic: nblocks", len(u4), "maxsize", int(c4.max()),
          "sizes>200:", int((c4 > 200).sum()), flush=True)
    np.save('glove4_keys.npy', k4)
    np.save('glove4_uniq.npy', u4)
