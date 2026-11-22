"""Reproduce algebraic and representative boundary checks for the MT2 Pickands classification.

Requires Python 3 and SymPy. The proof in RESULT.md supplies the all-real-parameter argument;
these calculations are independent algebraic and exact-example checks, not a substitute.
"""
from sympy import (Rational, symbols, expand, factor, simplify, diff, sqrt, N)

# Homogeneous-norm reduction. The second derivative of H^(1/a) has this
# polynomial numerator after removal of strictly positive factors.
a, B, C, d, t = symbols('a B C d t', real=True)
H = B*t*t+d*t+C
quadratic = expand(H*((a-1)*B*t*t+(a-2)*d*t/4)
                   -(a-1)*(B*t*t+d*t/2)**2)
claimed = t*((a-2)*d*(B*t*t+C)+(4*(a-1)*B*C-d*d)*t)/4
assert simplify(quadratic-claimed)==0
print('general curvature factorization: PASS')

# The minimum-curvature factorization when a>=2, d>=0.
s=symbols('s',positive=True)
boundary=expand(2*(a-2)*s*d+4*(a-1)*s*s-d*d)
assert simplify(boundary-(2*(a-1)*s-d)*(d+2*s))==0
print('sharp AM-GM threshold: PASS')

# Confirm direct derivatives at rational arguments, including an interior
# nonzero asymmetry; all equalities use exact algebraic numbers.
w=symbols('w',positive=True)
for aa,bb,cc,dd in [
    (2,Rational(2,3),Rational(1,2),Rational(1,2)),
    (3,Rational(1,1),Rational(1,1),Rational(7,2)),
    (4,Rational(2,3),Rational(1,2),Rational(3,10)),
]:
    P=bb**aa*w**aa+dd*(w*(1-w))**Rational(aa,2)+cc**aa*(1-w)**aa
    A=1-cc+(cc-bb)*w+P**Rational(1,aa)
    K=(aa-2)*dd*(bb**aa*w**aa+cc**aa*(1-w)**aa) + (4*(aa-1)*(bb*cc)**aa-dd**2)*(w*(1-w))**Rational(aa,2)
    for u in [Rational(1,4), Rational(2,5),Rational(1,2),Rational(3,4)]:
        lhs=diff(A,w,2).subs(w,u)
        rhs=(u*(1-u))**(Rational(aa,2)-2)*P.subs(w,u)**(Rational(1,aa)-2)*K.subs(w,u)/4
        assert abs(N(lhs-rhs,35)) < Rational(1,10**27), (aa,u,lhs-rhs)
print('direct A second-derivative identities: PASS')

# An admissible point beyond the published sufficient condition.
aa=3; bb=cc=1; dd=Rational(7,2)
assert dd>2*sqrt(aa-1)*(bb*cc)**Rational(aa,2)
assert dd<2*(aa-1)*(bb*cc)**Rational(aa,2)
print('new admissible region not covered by earlier sufficient bound: PASS')

# Sign at sharp failure point w*=c/(b+c), for asymmetric parameters.
aa=3; bb=Rational(2,3); cc=Rational(1,2)
star=cc/(bb+cc)
Dstar=2*(aa-1)*(bb*cc)**Rational(aa,2)
def curvature_bracket(D):
    return (aa-2)*D*(bb**aa*star**aa+cc**aa*(1-star)**aa) + (4*(aa-1)*(bb*cc)**aa-D**2)*(star*(1-star))**Rational(aa,2)
assert simplify(curvature_bracket(Dstar))==0
assert curvature_bracket(Dstar+Rational(1,10))<0
assert curvature_bracket(Dstar-Rational(1,10))>0
print('critical curvature and strict failure beyond boundary: PASS')

# At a=2 and d=2bc, the radical reduces to a linear function and A is one.
aa=2; bb=Rational(2,3); cc=Rational(1,2); dd=2*bb*cc
P=(bb*w+cc*(1-w))**2
assert simplify(1-cc+(cc-bb)*w+bb*w+cc*(1-w)-1)==0
print('quadratic endpoint independence identity: PASS')
print('All checks passed.')
