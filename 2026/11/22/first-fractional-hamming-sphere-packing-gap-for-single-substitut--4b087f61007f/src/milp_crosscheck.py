#!/usr/bin/env python3
"""Separate exact-size MILP cross-check (requires numpy and scipy/HiGHS).

The standalone exhaustive C++ search, not the numerical MILP, is the finite
upper-bound argument; this check uses an separately generated conflict graph.
"""
from itertools import combinations
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix

def generate(n):
    masks=[]
    for positions in combinations(range(2*n),n):
        s=set(positions)
        partial=0
        for i in range(2*n):
            partial+=1 if i in s else -1
            if partial<0:break
        else:
            masks.append(sum(1<<i for i in positions))
    return masks

for n,expected in enumerate([1,1,2,4,10,22],1):
    source=generate(n)
    conflicts=[(i,j) for i in range(len(source)) for j in range(i) if (source[i]^source[j]).bit_count()==2]
    A=lil_matrix((len(conflicts),len(source)))
    for k,(i,j) in enumerate(conflicts): A[k,i]=1;A[k,j]=1
    r=milp(-np.ones(len(source)),integrality=np.ones(len(source)),bounds=Bounds(0,1),constraints=LinearConstraint(A.tocsr(),0,1),options={'mip_rel_gap':0.0,'time_limit':90.0})
    assert r.status==0 and abs(r.fun+expected)<1e-6 and r.mip_gap==0
    print(f'MILP_OK n={n} maximum={expected} conflicts={len(conflicts)}')
print('MILP_ALL_OK')
