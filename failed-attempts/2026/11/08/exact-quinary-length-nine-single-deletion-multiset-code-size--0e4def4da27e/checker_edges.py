"""Independent pairwise-graph MILP verification of S_5(9,1)=143.

Requires Python 3, numpy 2.x and scipy 1.17.x (HiGHS mixed-integer solver).
This is an independent direct incompatibility encoding, not the 495-clique
encoding used by checker.py. All 4,950 incompatible pairs are generated.
"""
import itertools
from math import comb
import numpy as np
from scipy.sparse import coo_array
from scipy.optimize import milp, Bounds, LinearConstraint

def compositions(n,q):
    if q==1:
        yield (n,)
    else:
        for k in range(n+1):
            for tail in compositions(n-k,q-1):
                yield (k,)+tail

n,q=9,5
xs=list(compositions(n,q)); pos={x:i for i,x in enumerate(xs)}
assert len(xs)==comb(13,4)==715
pairs=[]
for i,x in enumerate(xs):
    for a in range(q):
        if x[a]==0: continue
        for b in range(q):
            if b==a: continue
            y=list(x);y[a]-=1;y[b]+=1
            j=pos[tuple(y)]
            if i<j:pairs.append((i,j))
assert len(pairs)==4950 and len(set(pairs))==4950
rr=[];cc=[]
for k,(i,j) in enumerate(pairs):rr.extend([k,k]);cc.extend([i,j])
A=coo_array((np.ones(len(rr),dtype=np.float64),
             (np.array(rr,dtype=np.int32),np.array(cc,dtype=np.int32))),
            shape=(len(pairs),len(xs))).tocsr()
assert A.shape==(4950,715)
res=milp(-np.ones(715),integrality=np.ones(715,dtype=np.int32),
         bounds=Bounds(0,1),
         constraints=LinearConstraint(A,lb=0,ub=1),
         options={'mip_rel_gap':0.0,'time_limit':180})
assert res.status==0,('No global certificate',res.message)
assert res.x is not None and res.mip_dual_bound is not None
z=np.rint(res.x).astype(int)
assert np.max(np.asarray(A@z))<=1 and z.sum()==143
assert -143.000001<res.mip_dual_bound< -142.999999
print('INDEPENDENT_EDGE_VERIFY_OK: 715 vertices, 4950 pairs, maximum 143, dual bound',
      res.mip_dual_bound,'gap',res.mip_gap,flush=True)
