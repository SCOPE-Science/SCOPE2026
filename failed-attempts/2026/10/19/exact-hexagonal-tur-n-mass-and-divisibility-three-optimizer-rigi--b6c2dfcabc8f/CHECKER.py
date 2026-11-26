#!/usr/bin/env python3
"""Independent finite tests and symbolic contact-matrix identities for a seven-site Turan problem.

Dependencies: Python >=3.10, sympy, numpy, scipy. Run: python CHECKER.py.
The infinite family is proved in RESULT.md; testing does not replace the proof.
"""
import math
import cmath
import sympy as sp
import numpy as np
from scipy.optimize import linprog

def rho(n):
    return (n + 1) // 3

def S(n, k, l):
    u=2*math.pi*k/n
    v=2*math.pi*l/n
    return math.cos(u)+math.cos(v)+math.cos(u-v)

def formula(n):
    r=rho(n)
    return 2*math.cos(2*math.pi*r/n)+math.cos(4*math.pi*r/n)

for n in range(3,101):
    target=formula(n)
    m=min(S(n,k,l) for k in range(n) for l in range(n))
    assert abs(m-target)<4e-12,(n,m,target)

for n in range(3,26):
    rows=[]
    for k in range(n):
        for l in range(n):
            u=2*math.pi*k/n;v=2*math.pi*l/n
            rows.append([2*math.cos(u),-2*math.sin(u),
                2*math.cos(v),-2*math.sin(v),
                2*math.cos(u-v),-2*math.sin(u-v)])
    E=np.asarray(rows)
    lp=linprog(c=[-2,0,-2,0,-2,0],A_ub=-E,b_ub=np.ones(n*n),
        bounds=[(None,None)]*6,method='highs')
    assert lp.success,(n,lp.message)
    T=1-3/formula(n)
    assert abs((1-lp.fun)-T)<2e-8,(n,1-lp.fun,T)
    if n%3:
        # Six balanced contacts imply uniqueness among all six real coefficients.
        r=rho(n); k,l=r,2*r
        C=[]
        for j in range(6):
            u=2*math.pi*k/n;v=2*math.pi*l/n
            C.append([math.cos(u),-math.sin(u),
                math.cos(v),-math.sin(v),
                math.cos(u-v),-math.sin(u-v)])
            k,l=l%n,(l-k)%n
        assert len({tuple(int(x) for x in z) for z in np.round(np.array(C)*1e10).astype(int)})==6
        assert np.linalg.matrix_rank(np.array(C),tol=1e-8)==6,n
    else:
        r=n//3;k,l=r,2*r
        C=[]
        for j in range(2):
            u=2*math.pi*k/n;v=2*math.pi*l/n
            C.append([math.cos(u),-math.sin(u),
                math.cos(v),-math.sin(v),
                math.cos(u-v),-math.sin(u-v)])
            k,l=l%n,(l-k)%n
        assert np.linalg.matrix_rank(np.array(C),tol=1e-8)==2,n

# An independent exact symbolic proof of the orbit evaluation determinant factors.
t=sp.symbols('t')
w=(1+sp.sqrt(-3))/2
vec=[t,1/t,1/t**2,1/t,t,t**2]
p1=t*t+t+1
expected=[t**4+2*t**3+2*t+1,
    (1-sp.sqrt(-3))/2*(t-1)*(t+1)*p1,
    -(1+sp.sqrt(-3))/2*(t-1)**2*p1,
    -(t-1)**3*(t+1),
    (-1+sp.sqrt(-3))/2*(t-1)**2*p1,
    (1+sp.sqrt(-3))/2*(t-1)*(t+1)*p1]
for h in range(6):
    raw=sp.expand(t*t*sum(vec[j]*w**((h*j)%6) for j in range(6)),extension=sp.sqrt(-3))
    assert sp.simplify(raw-expected[h])==0,(h,sp.factor(raw-expected[h]))

for n in (3,4,5,6,7,8,9,10,11,12,13,16,31,64,97):
    print(f'n={n:3d}, minS={formula(n):.12f}, Turan_mass={1-3/formula(n):.12f}')
print('PASS: exhaustive grid minima n=3..100; unrestricted-coefficient LP n=3..25;')
print('contact ranks n=3..25; all six exact complex circulant eigenvalue factors.')
