#!/usr/bin/env python3
"""Exact symbolic and independent numerical checks for a biquadratic shear-map frequency law.

SymPy supplies polynomial identities; mpmath checks the integral against the closed form.
The analytic monotonicity argument and measure-theoretic scope are in RESULT.md.
"""
import sympy as S
from mpmath import mp

y, a, u, z, t = S.symbols('y a u z t', real=True)
e = S.symbols('e', positive=True)
P = lambda v, ep: a*(1-v**2)*(1-ep*v**2)
# The angular increment and transformed kick under (x,y)->(x,e*y).
assert S.simplify(P(y,e**2)-P(e*y,e**-2)) == 0
assert S.simplify(e*(y-t)- (e*y-e*t)) == 0
# Quadratic depth in u and uniform-action density.
y2 = 1 + (1-e**2)*u/e**2
Q = S.factor(-P(S.sqrt(y2),e**2)/(a*(e**2-1)**2/(4*e**2)))
assert S.simplify(Q-4*u*(1-u)) == 0
v = 4*(t*t-e*e)*(1-t*t)/(1-e*e)**2
M = S.factor(S.integrate(v,(t,e,1))/(1-e))
M2 = S.factor(S.integrate(v*v,(t,e,1))/(1-e))
V = S.factor(M2-M*M)
mean = 8*(e*e+3*e+1)/(15*(e+1)**2)
variance = 64*(3*e**4+8*e**3+13*e**2+8*e+3)/(1575*(e+1)**4)
assert S.simplify(M-mean)==0
assert S.simplify(V-variance)==0
assert S.simplify(S.diff(mean,e)+8*(e-1)/(15*(e+1)**3))==0
assert S.simplify(S.diff(variance,e)-128*(e-1)*(2*e*e+e+2)/(1575*(e+1)**5))==0
assert S.limit(mean,e,1)==S.Rational(2,3)
assert S.limit(variance,e,1)==S.Rational(4,45)
assert S.limit(mean,e,0)==S.Rational(8,15)
assert S.limit(variance,e,0)==S.Rational(64,525)
assert S.simplify(mean - mean.subs(e,1/e))==0
assert S.simplify(variance - variance.subs(e,1/e))==0
flux=4*a*S.Abs(e-1)**3*(e*e+3*e+1)/(15*e**3)
area=2*S.Abs(1/e-1)
max_speed=a*(e*e-1)**2/(4*e*e)
assert S.simplify(flux-area*max_speed*mean)==0
assert S.limit(flux.subs(a,1)/(e-1)**3,e,1,dir='+')==S.Rational(4,3)
# Numerical area-weighted distribution / survival, independent quadrature.
mp.dps = 50
for ee in ('0.22','0.5','0.81','1.08','1.3','2','4.5'):
    E=mp.mpf(ee)
    lo=min(1,1/E); hi=max(1,1/E)
    def ZZ(yy):
        return 4*E*E*(yy*yy-1)*(1-E*E*yy*yy)/(1-E*E)**2
    em=mp.quad(lambda yy: ZZ(yy),(lo,hi))/(hi-lo)
    ev=mp.quad(lambda yy: ZZ(yy)**2,(lo,hi))/(hi-lo)-em*em
    m_expected=8*(E**2+3*E+1)/(15*(E+1)**2)
    v_expected=64*(3*E**4+8*E**3+13*E**2+8*E+3)/(1575*(E+1)**4)
    assert abs(em-m_expected)<mp.mpf('1e-44')
    assert abs(ev-v_expected)<mp.mpf('1e-44')
    for zz in ('0.03','0.35','0.8'):
        Z=mp.mpf(zz); s=mp.sqrt(1-Z)
        u_lo=(1-s)/2; u_hi=(1+s)/2
        yy1=mp.sqrt((E**2+(1-E**2)*u_lo))/E
        yy2=mp.sqrt((E**2+(1-E**2)*u_hi))/E
        area_mass=abs(yy2-yy1)/(hi-lo)
        A=(1+E**2+(1-E**2)*s)/2
        B=(1+E**2-(1-E**2)*s)/2
        survival=(E+1)*s/(mp.sqrt(A)+mp.sqrt(B))
        assert abs(area_mass-survival)<mp.mpf('1e-44')
print('PASS: reciprocal conjugacy, exact quadratic depth, mean, variance, derivatives, flux, limits and 21 independent quadratures')
