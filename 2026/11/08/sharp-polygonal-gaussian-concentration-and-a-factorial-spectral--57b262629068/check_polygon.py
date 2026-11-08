#!/usr/bin/env python3
"""Independent symbolic and numerical checks for the polygonal Fock localization theorem.

Dependencies: Python 3, sympy, mpmath. Numerical tests illustrate, but do not prove,
the spectral assertions for infinitely many polygon sides.
"""
from __future__ import annotations
import math
import mpmath as mp
import sympy as sp

checks = 0

def check(ok, what):
    global checks
    assert bool(ok), what
    checks += 1

# Formal angular expansion: u is uniform on [-1,1], h=pi/N.
h, u, a = sp.symbols('h u a', real=True)
q = sp.series((h / sp.tan(h)) / sp.cos(h*u)**2, h, 0, 10).removeO()
check(sp.simplify(sp.integrate(q, (u, -1, 1))/2 - 1) == 0,
      'exact-area identity through order eight')
X=a*(q-1)
E=sp.series(sum((-X)**j/sp.factorial(j) for j in range(5)),h,0,10).removeO().expand()
expected = {
    0: sp.Integer(1), 2: sp.Integer(0),
    4: sp.Rational(2,45)*a**2,
    6: sp.Rational(4,2835)*a**2*(15-2*a),
    8: sp.Rational(2,14175)*a**2*(5*a*a-28*a+63),
}
for k, target in expected.items():
    got = sp.integrate(E.coeff(h,k), (u,-1,1))/2
    check(sp.simplify(got-target) == 0, f'h^{k} coefficient')
for k in (1,3,5,7,9):
    check(sp.simplify(E.coeff(h,k)) == 0, f'odd coefficient h^{k}')
check(sp.simplify(sp.integrate((u*u-sp.Rational(1,3))*sp.cos(sp.pi*u),(u,-1,1))/2 + 2/sp.pi**2)==0,
      'first Fock coupling Fourier coefficient')

mp.mp.dps = 65

def polygon_data(A, N):
    A=mp.mpf(A); N=int(N); h0=mp.pi/N
    s=lambda y: A*h0/mp.tan(h0)/mp.cos(h0*y)**2
    mass=1-mp.quad(lambda y: mp.exp(-s(y)),[-1,0,1])/2
    deficit=1-mp.exp(-A)-mass
    c4=2*A*A/45
    c6=4*A*A*(15-2*A)/2835
    c8=2*A*A*(5*A*A-28*A+63)/14175
    approximation=mp.exp(-A)*(c4*h0**4+c6*h0**6+c8*h0**8)
    return mass, deficit, approximation, s

for A in (mp.mpf('.5'), mp.mpf('2'), mp.mpf('9')):
    ratios=[]
    for N in (10,20,40,80):
        mass, deficit, approx, _ = polygon_data(A,N)
        h0=mp.pi/N
        ratio=deficit/(mp.exp(-A)*(2*A*A/45)*h0**4)
        ratios.append(abs(ratio-1))
        check(0<mass<1-mp.exp(-A), f'mass optimality test A={A}, N={N}')
        check(abs(deficit-approx)/h0**10 < mp.mpf('0.005'),
              f'order-ten remainder test A={A}, N={N}')
        check(abs(ratio-1)<mp.mpf('.07'), f'leading deficit test A={A}, N={N}')
    check(ratios[-1] < ratios[0], f'fourth order convergence A={A}')

for A in (mp.mpf('.7'),mp.mpf('2')):
    for N in (10,16,24,32):
        mass, _, _, S = polygon_data(A,N)
        sqf=mp.sqrt(mp.factorial(N))
        # Angular Fourier coefficient after subtracting the disk's zero mode.
        v=mp.quad(lambda y: mp.cos(mp.pi*y)*mp.gammainc(mp.mpf(N)/2+1,A,S(y)),
                  [-1,0,1])/(2*sqf)
        vpred=-2*mp.exp(-A)*A**(mp.mpf(N)/2+1)/(N*N*sqf)
        check(v<0, f'negative leading coupling A={A}, N={N}')
        check(abs(v/vpred-1)<mp.mpf('.065'),
              f'factorial Fock-coupling asymptotic A={A}, N={N}')

# Two-mode compression checks the beyond-all-orders correction quantitatively.
A=mp.mpf('2')
for N in (10,16,24):
    mass,_,_, S=polygon_data(A,N)
    sqf=mp.sqrt(mp.factorial(N))
    b=mp.quad(lambda y:mp.gammainc(N+1,0,S(y))/mp.factorial(N),
              [-1,0,1])/2
    v=mp.quad(lambda y:mp.cos(mp.pi*y)*mp.gammainc(mp.mpf(N)/2+1,A,S(y)),
              [-1,0,1])/(2*sqf)
    topgain=2*v*v/(mass-b+mp.sqrt((mass-b)**2+4*v*v))
    predicted=4*mp.exp(-2*A)*A**(N+2)/(N**4*mp.factorial(N)*(1-mp.exp(-A)))
    check(topgain>0, f'positive spectral gain at N={N}')
    check(abs(topgain/predicted-1)<mp.mpf('.09'),
          f'sharp beyond-all-orders coefficient at N={N}')
print('POLYGON_FOCK_CHECKS_PASS',checks)
