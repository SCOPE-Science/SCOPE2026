"""Exact structural algebra and rational interval checks for Chen--Perks hazard turns.
Run: python check.py (requires sympy for algebraic identities)."""
from fractions import Fraction as F
from math import factorial
import sympy as s

# Identity checks use independent symbolic differentiation.
x, a = s.symbols('x a', positive=True)
T=x**a
A=1-a
R=(2-a)/x-a*x**(a-1)+a*a*x**(a-1)/(A-a*T)
S=x**(a-1)/(A-a*T)
assert s.simplify(s.diff(R,x,2) - ((2-a)*(2-a*(1-a)*T)/x**3 +a*a*s.diff(S,x,2)))==0
w=1-a*T/A
positive_polynomial=2*w**2-(a*a+3*a)*w+2*a*a
assert s.simplify(x**(3-a)*(A-a*T)**3*s.diff(S,x,2)-A*A*positive_polynomial)==0
assert s.factor((a*a+3*a)**2-16*a*a)==a*a*(a-1)*(a+7)

# Rigorous interval for exp(z), z rational nonnegative. Geometric tail bound.
def exp_interval(z,n=96):
    assert z>=0 and n+2>z
    term=F(1)
    partial=term
    for k in range(1,n+1):
        term=term*z/k
        partial+=term
    next_term=term*z/(n+1)
    return partial,partial+next_term/(1-z/F(n+2))

def derivative_sign_at_y(y):
    # theta=1/5, beta=2, alpha=lambda=1/100, x=y^5.
    # h' = - 2 e^y (4-y)/(25*y^9) + e^(y^5/100)/(10^6*(1+ e^(y^5/100)/100)^2)
    E0,E1=exp_interval(y)
    Z0,Z1=exp_interval(y**5/100)
    g0=2*E0*(4-y)/(25*y**9)
    g1=2*E1*(4-y)/(25*y**9)
    q0=Z0/(10**6*(1+Z1/100)**2)
    q1=Z1/(10**6*(1+Z0/100)**2)
    lo,hi=q0-g1,q1-g0
    assert lo*hi>0
    return '+' if lo>0 else '-',float(lo),float(hi)

expectations=[(F(1),'-'),(F(7,2),'+'),(F(19,5),'-'),(F(399,100),'+')]
for y, sign in expectations:
    got,lo,hi=derivative_sign_at_y(y)
    assert got==sign,(y,got,sign)
    print('y=',str(y),'x=',str(y**5),'sign(h\' )=',got,'certified enclosure (float display only):',lo,hi)

# Independent high-precision root location check, not used for the theorem.
try:
    import mpmath as m
    m.mp.dps=60
    def hp(y):
        y=m.mpf(y);z=y**5/100;u=m.exp(z)/100
        return m.exp(z)/(10**6*(1+u)**2)-2*m.exp(y)*(4-y)/(25*y**9)
    for left,right in [('1','3.5'),('3.5','3.8'),('3.8','3.99')]:
        root=m.findroot(hp,(left,right))
        assert m.mpf(left)<root<m.mpf(right)
        print('root x ~',m.nstr(root**5,24))
except ImportError:
    print('mpmath unavailable: optional root approximations skipped')
print('PASS: 3 independent symbolic identities, discriminant, 4 exact-rational sign certificates')
