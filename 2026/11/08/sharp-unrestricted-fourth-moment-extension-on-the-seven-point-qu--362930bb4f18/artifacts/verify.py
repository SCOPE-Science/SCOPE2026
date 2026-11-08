#!/usr/bin/env python3
"""Exact finite checks for a seven-point quartic Fourier extension inequality.
Standard library only; finite tests corroborate the symbolic argument."""
from collections import defaultdict
from fractions import Fraction
from random import Random
from itertools import product
from cmath import exp,pi

P=7
F={t:(t,t**4%P) for t in range(P)}
fibers=defaultdict(list)
for a in range(P):
    for b in range(P):
        fibers[((a+b)%P,(a**4+b**4)%P)].append((a,b))
assert sum(map(len,fibers.values()))==49
unord=defaultdict(list)
for a in range(P):
    for b in range(a,P):
        unord[((a+b)%P,(a**4+b**4)%P)].append((a,b))
assert len([v for v in unord.values() if len(v)>1])==6
assert all(sorted(v)==sorted([(0,t),((4*t)%P,(4*t)%P)]) for t in range(1,P) for v in [unord[(t,t**4%P)]])
H=(1,2,4)
J=(3,5,6)

def direct_energy(z):
    return sum(abs(sum(z[a]*z[b] for a,b in v))**2 for v in fibers.values())

def energy_formula(z):
    S=sum(abs(w)**2 for w in z)
    return 2*S*S-sum(abs(w)**4 for w in z)+4*sum((z[0]*z[t]*(z[4*t%7].conjugate()**2)).real for t in range(1,7))

def deficit_sos(x):
    a=x[0]
    B1=sum(x[t]**2 for t in H)
    B2=sum(x[t]**2 for t in J)
    B=B1+B2
    one=2*sum(x[4*t%7]**2*(a-x[t])**2 for t in range(1,7))
    two=Fraction(2,3)*sum((x[s]**2-x[t]**2)**2 for O in (H,J) for i,s in enumerate(O) for t in O[i+1:])
    three=Fraction(1,6)*(3*a*a-B)**2
    four=Fraction(2,3)*B1*B2
    return one+two+three+four

random=Random(27112026)
for j in range(1000):
    z=[complex(random.randrange(-6,7),random.randrange(-6,7)) for _ in range(7)]
    assert abs(direct_energy(z)-energy_formula(z))<1e-8
    S=sum(abs(w)**2 for w in z)
    assert direct_energy(z) <= 2.5*S*S+1e-6
    x=[Fraction(random.randrange(0,8),random.randrange(1,5)) for _ in range(7)]
    S=sum(t*t for t in x)
    E=energy_formula(x)
    D=Fraction(5,2)*S*S-E
    assert D==deficit_sos(x),(x,D,deficit_sos(x))
for orbit in (H,J):
    for k in range(P):
        z=[0j]*P
        z[0]=1+0j
        for t in orbit:
            z[t]=exp(2j*pi*k*t/P)
        S=sum(abs(v)**2 for v in z)
        assert abs(direct_energy(z)/(S*S)-2.5)<1e-12
        assert abs(energy_formula(z)-40)<1e-11
# Four-atom equality also verified exactly using k=0.
for orbit in (H,J):
    z=[Fraction(1) if t==0 or t in orbit else Fraction(0) for t in range(P)]
    assert direct_energy(z)==40
print('QUARTIC_SEVEN_SHARP_PASS exact_integer_and_rational_tests=1000 projective_extremizers=14 pair_fibers=22')
