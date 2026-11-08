"""Finite consistency checks for the explicitly stated lattice Szego-kernel zero classification.

This script is supplemental numerical evidence, not a proof of the infinite theorem.
Run with Python 3 and mpmath >= 1.3.0.
"""
from mpmath import mp

mp.dps = 60

def rho(t):
    return mp.cos(t)/(1 + mp.sin(t))

def C(d, N):
    if N == 0:
        if d == 0: return mp.mpf('0.5')
        if d % 2 == 0: return mp.mpc(0)
        return 1j/(mp.pi*d)
    if d+N & 1:
        return 1j/mp.pi*mp.quad(lambda t: mp.sin(d*t)*rho(t)**N, [0, mp.pi/4, mp.pi/2])
    return 1/mp.pi*mp.quad(lambda t: mp.cos(d*t)*rho(t)**N, [0, mp.pi/4, mp.pi/2])

count = 0
for N in range(0, 14):
    for d in range(-22,23):
        v = C(d,N)
        zero = (N == 0 and d != 0 and d % 2 == 0) or (N > 0 and d == 0 and N % 2 == 1)
        if zero:
            assert abs(v) < mp.mpf('1e-47'), (d,N,v)
        elif N == 0:
            if d == 0: assert abs(v-mp.mpf('0.5')) < mp.mpf('1e-48')
            else: assert mp.im(v)*d > 0
        elif (d+N)%2 == 0:
            assert abs(mp.im(v)) < mp.mpf('1e-48')
            assert mp.re(v) > mp.mpf('1e-22'), (d,N,v)
        else:
            assert abs(mp.re(v)) < mp.mpf('1e-48')
            assert mp.im(v)*d > mp.mpf('1e-22'), (d,N,v)
        count += 1

for N in range(1,10):
    # Symmetry K(d,N) = +/- conjugate K(d,N) and horizontal reflection.
    for d in range(0,18):
        assert abs(C(-d,N)-mp.conj(C(d,N))) < mp.mpf('1e-42')
        count += 1
print(f'PASS {count} finite numerical classifications and symmetry checks')
