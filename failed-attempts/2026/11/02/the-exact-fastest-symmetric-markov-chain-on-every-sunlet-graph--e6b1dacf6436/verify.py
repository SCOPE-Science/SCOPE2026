#!/usr/bin/env python3
"""Direct numerical cross-checks for the fastest symmetric Markov chain on a cycle with leaves.

Requires Python 3.9+ and NumPy.  Finite computations are sanity checks, not proof
of the all-orders optimization theorem.
"""
import math
import random
from fractions import Fraction
import numpy as np

SEED = 20261025
rng = random.Random(SEED)


def params(m):
    d = 1.0 - math.cos(2.0 * math.pi / m)
    a = (4.0 - (2.0 - d) * math.sqrt(d)) / (2.0 * (4.0 + d*d))
    b = 1.0 - 2.0 * a
    mu = 2.0*(2.0-d+d**1.5)/(4.0+d*d)
    return d,a,b,mu


def block_eigs(m, a, b):
    vals = [1.0, 1.0-2.0*b]
    for j in range(1,m):
        d = 1.0 - math.cos(2.0*math.pi*j/m)
        v = math.hypot(b,a*d)
        vals.extend([1.0-b-a*d+v,1.0-b-a*d-v])
    return np.sort(np.array(vals))


def transition(m, rim_weights, spoke_weights):
    assert len(rim_weights)==len(spoke_weights)==m
    P = np.eye(2*m)
    for j,w in enumerate(rim_weights):
        k=(j+1)%m
        P[j,k]+=w;P[k,j]+=w
        P[j,j]-=w;P[k,k]-=w
    for j,w in enumerate(spoke_weights):
        P[j,m+j]+=w;P[m+j,j]+=w
        P[j,j]-=w;P[m+j,m+j]-=w
    assert np.min(P)>-1e-12
    return P


def actual_slem(P):
    v=np.linalg.eigvalsh(P)
    assert abs(v[-1]-1.0)<3e-12
    return max(abs(v[0]),abs(v[-2]))


formula_count=0
for m in range(3,201):
    d,a,b,mu=params(m)
    assert 0<a<.5 and 0<b<1 and abs(2*a+b-1)<1e-13
    objective = a*(2-d)+math.hypot(b,a*d)
    derivative = 2-d+((4+d*d)*a-2)/math.hypot(b,a*d)
    assert abs(objective-mu)<2e-13, (m,objective,mu)
    assert abs(derivative)<1e-8, (m,derivative)
    v=block_eigs(m,a,b)
    assert abs(max(abs(v[0]),abs(v[-2]))-mu)<3e-13
    formula_count+=1

full_spec_count=0
for m in range(3,42):
    _,a,b,mu=params(m)
    for attempt in range(5):
        if attempt==0:
            aa,bb=a,b
        else:
            aa=rng.random()/2
            bb=rng.random()*(1-2*aa)
        P=transition(m,[aa]*m,[bb]*m)
        v=np.linalg.eigvalsh(P)
        predicted=block_eigs(m,aa,bb)
        assert np.max(np.abs(v-predicted))<1.5e-12,(m,aa,bb)
        if attempt==0:assert abs(actual_slem(P)-mu)<1.5e-12
        full_spec_count+=1

symmetric_feasible_count=0
for m in range(3,121):
    _,_,_,mu=params(m)
    for trial in range(160):
        a=rng.random()/2
        b=rng.random()*(1-2*a)
        v=block_eigs(m,a,b)
        val=max(abs(v[0]),abs(v[-2]))
        assert val+2e-13>=mu,(m,a,b,val,mu)
        symmetric_feasible_count+=1

asymmetric_feasible_count=0
for m in range(3,13):
    _,_,_,mu=params(m)
    for _ in range(120):
        edge=[rng.random()/3 for j in range(m)]
        spoke=[rng.random()/3 for j in range(m)]
        P=transition(m,edge,spoke)
        val=actual_slem(P)
        assert val+2e-12>=mu, (m,val,mu)
        asymmetric_feasible_count+=1

_,a4,b4,mu4=params(4)
assert abs(a4-3/10)<1e-14 and abs(b4-2/5)<1e-14 and abs(mu4-4/5)<1e-14
q = Fraction(2,5)**2 + (Fraction(3,10)*Fraction(1,1))**2
assert q == Fraction(1,4)  # exact discriminant is the square of 1/2
assert Fraction(3,10)*(2-Fraction(1,1))+Fraction(1,2) == Fraction(4,5)

asymptotic_count=0
for m in [1000,2000,5000,10000]:
    _,a,b,mu=params(m)
    first=1-mu
    approximated=math.pi**2/m**2-math.sqrt(2)*math.pi**3/m**3
    assert abs(first-approximated)<1000/m**4
    assert abs(b-math.pi/(math.sqrt(2)*m))<100/m**3
    asymptotic_count+=1

print('FORMULA_AND_STATIONARITY_OK',formula_count)
print('FULL_MATRIX_FOURIER_SPECTRA_OK',full_spec_count)
print('FEASIBLE_SYMMETRIC_OBJECTIVES_OK',symmetric_feasible_count)
print('FEASIBLE_ASYMMETRIC_OBJECTIVES_OK',asymmetric_feasible_count)
print('EXACT_RATIONAL_N4_OK', '(a,b,mu)=(3/10,2/5,4/5)')
print('ASYMPTOTIC_SAMPLES_OK',asymptotic_count)
print('VERIFY_OK')
