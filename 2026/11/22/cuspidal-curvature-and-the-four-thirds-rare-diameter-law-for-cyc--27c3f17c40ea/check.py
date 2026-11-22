"""Reproducible numerical diagnostics for the one-arch cycloid rare-chord theorem.
The exact proof is in RESULT.md; these computations are supplementary.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gamma

PI = math.pi
D = 2*PI
C1 = 6**(4/3)*gamma(2/3)**2/(288*gamma(7/3))
C2 = 8/(9*8**2)*(3/math.sqrt(2))**(4/3)*gamma(2/3)**2/gamma(7/3)
assert abs(C1-C2)<1e-14
assert abs(C1-0.0583009007833961)<1e-14

def xloss(t):
    return t-math.sin(t)

def deficit(t,s):
    q = xloss(t)+xloss(s)
    dy = math.cos(t)-math.cos(s)
    xx = D-q
    radius = math.hypot(xx,dy)
    return (2*D*q-q*q-dy*dy)/(D+radius)

def weight(t):
    return 2*math.sin(t/2)

def mass(s):
    return 4*(1-math.cos(s/2))

def exact_tail(eps, with_mark=False):
    tmax = brentq(lambda t: deficit(t,0)-eps,1e-10,1)
    def integrand(t):
        if t>=tmax: return 0.
        smax=brentq(lambda s:deficit(t,s)-eps,1e-10,1)
        return weight(t)*mass(smax)/32
    p=quad(integrand,0,tmax,epsabs=2e-13,epsrel=5e-10,limit=200)[0]
    if not with_mark: return p
    e_u=quad(lambda t: integrand(t)*t**3/(6*eps),0,tmax,epsabs=2e-13,epsrel=5e-10,limit=200)[0]/p
    return p,e_u

for t in [0.01,0.08,0.2,0.4]:
    assert abs(xloss(t)/(t**3/6)-1)<0.011
for eps in [1e-2, 1e-3, 1e-4]:
    v=exact_tail(eps)
    ratio=v/(C1*eps**(4/3))
    print(f"eps={eps:.1e} direct_probability={v:.14g} asymptotic_ratio={ratio:.10f}")
    assert 0.90 < ratio < 1.08
# Discrete global diameter bound, supplementary only.
for i in range(201):
    t=2*PI*i/200
    for j in range(i+1,201):
        s=2*PI*j/200
        xy= (t-math.sin(t)-(s-math.sin(s)), math.cos(s)-math.cos(t))
        assert math.hypot(*xy)<=D+1e-13
_, e_u=exact_tail(1e-4, with_mark=True)
print(f"conditional E[scaled left deficit]={e_u:.9f}; Dirichlet prediction={2/7:.9f}")
assert abs(e_u-2/7)<0.01
print('PASS: coefficient equivalence, 3 direct quadratures, Dirichlet moment, 20,100 grid pairs')
