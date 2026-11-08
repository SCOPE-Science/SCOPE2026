"""Standalone numerical checks for fixed-volume solid-cylinder random-distance optimization.
Requires Python 3, NumPy and SciPy. Execute: python verify.py.
"""
import math
import random
import numpy as np
from scipy.special import roots_legendre
from scipy.optimize import brentq

# Radial separation density of two independent area-uniform points in unit disk.
def density(t):
    return (4*t/math.pi)*(np.arccos(t/2)-(t/2)*np.sqrt(np.maximum(0,1-t*t/4)))

N=420
x,w=roots_legendre(N)
t=x+1
u=(x+1)/2
wt=w*density(t)
wu=(w/2)*2*(1-u)
S=t[:,None]**2
H=u[None,:]**2
W=wt[:,None]*wu[None,:]
assert abs(sum(wt)-1)<2e-8
assert abs(sum(wu)-1)<2e-10

def stationarity(p,q):
    z=S+q*q*H
    weighted=W*np.exp((p/2)*np.log(z/(4+q*q)))
    return float((weighted*(q*q*H/z)).sum()/weighted.sum()-1/3)

def optimal(p):
    return brentq(lambda q:stationarity(p,q),1,2.1,xtol=2e-12)

q2=math.sqrt(3)
q4=math.sqrt(5*(math.sqrt(33)-1)/8)
assert abs(optimal(2)-q2)<3e-8
assert abs(optimal(4)-q4)<3e-8
# Predictions follow from radial/axial independence; checked against separate quadrature.
mean_u2=float((wt*t*t).sum())
mean_u4=float((wt*t**4).sum())
mean_h2=float((wu*u*u).sum())
mean_h4=float((wu*u**4).sum())
assert abs(mean_u2-1)<1e-7 and abs(mean_u4-5/3)<1e-7
assert abs(mean_h2-1/6)<1e-10 and abs(mean_h4-1/15)<1e-10
for q in [1.18,1.56,2.23]:
    e2=mean_u2+q*q*mean_h2
    e4=mean_u4+2*q*q*mean_u2*mean_h2+q**4*mean_h4
    assert abs(e2-(1+q*q/6))<1e-7
    assert abs(e4-(5/3+q*q/3+q**4/15))<1e-7

q100,q200,q400=optimal(100),optimal(200),optimal(400)
qinf=math.sqrt(2)
coefficient=9*qinf/4
for p,q,limit in [(100,q100,.09),(200,q200,.06),(400,q400,.03)]:
    assert q>qinf
    assert abs(p*(q-qinf)-coefficient)<limit

# Separate Cartesian-sampling test of the actual solid-cylinder distance moments.
rng=random.Random(16729)
q=1.61
n=350000
sum2=sum4=0.0
for _ in range(n):
    r1=math.sqrt(rng.random()); a1=2*math.pi*rng.random()
    r2=math.sqrt(rng.random()); a2=2*math.pi*rng.random()
    z1=q*rng.random(); z2=q*rng.random()
    s2=r1*r1+r2*r2-2*r1*r2*math.cos(a1-a2)+(z1-z2)**2
    sum2+=s2;sum4+=s2*s2
analytic2=1+q*q/6
analytic4=5/3+q*q/3+q**4/15
assert abs(sum2/n-analytic2)<.014
assert abs(sum4/n-analytic4)<.10
print('CYLINDER_VOLUME_DISTANCE_UNIQUENESS_ASYMPTOTICS_OK',n)
print('stationary_radii',q2,q4,q100,q200,q400,'asymptotic_coefficient',coefficient)
