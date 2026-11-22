"""Independent numeric vertex-pair adjacency validation for dimensions 3 and 4.
Requires numpy and scipy (HiGHS linear programming). Run: python check_lp.py.
For each candidate pair, asks whether its midpoint is a convex combination
of the other vertices. Failure of that feasibility is the edge condition.
"""
from itertools import product
import numpy as np
from scipy.optimize import linprog

def words(n):
    return [v+((-sum(v)) % 3,) for v in product(range(3), repeat=n-1)]

for n in (3,4):
    w=words(n)
    pts=np.zeros((len(w),3*n), dtype=np.float64)
    for k,a in enumerate(w):
        for i,v in enumerate(a):pts[k,3*i+v]=1.
    checked=0
    for i in range(len(w)):
        for j in range(i+1,len(w)):
            diff=[(b-a)%3 for a,b in zip(w[i],w[j])]
            nonzero=[v for v in diff if v]
            expected=(len(nonzero)==2 and sum(nonzero)%3==0) or (len(nonzero)==3 and len(set(nonzero))==1)
            others=[k for k in range(len(w)) if k not in (i,j)]
            A=np.vstack([pts[others].T,np.ones((1,len(others)))])
            b=np.r_[0.5*(pts[i]+pts[j]),1.]
            feasible=linprog(np.zeros(len(others)),A_eq=A,b_eq=b,bounds=(0,None),method='highs').success
            assert (not feasible)==expected, (n,i,j,feasible,expected)
            checked+=1
    print('LP_MIDPOINT_EXACT_MATCH',n,checked)
print('TERNARY_SPC_LP_ADJACENCY_PASS')
