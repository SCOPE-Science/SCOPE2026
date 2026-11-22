"""Reproduce algebra for the one-site noisy integrated-Wiener design theorem.
Run with Python 3 and SymPy. All crucial identities are exact rational polynomials.
Numerical root evaluations are illustrations, not substitutes for global proofs.
"""
from fractions import Fraction
import sympy as sp

t, s, eta = sp.symbols('t s eta', real=True)
K_left = s**2*(3*t-s)/6
K_right = t**2*(3*s-t)/6
C = sp.factor(sp.integrate(K_left**2, (s,0,t)) + sp.integrate(K_right**2,(s,t,1)))
assert sp.factor(C-t**4*(105-105*t+35*t**2-2*t**3)/1260)==0
D=t**3/3
H=2*t**3-30*t**2+75*t-60
U=8*t**3-105*t**2+210*t-105
F=2*t**3-35*t**2+105*t-105
G=4*t**3-45*t**2+75*t-30
assert sp.factor(sp.diff(C,t)+t**3*H/180)==0
eta_star=sp.factor(C*sp.diff(D,t)/sp.diff(C,t)-D)
assert sp.factor(eta_star+t**3*U/(21*H))==0
assert sp.factor(sp.diff(eta_star,t)+2*t**2*F*G/(7*H**2))==0
assert sp.factor(G-(4*t**3+15*(1-t)*(3*t-2)))==0
assert sp.factor(sp.diff(H,t)-(6*t**2-60*t+75))==0
assert sp.factor(sp.diff(U,t)-(24*t**2-210*t+210))==0
assert sp.factor(sp.diff(F,t)-(6*t**2-70*t+105))==0
assert U.subs(t,sp.Rational(2,3))<0 and U.subs(t,1)>0
assert H.subs(t,1)==-13 and F.subs(t,1)==-33
assert eta_star.subs(t,1)==sp.Rational(8,273)
assert sp.diff(eta_star,t).subs(t,1)==sp.Rational(264,1183)
assert C.subs(t,1)==sp.Rational(11,420)
assert sp.diff(C,t).subs(t,1)==sp.Rational(13,180)
R=sp.Rational(1,12)-C/(D+eta)
assert sp.factor(sp.diff(R,t)+sp.diff(C,t)*(eta-eta_star)/(D+eta)**2)==0
# Ordinary Brownian motion comparison (not the same integrated-Wiener process).
C_B=sp.integrate(s**2,(s,0,t))+(1-t)*t**2
assert sp.factor(C_B-(t**2-2*t**3/3))==0
assert sp.factor(sp.diff(C_B/(t+eta),t) + t*(4*t**2+(6*eta-3)*t-6*eta)/(3*(t+eta)**2))==0
assert sp.factor(sp.diff(C_B/(t+eta),t).subs(t,1)+1/(3*(1+eta)**2))==0
for noise in [sp.Rational(1,1000), sp.Rational(1,100), sp.Rational(8,273),sp.Rational(1,10)]:
    poly=sp.together(sp.diff(R,t)).as_numer_denom()[0]
    roots=[complex(x) for x in sp.nroots(poly.subs(eta,noise),maxsteps=200)]
    within=[z.real for z in roots if abs(z.imag)<1e-9 and 0.7<z.real<1.0]
    print('eta',noise, 'interior stationary points:',within)
print('Exact identities passed; global sign proof is in RESULT.md.')
