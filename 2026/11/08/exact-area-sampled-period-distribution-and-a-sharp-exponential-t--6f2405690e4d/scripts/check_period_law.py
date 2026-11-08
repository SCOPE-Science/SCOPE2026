"""Reproducible algebraic and numerical checks for the area-period distribution.

These computations are finite sanity checks; the theorem rests on the written proof.
"""
import sympy as s
import mpmath as m

X, Y, x, y = s.symbols('X Y x y', real=True)
vx, vy = (1-X**2)*Y, -(1-Y**2)*X
Q = (1-X**2)*(1-Y**2)
H = (1-Q)/2
assert s.expand(s.diff(Q,X)*vx+s.diff(Q,Y)*vy)==0
assert s.expand(s.diff(H,Y)-vx)==0
assert s.expand(-s.diff(H,X)-vy)==0
# Direct physical-time coordinate scaling from xdot=(1-4x²)y,
# ydot=-(1-4y²)x and X=2x,Y=2y (no time rescaling).
assert s.expand(2*(1-4*x**2)*y-vx.subs({X:2*x,Y:2*y}))==0
assert s.expand(-2*(1-4*y**2)*x-vy.subs({X:2*x,Y:2*y}))==0
print('REPLICATOR_FIRST_INTEGRAL_AND_PHYSICAL_TIME_OK')

m.mp.dps=60
for qstr in ['0.9','0.5','0.1','0.001','0.00000001']:
    q=m.mpf(qstr)
    k=m.sqrt(1-q)
    K=m.ellipk(1-q)
    E=m.ellipe(1-q)
    # Numerically integrate a quarter of a periodic orbit.
    quarter=m.quad(lambda angle:1/m.sqrt(1-(1-q)*m.sin(angle)**2),[0,m.pi/2])
    assert m.almosteq(quarter,K,rel_eps=m.mpf('1e-45'))
    # Convolution density integrated from zero by q*s parametrization.
    area_cdf=m.quad(lambda v:q*m.ellipk(1-q*v)/2,[m.mpf('1e-50'),1])
    area_formula=1-E+q*K
    assert m.almosteq(area_formula,area_cdf,rel_eps=m.mpf('1e-36'))
    t=4*K
    two_term=(2*t+4)*m.exp(-t/2)
    if q<m.mpf('0.001'):
        assert abs(area_formula/two_term-1)<m.mpf('0.003')
    print('Q',qstr,'T',m.nstr(t,12),'AREA_CDF',m.nstr(area_formula,12),'ASYMPTOTIC_RATIO',m.nstr(area_formula/two_term,12))
print('REPLICATOR_AREA_PERIOD_CDF_AND_TAIL_OK')
