"""Finite integer-programming check: all maximizing sets in Q4, for t=2,3.
Requires numpy and scipy (scipy.optimize.milp with HiGHS). The analytical proof
is independent of these finite checks.
"""
from itertools import permutations, combinations
import math
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csr_matrix, vstack

D=4
edges=[(u,u^(1<<i),i) for u in range(1<<D) for i in range(D) if u<(u^(1<<i))]
lookup={(u,v):j for j,(u,v,_) in enumerate(edges)}
rows=set()
for start in range(1<<D):
    for order in permutations(range(D)):
        u=start;path=[]
        for i in order:
            v=u^(1<<i);path.append(lookup[min(u,v),max(u,v)]);u=v
        rows.add(tuple(sorted(path)))
assert len(edges)==32
A=csr_matrix((np.ones(sum(map(len,rows))),
   ([j for j,path in enumerate(rows) for _ in path],
    [i for path in rows for i in path])),shape=(len(rows),len(edges)))
base_lb=np.zeros(A.shape[0]); base_ub=np.zeros(A.shape[0])

for t in (2,3):
    target=t*(1<<(D-1)); expected=set()
    for inds in combinations(range(D),t):
        expected.add(tuple(sorted(j for j,e in enumerate(edges) if e[2] in inds)))
    C=A.copy();lo=base_lb.copy();hi=base_ub.copy()+t
    seen=set()
    while True:
        sol=milp(c=-np.ones(len(edges)), integrality=np.ones(len(edges)),
                 bounds=Bounds(0,1),constraints=LinearConstraint(C,lo,hi),
                 options={'time_limit':60,'mip_rel_gap':0.0})
        assert sol.status==0,sol.message
        size=int(round(-sol.fun))
        if size<target:break
        assert size==target
        inds=tuple(np.flatnonzero(sol.x>0.5))
        assert inds not in seen
        seen.add(inds)
        # Exclude precisely this binary subset: the next maximizing binary
        # assignment must omit at least one of its selected edges.
        cut=csr_matrix((np.ones(len(inds)),([0]*len(inds),inds)),
                       shape=(1,len(edges)))
        C=vstack([C,cut],format='csr')
        lo=np.append(lo,0.0);hi=np.append(hi,len(inds)-1.0)
    assert seen==expected,(t,len(seen),len(expected))
    print(f'Q4 t={t} optimum_size={target} all_optima={len(seen)} next_best={size}: PASS')
