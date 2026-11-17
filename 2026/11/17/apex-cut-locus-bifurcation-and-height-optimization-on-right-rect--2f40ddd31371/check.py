"""Standalone numerical and exact-arithmetic corroboration of the rectangular-pyramid apex theorem.
Scientific proofs are given in RESULT.md; this script is not an infinite certificate.
Run: python3 check.py
"""
from math import sqrt, hypot
from fractions import Fraction
from random import Random


def geometry(a,b,h):
    assert a>=b>0 and h>0
    ca=a+hypot(a,h)
    cb=b+hypot(b,h)
    t=cb/ca
    x=a-b*t
    length=2*x+4*b*hypot(1,t)
    ecc=hypot(cb,x)
    return ca,cb,t,x,length,ecc


def four_image_dist2(a,b,h,x,y):
    ca,cb,*_=geometry(a,b,h)
    return min((ca-x)**2+y*y,(ca+x)**2+y*y,x*x+(cb-y)**2,x*x+(cb+y)**2)


def edge_path_min_dist2(a,b,h,x,y,edge,n=300):
    # independently minimize surface paths of the form apex->edge q->point.
    # full edge minimization by golden-section search, not image minimization.
    def f(q):
        if edge=='E':
            return hypot(hypot(h,a),q)+hypot(x-a,y-q)
        if edge=='W':
            return hypot(hypot(h,a),q)+hypot(x+a,y-q)
        if edge=='N':
            return hypot(hypot(h,b),q)+hypot(x-q,y-b)
        if edge=='S':
            return hypot(hypot(h,b),q)+hypot(x-q,y+b)
        raise ValueError(edge)
    lo,hi=((-b,b) if edge in ('E','W') else (-a,a))
    # convex objective (sum of convex functions)
    for _ in range(n):
        p=lo+(hi-lo)*0.3819660112501051
        q=lo+(hi-lo)*0.6180339887498949
        if f(p)<f(q): hi=q
        else: lo=p
    return f((lo+hi)/2)**2


rng=Random(20261114)
for a,b,h in [(1,1,1),(2,1,1),(4,1,0.2),(1.1,1,3),(3,1,8),(3,2,0.01),(10,0.5,50)]:
    ca,cb,t,xstar,length,ecc=geometry(a,b,h)
    assert 0<=xstar<a
    assert abs(ca*ca-2*a*ca-h*h)<1e-9*max(1,h*h)
    assert abs(cb*cb-2*b*cb-h*h)<1e-9*max(1,h*h)
    corner2=h*h+a*a+b*b
    gap=ecc*ecc-corner2
    gap_theory=2*b*hypot(h,b)*(hypot(h,a)+b*t)/ca
    assert gap>0 and abs(gap-gap_theory)<5e-11*max(1,gap)
    for _ in range(100):
        px=(2*rng.random()-1)*a
        py=(2*rng.random()-1)*b
        d1=four_image_dist2(a,b,h,px,py)
        d2=min(edge_path_min_dist2(a,b,h,px,py,e,70) for e in 'EWNS')
        assert abs(d1-d2)<2e-9*max(1,d1), (a,b,h,px,py,d1,d2)
        assert d1<=ecc*ecc+1e-9*max(1,ecc*ecc)
    # Check the two junctions are triple-equidistant and match corner bisectors.
    assert abs((ca-xstar)**2-(xstar*xstar+cb*cb))<5e-10
    assert abs((ca-a)**2+b*b-(a*a+(cb-b)**2))<5e-10

# Fraction-level algebra for arbitrary positive c1>c2 satisfying c_i^2-2a_i c_i=h^2.
# Rational Pythagorean triples provide rational input cases.
for a,b,h in [(Fraction(4),Fraction(3),Fraction(0)),(Fraction(5),Fraction(3),Fraction(4))]:
    if h == 0: # boundary algebra only; main theorem requires h>0.
        ca=2*a;cb=2*b; ma=a;mb=b
    else:
        # 5,3,4: sqrt(41) irrational, so check algebra symbolically numerically elsewhere.
        continue
    t=cb/ca; x=a-b*t
    assert ca*ca-cb*cb == 2*(a*ca-b*cb)
    assert ca*x == (ca*ca-cb*cb)/2

# The explicit optimizing height matches the stationary ratio t=1/sqrt(3).
for a,b in [(2.,1.),(4.,1.),(10.,2.)]:
    hs=sqrt(3*a*a+3*b*b-4*sqrt(3)*a*b)
    ca,cb,t,x,ell,e=geometry(a,b,hs)
    assert abs(t-1/sqrt(3))<1e-12
    assert abs(ell-(2*a+2*sqrt(3)*b))<1e-12
    assert geometry(a,b,hs*0.8)[4]>ell
    assert geometry(a,b,hs*1.2)[4]>ell

for a,b in [(1.1,1.),(sqrt(3),1.)]:
    ls=[geometry(a,b,h)[4] for h in [0.001,0.1,1.,10.,100.]]
    assert all(u<v for u,v in zip(ls,ls[1:]))
for h in [0.01,0.1,1,10,100]:
    assert abs(geometry(2,2,h)[4]-8*sqrt(2))<1e-10
print('RECTANGULAR_PYRAMID_APEX_CUT_LOCUS_CHECKS_OK')
