#!/usr/bin/env python3
"""Exact combinatorial checks and independent linear-program checks for path matchable-subgraph inballs.
Requires Python stdlib; SciPy is optional for linear-program corroboration.
"""
from fractions import Fraction
from math import sqrt, isclose
from itertools import product

def inv(n):
    m=n-1
    return [[Fraction((-1)**(i+j)*min(i+1,j+1)*(n-max(i+1,j+1)),n) for j in range(m)] for i in range(m)]

def gram(n):
    m=n-1
    return [[2 if i==j else 1 if abs(i-j)==1 else 0 for j in range(m)] for i in range(m)]

def multiply(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

def radius(n):
    w=[sqrt(Fraction(i*(n-i),n)) for i in range(1,n)]
    u=sqrt(Fraction(n-1,n))
    sums=[w[i]+w[i+1]+u for i in range(n-2)]
    r=1/max(sums)
    return r,w,u,sums

def is_perfect_matchable_subset(bits):
    # Components of the subgraph induced by chosen path vertices must all have even length.
    run=0
    for x in list(bits)+[0]:
        if x: run+=1
        elif run:
            if run%2: return False
            run=0
    return True

def matching_profiles(n):
    m=n-1
    for x in product((0,1),repeat=m):
        if any(x[i] and x[i+1] for i in range(m-1)): continue
        v=tuple((x[i-1] if i else 0)+(x[i] if i<m else 0) for i in range(n))
        yield x,v

def test(n):
    m=n-1
    assert multiply(gram(n),inv(n))==[[int(i==j) for j in range(m)] for i in range(m)]
    r,w,u,sums=radius(n)
    for i in range(m): assert abs(float(inv(n)[i][i])-w[i]**2)<1e-12
    for i in range(m-1):
        edge=inv(n)[i][i]+inv(n)[i+1][i+1]+2*inv(n)[i][i+1]
        assert edge==Fraction(n-1,n)
    k=n//2
    central={k-1} if n%2 else {k-2,k-1}  # zero-based edge-constraint indexes
    assert {i for i,s in enumerate(sums) if abs(s-max(sums))<1e-10}==central
    forced={z for i in central for z in [i,i+1]}
    assert len(forced)==(2 if n%2 else 3)
    # A relative-interior center: all non-forced lower-coordinate and noncentral upper facets strict.
    slack=min([1-r*sums[i] for i in range(m-1) if i not in central],default=1)
    eps=slack/10
    x=[r*w[i]+(0 if i in forced else eps) for i in range(m)]
    assert all(x[i]+1e-10>=r*w[i] for i in range(m))
    assert all(x[i]+x[i+1]+r*u<=1+1e-10 for i in range(m-1))
    for i in range(m):
        if i not in forced: assert x[i]>r*w[i]
    for i in range(m-1):
        if i not in central: assert x[i]+x[i+1]+r*u<1-1e-11
    if n<=14:
        a=list(matching_profiles(n))
        v={v for _,v in a}
        b={bits for bits in product((0,1),repeat=n) if is_perfect_matchable_subset(bits)}
        assert v==b and len(v)==len(a)
    return r,len(forced),len(central)

def independent_linear_program(n):
    import numpy as np
    from scipy.optimize import linprog
    m=n-1
    r,w,u,_=radius(n)
    # Variables [x_1,..,x_m,r]; for each facet its metric-clearance constraint.
    A=[];b=[]
    for i in range(m):
        row=[0.]*(m+1);row[i]=-1.;row[-1]=w[i]
        A.append(row);b.append(0.)
    for i in range(m-1):
        row=[0.]*(m+1);row[i]=row[i+1]=1.;row[-1]=u
        A.append(row);b.append(1.)
    objective=[0.] * m + [-1.]
    result=linprog(objective,A_ub=A,b_ub=b,bounds=[(None,None)]*(m+1),method='highs')
    assert result.success, result.message
    assert abs(result.x[-1]-r)<4e-8,(n,result.x[-1],r)
    return result.x[-1]

if __name__=='__main__':
    for n in range(3,31): test(n)
    try:
        import scipy
    except ImportError:
        print('SciPy not installed; exact checks still passed')
    else:
        for n in range(3,51): independent_linear_program(n)
        print('Independent LP verified n=3..50')
    print('PATH_MATCHABLE_INBALL_PASS n=3..30; enumerations n=3..14')
