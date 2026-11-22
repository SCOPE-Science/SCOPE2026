"""Reproduce spectral, moment, and threshold identities for the stated contact matrix.
The analytic proof is in RESULT.md; finite checks do not replace that proof.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt
import numpy as np
import sympy as sp

p = [F(4,5), F(1,5)]
s2 = sum((v*v for v in p), F(0)); s3=sum((v*v*v for v in p), F(0))
assert s2 == F(17,25) and s3 == F(13,25)
assert s3/s2**2 - 1 == F(36,289)
alpha=(1-s2)/s2
assert alpha == F(8,17)
Sneg = sp.Matrix([[sp.Rational(p[i].numerator,p[i].denominator)*(1-sp.Rational(alpha.numerator,alpha.denominator)) if i == j else sp.Rational(4,5) for j in range(2)] for i in range(2)])
assert Sneg == sp.Matrix([[sp.Rational(36,85),sp.Rational(4,5)],[sp.Rational(4,5),sp.Rational(9,85)]])
eigs = Sneg.eigenvals()
assert sp.simplify(max(eigs.keys(),key=lambda x:float(x))-(9+sp.sqrt(769))/34) == 0
assert sp.simplify(sp.Rational(19,20)*(9+sp.sqrt(769))/34-1)>0
assert sp.Rational(19,20)*(sp.Rational(20,17))>1
assert sp.simplify(sp.Rational(19,20)*(23+sp.sqrt(202))/34-1)>0
assert sp.simplify(sp.Rational(19,20)*(23+sp.sqrt(202))/34-1) > 0
assert sp.Rational(19,20)<1

rng=np.random.default_rng(27467)
checks=0
for m in range(2,10):
    for trial in range(110):
        raw=rng.uniform(.01,1.0,size=m)
        p=raw/sum(raw)
        s2=float(sum(p*p)); s3=float(sum(p**3))
        u=np.sqrt(p)
        B=np.diag(p/s2)-np.outer(u,u)
        assert abs(float(u@B@u)) < 1e-12
        assert abs(float(np.linalg.norm(B@u)**2)-(s3/s2**2-1)) < 1e-11
        emin=-s2/(1-s2)
        for e in (max(-1,emin), -0.15*min(1,-emin), 0., 0.2, 1.):
            S=(1-e)*np.outer(u,u)+e/s2*np.diag(p)
            eig=np.linalg.eigvalsh(S)[-1]
            assert eig >= 1-1e-12
            if abs(e)>1e-10 and np.ptp(p)>1e-6:
                assert eig>1+1e-12
            checks+=1
print('PASS: two-group exact radicals, quadratic coefficient and threshold reversal; randomized spectral checks:',checks)

# An exactly computed, two-dimensional Krylov compression gives a moment envelope.
from math import isclose
new_checks=0
for m in range(2,10):
    for _ in range(100):
        raw=rng.uniform(.02,1,size=m)
        p=raw/raw.sum()
        s2=np.sum(p**2);s3=np.sum(p**3);s4=np.sum(p**4)
        v=s3/s2**2-1
        t=(s4-2*s2*s3+s2**3)/(s2*(s3-s2**2))
        u=np.sqrt(p)
        w=(p/s2-1)*u/np.sqrt(v)
        assert abs(np.dot(u,w))<1e-11
        assert abs(np.dot(w,w)-1)<1e-11
        for e in (-0.5*min(1,s2/(1-s2)), 0.13,0.75,1.):
            S=(1-e)*np.outer(u,u)+e/s2*np.diag(p)
            lower=(1+e*t+np.sqrt((1-e*t)**2+4*e*e*v))/2
            actual=np.linalg.eigvalsh(S)[-1]
            assert actual+1e-10>=lower
            if len(set(np.round(p,7)))>=3:
                assert actual>lower+1e-14, (m, e, actual-lower, p.tolist())
            new_checks+=1
for a,b in [(2,1),(3,2),(6,3),(1,3)]:
    p=np.array([a]*3+[b]*2,dtype=float)
    p/=p.sum();s2=np.sum(p**2);s3=np.sum(p**3);s4=np.sum(p**4)
    v=s3/s2**2-1;t=(s4-2*s2*s3+s2**3)/(s2*(s3-s2**2))
    u=np.sqrt(p)
    for e in (-.1,.2,.7,1.):
        S=(1-e)*np.outer(u,u)+e/s2*np.diag(p)
        lower=(1+e*t+np.sqrt((1-e*t)**2+4*e*e*v))/2
        assert abs(np.linalg.eigvalsh(S)[-1]-lower)<1e-10
        new_checks+=1
print('PASS: sharp two-moment compression envelope and equality class checks:',new_checks)
