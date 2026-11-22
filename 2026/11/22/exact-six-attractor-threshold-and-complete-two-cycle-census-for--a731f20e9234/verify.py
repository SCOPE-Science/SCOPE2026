"""Exact algebraic checks for the cubic implicit two-cycle classification.

Requires Python >=3.10 and sympy. These checks are finite supplements
and do not replace the proof of completeness for all real step sizes.
"""
import sympy as S

h=S.symbols('h',positive=True)
x,y=S.symbols('x y',real=True)
H=lambda z:(1-h)*z+h*z**3
D=lambda z:1-h+3*h*z*z
checks=0

def verify(statement):
    global checks
    assert S.simplify(statement)==0, statement
    checks+=1

# Complete elimination identities, without restricting the real variables.
verify(S.expand((x-H(y))-(y-H(x))-(x-y)*(h*(x*x+x*y+y*y)-h+2)))
verify(S.expand((x-H(y))+(y-H(x))+h*(x+y)*(x*x-x*y+y*y-1)))

# Antipodal and symmetry-breaking branches evaluated exactly in radicals.
for hv in [S.Rational(9,4), S.Rational(5,2), S.Rational(11,4), S.Rational(3),
           S.Rational(31,10), S.Rational(25,8), S.Rational(13,4),
           S.Rational(7,2), S.Rational(4), S.Rational(5), S.Rational(16)]:
    aa=S.sqrt(1-2/hv)
    verify(S.expand(H(aa).subs(h,hv)+aa))
    verify(S.expand(H(-aa).subs(h,hv)-aa))
    verify(S.expand((D(aa)*D(-aa)).subs(h,hv)-(2*hv-5)**2))
    if hv>3:
        ss=S.sqrt(1-3/hv)
        dd=S.sqrt(1+1/hv)
        for sign in [1,-1]:
            u=(sign*ss+dd)/2
            v=(sign*ss-dd)/2
            verify(S.expand(H(u).subs(h,hv)-v))
            verify(S.expand(H(v).subs(h,hv)-u))
            verify(S.simplify((D(u)*D(v)).subs(h,hv)-(9-2*(hv-1)**2)))

# Independent full-composition factorization: includes all period-one and period-two real points.
t=S.symbols('t',real=True)
factor_target=h*t*(t-1)*(t+1)*(h*t**2-h+2)*(h**2*t**4-h**2*t**2+h*t**2+1)
verify(S.expand(H(H(t))-t-factor_target))

# Product multiplier and marked transition thresholds.
verify((9-2*(h-1)**2).subs(h,1+3/S.sqrt(2)))
verify((9-2*(h-1)**2).subs(h,1+S.sqrt(5))+1)
verify(((2*h-5)**2).subs(h,S.Rational(5,2)))
verify((2*h-5).subs(h,3)-1)

# Fixed-point branch multipliers and no internal zero of the fixed denominator
# in the asserted multi-attractor interval h>1+sqrt(5).
for hv in [S.Rational(13,4),S.Rational(4),S.Rational(10)]:
    for z in [S.Integer(-1), S.Integer(0), S.Integer(1)]:
        verify(H(z).subs(h,hv)-z)
        assert abs(float(D(z).subs(h,hv)))>1
        checks+=1
    assert (2*hv-5)**2>1
    assert abs(float(9-2*(hv-1)**2))>1
    checks+=2

print(f'PASS: {checks} exact symbolic checks; no assertion of exhaustive numerical verification')
