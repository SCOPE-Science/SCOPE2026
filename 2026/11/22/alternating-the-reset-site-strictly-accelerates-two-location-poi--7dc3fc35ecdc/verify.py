"""Reproducible checks for two-location correlated Poisson-reset first passage.

Requires Python 3, sympy, and numpy. Numerical checks are supplementary to
an analytic renewal proof; finite tests do not prove universal assertions.
"""
from fractions import Fraction
import math
import random
import sympy as sp
import numpy as np


def formula(a, b, c, r):
    return (a+b-2*a*b+4*c*(1-a)*(1-b)) / (
        2*r*(a*b+c*(a+b-2*a*b)))


def direct_renewal(a, b, c, r):
    ma, mb = (1-a)/r, (1-b)/r
    A, B = a+c*(1-a), b+c*(1-b)
    X, Y = c*(1-a), c*(1-b)
    det = A*B-X*Y
    ta, tb = (B*ma+X*mb)/det, (Y*ma+A*mb)/det
    return (ta+tb)/2


def symbolic_check():
    a,b,c,r=sp.symbols('a b c r', positive=True)
    f=formula(a,b,c,r)
    assert sp.simplify(f-direct_renewal(a,b,c,r))==0
    derivative= -(a-b)**2/(2*r*(a*b+c*(a+b-2*a*b))**2)
    assert sp.simplify(sp.diff(f,c)-derivative)==0
    iid_gain=(a-b)**2/(2*r*(a+b)*(a+b-a*b))
    assert sp.simplify(f.subs(c,sp.Rational(1,2))-f.subs(c,1)-iid_gain)==0
    assert sp.simplify(f.subs(c,sp.Rational(1,2))-(2-a-b)/(r*(a+b)))==0
    assert sp.simplify(f.subs(a,b).diff(c))==0


def discrete_cycle_check(n, i, j, D, L, r, c):
    # Independent spatial generator for two reset phases on a killed cycle.
    k=D*(n/L)**2
    s=n-1
    A=np.zeros((2*s,2*s))
    bvec=np.ones(2*s)
    def pos(phase,vertex):return phase*s+vertex-1
    for phase in (0,1):
        for vertex in range(1,n):
            row=pos(phase,vertex)
            A[row,row]+=2*k+r
            for neighbor in (vertex-1,vertex+1):
                if 1<=neighbor<n:A[row,pos(phase,neighbor)]-=k
            location=(i,j)[phase]
            next_location=(i,j)[1-phase]
            A[row,pos(phase,location)]-=r*(1-c)
            A[row,pos(1-phase,next_location)]-=r*c
    times=np.linalg.solve(A,bvec)
    independent=(times[pos(0,i)]+times[pos(1,j)])/2
    # Discounted *reset-free* target hitting, separately solved.
    B=np.zeros((s,s))
    rhs=np.zeros(s)
    for vertex in range(1,n):
        idx=vertex-1
        B[idx,idx]=2*k+r
        for neighbor in (vertex-1,vertex+1):
            if neighbor in (0,n):rhs[idx]+=k
            else:B[idx,neighbor-1]-=k
    f=np.linalg.solve(B,rhs)
    from_renewal=formula(f[i-1],f[j-1],c,r)
    return independent,from_renewal


def numerical_checks():
    rng=random.Random(40017)
    for _ in range(120):
        a=Fraction(rng.randrange(1,99),100)
        b=Fraction(rng.randrange(1,99),100)
        c=Fraction(rng.randrange(0,101),100)
        r=Fraction(rng.randrange(1,100),10)
        assert formula(a,b,c,r)==direct_renewal(a,b,c,r)
        assert formula(a,b,0,r)>=formula(a,b,c,r)>=formula(a,b,1,r)
        if a!=b and c<1:
            assert formula(a,b,c,r)>formula(a,b,1,r)
    # Compare complete killed generator with independently derived renewal.
    count=0
    for n,i,j,D,L,r in [(10,2,4,1.,1.,3.),(12,2,7,.7,2.,.8),
                         (16,4,9,1.,1.,5.),(18,3,15,2.,3.,1.5)]:
        for c in [0.,.1,.5,.7,1.]:
            direct,renewal=discrete_cycle_check(n,i,j,D,L,r,c)
            assert abs(direct-renewal)<2e-11*(1+abs(direct)), (direct,renewal)
            count+=1
    L,D,r,x,y=1.,1.,4.,.2,.47
    q=math.sqrt(r/D)
    a=math.cosh((L/2-x)*q)/math.cosh(L*q/2)
    b=math.cosh((L/2-y)*q)/math.cosh(L*q/2)
    expected=[formula(a,b,c,r) for c in (0,.25,.5,.75,1)]
    assert all(expected[k]>expected[k+1] for k in range(4))
    assert abs(expected[2]-expected[-1]-(a-b)**2/(2*r*(a+b)*(a+b-a*b)))<1e-14
    print('PASS: symbolic derivative and rational identities; 120 exact rational cases;'
          f' {count} independent killed-generator comparisons; ring example.' )
    print('Ring example: success probabilities',repr(a),repr(b))
    print('Ring MFPT for c = 0,.25,.5,.75,1:',*[f'{t:.12f}' for t in expected])


if __name__=='__main__':
    symbolic_check()
    numerical_checks()
