"""Independent numerical checks of exact fixed-arc triangle-area geometry.

Run: python3 checker.py
Dependencies: standard Python 3, scipy.
"""
import math
import random
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

P=math.pi
L0=4*P/3

def F(s):
    return math.sin(s/2)*(1-math.cos(s/2))

def area(s,t):
    return math.sin(s/2)*(math.cos(t)-math.cos(s/2))

def direct_area(u,s,t):
    angles=(u,u+s/2+t,u+s)
    x=[(math.cos(q),math.sin(q)) for q in angles]
    return abs(sum(x[j][0]*x[(j+1)%3][1]-x[j][1]*x[(j+1)%3][0] for j in range(3)))/2

for _ in range(400):
    L=random.uniform(.3,2*P)
    s=random.uniform(.03,L)
    t=random.uniform(-s/2,s/2)
    u=random.uniform(0,L-s)
    assert abs(area(s,t)-direct_area(u,s,t))<4e-15
    assert area(s,t)<=F(min(L,L0))+1e-13

for L in [1.5,2.7,3.8,4.15, L0,4.35,5.2,6.1]:
    optimum=min(L,L0)
    res=minimize_scalar(lambda s: -F(s),bounds=(0,L),method='bounded',options={'xatol':1e-13})
    assert abs(F(optimum)+res.fun)<5e-8

# Geometric high-area probability integrated exactly in the offset and starting angle.
def tail(L,eps):
    m=F(min(L,L0))
    # Find intervals where F(s)>=m-eps, with numerical bracketing.
    from scipy.optimize import brentq
    peak=min(L,L0)
    threshold=m-eps
    lo=brentq(lambda s:F(s)-threshold,1e-15,peak-1e-13)
    if L>L0:
        hi=brentq(lambda s:F(s)-threshold,peak+1e-13,L) if F(L)<threshold else L
    else:
        hi=L
    def f(s):
        a=m-eps
        v=math.cos(s/2)+a/math.sin(s/2)
        if v>=1: return 0.
        return (L-s)*math.acos(max(-1,min(1,v)))
    return 12/L**3 *quad(f,lo,hi,epsabs=1e-13,epsrel=2e-11,limit=300,points=[peak] if lo<peak<hi else None)[0]

def c_small(L):
    z=L/2
    a=.5*(1-math.cos(z))*(1+2*math.cos(z))
    b=.5*math.sin(z)
    return 16/(5*L**3*a*a*math.sqrt(b))

def c_critical():
    a0=3*math.sqrt(3)/16
    b0=math.sqrt(3)/4
    return 4/(L0**3*a0*math.sqrt(b0))

def c_large(L):return 16*math.pi*(L-L0)/L**3

for L,power,coefficient in [(2.8,2.5,c_small(2.8)),(L0,1.5,c_critical()),(5.2,1.,c_large(5.2))]:
    errors=[]
    for e in [2e-3,4e-4,8e-5]:
        numerical=tail(L,e)
        ratio=numerical/(coefficient*e**power)
        errors.append(abs(ratio-1))
        print('L,epsilon,tail,coefficient,ratio',L,e,numerical,coefficient,ratio)
    assert errors[-1]<.018,(L,errors)
    assert errors[-1]<errors[0]

assert abs(c_critical()-18/(3**(.75)*P**3))<1e-12
print('FIXED_CIRCULAR_ARC_AREA_PHASE_CHECKS_OK')
