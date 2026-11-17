"""Reproducibility checks for an algebraic-cycle area law.

Dependencies: Python 3.10+, sympy, mpmath. Finite checks do not replace proofs.
"""
import math
import sympy as sp
import mpmath as mp

x, y, a = sp.symbols('x y a')
f = sp.Rational(1,4) + x-x*x + a*x**3 + x*y + x*x*y*y
P = 2*(1+2*x-2*a*x*x+6*x*y)
Q = 8-3*a-14*a*x-2*a*x*y-8*y*y
cofactor = 4*(2-3*a*x+2*y)
assert sp.expand(P*sp.diff(f,x)+Q*sp.diff(f,y)-cofactor*f) == 0

mp.mp.dps = 70

def area_forms(aval):
    aa = mp.mpf(aval)
    al = (1-mp.sqrt(1-4*aa))/2
    be = (1+mp.sqrt(1-4*aa))/2
    m = 1-al/be
    exact = (4*be**mp.mpf('1.5')/(3*aa))*((2-m)*mp.ellipe(m)-2*(1-m)*mp.ellipk(m))
    area_by_slice = (2/aa)*mp.quad(lambda t:
        mp.sqrt((be-al)*(1-t)*(be-al)*t/(al+(be-al)*t))*(be-al),
        [0, mp.mpf('0.5'), 1])
    return exact, area_by_slice

for aa in ['0.01','0.04','0.11','0.20','0.245']:
    area, quad = area_forms(aa)
    assert abs(area-quad) < mp.mpf('1e-50')*max(1, abs(area))

for aa in ['0.00001','0.000001','0.0000001']:
    area, _ = area_forms(aa)
    a0 = mp.mpf(aa)
    approx = 4/(3*a0) + mp.log(a0)-1-mp.log(16)
    assert abs(area-approx) < 8*a0*abs(mp.log(a0))

for delta in ['0.001','0.0001','0.00001']:
    d = mp.mpf(delta)
    area, _ = area_forms(mp.mpf('0.25')-d)
    normalized = area/(4*mp.sqrt(2)*mp.pi*d)
    assert abs(normalized-1) < 5*d

assert area_forms('0.01')[0] > area_forms('0.1')[0] > area_forms('0.2')[0]
print('CLS_QUARTIC_ELLIPTIC_AREA_CHECK_OK')
