import sys, time
sys.path.insert(0, '.')
import numpy as np, itertools
from k3p_common import *

t0 = time.time()
mono4 = enum_monomials(4)
print("n_quartic_monomials", mono4.shape[0], flush=True)
g4 = grades_of(mono4)
uniq, counts = np.unique(g4, return_counts=True)
print("nblocks", len(uniq), flush=True)
ord_ = np.argsort(counts)
for i in ord_:
    print(f"block {int(uniq[i]):x} N={int(counts[i])}", flush=True)
np.save('q4_grades.npy', g4)
