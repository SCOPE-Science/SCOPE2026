"""Reproducible finite checks for coalescing radial Fock composition sums.

The analytic statements require the proof; these checks are diagnostic, not a
replacement for the limiting arguments.
"""
from math import exp, gamma, comb, isclose
from fractions import Fraction

checks=0

def verify(a,b,message):
    global checks
    assert a==b,(message,a,b)
    checks+=1

def approx(a,b,tolerance,message):
    global checks
    assert abs(a-b) <= tolerance,(message,a,b,abs(a-b))
    checks+=1

# Four-rate Vandermonde cancellation through degree two.
rates=[1,2,3,4]
coefs=[1,-3,3,-1]
for k in range(3):
    verify(sum(c*t**k for c,t in zip(coefs,rates)),0,"vanishing moment")
verify(sum(c*t**3 for c,t in zip(coefs,rates)),-6,"third moment")

# Exact finite Fock diagonal eigenvalues for three distinct positive rates.
r=Fraction(4,5)
q=Fraction(3,4)
for n in range(125):
    direct=sum(c*(r*q**t)**n for c,t in [(1,1),(-2,2),(1,3)])
    factor=r**n*q**n*(1-q**n)**2
    verify(direct,factor,"diagonal finite difference")

# Hilbert--Schmidt squared norm: exact independent rational geometric sum.
rhs=sum(Fraction((-1)**k*comb(4,k),1)/(1-r*r*q**(2+k)) for k in range(5))
partial=sum((r**n*q**n*(1-q**n)**2)**2 for n in range(250))
assert rhs > 0
approx(float(rhs),float(partial),1e-65,"geometric Hilbert--Schmidt trace")

def trace(delta,eps,p):
    total=0.0
    n=0
    while True:
        x=eps*n
        val=exp(-(delta+eps)*n)*(-__import__('math').expm1(-x))**2
        total+=val**p
        if n>2 and n*(delta+eps)>50: break
        n+=1
    return total

# For F(x)=exp(-x)(1-exp(-x))^2 the p=2 integral is B(2 tau+2,5).
def exact_l2_profile(tau):
    return gamma(2*tau+2)*gamma(5)/gamma(2*tau+7)

for tau in (0,0.5,2):
    expected=exact_l2_profile(tau)
    for eps in (0.025,0.0125,0.00625):
        actual=eps*trace(tau*eps,eps,2)
        approx(actual,expected,0.00025,"critical Hilbert--Schmidt profile")
        # Uniform operator norm: an actual n-grid maximization.
        op=max(exp(-(tau+1)*eps*n)*(-__import__('math').expm1(-eps*n))**2 for n in range(2500))
        peak=4*(tau+1)**(tau+1)/(tau+3)**(tau+3)
        approx(op,peak,0.00015,"critical operator norm")

# Separated damping scale; epsilon/delta approaches zero.
for delta,eps in ((0.04,0.00008),(0.02,0.00001)):
    trace2=trace(delta,eps,2)
    expected=gamma(5)/(2**5)
    approx((delta**5/eps**4)*trace2,expected,0.07,"separated trace coefficient")
    op=max(exp(-(delta+eps)*n)*(-__import__('math').expm1(-eps*n))**2 for n in range(4000))
    approx((delta/eps)**2*op,4/exp(2),0.04,"separated norm coefficient")

print('FOCK_COALESCENCE_DIAGNOSTIC_OK',checks)
