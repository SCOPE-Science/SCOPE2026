#!/usr/bin/env python3
"""Exact rational checks for the priced four-cycle spectral-gap theorem.

This finite replay checks formula identities, endpoint cases, and randomly selected
feasible competitors. The mathematical proof is in RESULT.md.
"""
from fractions import Fraction as Q
import random
import sympy as sp


def weighted_laplacian(a, b1, c, b2):
    L = sp.zeros(4)
    for i,j,w in [(0,1,a),(1,2,b1),(2,3,c),(3,0,b2)]:
        L[i,i] += w
        L[j,j] += w
        L[i,j] -= w
        L[j,i] -= w
    return L


def formula(d, budget):
    D=d*d+2*d+5
    if d<3:
        return budget*(d+1)/(d*D), 2*budget/D, budget*(d+1)/D, 2*budget/D, 4*budget/D
    return sp.S(0),3*budget/10,4*budget/10,3*budget/10,budget/5


def check_exact_sample(d, B):
    a,b,c,b2,lam=formula(d,B)
    L=weighted_laplacian(a,b,c,b2)
    assert sp.simplify(d*d*a+b+b2+c-B)==0
    eigens=L.eigenvals()
    vals=sorted((sp.simplify(x) for x in eigens.keys()), key=lambda z: float(z))
    assert vals[0]==0 and sp.simplify(vals[1]-lam)==0, (d,B,vals,lam)
    if d<3:
        assert L.eigenvals().get(lam)==2, (d,B,L.eigenvals(),lam)
    v=sp.Matrix([1,1,-1,-1]); u=sp.Matrix([d,-d,-1,1])
    if d<3:
        assert L*v==lam*v and L*u==lam*u
        tau=2*(d*d+1)/(d*d+2*d+5)
        assert 0 < tau < 1
        for edge,price in [((0,1),d*d),((1,2),1),((2,3),1),((3,0),1)]:
            i,j=edge
            coeff=sp.simplify(tau*(u[i]-u[j])**2/(u.dot(u))+(1-tau)*(v[i]-v[j])**2/(v.dot(v)))
            assert sp.simplify(coeff-4*price/(d*d+2*d+5))==0
    else:
        x=sp.Matrix([-3,3,1,-1])
        assert L*x==lam*x
        if d>3:assert a==0


def check_critical_family():
    for a in [sp.S(0),sp.Rational(1,200),sp.Rational(1,30),sp.Rational(1,15)]:
        b=sp.Rational(3,10)-3*a
        c=sp.Rational(2,5)-3*a
        L=weighted_laplacian(a,b,c,b)
        assert 9*a+2*b+c==1
        assert sorted(L.eigenvals(),key=float)[1]==sp.Rational(1,5)
    # Just past the family endpoint, the symmetry mode gives a strict loss.
    a=sp.Rational(7,100)
    b=sp.Rational(3,10)-3*a
    c=sp.Rational(2,5)-3*a
    assert 2*b<sp.Rational(1,5)


def check_rational_competitors():
    rng=random.Random(20261101)
    checks=0
    for d in [sp.Rational(1,5),sp.Rational(1,2),sp.S(1),sp.Rational(3,2),sp.S(2),sp.Rational(5,2),sp.S(3),sp.S(4),sp.S(7)]:
        a,b,c,b2,target=formula(d,sp.S(1))
        for _ in range(160):
            raw=[sp.S(rng.randrange(1,31)) for i in range(4)]
            cost=d*d*raw[0]+raw[1]+raw[2]+raw[3]
            w=[q/cost for q in raw]
            L=weighted_laplacian(*w)
            # Rayleigh with closed-form witness is an exact, unconditional upper bound.
            if d<=3:
                v=sp.Matrix([1,1,-1,-1]);u=sp.Matrix([d,-d,-1,1])
                tau=2*(d*d+1)/(d*d+2*d+5)
                cert=sp.simplify(tau*(u.dot(L*u))/u.dot(u)+(1-tau)*(v.dot(L*v))/v.dot(v))
            else:
                x=sp.Matrix([-3,3,1,-1]);cert=sp.simplify(x.dot(L*x)/x.dot(x))
            assert cert<=target and target>0
            checks+=1
    return checks



def check_symbolic_identities():
    d,B=sp.symbols('d B',real=True,positive=True)
    D=d*d+2*d+5
    tau=2*(d*d+1)/D
    v=sp.Matrix([1,1,-1,-1]);u=sp.Matrix([d,-d,-1,1])
    edges=[(0,1,d*d),(1,2,sp.S(1)),(2,3,sp.S(1)),(3,0,sp.S(1))]
    for i,j,price in edges:
        lhs=(1-tau)*(v[i]-v[j])**2/v.dot(v)+tau*(u[i]-u[j])**2/u.dot(u)
        assert sp.factor(lhs-4*price/D)==0
    a=B*(d+1)/(d*D);b=2*B/D;c=B*(d+1)/D
    L=weighted_laplacian(a,b,c,b)
    assert sp.factor(d*d*a+2*b+c-B)==0
    assert all(sp.factor(q)==0 for q in L*v-4*B/D*v)
    assert all(sp.factor(q)==0 for q in L*u-4*B/D*u)
    assert sp.factor(2*(a+c)-4*B/D)==2*B*(d*d+1)/(d*D)
    assert sp.factor(1-tau)==-((d-3)*(d+1))/D
    x=sp.Matrix([-3,3,1,-1])
    ap=sp.S(0);bp=3*B/10;cp=2*B/5
    Lp=weighted_laplacian(ap,bp,cp,bp)
    assert all(sp.factor(q)==0 for q in Lp*x-B/5*x)
    assert sp.factor(d*d*ap+2*bp+cp-B)==0
    return 4+2+2+1+2+1

def main():
    identities=check_symbolic_identities()
    cases=0
    for d in [sp.Rational(1,5),sp.Rational(1,2),sp.S(1),sp.Rational(3,2),sp.S(2),sp.Rational(5,2),sp.S(3),sp.S(4),sp.S(7)]:
        for B in [sp.Rational(1,3),sp.S(1),sp.Rational(7,3)]:
            check_exact_sample(d,B)
            cases+=1
    check_critical_family()
    comps=check_rational_competitors()
    print(f'PASS: {identities} symbolic identities; {cases} exact rational spectra; 4 critical allocations; {comps} exact rational competitor certificates')

if __name__=='__main__':main()
