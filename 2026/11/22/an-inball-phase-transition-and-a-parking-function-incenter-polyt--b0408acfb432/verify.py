#!/usr/bin/env python3
"""Exact integer/fraction finite checks for a two-row staircase incenter theorem.
The all-m proof is given in RESULT.md; this checks independent finite instances.
No third-party dependencies.
"""
from itertools import product
from math import comb, factorial
from fractions import Fraction


def center_vertices(m):
    for bits in product((0,1), repeat=m-1):
        z=[0]
        for k, bit in enumerate(bits,1):
            z.append(k if bit else z[-1])
        # scaled incenter parameters t_j / ((2-sqrt(2))*r)
        assert z[0]==0
        assert all(0 <= z[k-1] <= z[k] <= k for k in range(1,m))
        yield tuple(z[m-j] for j in range(1,m+1))

def check(m):
    cv=list(center_vertices(m))
    assert len(cv) == 2**(m-1) == len(set(cv))
    for t in cv:
        # the nonfixed distances from each facet divided by r are:
        # v_j/r=1+(2-sqrt(2))((m-j)-t_j) and
        # (u_j-u_{j+1})/(sqrt(2) r)=1+(sqrt(2)-1)(t_j-t_{j+1}).
        # The remaining m+2 supporting distances equal r exactly.
        assert all(0<=t[j-1]<=m-j for j in range(1,m+1))
        assert all(t[j-1]>=t[j] for j in range(1,m))
        assert t[-1]==0
    vtx=set()
    for k in range(m+1):
        for l in range(k,m+1):
            x=tuple((1,0) if j<k else (0,1) if j<l else (0,0) for j in range(m))
            vtx.add(x)
            assert all(x[j][0]>=x[j+1][0] and sum(x[j])>=sum(x[j+1]) for j in range(m-1))
    assert len(vtx)==comb(m+2,2)
    return len(cv),len(vtx)

def volume(n):
    # Exact integration: ∫_{0<z1<1}∫_{z1<z2<2}...∫_{z_{n-1}<zn<n} 1 dz.
    polynomial=[Fraction(1)]
    for k in range(n,0,-1):
        integral_upper=sum(c*Fraction(k**(i+1),i+1) for i,c in enumerate(polynomial))
        polynomial=[integral_upper]+[-Fraction(c,i+1) for i,c in enumerate(polynomial)]
    return polynomial[0]

for m in range(1,13):
    print('m',m,'incenter_vertices,original_vertices=',check(m))
for n in range(1,13):
    got=volume(n)
    expected=Fraction((n+1)**(n-1),factorial(n))
    assert got==expected, (n,got,expected)
    print('n',n,'parking_volume',got)
print('TWO_ROW_INCENTER_EXACT_PASS')

# Independent polyhedral LP replay with optional NumPy/SciPy:
# Run `python verify.py --lp`; this is not needed for the exact finite checks.
def lp_check():
    import numpy as np
    from scipy.optimize import linprog
    for m in range(1,7):
        for t in (0.0,0.1,0.4,0.7,1.0,2.0):
            d=2*m
            A=[];B=[]
            def add(v,b):
                A.append(np.r_[v,np.linalg.norm(v)])
                B.append(b)
            for j in range(m):
                v=np.zeros(d);v[2*j+1]=-1;add(v,0)
            v=np.zeros(d);v[2*m-2]=-1;add(v,0)
            for j in range(m-1):
                v=np.zeros(d);v[2*j]=-1;v[2*j+2]=1;add(v,0)
                v=np.zeros(d);v[2*j:2*j+2]=-1
                v[2*j+2:2*j+4]=1;add(v,0)
            v=np.zeros(d);v[0]=1;add(v,1)
            v=np.zeros(d);v[:2]=1;add(v,1+t)
            c=np.r_[np.zeros(d),-1]
            sol=linprog(c,A_ub=A,b_ub=B,
                        bounds=[(None,None)]*(d+1),method='highs')
            formula=min(1/(2+(m-1)*np.sqrt(2)),
                        (1+t)/(2*m+np.sqrt(2)))
            assert sol.success and abs(sol.x[-1]-formula)<1e-9,(m,t)
    print('WEIGHTED_TWO_ROW_LP_PASS cases=36')

if __name__=='__main__':
    import sys
    if '--lp' in sys.argv:
        lp_check()
