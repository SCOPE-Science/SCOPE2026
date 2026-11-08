"""Standalone algebra and finite trajectory spot-checks for a planar Ricker limit theorem.

Requires Python 3, sympy and mpmath. These checks corroborate, but do not
replace, the all-parameter analytical arguments in RESULT.md.
"""
from fractions import Fraction
import sympy as sp
import mpmath as mp

w = sp.symbols('w')
g = lambda t: t * sp.exp(2 * (1 - t))
G = sp.series(g(g(1 + w)) - 1, w, 0, 7).removeO().expand()
assert sp.simplify(G - (w - sp.Rational(4, 3) * w**3
                            + sp.Rational(8, 15) * w**5
                            + sp.Rational(4, 9) * w**6)) == 0
print('PASS: exact sixth-order second-iterate Taylor coefficients')

for alpha, beta in [(Fraction(1,4), Fraction(3,5)),
                    (Fraction(4,5), Fraction(1,5)),
                    (Fraction(1,5), Fraction(3,7))]:
    u = 2*(1-alpha)/(1-alpha*beta)
    v = 2*(1-beta)/(1-alpha*beta)
    c = u*(1-beta)
    assert u+alpha*v == 2 and beta*u+v == 2
    assert c == v*(1-alpha) and 0 < c < 2
    if (alpha, beta) == (Fraction(1, 5), Fraction(3, 7)):
        assert c == 1  # Exact transverse supergeometric-resonance curve.
print('PASS: exact rational equilibrium and log-difference contraction identities')

mp.mp.dps = 65
for ap,bp,x0,y0 in [('0.25','0.6','0.71','1.51'),
                    ('0.8','0.2','1.4','0.65'),
                    ('0.2',str(mp.mpf(3)/7),'0.81','1.3')]:
    a,b = mp.mpf(ap),mp.mpf(bp)
    u,v = 2*(1-a)/(1-a*b),2*(1-b)/(1-a*b)
    x,y = mp.mpf(x0),mp.mpf(y0)
    snapshots = {}
    for n in range(14001):
        if n in (4000, 8000, 14000):
            m=n//2
            dx=x/u-1
            dy=y/v-1
            assert dx != 0 and dy != 0
            snapshots[n] = (m*dx**2,
                            1/dx**2-mp.mpf(8)*m/3-mp.mpf(8)/5*mp.log(m),
                            abs(x/u-y/v))
        if n<14000:
            x,y=x*mp.exp(2-x-a*y),y*mp.exp(2-y-b*x)
    rate = snapshots[14000][0]
    assert abs(rate-mp.mpf(3)/8) < mp.mpf('0.0025'), (ap,bp,rate)
    assert abs(snapshots[14000][1]-snapshots[8000][1]) < mp.mpf('0.06'), (ap,bp,snapshots)
    assert snapshots[14000][2] < mp.mpf('1e-25'), (ap,bp,snapshots[14000][2])
    print(f'PASS: asymmetric pair ({ap}, {bp}): m*w^2 = {float(rate):.9f}, '
          f'residual change = {float(snapshots[14000][1]-snapshots[8000][1]):.9f}')
print('PASS: 3 long high-precision asymmetric orbit tests')
