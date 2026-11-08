#!/usr/bin/env python3
"""Independent deletion-hypergraph integer-programming cross-check (requires SciPy)."""
from itertools import product
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, linprog, milp
from scipy.sparse import lil_matrix

n=16
W=[]
for wordtuple in product('01',repeat=n):
    word=''.join(wordtuple)
    parts=word.split('1')
    if all(len(part)>=2 for part in parts): W.append(word)
assert len(W)==129
D=[{w[:j]+w[j+1:] for j in range(n)} for w in W]
outputs=sorted(set().union(*D))
row={s:i for i,s in enumerate(outputs)}
A=lil_matrix((len(outputs),len(W)),dtype=float)
for j,shadow in enumerate(D):
    for s in shadow:A[row[s],j]=1
A=A.tocsr()
obj=-np.ones(len(W))
lo=np.zeros(len(outputs)); hi=np.ones(len(outputs))
res=milp(obj,integrality=np.ones(len(W)),bounds=Bounds(np.zeros(len(W)),np.ones(len(W))),constraints=LinearConstraint(A,lo,hi),options={'mip_rel_gap':0.0,'time_limit':45})
assert res.status==0 and abs(res.fun+14)<1e-6
assert abs(res.mip_dual_bound+14)<1e-6
lp=linprog(obj,A_ub=A,b_ub=hi,bounds=(0,1),method='highs')
assert lp.success and -lp.fun>17
print('INDEPENDENT_MODEL_OK n16_mip=14 n16_lp=',round(-lp.fun,9))
