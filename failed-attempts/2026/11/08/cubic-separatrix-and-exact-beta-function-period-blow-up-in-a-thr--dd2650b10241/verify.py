"""Standalone numerical and algebraic checks for the three-phase quadrature orbit-period theorem.
Run with: python verify.py. Requires Python, NumPy and SciPy.
All-level assertions remain analytical; this script tests representative energies only.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.special import beta

PI=math.pi
HMAX=3*math.sqrt(3)/2
C=2**(2/3)*beta(1/3,1/3)

def hamiltonian(x,y):
    return math.sin(x)+math.sin(y)-math.sin(x+y)

def level_period(energy, sample_count=6000):
    center=2*PI/3
    total=0.0
    for j in range(sample_count):
        angle=2*PI*(j+0.5)/sample_count
        c,s=math.cos(angle),math.sin(angle)
        bounds=[]
        if c<0: bounds.append(-center/c)
        if s<0: bounds.append(-center/s)
        if c+s>0: bounds.append((2*PI-2*center)/(c+s))
        upper=min(bounds)
        r=brentq(lambda rad:hamiltonian(center+rad*c,center+rad*s)-energy,0,upper,xtol=1e-13)
        x,y=center+r*c,center+r*s
        grad_r=(math.cos(x)-math.cos(x+y))*c+(math.cos(y)-math.cos(x+y))*s
        assert grad_r<0
        total += r/(-grad_r)
    return 2*PI*total/sample_count

assert abs(hamiltonian(2*PI/3,2*PI/3)-HMAX)<1e-14
for x in (0.1,0.4,1.2,2.3):
    for y in (0.15,0.8,1.7,2.9):
        lhs=hamiltonian(x,y)
        rhs=4*math.sin(x/2)*math.sin(y/2)*math.sin((x+y)/2)
        assert abs(lhs-rhs)<1e-14
assert abs(C-8.413092631952725)<1e-11
values=[]
for E in (0.1,0.01,0.001,0.0001):
    T=level_period(E)
    scaled=T*E**(1/3)
    values.append(scaled)
    assert abs(scaled/C-1)<(0.05 if E==0.1 else 0.011 if E==0.01 else 0.003 if E==0.001 else 0.0007)
assert all(values[j]<values[j+1] for j in range(len(values)-1))
assert abs(level_period(HMAX-1e-4)-4*PI/3)<0.01
print('VERIFY_OK factor_identity=16 center_energy=1 period_levels=4 center_limit=1 beta_constant=1')
print('PERIOD_SCALED', ' '.join(f'{a:.11f}' for a in values))
