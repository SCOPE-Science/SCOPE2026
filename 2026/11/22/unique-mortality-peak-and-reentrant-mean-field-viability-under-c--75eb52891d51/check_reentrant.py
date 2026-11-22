#!/usr/bin/env python3
"""Independent arithmetic witnesses for the clipped-Gaussian mortality theorem.

Analytic uniqueness follows from the one-sign-change integral in RESULT.md;
this script checks the stated exact rational bounds and optional quadrature diagnostics.
"""
from fractions import Fraction as F
from math import factorial

x = F(71,100)
q = F(1,100)
A = F(18,25)
cl, cu = F(39894,100000), F(39895,100000)
pi_lo, pi_hi = F(314159,100000), F(314160,100000)
assert 2*pi_hi*cl*cl < 1 < 2*pi_lo*cu*cu

# Alternating Gaussian-integral Maclaurin bounds on [0,x].
def partial(n):
    return sum(((-1)**k)*x**(2*k+1)/F(2**k*factorial(k)*(2*k+1)) for k in range(n+1))
Jlower, Jupper = partial(3), partial(2)
assert Jlower < Jupper
p_lower, p_upper = F(1,2)-cu*Jupper, F(1,2)-cl*Jlower
assert F(238,1000)<p_lower<p_upper<F(240,1000)

u = x*x/2
phi_upper = cu*(1-u+u*u/2)
assert phi_upper < F(312,1000)

# Jensen on the Gaussian tail conditioned on A+Z>q.
B = (F(238,1000)/(1+q)
     + F(760,1000)**2/((1+A)*F(762,1000)+F(312,1000)))
assert B==F(6059777,10242915)
assert B>F(59,100)
# 2-sqrt(2)<59/100; no floating calculations in these comparisons.
assert F(141,100)**2<2
assert F(25,43)<F(585,1000)  # noiseless below critical
assert F(50,101)<F(585,1000) # large-noise limit below critical
assert (2-F(25,43))**2>2 and (2-F(50,101))**2>2
print('PASS: exact Gaussian probability bounds, conditional-Jensen witness, and endpoint regimes')
print('Certified lower bound for mortality at sigma=1:',str(B),'=',float(B))

try:
    import mpmath as mp
    mp.mp.dps = 40
    eps = mp.mpf(1)/100; a=mp.mpf(18)/25
    c=2-mp.sqrt(2)
    def death(s):
        k=(eps-a)/s
        normal=lambda z: mp.exp(-z*z/2)/mp.sqrt(2*mp.pi)
        return mp.ncdf(k)/(1+eps)+mp.quad(lambda z: normal(z)/(1+a+s*z),[k,0,mp.inf])
    r1=mp.findroot(lambda s:death(s)-c,(mp.mpf('.13'),mp.mpf('.17')))
    r2=mp.findroot(lambda s:death(s)-c,(mp.mpf('6'),mp.mpf('7')))
    print('Diagnostic numerical crossover sigma values:',mp.nstr(r1,16),mp.nstr(r2,16))
    assert mp.mpf('.14')<r1<mp.mpf('.16') and mp.mpf('6')<r2<mp.mpf('7')
    print('PASS: supplementary high-precision quadrature')
except ImportError:
    print('mpmath unavailable: optional quadrature skipped; exact witness passed')
