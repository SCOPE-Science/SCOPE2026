"""Independent optimization/check of the finite identifying-code minima.
Uses a set-cover mixed-integer formulation for closed-neighborhood domination
and pairwise separation; this is a crosscheck, not the exhaustive certificate.
"""
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
import numpy as np
for q in range(3,7):
    verts=[(a,b) for a in range(q) for b in range(q) if a!=b]
    n=len(verts)
    closed=[]
    for a,b in verts:
        closed.append({j for j,(c,d) in enumerate(verts) if (a,b)==(c,d) or (b==c) or (d==a)})
    demands=closed+[closed[i]^closed[j] for i in range(n) for j in range(i)]
    A=lil_matrix((len(demands),n),dtype=float)
    for i,S in enumerate(demands): A[i,list(S)]=1
    res=milp(np.ones(n),integrality=np.ones(n),bounds=Bounds(0,1),
        constraints=LinearConstraint(A.tocsr(),np.ones(len(demands)),np.inf),
        options={'time_limit':30,'mip_rel_gap':0})
    assert res.status==0, (q,res.message)
    assert round(res.fun)=={3:4,4:4,5:5,6:7}[q], (q,res.fun)
    assert all(sum(round(res.x[j]) for j in S)>0 for S in demands)
    print(q,round(res.fun),'crosschecked')
