#!/usr/bin/env python3
"""Numerical diagnostics for sharp Brownian nearest-site renewal transport.

Requires only Python 3 standard-library modules. Numeric checks are not proofs.
"""
import math

PI = math.pi

def Q(z):
    return 0.5 * math.erfc(z / math.sqrt(2))

def phi(z):
    return math.exp(-z*z/2) / math.sqrt(2*PI)

def f_tail(t):
    return 2 * sum((2*k+1)*Q((k+0.5)/math.sqrt(2*t)) for k in range(100))

def f_fourier(t):
    return 2*t + 1/12 + sum((-1)**n * (8*t+1/(PI**2*n*n))*math.exp(-4*PI**2*n*n*t) for n in range(1,35))

def fp_tail(t):
    return sum((2*k+1)*z*phi(z)/t for k in range(100) for z in [(k+0.5)/math.sqrt(2*t)])

def fpp_fourier(t):
    return sum((-1)**n*(128*PI**4*n**4*t-48*PI**2*n*n)*math.exp(-4*PI**2*n*n*t) for n in range(1,35))

def h(t):
    return t*fp_tail(t)-f_tail(t)

def ratio(t):
    return f_tail(t)/(2*t)

def poisson_formula(alpha):
    return alpha*alpha*math.cosh(alpha)/(math.sinh(alpha)**2)

checks=0
for i in range(1,161):
    t=0.0125 + i*0.008
    assert abs(f_tail(t)-f_fourier(t)) < 2e-10, (t, f_tail(t), f_fourier(t))
    checks+=1
for i in range(1,101):
    t=i/1600
    assert h(t)>0, ('low-interval rise',t,h(t))
    checks+=1
for i in range(1,101):
    t=0.0625+i/500
    assert fpp_fourier(t)<0, ('high-interval concavity',t,fpp_fourier(t))
    checks+=1
lo,hi=0.0625,0.25
assert h(lo)>0 and h(hi)<0
for _ in range(80):
    mid=(lo+hi)/2
    if h(mid)>0: lo=mid
    else: hi=mid
star=(lo+hi)/2
val=ratio(star)
assert abs(star-0.0918903456528753)<2e-12
assert abs(val-1.332477887348382)<2e-11
checks+=4
assert ratio(0.1) > 1.30
assert 10*Q(math.sqrt(5)/2) > 1.25
checks+=2
# The Laplace distribution is the exponential-time mixture of Gaussian steps.
for a in (0.4,0.8,1.2,1.6061152988027674,2,3):
    z=math.exp(-2*a)
    exp_k2=math.exp(-a)*(1+z)/(1-z)**2
    by_reward=2*a*a*exp_k2
    assert abs(by_reward-poisson_formula(a))<1e-11
    assert by_reward < 1.25
    checks+=2
# Direct positivity check of the hyperbolic comparison, supplementary to series proof.
for j in range(1,151):
    a=j/35
    assert 5*math.sinh(a)**2 - 4*a*a*math.cosh(a)>0
    checks+=1
print('checks_passed:',checks)
print('theta_star:',format(star,'.16f'))
print('max_Deff_over_D:',format(val,'.16f'))
print('periodic_ratio_at_theta_0.1:',format(ratio(0.1),'.16f'))
print('best_Poisson_published_near:',format(poisson_formula(1.6061152988027674),'.16f'))
