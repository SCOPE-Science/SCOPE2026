#!/usr/bin/env python3
"""Supplementary exact and numerical tests for the stated finite Fourier phase classification."""
import cmath, math
from fractions import Fraction

def gram_three(p,q):
    t=Fraction(p,q)
    assert 0<t<=Fraction(1,4)
    s=(1-t)/3
    tau=t/s
    z=cmath.exp(1j*math.acos(-float(1+tau)/2))
    H=((1,1,z),(z,1,1),(1,z,1))
    U=[[math.sqrt(float(s))*a for a in row] for row in H]
    U.append([math.sqrt(float(t))]*3)
    for j in range(3):
        for k in range(3):
            inner=sum(U[r][j].conjugate()*U[r][k] for r in range(4))
            assert abs(inner-(1 if j==k else 0))<2e-13

def cubic_identity(tau):
    # (x-1)(x*x+(1+tau)*x+1) = x**3 + tau*x*x - tau*x -1
    assert (-1)*(1+tau)+1 == -tau
    assert (1+tau)-1 == tau

for p,q in ((1,100),(1,10),(1,5),(7,32),(1,4)):
    gram_three(p,q)
for p,q in ((1,100),(1,10),(1,5),(1,4),(3,10),(1,3),(2,5)):
    t=Fraction(p,q)
    tau=t/((1-t)/3)
    cubic_identity(tau)
    if t>Fraction(1,4):
        assert tau>1
# Equality at uniform four-site mass: 4-point DFT unitary.
for j in range(4):
    for k in range(4):
        entry=sum(cmath.exp(2j*math.pi*r*(k-j)/4) for r in range(4))/4
        assert abs(entry-(1 if j==k else 0)) < 2e-14
print('PASS: 5 constructive isometries, 7 cubic identities, 16 DFT Gram entries')
