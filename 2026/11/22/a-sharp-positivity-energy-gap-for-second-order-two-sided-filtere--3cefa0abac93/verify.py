#!/usr/bin/env python3
"""Exact algebraic checks for the three-site SSP-EIN2 positivity frontier.

Requires Python 3, SymPy and NumPy. No external data, services or files.
Finite samples below are diagnostics; the proof is the algebraic sign argument
in RESULT.md, not numerical sampling.
"""
import sympy as S
import numpy as np

z, rho = S.symbols('z rho', real=True, positive=True)
q = lambda t: 16*t*(1+t)**2/(2+t)**4
q1,q3=q(z),q(3*z)
alpha= (S.Integer(107)+51*S.sqrt(17))/512
zmax=(3+S.sqrt(17))/2
assert S.simplify(S.diff(q(z),z)+16*(z+1)*(z*z-3*z-2)/(z+2)**5)==0
assert S.simplify(q(zmax)-2*alpha)==0

# Derivation of the three-vertex nonlocal entry.
W1,W3=rho*q1,rho*q3
G1,G3=1-W1+W1**2/2,1-W3+W3**2/2
T13=S.factor((2-3*G1+G3)/6)
assert S.simplify(6*T13-(3*(W1-W1**2/2)-(W3-W3**2/2)))==0
assert S.simplify((3*q1-q3) - 192*z**3*(3*z+4)*(6*z**3+17*z**2+16*z+4)/((z+2)**4*(3*z+2)**4))==0

Mpoly=S.Poly(3159*z**12+28512*z**11+114210*z**10+261936*z**9+363279*z**8+275520*z**7+28560*z**6-165888*z**5-179296*z**4-93184*z**3-26880*z**2-4096*z-256,z)
assert S.simplify(3*q1**2-q3**2-1536*z**2*Mpoly.as_expr()/((z+2)**8*(3*z+2)**8))==0

R=S.factor(2*(3*q1-q3)/(3*q1**2-q3**2))
Rclosed=z*(z+2)**4*(3*z+2)**4*(3*z+4)*(6*z**3+17*z**2+16*z+4)/(4*Mpoly.as_expr())
assert S.simplify(R-Rclosed)==0

Ppoly=S.Poly(85293*z**18+857304*z**17+3216348*z**16+2103894*z**15-30456891*z**14-156491298*z**13-437380110*z**12-847556556*z**11-1222989168*z**10-1350183024*z**9-1150054752*z**8-755005824*z**7-380042496*z**6-145907712*z**5-42588672*z**4-9387008*z**3-1511424*z**2-159744*z-8192,z)
# Differentiate and verify sign of the derivative exactly; no approximate roots needed.
assert S.simplify(S.diff(R,z)/Ppoly.as_expr()-(z+2)**3*(3*z+2)**3/(2*Mpoly.as_expr()**2))==0

def variations(poly):
    cs=[S.sign(c) for c in poly.all_coeffs() if c!=0]
    return sum(a!=b for a,b in zip(cs,cs[1:]))
assert variations(Mpoly)==1
assert Mpoly.eval(0)<0 and Mpoly.eval(1)>0
assert variations(Ppoly)==1
assert Ppoly.eval(3)<0 and Ppoly.eval(4)>0
assert Mpoly.eval(3)>0

# Sharp rational counterexample inside the unconditional energy-stability range.
zw=S.Rational(4); rw=S.Rational(3,2)
w1,w3=rw*q(zw),rw*q(3*zw)
assert (w1,w3)==(S.Rational(50,27), S.Rational(3042,2401))
T13_w=S.factor(T13.subs({z:zw,rho:rw}))
assert T13_w == -S.Rational(37010590,4202539929)
assert S.simplify(rw*alpha-1)<0

# Independent exact matrix check by two-stage filtered Heun using resolvents.
L=S.Matrix([[1,-1,0],[-1,2,-1],[0,-1,1]])
J=(S.eye(3)+zw*L/2).inv()
Filter=2*J-J*J
B=rw*zw*Filter*L*Filter
Heun=S.eye(3)-B+B*B/2
assert S.factor(Heun[0,2])==T13_w
assert (L*S.ones(3,1))==S.zeros(3,1)
assert Heun*S.ones(3,1)==S.ones(3,1)
assert Heun==Heun.T

# Useful float checks of the root and value, not a uniqueness proof.
from scipy.optimize import brentq
zs=brentq(lambda t: float(Ppoly.eval(t)/t**18),3.0,4.0,xtol=1e-13)
rstar=float(Rclosed.subs(z,zs))
assert 3.84702<zs<3.84703
assert 1.480920<rstar<1.480922
assert float(alpha)<1/rstar
assert 1/rstar<0.676

# Diagnostic parameter/step grid in energy-stable region.
rg=np.random.default_rng(221802)
for _ in range(2000):
    zz=10**rg.uniform(-4,4)
    rr=rg.uniform(1e-7,float(1/alpha))
    b1=rr*float(q(zz)); b3=rr*float(q(3*zz))
    g1=1-b1+b1*b1/2;g3=1-b3+b3*b3/2
    T=np.array([[1/3+g1/2+g3/6, (1-g3)/3, (2-3*g1+g3)/6],
                [(1-g3)/3,1/3+2*g3/3,(1-g3)/3],
                [(2-3*g1+g3)/6,(1-g3)/3,1/3+g1/2+g3/6]])
    assert np.max(abs(T@np.ones(3)-np.ones(3)))<2e-13
    assert np.max(abs(T-T.T))<2e-13
    assert .5-1e-13<=g1<=1+1e-13 and .5-1e-13<=g3<=1+1e-13
    if rr <=rstar-1e-7: assert T.min()>=-2e-12
print('PASS: exact modal formula, rational witness, 1-sign-change global extrema, 2000 finite matrix diagnostics')
print('critical_z',format(zs,'.14f'),'critical_a_over_s',format(rstar,'.14f'),'critical_s_over_a',format(1/rstar,'.14f'))
print('energy_s_over_a',S.N(alpha,16),'witness_T13',T13_w)
