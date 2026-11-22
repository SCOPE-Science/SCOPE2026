"""Exact symbolic checks for the degree-nine (3,3) polynomial-composition closure.

Run: python verify_composition_33.py
Requires Python 3 and sympy. Scientific argument is in RESULT.md; this verifies
coefficient identities, differential-rank certificates, and two tangent spaces.
"""
from sympy import symbols, Poly, expand, Matrix, factor, eye

t, a, b, c1, c2, c3 = symbols('t a b c1 c2 c3')
H = a*t**3+b*t
F = expand(c1*H + c2*H**2 + c3*H**3)
EXPECTED = {1:c1*b,2:c2*b**2,3:c1*a+c3*b**3,
            4:2*c2*a*b,5:3*c3*a*b**2,
            6:c2*a**2,7:3*c3*a**2*b,9:c3*a**3}
assert set(Poly(F,t).monoms()) <= {(i,) for i in EXPECTED}
for k,v in EXPECTED.items():
    assert expand(Poly(F,t).nth(k)-v)==0, (k,v)
assert Poly(F,t).nth(8)==0

# a != 0: take a=1, differentiate H with respect to b.  Projective
# differential consists of H,H^2,H^3 and the weighted derivatives
# t, tH, tH^2.  This minor has determinant 1 for every b.
H3=t**3+b*t
cols=[expand(H3**i) for i in (1,2,3)] + [expand(t*H3**i) for i in (0,1,2)]
M=Matrix([[Poly(col,t).nth(i) for col in cols] for i in (1,3,4,6,7,9)])
assert expand(M.det())==1

# a=0, b=1: the varying-base derivative is
# c1*t^3+2*c2*t^4+3*c3*t^5.  Its projection to the quotient
# of the span(t,t^2,t^3) vanishes precisely when c2=c3=0.
Hb=t+a*t**3
D=expand((c1+2*c2*Hb+3*c3*Hb**2)*t**3).subs(a,0)
assert Poly(D,t).nth(4)==2*c2
assert Poly(D,t).nth(5)==3*c3

# At each point beta*t+alpha*t^3 with alpha!=0 the two projective
# tangent spaces have common span(t,t^3); their sum has vector rank 6.
alpha,beta=symbols('alpha beta')
J=alpha*t**3+beta*t
TA=[t,t**2,t**3,t**5]
TB=[t,t**3,expand(J**2),expand(J**3)]
# Show a constant nonzero 6x6 minor for their sum (up to factor alpha).
U=[t,t**2,t**3,t**5,expand(J**2),expand(J**3)]
R=Matrix([[Poly(col,t).nth(i) for col in U] for i in (1,2,3,5,6,9)])
assert factor(R.det())==alpha**5, factor(R.det())

# Affine chart F=t+lambda*t^2+B*t^3+...
# with normalized H=t+a*t^3 and c1=1, c2=lambda, c3=mu.
lam,mu=symbols('lam mu')
Fchart=expand((t+a*t**3)+lam*(t+a*t**3)**2+mu*(t+a*t**3)**3)
expected_chart={1:1,2:lam,3:a+mu,4:2*a*lam,5:3*a*mu,
                6:a**2*lam,7:3*a**2*mu,9:a**3*mu}
for i,v in expected_chart.items(): assert expand(Poly(Fchart,t).nth(i)-v)==0
# Reduced inverse image of the nonnormal line in this chart is
# lam=0 and a*mu=0: the two normalization branches meet at a=mu=0.

print('PASS: all coefficient identities, immersion and tangent-rank certificates')
