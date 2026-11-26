#!/usr/bin/env python3
"""Independent integer-flow lower-bound check for q=2,3,4.
Requires SciPy with scipy.optimize.milp. The relaxation below is a necessary
condition for a cyclic cover, so its optimum certifies a valid lower bound.
"""
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from itertools import product

def check(q):
    states=list(product(range(q),repeat=2))
    triples=list(product(range(q),repeat=3))
    pairs=list(sorted({tuple(sorted(v)) for v in states}))
    si={v:i for i,v in enumerate(states)}
    pi={v:i for i,v in enumerate(pairs)}
    A=np.zeros((len(states)+len(pairs),len(triples)),dtype=float)
    for j,(a,b,c) in enumerate(triples):
        A[si[(a,b)],j]+=1
        A[si[(b,c)],j]-=1
        u=tuple(sorted((a,b))); v=tuple(sorted((b,c)))
        if u!=v:A[len(states)+pi[u],j]+=1
    lo=np.zeros(len(states)+len(pairs)); hi=np.zeros_like(lo)
    lo[len(states):]=1; hi[len(states):]=np.inf
    lower=np.array([1 if a==c else 0 for a,b,c in triples],dtype=float)
    ans=milp(np.ones(len(triples)), integrality=np.ones(len(triples)),
         bounds=Bounds(lower,np.full(len(triples),np.inf)),
         constraints=LinearConstraint(A,lo,hi), options={'time_limit':30.0})
    assert ans.success,ans.message
    opt=round(ans.fun)
    predicted=(3*q*q+q+(q if q%2==0 else 0))//2
    assert opt==predicted,(q,opt,predicted)
    return opt

if __name__=='__main__':
    for q in [2,3,4]:print('q=%d, integer-flow optimum=%d'%(q,check(q)))
