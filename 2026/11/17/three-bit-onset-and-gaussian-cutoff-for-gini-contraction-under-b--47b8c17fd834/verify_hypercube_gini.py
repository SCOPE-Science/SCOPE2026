"""Reproducible symbolic and exact-cut checks for Boolean-noise Gini estimates.
Run with Python 3 and sympy installed. Does not substitute for the general-dimensional proof.
"""
from itertools import permutations
from fractions import Fraction
from math import comb
import sympy as s
r=s.symbols('r',real=True)

def cube_matrix(d):
    n=1<<d
    return [[s.prod(((1+r)/2 if not ((i^j)>>k&1) else (1-r)/2) for k in range(d)) for j in range(n)] for i in range(n)]

def cube_reps(d):
    n=1<<d; perms=list(permutations(range(d)))
    automorphisms=[]
    for perm in perms:
        for t in range(n):
            automorphisms.append(tuple(sum(((x>>k)&1)<<perm[k] for k in range(d))^t for x in range(n)))
    seen=set(); reps=[]
    for mask in range(1,(1<<n)-1):
        if mask in seen: continue
        orbit=set()
        for perm in automorphisms:
            a=sum(1<<perm[k] for k in range(n) if (mask>>k)&1)
            orbit.update((a,((1<<n)-1)^a))
        seen.update(orbit)
        reps.append((mask,len(orbit)))
    return reps,seen

reps,seen=cube_reps(3)
assert len(reps)==13 and len(seen)==254
assert [a for a,_ in reps]==[1,3,6,7,15,22,23,24,25,27,30,60,105]
T=cube_matrix(3)
Rstar=r*(15-r*r)/14
critical={22:s.Rational(1,3),25:s.sqrt(5)-2,30:s.sqrt(2)-1}
from sympy.polys.polytools import intervals
for mask,_ in reps:
    S=[j for j in range(8) if mask>>j&1];k=len(S)
    v=[s.expand(sum(T[i][j] for j in S)) for i in range(8)]
    diffs=[s.factor(v[i]-v[j]) for i in range(8) for j in range(i+1,8)]
    roots=set()
    for ex in diffs:
        if ex==0:continue
        z=s.solveset(ex,r,domain=s.Interval.open(0,1))
        assert z.is_FiniteSet, (mask,ex,z)
        roots.update(z)
    assert roots==({critical[mask]} if mask in critical else set()),(mask,roots)
    cuts=[s.Integer(0),*sorted(roots,key=lambda x:float(x)),s.Integer(1)]
    for left,right in zip(cuts,cuts[1:]):
        sample=(float(left)+float(right))/2
        expr=s.factor(sum(s.sign(ex.subs(r,sample))*ex for ex in diffs)/(k*(8-k)))
        # Prove bound by positivity on [left,right] using actual algebraic minimum and roots.
        poly=s.factor(Rstar-expr)
        assert poly.subs(r,(left+right)/2)>-s.Rational(1,10**9)
        candidates=[left,right]
        deriv=s.diff(poly,r)
        if deriv != 0:
            zz=s.solveset(deriv,r,domain=s.Interval(left,right))
            assert zz.is_FiniteSet, (mask,deriv,zz)
            candidates.extend(list(zz))
        assert all(float(poly.subs(r,c))>-1e-9 for c in candidates), (mask,poly,candidates)
print('SYMBOLIC_ALL_13_CUBE_ORBITS_EXACT_DOMAINS_PASS')

# Full cut enumeration over rational channels, including 2-bit equality and 3-bit sharpness.
for d in (1,2,3):
    n=1<<d
    for rr in (Fraction(0),Fraction(1,9),Fraction(1,3),Fraction(3,5),Fraction(8,9),Fraction(1)):
        T=[[Fraction((1+rr)**(d-(i^j).bit_count())*(1-rr)**((i^j).bit_count()),2**d) for j in range(n)] for i in range(n)]
        target=rr if d<=2 else rr*(15-rr**2)/14
        vals=[]
        for m in range(1,1<<(n-1)):
            S=[i for i in range(n-1) if m>>i&1]
            k=len(S)
            v=[sum(row[j] for j in S) for row in T]
            g=sum(abs(v[i]-v[j]) for i in range(n) for j in range(i+1,n))
            vals.append(g/Fraction(k*(n-k)))
        assert max(vals)==target,(d,rr,max(vals),target)
print('ALL_BINARY_CUTS_D1_TO_D3_EXACT_RATIONAL_PASS')

# Independent numerical evidence at dimension 4 and several noise strengths.
import numpy as np
for rr in (.1,.4,.8):
    d=4;n=16
    A=np.asarray([[((1+rr)/2)**(d-(i^j).bit_count())*((1-rr)/2)**((i^j).bit_count()) for j in range(n)] for i in range(n)])
    v=A[:,0];single=sum(abs(v[i]-v[j]) for i in range(n) for j in range(i+1,n))/(n-1)
    for mask in range(1,1<<(n-1)):
        k=mask.bit_count();x=A[:,[i for i in range(n-1) if mask>>i&1]].sum(axis=1)
        val=np.abs(x[:,None]-x[None,:]).sum()/2/(k*(n-k))
        assert val<=single+1e-10
print('DIMENSION4_ALL_CUTS_NUMERICAL_TESTS_PASS')
print('HYPERCUBE_GINI_CHECKS_PASS')
