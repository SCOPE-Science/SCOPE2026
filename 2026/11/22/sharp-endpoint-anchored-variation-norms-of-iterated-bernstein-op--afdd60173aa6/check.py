"""Reproducible arithmetic checks for anchored Bernstein variation norm.
Run: python3 check.py (requires Python stdlib and numpy for numerical stress tests).
Finite checks supplement, never replace, the universal proof.
"""
from fractions import Fraction as F
from math import comb
import random


def matrix(n):
    P=[]
    for i in range(n+1):
        x=F(i,n)
        P.append([F(comb(n,j))*x**j*(1-x)**(n-j) for j in range(n+1)])
    return P

def mul(M,v):
    return [sum((a*b for a,b in zip(row,v)),F(0)) for row in M]

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))

def survival(n,r):
    P=matrix(n)
    v=[F(0)]+[F(1)]*(n-1)+[F(0)]
    for _ in range(r-1):
        v=mul(P,v)
    b=[F(comb(n,j),2**n) for j in range(n+1)]
    return dot(b,v)

def bernstein_derivative_var(n,values):
    # Bernstein derivative expansion in power basis; variation by sampling roots.
    import numpy as np
    diff=[float(n*(values[j+1]-values[j])) for j in range(n)]
    coeff=[]
    for k in range(n):
        coeff.append(sum(diff[j]*comb(n-1,j)*comb(n-1-j,k-j)*(-1)**(k-j) for j in range(k+1)))
    roots=np.polynomial.polynomial.polyroots(coeff)
    roots=sorted([float(z.real) for z in roots if abs(z.imag)<1e-7 and 1e-9<float(z.real)<1-1e-9])
    x=[0.0]+roots+[1.0]
    def val(t):
        return sum(float(values[j])*comb(n,j)*t**j*(1-t)**(n-j) for j in range(n+1))
    return sum(abs(val(x[k+1])-val(x[k])) for k in range(len(x)-1))

for n in range(2,9):
    P=matrix(n)
    for i,row in enumerate(P):
        assert sum(row)==1
        assert (row[0]==1 if i==0 else True)
    c=[survival(n,r) for r in range(1,6)]
    assert c[0]==1-F(1,2**(n-1))
    lam=F(n-1,n)
    assert all(lam**r<=c[r-1]<=F(n*n,4*(n-1))*lam**r for r in range(1,6))
    assert all(c[r]>c[r+1] for r in range(4))
    for r in range(1,4):
        for s in range(1,4):
            if r+s>5: continue
            if n==2:assert c[r+s-1]==c[r-1]*c[s-1]
            else:assert c[r+s-1]<c[r-1]*c[s-1]
    print('EXACT_SURVIVAL_AND_RATE_PASS',n,[float(v) for v in c])
print('EXACT_BOUND_AND_SUBMULTIPLICATIVITY_PASS')

rng=random.Random(20261117)
tests=0
for n in range(2,9):
    P=matrix(n)
    for r in range(1,4):
        bound=float(survival(n,r))
        for _ in range(80):
            nodal=[0]+[rng.randint(-9,9) for _ in range(n-1)]+[0]
            v=list(map(F,nodal))
            var_in=sum(abs(nodal[j+1]-nodal[j]) for j in range(n))
            if var_in==0:continue
            for __ in range(r-1):v=mul(P,v)
            var_out=bernstein_derivative_var(n,v)
            assert var_out<=bound*var_in+2e-6, (n,r,nodal,var_out,bound*var_in)
            tests+=1
print('RANDOM_BV_INEQUALITIES_PASS',tests)
print('ALL_ANCHORED_BERNSTEIN_CHECKS_PASS')
