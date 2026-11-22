"""Standalone finite checks for the expanding uniform-MA(1) spectral theorem.
Run: python check.py. Finite checks corroborate, not prove, infinite claims.
"""
from itertools import combinations
from fractions import Fraction
from math import factorial
import numpy as np
from scipy.optimize import brentq

checks = 0

def det_fraction(A):
    n = len(A)
    if not n: return Fraction(1)
    b = [[Fraction(x) for x in row] for row in A]
    sign = 1
    out = Fraction(1)
    for j in range(n):
        k = next((i for i in range(j,n) if b[i][j]),None)
        if k is None: return Fraction(0)
        if k != j:
            b[j],b[k] = b[k],b[j]
            sign = -sign
        p = b[j][j]; out *= p
        for i in range(j+1,n):
            v = b[i][j]/p
            for z in range(j+1,n): b[i][z] -= v*b[j][z]
            b[i][j]=0
    return out*sign

for q in (Fraction(1,2),Fraction(1,3),Fraction(2,3),Fraction(3,4)):
    for N in range(2,9):
        xs=[Fraction(2*i+1,2*N) for i in range(N)]
        for k in range(1, min(N,5)+1):
            for I in combinations(range(N),k):
                a=[[int(xs[j] < xs[i]/q) for j in I] for i in I]
                observed=det_fraction(a)
                expected=int(all(xs[I[j]] <= q*xs[I[j+1]] for j in range(k-1)))
                assert observed == expected,(q,N,I,a,observed,expected)
                checks+=1

# Exact Newton power sums for the limiting zero reciprocals, at rational q.
for q in (Fraction(1,2),Fraction(1,3),Fraction(2,3),Fraction(3,4)):
    coeff=[(-1)**k*q**(k*(k-1)//2)/factorial(k) for k in range(4)]
    # The formal product has elementary symmetric coefficients e_k.
    e1=-coeff[1];e2=coeff[2];e3=-coeff[3]
    p1=e1;p2=e1*p1-2*e2;p3=e1*p2-e2*p1+3*e3
    assert p1==1 and p2==1-q and p3==1-Fraction(3,2)*q+q**3/Fraction(2)
    checks+=3

def defexp(q,z):
    term=1.0
    out=1.0
    for n in range(1,300):
        term*=z*(q**(n-1))/n
        out+=term
        if abs(term)<1e-14: break
    return out

def positive_zeros(q, maxz):
    grid=np.linspace(0,maxz,20001)
    prev=defexp(q,0)
    roots=[]
    for i in range(1,len(grid)):
        v=defexp(q,-grid[i])
        if v*prev<0:
            roots.append(brentq(lambda z:defexp(q,-z),grid[i-1],grid[i],xtol=1e-12))
        prev=v
    return roots

for q,maxz in ((0.5,25),(0.25,55),(0.1,26)):
    roots=positive_zeros(q,maxz)
    assert len(roots)>=2, (q, roots)
    assert all(roots[i+1]>roots[i] for i in range(len(roots)-1))
    checks+=2
    for N in (50,100,150):
        x=(np.arange(N)+.5)/N
        A=(x[None,:]<x[:,None]/q)/N
        eig=np.linalg.eigvals(A)
        ev=sorted([e.real for e in eig if abs(e.imag)<1e-7 and e.real>1e-4],reverse=True)
        assert len(ev)>=2 and abs(ev[0]-1/roots[0])<.015 and abs(ev[1]-1/roots[1])<.015, (q,N,roots,ev[:3])
        checks+=1
    print(f'q={q}: roots={roots[:3]}, predicted modal ratio={roots[0]/roots[1]:.9f}')

print('PASS:',checks,'exact minor/Newton and numerical approximation checks')
