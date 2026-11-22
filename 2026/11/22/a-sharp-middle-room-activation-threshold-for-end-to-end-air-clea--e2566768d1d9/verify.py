#!/usr/bin/env python3
"""Checks for a three-compartment steady contaminant-removal allocation.

All quantities are dimensionless rates. The exhaustive mathematical claim is
proved separately; this program provides exact identities and numerical tests.
Only Python standard-library modules are required.
"""
from fractions import Fraction
from math import sqrt, isclose
import random


def determinant(A):
    a,b,c=A[0]
    d,e,f=A[1]
    g,h,i=A[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def matrix(k,v,x):
    a,b,c=x
    return [[v+k+a,-k,0],[-k,v+2*k+b,-k],[0,-k,v+k+c]]


def concentration(k,v,x,q=1):
    """Cramer's rule (replaces matrix third column with the source vector)."""
    A=matrix(k,v,x)
    D=determinant(A)
    assert D>0
    rhs=[[A[0][0],A[0][1],q],
         [A[1][0],A[1][1],0],
         [A[2][0],A[2][1],0]]
    # Determinant of matrix with its third column replaced by (q,0,0).
    return determinant(rhs)/D


def optimum(k,v,F):
    assert k>0 and v>=0 and F>0
    critical=sqrt(v*v+4*k*v)-v
    if F<=critical:
        u=F/2
    else:
        u=(F+k-3*(v+k)+sqrt((F+k+3*(v+k))**2-12*k*k))/6
    return (u,F-2*u,u),critical


def direct_determinant(k,v,x):
    x1,x2,x3=x
    return ((v+k+x1)*(v+2*k+x2)*(v+k+x3)
            -k*k*((v+k+x1)+(v+k+x3)))


def audit():
    checks=0
    # Exact-rational algebraic equalities, including a sharp activation point.
    for k,v,F in [(Fraction(1),Fraction(1,2),Fraction(1)),
                  (Fraction(1),Fraction(1,2),Fraction(1,2)),
                  (Fraction(2),Fraction(1),Fraction(3)),
                  (Fraction(3),Fraction(0),Fraction(2))]:
        u=F/2
        x=(u,F-2*u,u)
        assert determinant(matrix(k,v,x))==direct_determinant(k,v,x)
        assert concentration(k,v,x)==k*k/direct_determinant(k,v,x)
        checks+=2
    # For k=1,v=1/2 the exact critical filtration budget is F=1.
    assert optimum(1,.5,.5)[0]==(.25,0,.25);checks+=1
    assert optimum(1,.5,1)[0]==(.5,0,.5);checks+=1
    x,fc=optimum(1,.5,2)
    assert fc==1.0 and x[0]>x[1]>0
    assert isclose(x[0],(sqrt(177)-3)/12,rel_tol=0,abs_tol=1e-13)
    assert isclose(x[1],(15-sqrt(177))/6,rel_tol=0,abs_tol=1e-13)
    checks+=3
    # Two-compartment baseline: exact quadratic maximized at equal split.
    for k,v,F in [(1,0,1),(1,.5,2),(2,4,1),(4,.2,11)]:
        D=lambda x:(v+k+x)*(v+k+F-x)-k*k
        assert D(F/2)>D(0) and D(F/2)>D(F)
        checks+=2
    rng=random.Random(167431)
    for _ in range(45):
        k=10**rng.uniform(-1,1)
        v=0.0 if rng.random()<.2 else 10**rng.uniform(-2,1)
        F=10**rng.uniform(-2,1.6)
        x,fc=optimum(k,v,F)
        assert min(x)>=-1e-10 and abs(sum(x)-F)<1e-10
        checks+=2
        D=determinant(matrix(k,v,x))
        assert isclose(D,direct_determinant(k,v,x),rel_tol=1e-12,abs_tol=1e-10)
        assert isclose(concentration(k,v,x),k*k/D,rel_tol=2e-12,abs_tol=1e-11)
        checks+=2
        if F<=fc:
            assert abs(x[1])<1e-12
        else:
            assert 0<x[1]<x[0]<F/2
        checks+=1
        # Numerical global stress test: every random allocation is no better.
        for _ in range(1100):
            t1,t2=rng.random(),rng.random()
            cut=sorted((t1,t2))
            xx=(F*cut[0],F*(cut[1]-cut[0]),F*(1-cut[1]))
            actual=determinant(matrix(k,v,xx))
            assert actual<=D+max(1e-8,1e-10*D)
            checks+=1
        # Equalizing endpoints at any fixed center weakly improves the determinant.
        for _ in range(100):
            mid=F*rng.random()
            left=(F-mid)*rng.random()
            alt=(left,mid,F-mid-left)
            equal=((F-mid)/2,mid,(F-mid)/2)
            assert determinant(matrix(k,v,alt))<=determinant(matrix(k,v,equal))+1e-8
            checks+=1
        # A stationary interior optimum solves the exact derivative equation.
        if F>fc:
            u=x[0]
            assert abs((v+k+u)*(F+k-3*u)-k*k)<1e-8*(1+k*k)
            checks+=1
    return checks

if __name__=='__main__':
    print('PASS',audit(),'assertions')
