"""Exact reproducible checks for centered affine moments on a uniform triangle."""
from fractions import Fraction
from math import comb, factorial
import sympy as S

A,B=S.symbols('A B', real=True)
coeff=(A,B,-A-B)
p2=S.expand(sum(z**2 for z in coeff))
p3=S.expand(sum(z**3 for z in coeff))
u=p2/2
v=p3/3

def direct_moment(degree):
    out=S.Integer(0)
    for i in range(degree+1):
        for j in range(degree-i+1):
            k=degree-i-j
            # The multinomial factor cancels factorials of Dirichlet moments.
            out+=S.Rational(2*factorial(degree),factorial(degree+2))*coeff[0]**i*coeff[1]**j*coeff[2]**k
    return S.expand(out)

h=[S.Integer(1),S.Integer(0)]
for k in range(2,19):
    h.append(S.expand((u*h[k-2])+(v*h[k-3] if k>=3 else 0)))
for degree in range(0,19):
    predicted=S.expand(S.Rational(2*factorial(degree),factorial(degree+2))*h[degree])
    assert S.simplify(direct_moment(degree)-predicted)==0, degree
print('EXACT_DIRICHLET_AND_GENERATING_RECURRENCE_OK',19)

for m in range(1,10):
    eta=S.symbols('eta', real=True)
    profile=S.Rational(2*6**m,(2*m+1)*(2*m+2))*sum(
        S.binomial(m-j,2*j)*(S.Rational(4,27)*eta)**j for j in range(m//3+1))
    ratio=S.expand(direct_moment(2*m)/((p2/12)**m))
    substituted=S.factor(profile.subs(eta,6*p3**2/p2**3))
    assert S.cancel(ratio-substituted)==0, m
print('ALL_EVEN_MOMENT_PROFILES_OK',9)

D=S.prod((coeff[i]-coeff[j])**2 for i in range(3) for j in range(i+1,3))
assert S.expand(D-(p2**3/2-3*p3**2))==0
assert S.factor(p3.subs({A:1,B:-1}))==0
assert S.simplify(6*p3.subs({A:2,B:-1})**2/p2.subs({A:2,B:-1})**3)==1
print('DISCRIMINANT_AND_SHARP_EQUALITY_CLASSES_OK')

r=S.symbols('r', real=True, nonnegative=True)
H=(1+r)*(2*r**4+6*r**3+7*r**2+6*r+2)/((r+2)*(2*r+1))
G=H/(1+r+r**2)**S.Rational(3,2)
# Independent Hermite--Genocchi divided-difference computation of E|f|^3.
knots=(-S.Integer(1),-r,1+r)
absolute_fifths=(S.Integer(1),r**5,(1+r)**5)
divided_difference=sum(absolute_fifths[i]/S.prod(knots[i]-knots[j] for j in range(3) if j!=i) for i in range(3))
assert S.factor(divided_difference-H)==0
print('ABSOLUTE_CUBIC_MOMENT_DIVIDED_DIFFERENCE_OK')
claimed=S.Rational(1,2)*r*(r-1)*(2*r**4+14*r**3+25*r**2+14*r+2)/((r+2)**2*(2*r+1)**2*(1+r+r**2)**S.Rational(5,2))
assert S.simplify(S.diff(G,r)-claimed)==0
C=S.Rational(6)**S.Rational(3,2)/10
assert S.simplify(C*G.subs(r,0)-3*S.sqrt(6)/5)==0
assert S.simplify(C*G.subs(r,1)-46*S.sqrt(2)/45)==0
print('ABSOLUTE_CUBIC_MOMENT_MONOTONICITY_AND_ENDPOINTS_OK')

for m in range(1,10):
    base=S.Rational(2*6**m,(2*m+1)*(2*m+2))
    atvertex=S.Rational(2**(m+1)*(2**(2*m+2)+6*m+5),9*(2*m+1)*(2*m+2))
    x=S.symbols('x')
    term=base*sum(S.binomial(m-j,2*j)*S.Rational(4,27)**j for j in range(m//3+1))
    assert S.factor(term-atvertex)==0
print('EXACT_VERTEX_AND_EDGE_ENVELOPES_OK',9)
print('ALL_TRIANGLE_MOMENT_CHECKS_OK')
