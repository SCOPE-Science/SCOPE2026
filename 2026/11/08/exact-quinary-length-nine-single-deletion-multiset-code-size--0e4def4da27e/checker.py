"""Reproduce the exact one-deletion multiset code optimization for q=5,n=9.

Requires Python 3, numpy 2.x, scipy 1.17 or compatible HiGHS MILP.
No input data, remote access, or external certificates are needed.
The full search is performed by an MILP branch-and-bound solver; status=0
and a matching global dual bound are essential (not merely a feasible code).
"""
from itertools import combinations
from math import comb
import numpy as np
from scipy.sparse import coo_array
from scipy.optimize import Bounds, LinearConstraint, milp

N, Q = 9, 5

def compositions(n, q):
    if q == 1:
        yield (n,)
    else:
        for k in range(n + 1):
            for tail in compositions(n - k, q - 1):
                yield (k,) + tail

vertices = list(compositions(N, Q))
parents = list(compositions(N-1, Q))
assert len(vertices) == comb(N+Q-1, Q-1) == 715
assert len(parents) == comb(N+Q-2, Q-1) == 495
index = {x: i for i, x in enumerate(vertices)}
assert len(index) == 715
rows, cols = [], []
for r, y in enumerate(parents):
    children = set()
    for symbol in range(Q):
        z = list(y)
        z[symbol] += 1
        j = index[tuple(z)]
        children.add(j)
        rows.append(r)
        cols.append(j)
    assert len(children) == Q

# A code has no pair of codewords with a common one-deletion output
# exactly when each row of A contains at most one selected column.
A = coo_array((np.ones(len(rows), dtype=np.float64),
               (np.array(rows,dtype=np.int32),np.array(cols,dtype=np.int32))),
              shape=(len(parents),len(vertices))).tocsr()
assert A.shape == (495,715) and A.nnz == 2475
assert np.all(np.diff(A.indptr) == 5)

# Fully explicit optimal construction: one weighted-symbol syndrome class.
code = [i for i,x in enumerate(vertices)
        if sum(j*x[j] for j in range(Q)) % Q == 0]
syndrome_counts = [sum(sum(j*x[j] for j in range(Q)) % Q == s for x in vertices)
                   for s in range(Q)]
assert syndrome_counts == [143]*Q and len(code)==143
assert np.max(np.asarray(A[:,code].sum(axis=1))) <= 1
# Independently compare all codeword pairs using direct multiset distance.
for i,j in combinations(code,2):
    a,b=vertices[i],vertices[j]
    assert sum(abs(a[k]-b[k]) for k in range(Q)) >= 4
print('LOWER: explicit 143-word code, all 10,153 pairs checked',flush=True)

# This is the entire finite integer optimization, rather than a sample.
# It is exactly equivalent to the mathematical code problem.
res=milp(c=-np.ones(len(vertices)),
         integrality=np.ones(len(vertices),dtype=np.int32),
         bounds=Bounds(0.0,1.0),
         constraints=LinearConstraint(A,lb=np.zeros(len(parents)),
                                          ub=np.ones(len(parents))),
         options={'mip_rel_gap':0.0,'time_limit':180})
assert res.status == 0, ('global optimization not certified',res.message)
assert res.x is not None and res.mip_dual_bound is not None
# All objectives are integers, so a verified lower bound > -144 excludes 144.
assert res.mip_dual_bound > -143.000001, res.mip_dual_bound
assert res.fun > -143.000001 and res.fun < -142.999999, res.fun
u=np.rint(res.x).astype(int)
assert set(u).issubset({0,1}) and u.sum()==143
assert np.max(np.asarray(A@u))<=1.0
print('UPPER: integer branch-and-bound optimal status',res.status,
      'optimal objective',int(u.sum()),'dual bound',res.mip_dual_bound,
      'gap',res.mip_gap,flush=True)
print('VERIFY_OK S_5(9,1)=143',flush=True)
