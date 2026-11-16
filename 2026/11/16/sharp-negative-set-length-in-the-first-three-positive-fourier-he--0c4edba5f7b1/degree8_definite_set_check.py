"""Exact identities and independent numerical checks for the finite Hermite sign-set theorem.

Requires Python 3, sympy and numpy. Every infinite/global conclusion is proved
analytically in RESULT.md; finite computations only check its algebraic reductions.
"""
import math
import sympy as sp
import numpy as np

z, r, u, t = sp.symbols('z r u t', real=True)
alpha = -sp.Rational(1, 2)
L0 = sp.assoc_laguerre(0, alpha, z)
L2 = sp.assoc_laguerre(2, alpha, z)
L4 = sp.assoc_laguerre(4, alpha, z)
S = sp.expand(L4 + r * L2 - (L4.subs(z, 0) + r * L2.subs(z, 0)) * L0)
q = 2*z**3-28*z**2+(105+24*r)*z-105-72*r
assert sp.simplify(S-z*q/48)==0
r0 = -sp.Rational(35, 24)
assert sp.factor(q.subs(r, r0)) == 2*z*(z*z-14*z+35)
assert sp.factor(S.subs(r, r0)) == z*z*(z*z-14*z+35)/24
assert q.subs(z,3) == 12

# Fourier transform of (2*pi*x*x)^k exp(-pi*x*x) is
# (-1)^k 2^(-k) H_(2k)(sqrt(pi)*xi) exp(-pi*xi*xi).
y = 2*sp.pi*u*u
p = z*z*(z*z-14*z+35)
c = sp.Poly(p,z)
fourier = sp.expand(sum(c.nth(k)*(-1)**k*sp.hermite(2*k,sp.sqrt(sp.pi)*u)/2**k for k in range(5)))
assert sp.expand(fourier - p.subs(z,y))==0

D = sp.factor(sp.discriminant(q,z))
assert sp.simplify(D + 12*(9216*r**3-15168*r**2+16128*r-7105))==0
F = 9216*r**3-15168*r**2+16128*r-7105
assert sp.discriminant(sp.diff(F,r),r)<0
assert F.subs(r,0)<0<F.subs(r,1)
P = 2*z**3-23*z**2+84*z-105
assert sp.simplify(sp.diff(P,z)-2*(z-3)*(3*z-14)) == 0
assert P.subs(z,3)<0 and P.subs(z,sp.Rational(14,3))<0
assert sp.simplify(P.subs(z,sp.sqrt(35))) == -910+154*sp.sqrt(35)
assert 154**2*35>910**2

# Implicit derivative of a root y(r) and concavity certificate for sqrt(y(r)).
R = sp.solve(q,r)[0]
qy = sp.simplify(sp.diff(q,z).subs(r,R))
d1 = sp.factor(-sp.diff(q,r)/qy)
d2 = sp.factor(-(sp.diff(q,z,2)*d1**2+2*sp.diff(q,z,r)*d1)/qy)
H = 6*z**4-65*z**3+261*z**2-441*z+315
assert sp.simplify(2*z*d2-d1*d1+144*(z-3)**3*H/P**3)==0

# Strict positivity of H via exact Bernstein-positive subdivisions on [0,3]
# and a positive-power expansion on [3,infinity).
def bernstein_coefficients(poly, lo, hi, deg=4):
    v = sp.Poly(sp.expand(poly.subs(z,lo+(hi-lo)*t)),t)
    return [sp.simplify(sum(v.nth(i)*sp.binomial(k,i)/sp.binomial(deg,i) for i in range(k+1))) for k in range(deg+1)]
assert bernstein_coefficients(H,0,2)==[315,sp.Rational(189,2),48,sp.Rational(91,2),53]
assert bernstein_coefficients(H,2,3)==[53,sp.Rational(227,4),63,sp.Rational(135,2),72]
assert sp.expand(H.subs(z,t+3))==6*t**4+7*t**3+18*t+72

# Closed-form negative interval and length at the extremizer.
root_lo=7-sp.sqrt(14)
root_hi=7+sp.sqrt(14)
assert sp.simplify((sp.sqrt(root_hi)-sp.sqrt(root_lo))**2 - (14-2*sp.sqrt(35)))==0
m_exact = 2*sp.sqrt((7-sp.sqrt(35))/sp.pi)
assert abs(float(m_exact)-1.1747723539032928)<1e-13
assert sp.sqrt(6/sp.pi)>m_exact

# Independent root-count and set-length checks for representative parameters.
def numeric_negative_set_measure(rr):
    roots = np.roots([2.,-28.,105.+24.*rr,-105.-72.*rr])
    cuts=[0.]+sorted(float(v.real) for v in roots if abs(v.imag)<1.e-7 and v.real>0.)+[float('inf')]
    length=0.
    for a,b in zip(cuts[:-1],cuts[1:]):
        probe=a+1. if math.isinf(b) else (a+b)/2.
        if np.polyval([2.,-28.,105.+24.*rr,-105.-72.*rr],probe)<0:
            assert not math.isinf(b)
            length+=math.sqrt(b)-math.sqrt(a)
    return math.sqrt(2/math.pi)*length
v0=float(m_exact)
for rr in [-100,-10,-3,-2,-1.5,0,0.5,0.70,0.71,0.72,1,10,100]:
    observed=numeric_negative_set_measure(rr)
    assert observed>v0-1.e-8,(rr,observed)
assert abs(numeric_negative_set_measure(-35/24)-v0)<1e-12
print('PASS: 22 exact structural identities and 14 independent numerical configurations')
print('optimal negative-set length:',v0)
print('optimizer: exp(-pi*x*x)*(2*pi*x*x)^2*((2*pi*x*x)^2-14*(2*pi*x*x)+35)')
