"""Exact symbolic identities and supplementary finite checks for two-phase BAOAB."""
from fractions import Fraction
import math
import random
import sympy as sp

s, t = sp.symbols('s t', positive=True)
D = 32 - (4-s*t)*(s+t)**2
A_s = 1-s*(s+t)/4
A_t = 1-t*(s+t)/4
V_s = 1 + (s-t)*(s*t*(s+t)+4*(s-t))/D
V_t = 1 - (s-t)*(s*t*(s+t)-4*(s-t))/D
mean = (V_s + V_t)/2

identities = {
    's_step_variance': V_s-A_s**2*V_t-s*s/2-A_s*s*t/2,
    't_step_variance': V_t-A_t**2*V_s-t*t/2-A_t*s*t/2,
    'determinant_factor': 1-A_s**2*A_t**2-(s+t)**2*(4-s*t)*D/256,
    'phase_mean': mean-1-4*(s-t)**2/D,
    'phase_gap': V_s-V_t-2*s*t*(s+t)*(s-t)/D,
    'mixture_kurtosis': sp.Rational(3,4)*(V_s-V_t)**2-3*s*s*t*t*(s+t)**2*(s-t)**2/D**2,
    'weighted_observation_mean': (s*V_s+t*V_t)/(s+t)-1-(s-t)**2*(s*t+4)/D,
}
for name, expression in identities.items():
    assert sp.cancel(expression) == 0, (name, sp.factor(expression))
print('PASS: 7 exact symbolic identities')

for aa,bb,vs,vt,va in [
    (1, Fraction(1,2), Fraction(204,193),Fraction(198,193),Fraction(201,193)),
    (1, Fraction(4,5), Fraction(345,338),Fraction(168,169),Fraction(681,676)),
]:
    z = {s:sp.Rational(aa), t:sp.Rational(bb)}
    assert sp.simplify(V_s.subs(z)-sp.Rational(vs.numerator,vs.denominator)) == 0
    assert sp.simplify(V_t.subs(z)-sp.Rational(vt.numerator,vt.denominator)) == 0
    assert sp.simplify(mean.subs(z)-sp.Rational(va.numerator,va.denominator)) == 0
print('PASS: 6 exact rational phase moments')

# Independently implement the original BAOAB linear update as a 2x2 map;
# matrix composition does not reuse the scalar-variance recursions.
def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def mt(a):
    return [[a[j][i] for j in range(2)] for i in range(2)]
def step(h,cov):
    B=[[1.,0.],[-h/2.,1.]]
    A=[[1.,h/2.],[0.,1.]]
    O=[[1.,0.],[0.,0.]]
    M=mm(B,mm(A,mm(O,mm(A,B))))
    noise=[h/2.,1.-h*h/4.]
    temp=mm(M,mm(cov,mt(M)))
    return [[temp[i][j]+noise[i]*noise[j] for j in range(2)] for i in range(2)]

rng = random.Random(300219)
for i in range(120):
    aa = rng.uniform(.25,1.75)
    bb = rng.uniform(.25,1.75)
    cov=[[0.,0.],[0.,0.]]
    for _ in range(500):
        cov_s=step(aa,cov)
        cov=step(bb,cov_s)
    x,y=float(V_s.subs({s:aa,t:bb})),float(V_t.subs({s:aa,t:bb}))
    assert abs(cov_s[0][0]-x)<2e-9,(i,'s',cov_s[0][0],x)
    assert abs(cov[0][0]-y)<2e-9,(i,'t',cov[0][0],y)
print('PASS: 120 direct 2x2 matrix-covariance comparisons')

for i in range(15000):
    aa = rng.uniform(1e-4,2-1e-4)
    bb = rng.uniform(1e-4,2-1e-4)
    d=32-(4-aa*bb)*(aa+bb)**2
    r=4*(aa-bb)**2/d
    assert d>0
    assert 0 <= r < 1+1e-10, (i,aa,bb,d,r)
    if aa != bb: assert r>0
print('PASS: 15,000 finite-domain supplementary inequalities')
print('All checks passed. Global bounds and uniqueness are proved analytically in RESULT.md.')
