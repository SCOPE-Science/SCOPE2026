#!/usr/bin/env python3
"""Independent checks for nearest-site Brownian resetting cumulant theorem.
Run: python local_reset_positive_kurtosis_checker.py
Requires: mpmath, sympy. Numerical checks are supplementary to the proof.
"""
import mpmath as mp
import sympy as sp
mp.mp.dps = 65
checks = 0

def test(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

x = sp.symbols('x', positive=True)
s = sp.sinh(x); c = sp.cosh(x)
B = sp.cosh(2*x)-1
C1 = x*sp.sinh(x)/2
H1 = x*sp.sinh(2*x)
a = c/(2*B)
b = (c/sp.Integer(24) + (C1+1)*a/2 - H1*a*a)/B
F = 2*s**3 + 6*s - 3*x*s*s - 6*x
# A derived expression and its positive-series form are checked symbolically.
test(sp.simplify(sp.expand_trig(b - c*F/(96*s**5))) == 0,
     'fourth cumulant algebra')
test(sp.simplify(sp.expand_trig(2*F - (sp.sinh(3*x)+9*sp.sinh(x)-3*x*sp.cosh(2*x)-9*x))) == 0,
     'power-series positivity identity')
test(sp.simplify(sp.expand_trig(a - c/(4*s*s))) == 0,
     'quadratic coefficient')
test(sp.limit(b,x,0) == sp.Rational(1,1920),
     'zero-rate coefficient')
G = x*(s*s+2)-2*s
test(sp.simplify(sp.expand_trig(2*G-(x*(sp.cosh(2*x)+3)-4*sp.sinh(x))))==0, 'upper CV bound identity')

# The proof uses: coefficient of x^(2n+1) in 2F, n>=2, is
# (3^(2n+1)+9-3(2n+1)4^n)/(2n+1)! > 0.
for n in range(2,65):
    numerator = 3**(2*n+1) + 9 - 3*(2*n+1)*4**n
    test(numerator > 0, 'series coefficient n=%d' % n)
    test((2*n+1)*4**n-4>0, 'upper CV series n=%d' % n)

# Independent derivatives of the first-passage Laplace transform and implicit
# renewal pole; these tests do not use the closed fourth-cumulant formula.
for alpha in ['0.05','0.3','0.8','1.0','1.606115298802767','2.5','4.0','7.0']:
    z = mp.mpf(alpha); D = mp.mpf(1); ell = mp.mpf(1)
    rate = 4*D*z*z/(ell*ell)
    def lap(v):
        a0 = (ell/2)*mp.sqrt((rate+v)/D)
        return (v+rate*mp.cosh(a0))/(rate*mp.cosh(a0)+v*mp.cosh(2*a0))
    mean = -mp.diff(lap, 0)
    second = mp.diff(lap, 0, 2)
    cv2 = second/mean**2-1
    S = mp.sinh(z); C = mp.cosh(z)
    FF = 2*S**3+6*S-3*z*S*S-6*z
    d_eff = D*z*z*C/S**2
    fourth_rate = rate*ell**4*C*FF/(4*S**5)
    test(mp.mpf(2)/3 < cv2 < 1, 'sharp CV interval at '+alpha)
    test(mp.almosteq(mean, 2*S*S/(rate*C), rel_eps=mp.mpf('1e-50')), 'mean FPT at '+alpha)
    test(mp.almosteq(ell**2/(2*mean),d_eff,rel_eps=mp.mpf('1e-50')), 'diffusivity at '+alpha)
    test(mp.almosteq(ell**4*(3*second-5*mean**2)/(mean**3),fourth_rate,rel_eps=mp.mpf('1e-47')), 'fourth cumulant at '+alpha)
    test(fourth_rate>0, 'strict positive fourth cumulant at '+alpha)
    for h in [mp.mpf('0.01'),mp.mpf('0.03')]:
        # Positive SCGF root from exact renewal equation (not a derivative).
        pole=mp.findroot(lambda v: mp.cosh(h*ell)*lap(v)-1, (d_eff*h*h*mp.mpf('.8'),d_eff*h*h*mp.mpf('1.2')))
        predicted=d_eff*h*h+fourth_rate*h**4/24
        test(abs(pole-predicted) < mp.mpf('3')*h**6, 'tilt pole expansion at '+alpha)

# Check the renewal first passage transform by direct ODE matching, with no
# derivative or use of the cumulant expansion.
for alpha in ['0.25','1','2','4']:
    z = mp.mpf(alpha); rate = 4*z*z
    for s_lap in [mp.mpf('0.2'),mp.mpf('1.3'),mp.mpf('5')]:
        q=mp.sqrt(rate+s_lap); h=mp.mpf('0.5')
        # Interior: u(x)=u(0)[r+s cosh(qx)]/(r+s).
        # Outer: u''-q^2u=-r, u(1)=1. Match u,u' at x=h.
        C=mp.cosh(q*h); H=mp.cosh(2*q*h)
        u0=(s_lap+rate*C)/(rate*C+s_lap*H)
        Bouter=s_lap/(rate+s_lap)*(1+u0)*mp.tanh(q*h)
        ui=u0*(rate+s_lap*C)/(rate+s_lap)
        uo=(rate+s_lap*C)/(rate+s_lap)-Bouter*mp.sinh(q*h)
        di=u0*s_lap*q*mp.sinh(q*h)/(rate+s_lap)
        do=q*(-s_lap*mp.sinh(q*h)/(rate+s_lap)+Bouter*C)
        test(mp.almosteq(ui,uo,rel_eps=mp.mpf('1e-50')),'BVP continuity')
        test(mp.almosteq(di,do,rel_eps=mp.mpf('1e-50')),'BVP flux match')
        test(0<u0<1,'Laplace probability bound')

print('PASS',checks,'independent symbolic, first-passage ODE, Laplace-moment and renewal-pole checks')
