"""Reproduce numerical tests for the random-apex spherical area law.
The proof is geometric; numeric quadrature is a separate diagnostic.
Run: python lexell_area_checker.py  (requires scipy and numpy).
"""
import math
import numpy as np
from scipy.integrate import quad

def cdf(beta,t):
    assert 0<beta<math.pi/2 and 0<=t<=2*math.pi
    a=t/2
    c=math.cos(beta)
    L=math.sqrt(1-c*c*math.cos(a)**2)
    return a/math.pi + c*math.sin(a)*math.acos(-c*math.cos(a))/(math.pi*L)

def independent_quadrature(beta,t):
    # Condition on X of a surface-uniform point of S^2. X is uniform [-1,1],
    # and Z|X=x is arcsine on [-sqrt(1-x^2),sqrt(1-x^2)].
    a=t/2
    c=math.cos(beta)
    s=math.sin(beta)
    if a==0:return 0.
    if a==math.pi:return 1.
    def arcsin_prob(x,shift,angle):
        R=math.sqrt(max(0.,1-x*x))
        q=(shift)*math.tan(angle)/(s*R) if R>0 else math.inf
        return math.asin(min(1.,max(0.,q)))
    if a<=math.pi/2:
        val,_=quad(lambda x:arcsin_prob(x,c+x,a),-c,1.,epsabs=2e-10,epsrel=1e-10,limit=300)
        return val/math.pi
    val,_=quad(lambda x:math.pi/2-arcsin_prob(x,-c-x,math.pi-a),-1.,-c,epsabs=2e-10,epsrel=1e-10,limit=300)
    return (1+c)/2+val/math.pi

for beta in [0.12,0.4,0.73,1.3,1.52]:
    prev=1.1
    for t in [0,0.11,0.58,1.0,2.4,math.pi,4.3,5.98,2*math.pi]:
        got=cdf(beta,t)
        if t not in (0,2*math.pi):
            indep=independent_quadrature(beta,t)
            assert abs(indep-got)<4e-8,(beta,t,got,indep)
        assert 0<=got<=1+1e-12
    assert abs(cdf(beta,math.pi)-(1+math.cos(beta))/2)<1e-13
for t in [0.11,1.,3.,5.7]:
    vals=[cdf(b,t) for b in [0.1,0.3,0.75,1.2,1.55]]
    assert all(vals[i]>vals[i+1] for i in range(len(vals)-1))
for u in [0.1,0.5,1,2,5]:
    for beta in [1e-2,2e-3]:
        assert abs(cdf(beta,2*beta*u)-u/math.sqrt(1+u*u))<4e-2
print('PASS: 35 independent deterministic quadrature comparisons, 5 half-area identities, monotonic samples and small-base asymptotics')
