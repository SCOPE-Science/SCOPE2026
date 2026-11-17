#!/usr/bin/env python3
"""Finite reproducibility diagnostics for a Poisson--Gaussian sub-gamma scale.

These checks do not prove statements quantified over all real parameters.
"""
from fractions import Fraction
from math import exp, expm1, log, factorial, isclose

checks = 0

def check(condition, msg):
    global checks
    checks += 1
    assert condition, msg

def h(x):
    if x < .2:
        return sum(2 * x**n / factorial(n + 2) for n in range(1, 65))
    return 2 * (expm1(x) - x - .5*x*x) / (x*x)

def hp(x):
    if x < .2:
        return sum(2 * n * x**(n-1) / factorial(n+2) for n in range(1, 65))
    A = expm1(x) - x - .5*x*x
    return 2*(expm1(x)-x)/(x*x) - 4*A/(x*x*x)

def theta_crit(x):
    H = h(x)
    return (x*hp(x) - H) / (H*H)

def phi(theta, x):
    H=h(x)
    return theta*H / (x*(1+theta*H))

def optimizer(theta):
    lo = 0.0
    hi = max(1.0, -log(theta)+10.0)
    check(theta_crit(hi) < theta, 'root upper bound')
    for _ in range(100):
        mid = (lo+hi)/2
        if theta_crit(mid) > theta:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

# Exact coefficient identities establishing the strictly decreasing quotient sequence.
for n in range(2,151):
    A=Fraction(2*(n-1), factorial(n+2))
    B=sum((Fraction(4,factorial(k+2)*factorial(n-k+2)) for k in range(1,n)), Fraction(0))
    S=2**(n+4)-n*n-9*n-22
    r=Fraction((n-1)*(n+3)*(n+4),2*S)
    check(S>0 and A/B==r, f'exact quotient n={n}')
    if n>=3:
        previous=Fraction((n-2)*(n+2)*(n+3),2*(2**(n+3)-(n-1)**2-9*(n-1)-22))
        check(r<previous, f'coefficient ratio monotone n={n}')
    D=(n-1)*(n+3)*(2**(n+5)-(n+1)**2-9*(n+1)-22)-n*(n+5)*S
    D_derived=(n-3)*(n+2)*2**(n+4)+n**3+16*n*n+79*n+96
    check(D==D_derived and D>0, f'polynomial identity n={n}')

# The transform K_X(t)/(V*t*t/2) = 1+theta*h(b*t).
for theta in (.1,.3,.75,1.0):
    for x in (.03,.1,.4,1.,3.,6.):
        # Set b=1, lambda=theta, Gaussian variance=1-theta, V=1.
        K=theta*(expm1(x)-x)+(1-theta)*x*x/2
        check(isclose(2*K/(x*x),1+theta*h(x),rel_tol=2e-11,abs_tol=2e-11), 'cumulant transform')

# Shape and unique maximizers, both sides of phase transition.
xs=[.001,.003,.01,.03,.1,.3,1,2,4,8,15,25,40]
for i,x in enumerate(xs):
    check(theta_crit(x)>0 and theta_crit(x)<.75,'theta range')
    if i:
        check(theta_crit(xs[i-1])>theta_crit(x),'theta strict decrease on grid')
for theta in (.05,.1,.25,.5,.7,.74,.749,.7499):
    root=optimizer(theta)
    check(abs(theta_crit(root)-theta)<2e-8, 'interior root')
    check(phi(theta,root)>theta/3, 'strict positive interior gain')
    for factor in (.25,.5,.8,1.25,2,3):
        x=max(root*factor,1.e-6)
        check(phi(theta,root)>=phi(theta,x)-1e-12,'maximizer grid')
for theta in (.75,.8,1.0):
    for x in xs:
        check(phi(theta,x)<theta/3, 'boundary case grid')

# Universal boundary series and high-noise asymptotic, without miscalling tests proofs.
for eps in (.003,.001,.0003):
    theta=.75-eps
    root=optimizer(theta)
    check(abs(root/eps-40/3)<1., 'critical root slope diagnostic')
    check(abs((phi(theta,root)-theta/3)/(eps*eps)-5/9)<.03, 'critical gain diagnostic')
for theta in (1e-6,1e-8,1e-10):
    root=optimizer(theta)
    L=log(1/theta)
    approx=L+3*log(L)-log(2)
    check(abs(root-approx)<3.,'high-noise loglog order')
    c=phi(theta,root)
    check(abs((1/c)-root-1)<.25,'high-noise inverse constant')

print('PASS',checks,'finite exact/numerical checks')
