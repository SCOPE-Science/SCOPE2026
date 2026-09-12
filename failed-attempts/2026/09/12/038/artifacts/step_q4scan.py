import sys, time
sys.path.insert(0, '.')
import numpy as np
from k3p_common import *

t0 = time.time()
mono4 = enum_monomials(4)
k4 = np.load('glove4_keys.npy')
u4 = np.load('glove4_uniq.npy')
Q = sample_Q(300, 4242)
Qt = sample_Q(120, 9137)   # holdout
print("loaded", mono4.shape, len(u4), flush=True)

QUIRK_THRESHOLD = 0   # record every nonzero kernel
surv = []
sddone = 0
for bi, key in enumerate(u4):
    cols = mono4[k4 == key]
    n = cols.shape[0]
    E = eval_block(Q, cols)
    B = jordan_null(E)
    if B.shape[0]:
        Et = eval_block(Qt, cols)
        if np.any((Et @ B.T) % P):
            print("HOLDOUT FAIL", hex(int(key)), flush=True)
            continue
        surv.append((int(key), cols, B))
    sddone += 1
    if sddone % 40000 == 0:
        print(f"...{sddone}/{len(u4)} surv={len(surv)} t={time.time()-t0:.0f}s",
              flush=True)

print("QUARTIC_SURV_BLOCKS", len(surv), "t=", round(time.time() - t0, 1), flush=True)
tot = sum(B.shape[0] for _, _, B in surv)
print("QUARTIC_SURV_DIM", tot, flush=True)
import pickle
with open('quartic_surv.pkl', 'wb') as f:
    pickle.dump([(k, c, B) for k, c, B in surv], f)
for k, c, B in surv[:50]:
    print(hex(k), "N=", c.shape[0], "k=", B.shape[0], flush=True)
