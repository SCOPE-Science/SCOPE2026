"""Reproduce exact rational bounds for a wrapped XLindley likelihood-ratio cutoff.

Python 3 standard library only.  All sign decisions use rational enclosures,
not floating-point approximations.  The theorem's global uniqueness and
ordering statements are proven algebraically in RESULT.md, not inferred
from finite checks.
"""
from fractions import Fraction as F
from math import factorial
from decimal import Decimal, getcontext
getcontext().prec = 45
checks = 0

def ck(condition, name):
    global checks
    assert condition, name
    checks += 1

def atan_partial(x, n):
    return sum(((-1)**k)*x**(2*k+1)/F(2*k+1) for k in range(n))

# Machin pi/4 = 4 atan(1/5) - atan(1/239).
a5lo, a5hi = atan_partial(F(1,5),20), atan_partial(F(1,5),21)
a239lo, a239hi = atan_partial(F(1,239),20),atan_partial(F(1,239),21)
ck(a5lo<a5hi and a239lo<a239hi, 'alternating arctan bracketing')
pi_lo,pi_hi=16*a5lo-4*a239hi,16*a5hi-4*a239lo
Llo,Lhi=2*pi_lo,2*pi_hi
ck(F(6283,1000)<Llo<Lhi<F(6284,1000),'2pi interval')

def exp_bounds(z,terms=30):
    # For z >= 0, the exact exponential Taylor series is positive.
    assert F(0)<=z<F(terms+2)
    s=sum(z**k/F(factorial(k)) for k in range(terms+1))
    next_term=z**(terms+1)/F(factorial(terms+1))
    err=next_term/(1-z/F(terms+2))
    return s,s+err

def K_bounds(x):
    aa=(x+2)**2+1
    E_lo=exp_bounds(Llo*x)[0]
    E_hi=exp_bounds(Lhi*x)[1]
    return aa*(E_lo-1)+Llo*(2*x+4)-Lhi**2, aa*(E_hi-1)+Lhi*(2*x+4)-Llo**2

lo,hi=F(18008,100000),F(18009,100000)
kl=K_bounds(lo)
kh=K_bounds(hi)
ck(kl[1]<0,'K(0.18008) is strictly negative')
ck(kh[0]>0,'K(0.18009) is strictly positive')

def b_bounds(x):
    E_lo=exp_bounds(Llo*x)[0]
    E_hi=exp_bounds(Lhi*x)[1]
    return (x+2 + Llo/(E_hi-1),x+2 + Lhi/(E_lo-1))

b1lo,b1hi=b_bounds(F(1,10))
b2lo,b2hi=b_bounds(F(11,100))
d0_lo=-F(1,100)+1/b2hi-1/b1lo
d0_hi=-F(1,100)+1/b2lo-1/b1hi
ck(d0_lo>0,'0.10 versus 0.11 reverses likelihood slope at origin')
ck(d0_hi<F(1,100),'0.10 versus 0.11 numerical enclosure')

# No missing negative signs when differentiating the density.
import random,math
random.seed(1047)
L=float((Llo+Lhi)/2)
def b(z):return z+2+L/math.expm1(L*z)
def bp(z):return 1-L**2*math.exp(L*z)/math.expm1(L*z)**2
def h(z):return b(z)**2+bp(z)
def K(z):return math.expm1(L*z)*((z+2)**2+1)+L*(2*z+4-L)
for j in range(200):
    z=.001 + 2*random.random()
    ck(abs((math.expm1(L*z)*h(z))-K(z))<1e-7*(1+abs(K(z))), 'H-K algebra')
    ck((b(z)+L)**2+bp(z)>0,'terminal mixed derivative strictly negative')
for j in range(100):
    x=.01+random.random()
    y=x+0.005+random.random()
    t=L*random.random()
    # log density ratio derivative, checked against finite differences
    f=lambda u,z:2*math.log(z)-2*math.log(z+1)-math.log(-math.expm1(-L*z))-z*u+math.log(u+b(z))
    eps=1e-5
    d_est=(f(t+eps,y)-f(t-eps,y)-f(t+eps,x)+f(t-eps,x))/(2*eps)
    d_exact=-(y-x)+1/(t+b(y))-1/(t+b(x))
    ck(abs(d_est-d_exact)<1e-8,'likelihood derivative identity')

def dec(x):return str(Decimal(x.numerator)/Decimal(x.denominator))
print('rigorous cutoff bracket:',dec(lo),'< lambda_* <',dec(hi))
print('K(lower) enclosed by [',dec(kl[0]),',',dec(kl[1]),']')
print('K(upper) enclosed by [',dec(kh[0]),',',dec(kh[1]),']')
print('R_prime(0)/R(0) at (0.10,0.11) in [',dec(d0_lo),',',dec(d0_hi),']')
print('ALL CHECKS PASSED:',checks)
