#!/usr/bin/env python3
"""Self-contained exact checks of two-lossy-spin first-passage moments.

Only the standard library is used. The finite checks supplement the algebraic
proof; they are not an exhaustive proof of the parameter-uniform statements.
"""
from fractions import Fraction as F
from itertools import product
from math import isclose, sqrt
import cmath


def mat_solve(matrix, rhs):
    n = len(rhs)
    a = [list(row) + [rhs[i]] for i, row in enumerate(matrix)]
    for k in range(n):
        piv = next((i for i in range(k, n) if a[i][k]), None)
        assert piv is not None
        a[k], a[piv] = a[piv], a[k]
        z = a[k][k]
        a[k] = [u / z for u in a[k]]
        for i in range(n):
            if i == k:
                continue
            z = a[i][k]
            a[i] = [a[i][h] - z * a[k][h] for h in range(n+1)]
    return [a[i][n] for i in range(n)]


def independent_moments(x,y,j):
    s = x+y
    # Negative of the reduced Liouvillian on (rho11,rho22,rho33,2 Im rho12).
    B = [[x, F(0), -y, -j],
         [F(0), y, -x, j],
         [F(0), F(0), s, F(0)],
         [2*j, -2*j, F(0), s/2]]
    a = mat_solve(B,[F(0),F(0),F(1),F(0)])
    b = mat_solve(B,a)
    return sum(a[:3]), 2*sum(b[:3])


def claimed_moments(x,y,j):
    s=x+y; p=x*y; q=x*x+x*y+y*y; t=j*j
    m1=(12*t+q)/(s*(4*t+p))
    m2=2*(112*t*t + 8*t*(s*s+3*p) + q*q-2*p*p)/(s*s*(4*t+p)**2)
    cv=(80*t*t+8*t*(9*p-s*s)+q*q-4*p*p)/(q+12*t)**2
    return m1,m2,cv


def check():
    n=0
    xs=[F(1,5),F(1,2),F(1),F(3,2),F(3),F(7)]
    ys=[F(1,4),F(2,3),F(1),F(2),F(5)]
    js=[F(0),F(1,9),F(1,4),F(1,2),F(1),F(3),F(9)]
    for x,y,j in product(xs,ys,js):
        independent=independent_moments(x,y,j)
        m1,m2,cv=claimed_moments(x,y,j)
        assert independent == (m1,m2)
        assert cv == m2/m1**2 - 1
        assert m1>0 and m2>m1*m1
        # Exact polynomial derivative check at each tested triple:
        s=x+y; p=x*y; q=s*s-p; t=j*j; d=x-y
        numerator=80*t*t+8*t*(9*p-s*s)+q*q-4*p*p
        numerator_prime=160*t+8*(9*p-s*s)
        assert numerator_prime*(q+12*t)-24*numerator == -32*d*d*(s*s-8*t)
        # Exact strict improvement at the universal squared-coupling optimum.
        tstar=s*s/8
        cvstar=(x*x+8*p+y*y)/(5*x*x+8*p+5*y*y)
        nstar=80*tstar*tstar+8*tstar*(9*p-s*s)+q*q-4*p*p
        assert nstar/(q+12*tstar)**2==cvstar
        assert F(5,9)-cvstar == 16*d*d/(9*(5*x*x+8*p+5*y*y))
        if x != y:
            assert cvstar < F(5,9)
            assert cvstar < claimed_moments(x,y,F(0))[2]
        else:
            assert cvstar == F(5,9) == cv
        n+=10

    # Independent closed spectral representation (the source's eigenmodes),
    # evaluated in complex arithmetic without matrix inversion.
    triples=[(.3,1.7,.05),(.3,1.7,1.0),(1.,2.,.5),(1.,2.,3.),
             (2.,2.,.2),(1.,5.,.7),(2.,4.,2.),(3.,.1,5.)]
    for x,y,j in triples:
        d=x-y; s=x+y; lam=cmath.sqrt(d*d-16*j*j)
        if abs(lam)<1e-10: continue
        a=-32*j*j/(lam*lam); b=d*d/(lam*lam)
        poles=[s/2,s,(s-lam)/2,(s+lam)/2]
        coeffs=[a,-1,b,b]
        m1_spec=sum(c/p for c,p in zip(coeffs,poles))
        m2_spec=2*sum(c/p**2 for c,p in zip(coeffs,poles))
        f1,f2,_=claimed_moments(F(str(x)),F(str(y)),F(str(j)))
        assert abs(m1_spec.imag)<1e-10
        assert abs(m2_spec.imag)<1e-10
        assert isclose(m1_spec.real,float(f1),rel_tol=1e-10,abs_tol=1e-10)
        assert isclose(m2_spec.real,float(f2),rel_tol=1e-10,abs_tol=1e-10)
        n+=4
    # Physical unit-rate example (gamma1,gamma2)=(2,1).
    a,b=F(2),F(1)
    assert claimed_moments(a,b,F(0))[2]==F(33,49)
    assert (a*a+8*a*b+b*b)/(5*a*a+8*a*b+5*b*b)==F(21,41)
    assert F(21,41) < F(5,9) < F(33,49)
    n+=3
    print('PASS:',n,'exact-rational identities / independent spectral assertions')

if __name__=='__main__':
    check()
