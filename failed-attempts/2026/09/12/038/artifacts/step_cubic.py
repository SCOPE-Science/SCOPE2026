import sys, time, itertools
sys.path.insert(0, '.')
import numpy as np
from k3p_common import *

t0 = time.time()
R = 300
Q = sample_Q(R, 1001)
Qt = sample_Q(120, 777001)   # fresh-seed holdout

# --- Quadrics (redo with shared tooling, verify) ---
mono2 = enum_monomials(2); g2 = grades_of(mono2)
uniq2 = np.unique(g2)
print("quad blocks:", len(uniq2), flush=True)
qbasis = {}
for key in uniq2:
    cols = mono2[g2 == key]
    E = eval_block(Q, cols)
    if E.shape[0] < E.shape[1] + 30:
        Qb = sample_Q(E.shape[1] + 30, int(key) + 5)
        E = eval_block(Qb, cols)
    B = jordan_null(E)
    if B.shape[0]:
        # cross-validate on holdout
        Et = eval_block(Qt, cols)
        res = (Et @ B.T) % P
        if np.any(res):
            print("QUAD HOLDOUT FAIL", hex(int(key)), flush=True)
        else:
            qbasis[int(key)] = (cols, B)
print("quad dim total:", sum(B.shape[0] for _, B in qbasis.values()), flush=True)

# --- Cubics ---
mono3 = enum_monomials(3); g3 = grades_of(mono3)
uniq3 = np.unique(g3)
print("cubic blocks:", len(uniq3), flush=True)
cb = {}
tot = 0
fails = 0
for i, key in enumerate(uniq3):
    cols = mono3[g3 == key]
    n = cols.shape[0]
    Qb = sample_Q(n + 30, 2000 + int(key)) if R < n + 30 else Q
    E = eval_block(Qb, cols)
    B = jordan_null(E)
    if B.shape[0]:
        Et = eval_block(Qt, cols)
        if np.any((Et @ B.T) % P):
            fails += 1
            print("CUBIC HOLDOUT FAIL block", hex(int(key)), "n=", n,
                  "k=", B.shape[0], flush=True)
        else:
            cb[int(key)] = (cols, B); tot += B.shape[0]
print("CUBIC_DIM_TOTAL", tot, "nblocks_nonzero", len(cb), "fails", fails,
      "time", round(time.time() - t0, 1), flush=True)
np.save('cubic_keys.npy', np.array(list(cb.keys())))
for k, (c, B) in cb.items():
    np.save(f'cubic_{k:x}.npy', np.vstack([c.T, B]) if False else c)
    np.save(f'cubicB_{k:x}.npy', B)
