"""Direct matrix-exponential verification of phase-controlled transport."""
import numpy as np
from scipy.linalg import expm
from fractions import Fraction
from math import pi, sqrt


def matrix_from_phases(z):
    m = len(z)
    H = np.zeros((m+2, m+2), dtype=complex)
    for j, phase in enumerate(z):
        H[0,j+2] = 1
        H[j+2,0] = 1
        H[1,j+2] = phase
        H[j+2,1] = np.conj(phase)
    return H

def predicted(z, t):
    m=len(z)
    S=sum(z)
    s=abs(S)
    if s < 1e-12:
        return 0j
    lp=np.sqrt(m+s)
    lm=np.sqrt(m-s)
    # hub block is [[m, conj(S)], [S, m]]
    return (S/s)*(np.cos(lp*t)-np.cos(lm*t))/2

rng = np.random.default_rng(20261120)
max_error=0.
for m in range(2,13):
    for _ in range(24):
        z=np.exp(1j*rng.uniform(-pi,pi,m))
        t=float(rng.uniform(0.0,17.0))
        H=matrix_from_phases(z)
        amplitude=expm(-1j*t*H)[1,0]
        err=abs(amplitude-predicted(z,t))
        max_error=max(max_error,err)
        assert err < 2e-13, (m,t,err)
print('PASS: 264 full matrix-exponential comparisons; max error',max_error)

# Opposite-parity frequency ratio 2:1, phases 3/5 +/- 4i/5, m=2.
z=[(3+4j)/5,(3-4j)/5]
t=pi*sqrt(5)/2
assert abs(abs(expm(-1j*t*matrix_from_phases(z))[1,0])**2-1)<3e-13
print('PASS: exact transfer example at time pi*sqrt(5)/2')

# Rational both-odd 3:1 ratio, phases 4/5 +/- 3i/5.
z=[(4+3j)/5,(4-3j)/5]
period=2*pi/sqrt(2/5)
ss=np.linspace(0,period,100001)
prob=np.abs([predicted(z,t) for t in ss])**2
maxsample=max(prob)
assert abs(maxsample-16/27)<1e-8,(maxsample,16/27)
print('PASS: both-odd 3:1 resonance maximum probability 16/27')

# Destructive interference with two opposed branch phases.
z=[1+0j,-1+0j]
assert np.max(np.abs([expm(-1j*t*matrix_from_phases(z))[1,0] for t in [0.1,1.,2.,5.,10.]])) < 1e-14
print('PASS: S=0 exact dark configuration')

# Irrational ratio sqrt(3), phasors exp(+/-i pi/3), time 15pi.
z=[np.exp(1j*pi/3),np.exp(-1j*pi/3)]
p=abs(expm(-1j*15*pi*matrix_from_phases(z))[1,0])**2
assert p > 0.998
print('PASS: irrational ratio sqrt(3), fidelity at t=15pi',p)
