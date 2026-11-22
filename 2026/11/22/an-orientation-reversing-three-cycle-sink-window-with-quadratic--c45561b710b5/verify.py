"""Exact algebraic verification of the period-three reduction and stability theorem.
Requires SymPy. Numerical probes are supplementary and not an infinite proof.
"""
import sympy as s
u,c,t,b=s.symbols('u c t b',real=True)
L=s.Symbol('L')
q=lambda x: c-x*x
D=s.cancel((q(q(q(u)))-u)/(q(u)-u))
assert s.denom(D)==1
assert s.factor(s.discriminant(D,u)) == (4*c-7)**3*(16*c*c-4*c+7)**2
C=(t*t+7)/4
Sp=(1+t)/2; Sm=(1-t)/2
Pp=(-t*t+2*t-9)/4; Pm=(-t*t-2*t-9)/4
Qp=(t*t-1-t*(t*t+7))/8; Qm=(t*t-1+t*(t*t+7))/8
Gp=u**3-Sp*u**2+Pp*u-Qp; Gm=u**3-Sm*u**2+Pm*u-Qm
assert s.expand(D.subs(c,C)-Gp*Gm)==0
for G,Q,sign in [(Gp,Qp,1),(Gm,Qm,-1)]:
    assert s.factor(s.discriminant(G,u))==(t*t-sign*t+7)**2
    # q permutes the three roots
    assert s.rem(s.Poly(G.subs(u,C-u*u),u),s.Poly(G,u)).is_zero
    assert s.expand(-8*Q-(8-4*C+sign*4*C*t))==0
A,B,C3=s.symbols('A B C3',real=True)
J=lambda w:s.Matrix([[0,-2*w,-b],[1,0,0],[0,1,0]])
P=J(C3)*J(B)*J(A)
assert s.factor(P.charpoly(L).as_expr()-((L+b)**3+8*L*A*B*C3))==0
M=s.symbols('M')
assert s.factor((L+b)**3-M*L).subs(M,-(1-b*b)**3).expand()==s.expand((L+b**3)*(L**2+(3*b-b**3)*L+1))
# At zero multiplier, the matrix has all Floquet multipliers -b.
assert s.factor(P.det()+b**3)==0
print('PASS: dynatomic degree/discriminant; two real cubic factors; exact q-permutation; multipliers; Floquet polynomial; complex-pair factor.')

# Check stable example and nonstable example at rational b and c with exact high precision.
from math import sqrt
for B in [s.Rational(1,10),s.Rational(1,4),s.Rational(1,2)]:
    fb=float(B)
    for cf in [1.751,1.753,1.755,1.757,1.765,1.8]:
        if cf<=1.75: continue
        mm=8-4*cf-4*cf*sqrt(4*cf-7)
        poly=s.Poly((L+B)**3-(1+B)**3*s.Float(mm)*L,L)
        vals=[complex(v) for v in s.nroots(poly)]
        schur=(-(1-fb)**3 < mm < ((1-fb)/(1+fb))**3)
        calc=all(abs(v)<1-1e-7 for v in vals)
        assert schur==calc,(B,cf,mm,vals,schur,calc)
print('PASS: 18 independent three-step numerical Floquet/Jury comparisons.')

# Threshold parametrization and asymptotic constants: analytic identities.
T=s.symbols('T',positive=True)
phi=lambda v:v**3+v**2+7*v
assert s.expand((8-4*((T*T+7)/4)-4*((T*T+7)/4)*T) -(1-phi(T)))==0
assert s.limit((1-((1-b)/(1+b))**3)/b,b,0)==6
assert s.limit(((1-b)**3+((1-b)/(1+b))**3)/(1-b)**3,b,1)==s.Rational(9,8)
print('PASS: exact threshold cubic, small-coupling and strong-coupling asymptotic prefactors.')
