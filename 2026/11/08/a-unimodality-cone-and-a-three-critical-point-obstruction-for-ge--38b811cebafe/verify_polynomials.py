"""Exact algebraic checks for the four-periodic trial-bound unimodality theorem.

Run: python verify_polynomials.py (requires SymPy).
The theorem uses the displayed positivity argument, not numerical testing.
"""
from fractions import Fraction
import sympy as sp

z,u,b=sp.symbols('z u b', real=True)
D=u**2

def G(k):
    return sp.expand(z**k*((2*k+1)-(2*k+3)*z+D*z**4*((7-2*k)-(5-2*k)*z)))

def W(P,Q):
    return sp.expand(sp.diff(P,z)*Q-P*sp.diff(Q,z))

Q_A=(u**3*z**8-6*u**3*z**7-3*u**3*z**6
    +15*u**2*z**6-18*u**2*z**5-21*u**2*z**4
    +63*u*z**4-90*u*z**3+35*u*z**2+81*z**2-78*z+21)
Q_13=3*D*z**6-6*D*z**5-5*D*z**4+45*z**2-58*z+21
Q_23=D*z**6-6*D*z**5-3*D*z**4+63*z**2-90*z+35
checks = [
 -W(G(0)+u*G(2),G(3))-z**2*(1-D*z**4)*Q_A,
 -W(G(1),G(3))-2*z**3*(1-D*z**4)*Q_13,
 -W(G(2),G(3))-z**4*(1-D*z**4)*Q_23,
 Q_A.subs(u,0)-3*(27*z**2-26*z+7),
 Q_A.subs(u,1)-(1-z)**3*(21-15*z+8*z**2+3*z**4-z**5),
 Q_13.subs(u,1)-(1-z)**3*(21+5*z-3*z**2-3*z**3),
 Q_23.subs(u,1)-(1-z)**3*(35+15*z+3*z**2-z**3),
 sp.diff(Q_A,u,2)-(6*u*z**6*(z**2-6*z-3)+6*z**4*(5*z**2-6*z-7)),
]
for i,x in enumerate(checks,1):
    assert sp.expand(x)==0, f'identity {i}'

a=sp.Rational(1,1000)
b0=sp.Rational(1,1000)
c=sp.Rational(73,100)
d0=sp.Rational(49,50)
trial_G=sum(t*z**k*((2*k+1)-(2*k+3)*z+d0*z**4*((7-2*k)-(5-2*k)*z))
            for k,t in enumerate((1,a,b0,c)))
points=(sp.Rational(1,2),sp.Rational(3,5),sp.Rational(3,4),sp.Rational(9,10))
values=[sp.factor(trial_G.subs(z,p)) for p in points]
assert all(v!=0 for v in values)
assert [sp.sign(v) for v in values]==[1,-1,1,-1]
print('FOUR_PERIOD_TRIAL_EXACT_OK',len(checks),'identities',len(values),'rational sign certificates')
for p,v in zip(points,values):
    print(str(p),str(v))
