"""Reproducible ancillary checks for a Gaussian-weighted even Fock function.

The all-parameter classification follows from the analytic proof in RESULT.md;
these tests validate derivative algebra, root locations, and representative signs.
"""
import math

import sympy as sp
from scipy.optimize import brentq

x, y, a = sp.symbols('x y a', real=True, positive=True)
L = -x*x-y*y + sp.log((sp.cosh(2*a*x)+sp.cos(2*a*y))/2)
assert sp.simplify(sp.diff(L,x) - (-2*x + 2*a*sp.sinh(2*a*x)/(sp.cosh(2*a*x)+sp.cos(2*a*y)))) == 0
assert sp.simplify(sp.diff(L,y) - (-2*y - 2*a*sp.sin(2*a*y)/(sp.cosh(2*a*x)+sp.cos(2*a*y)))) == 0
assert sp.simplify(sp.diff(L,x,y).subs(x, 0)) == 0
assert sp.simplify(sp.diff(L,x,y).subs(y, 0)) == 0
assert sp.simplify(sp.diff(L,x,x).subs({x:0,y:0}) - 2*(a*a-1)) == 0
assert sp.simplify(sp.diff(L,y,y).subs({x:0,y:0}) + 2*(a*a+1)) == 0
assert sp.series(-x*x+2*sp.log(sp.cosh(x)),x,0,6).removeO().expand() == -x**4/sp.Integer(6)

checks = 7
for av in (0.5, 1.0, 1.4, 2.3):
    if av > 1:
        xr = brentq(lambda xx: av*math.tanh(av*xx)-xx, 1e-6, av)
        assert 0 < xr < av
        assert -2+2*av*av/(math.cosh(av*xr)**2) < 0
        assert -2-2*av*av/(math.cosh(av*xr)**2) < 0
        checks += 3
    for k in range(5):
        left=(k+0.5)*math.pi/av
        right=(k+1)*math.pi/av
        # Avoid cancellation at the tangent pole by a strict interior bracket.
        yl=left+1e-7/av
        yr=right-1e-7/av
        yr0=brentq(lambda yy: yy+av*math.tan(av*yy),yl,yr)
        assert left<yr0<right
        assert abs(yr0+av*math.tan(av*yr0))<1e-7
        assert av*av+yr0*yr0-1>0
        assert -1-av*av-yr0*yr0<0
        checks += 4

ap=1+1e-5
xp=brentq(lambda xx: ap*math.tanh(ap*xx)-xx,1e-7,ap)
assert abs(xp/math.sqrt(6*(ap-1))-1)<0.0002
checks+=1
print(f'EVEN_FOCK_MORSE_CHECK_PASS symbolic=7 numeric={checks-7} stationary_axis_roots=20')
