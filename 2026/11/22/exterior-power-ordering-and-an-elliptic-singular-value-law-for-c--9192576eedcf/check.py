"""Standalone finite diagnostics for generalized Cesaro singular ordering.
Run with Python 3, NumPy and SciPy: python check.py.
All asymptotic and infinite-dimensional conclusions require the written proof.
"""
from itertools import combinations
from fractions import Fraction
from math import comb, factorial, pi
import numpy as np
from scipy.special import ellipk

def matrix(t, N):
    x=np.arange(N)[:,None]-np.arange(N)[None,:]
    return np.where(x>=0, float(t)**np.maximum(x,0)/(np.arange(N)[:,None]+1), 0.)

def determinant_int(M):
    # Exact fraction Gaussian elimination, small square matrices only.
    a=[[Fraction(x) for x in row] for row in M]
    n=len(a); ans=Fraction(1)
    for c in range(n):
        t=next((i for i in range(c,n) if a[i][c]),None)
        if t is None:return Fraction(0)
        if t!=c:
            a[t],a[c]=a[c],a[t];ans=-ans
        p=a[c][c];ans*=p
        for i in range(c+1,n):
            if a[i][c]:
                z=a[i][c]/p
                for j in range(c+1,n):a[i][j]-=z*a[c][j]
                a[i][c]=Fraction(0)
    return ans

# Every determinant of the lower triangular step matrix is 0 or 1.
checks=0
for k in range(1,4):
  ix=list(combinations(range(7),k))
  for I in ix:
    for J in ix:
      d=determinant_int([[int(i>=j) for j in J] for i in I])
      assert d in (0,1), (I,J,d)
      expected=int(all(J[h]<=I[h] and (h+1==k or I[h]<J[h+1]) for h in range(k)))
      assert d==expected,(I,J,d,expected)
      checks+=1

# Finite-section product ordering (the last product is fixed by the diagonal).
for N in (7, 12, 24, 48):
    previous=None
    for t in (0.,.14,.32,.59,.83):
        v=np.linalg.svd(matrix(t,N),compute_uv=False)
        cp=np.cumsum(np.log(v))
        if previous is not None:
            assert np.all(cp[:-1]>=previous[:-1]-2e-10)
            assert abs(cp[-1]-previous[-1])<2e-10
        previous=cp
        checks+=N

# The exact weak-trace constant is the complete elliptic integral.
for t in (0.,.15,.40,.70):
    chi=2*ellipk(4*t/(1+t)**2)/(pi*(1+t))
    approx=np.mean((1+t*t-2*t*np.cos(2*pi*np.arange(10000)/10000))**(-.5))
    assert abs(chi-approx)<5e-12
    if t>0:
        sv=np.linalg.svd(matrix(t,320),compute_uv=False)
        for rank in (15,30,50,70):
            assert abs(rank*sv[rank-1]-chi)<0.015,(t,rank,rank*sv[rank-1],chi)
            checks+=1
print('PASS:',checks,'finite exact and numerical checks; not an infinite-dimensional proof')
