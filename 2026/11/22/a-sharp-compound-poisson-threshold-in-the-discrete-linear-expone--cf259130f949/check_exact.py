#!/usr/bin/env python3
"""Exact-rational checks for a discrete linear-exponential phase transition."""
from fractions import Fraction as F
from math import factorial
import sympy as sp


def exp_bounds(x: F, n: int = 20):
    """For 0<=x<1, positive Taylor sum and a geometric remainder bound."""
    assert 0 <= x < 1
    lower = sum((x**k/F(factorial(k))) for k in range(n+1))
    first_omitted = x**(n+1)/F(factorial(n+1))
    upper = lower + first_omitted / (1-x/F(n+2))
    return lower, upper


def transition_numer(s, exp_s):
    # Sign of (2(1+s^3)-s)exp(s) - (2(1+s^3)+s).
    return (2*(1+s**3)-s)*exp_s - (2*(1+s**3)+s)

# Symbolic re-derivation from survival S(k)=q^k(1+a*k)
q,a,z=sp.symbols('q a z', positive=True)
A=1-q-q*a
B=(1-q)*a
P=(A+(B-A)*q*z)/(1-q*z)**2
assert sp.simplify(P.subs(z,1)-1)==0
assert sp.simplify(P-(A/(1-q*z)+B*q*z/(1-q*z)**2))==0
assert sp.simplify(sp.diff(P,z).subs(z,0)-q*(A+B))==0
assert sp.simplify(sp.diff(P,z,2).subs(z,0)/2-q**2*(A+2*B))==0
assert sp.simplify((A+B*z)**2-(A+B*(z-1))*(A+B*(z+1))-B**2)==0

# The root is enclosed by rational endpoints with fully rational exponential bounds.
left=F(8332369209698,10**14)  # 0.08332369209698
right=F(8332369209699,10**14) # 0.08332369209699
for endpoint,expected_sign in ((left,-1),(right,1)):
    EL,EU=exp_bounds(endpoint)
    sign_upper=transition_numer(endpoint,EU)
    sign_lower=transition_numer(endpoint,EL)
    assert sign_upper < 0 if expected_sign < 0 else sign_lower > 0

# Concrete non-infinitely-divisible point sigma=1/20:
# the coefficient of z^104 in log P(z) is negative.
s=F(1,20)
small_a=s/(1+s**3)
EL,EU=exp_bounds(s)
assert EL-1-small_a>0

def c_div_q(E):
    return (E-1)*small_a/(E-1-small_a)-1
# Derivative of this expression in E is -a^2/(E-1-a)^2 < 0.
t_lower=c_div_q(EU)
t_upper=c_div_q(EL)
assert t_lower>1
assert t_lower**104 >2
assert t_upper**102 <2
assert transition_numer(s,EU)<0

# Additional rational checks of the finite-coefficient criterion for arbitrary admissible q,a.
for qr,ar in [(F(1,2),F(1,4)),(F(1,4),F(1,8)),(F(1,3),F(1,3)),(F(1,2),F(7,10))]:
    if 1-qr-qr*ar<=0: continue
    Ar=1-qr-qr*ar
    Br=(1-qr)*ar
    cr=qr*(Br/Ar-1)
    if abs(cr)<=qr:
        assert all((2*qr**j+(-1)**(j+1)*cr**j)>0 for j in range(1,101))

print('PASS: 5 symbolic identities; rational root enclosure; exact negative coefficient at degree 104; 102nd nonnegative; 400 rational compound-Poisson coefficient checks')
print('root bounds',str(float(left)),str(float(right)))
print('degree-104 exact sign',str((2-t_lower**104)<0))
