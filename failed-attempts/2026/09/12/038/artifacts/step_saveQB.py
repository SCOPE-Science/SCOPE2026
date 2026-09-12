import sys
sys.path.insert(0, '.')
import numpy as np
from k3p_common import *
from sympy import symbols, expand

# Recompute quadric basis compactly and save; load cubics; print keys/dims/terms
Q = sample_Q(300, 1001)
mono2 = enum_monomials(2); g2 = grades_of(mono2)
qb = {}
for key in np.unique(g2):
    cols = mono2[g2 == key]
    B = jordan_null(eval_block(Q, cols))
    if B.shape[0]:
        qb[int(key)] = (cols, B)
print("QUAD", {hex(k): v[1].shape[0] for k, v in qb.items()})
np.save('quad_keys.npy', np.array(list(qb.keys())))
for k, (c, B) in qb.items():
    np.save(f'quad_{k:x}.npy', c); np.save(f'quadB_{k:x}.npy', B)

ck = np.load('cubic_keys.npy')
print("CUBIC keys", [hex(int(k)) for k in ck])
for k in ck:
    B = np.load(f'cubicB_{int(k):x}.npy')
    print(hex(int(k)), "dim", B.shape[0], "density nnz/row:",
          [int((r != 0).sum()) for r in B])
