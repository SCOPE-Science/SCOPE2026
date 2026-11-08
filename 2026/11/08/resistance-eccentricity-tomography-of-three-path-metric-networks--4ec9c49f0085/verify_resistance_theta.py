"""Independent electrical-network checks of resistance eccentricity reconstruction.

Run with Python 3: python verify_resistance_theta.py
The proof is analytic; these finite checks are diagnostic only.
"""
from fractions import Fraction as Q
from math import sqrt, isclose
from random import Random


def resistance_at(a, i, x):
    """Direct 2x2 Kirchhoff solve after adding an interior subdivision vertex."""
    g1=1/x
    g2=1/(a[i]-x)
    g0=sum((1/t for j,t in enumerate(a) if i!=j), Q(0))
    aa=g1+g0
    bb=g1+g2
    det=aa*bb-g1*g1
    va=(bb-g1)/det  # currents +1 at A, -1 at X
    vx=(g1-aa)/det
    return va-vx


def formula(a, i, x):
    r=1/sum((1/t for t in a),Q(0))
    return x-(a[i]-r)*x*x/(a[i]*a[i])

rng=Random(20261102)
exact_cases=0
for k in range(3,9):
    for rep in range(20):
        a=[Q(rng.randrange(2,30),rng.randrange(2,20)) for _ in range(k)]
        i=rng.randrange(k)
        x=a[i]*Q(rng.randrange(1,99),100)
        assert resistance_at(a,i,x)==formula(a,i,x)
        exact_cases+=1

inverse_cases=0
bounds_cases=0
for k in range(3,11):
    for rep in range(1000):
        a=[10**rng.uniform(-2,2) for _ in range(k)]
        L=sum(a)
        r=1/sum(1/x for x in a)
        m=max(a)
        E=m*m/(4*(m-r))
        assert L/(4*(k-1)) <= E+1e-11*L < L/4+1e-11*L
        assert isclose(2*(E+sqrt(E*(E-r))),m,rel_tol=5e-12,abs_tol=1e-12)
        bounds_cases+=1
        if k==3:
            S=L-m
            C=1/r-1/m
            d=S*S-4*S/C
            assert d>=-1e-10*S*S
            other=sorted([(S+sqrt(max(0,d)))/2,(S-sqrt(max(0,d)))/2])
            expected=sorted(a)
            assert isclose(other[0],expected[0],rel_tol=1e-8,abs_tol=1e-10)
            assert isclose(other[1],expected[1],rel_tol=1e-8,abs_tol=1e-10)
            inverse_cases+=1

# Two different four-arm graphs with all three scalar measurements equal.
sqrtterm=sqrt(15/7)
a=[5,1,2,3]
b=[5,1.5,2.25+0.75*sqrtterm,2.25-0.75*sqrtterm]
assert not all(isclose(x,y,abs_tol=1e-8) for x,y in zip(sorted(a),sorted(b)))
assert isclose(sum(a),sum(b),abs_tol=1e-12)
ra=1/sum(1/x for x in a)
rb=1/sum(1/x for x in b)
assert isclose(ra,rb,abs_tol=1e-12)
assert isclose(max(a)**2/(4*(max(a)-ra)),max(b)**2/(4*(max(b)-rb)),abs_tol=1e-12)

print(f'VERIFY_OK exact_nodal_cases={exact_cases} random_global_bounds={bounds_cases} inverse_theta_cases={inverse_cases} four_arm_counterexample=1')
