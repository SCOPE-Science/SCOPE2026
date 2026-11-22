#!/usr/bin/env python3
"""Standalone elementary checks for two basin certificates.

Numerical trajectories and rational spot checks do not replace the universal proof.
"""
import math
import random
from fractions import Fraction as Q
from decimal import Decimal, getcontext

rng=random.Random(261012319)
# Exact cancellation: f(u)-f(1) = -(u-1)*phi*(u-u_c).
for _ in range(900):
    a=Q(rng.randint(1,8),10)
    low=Q(1,1)/(2-a)
    phi=low+(1-low)*Q(rng.randint(1,9),10)
    u=Q(rng.randint(1,40),20)
    f=lambda x:(1-phi*x)*(x-a)
    uc=a+1/phi-1
    assert f(u)-f(1)==-phi*(u-1)*(u-uc)
    assert a<uc<1
    fm=(1-a*phi)**2/(4*phi)
    xv=(1+a*phi)/(2*phi)
    assert f(xv)==fm

getcontext().prec=65
D=Decimal
fmax=D(9)/D(80)
c=D(1)/D(10)*(D(8)/D(5)).ln()
uc=D(3)/D(4)
B=(uc-D(1)-uc.ln())/D(10)
H=((D(4)/D(5))-D(1)-(D(4)/D(5)).ln())/D(10)
assert D('0.00231')<H<D('0.00232') and H<B
assert D('0.00376')<B<D('0.00378')

def g(t): return t.exp()-D(1)-t-c/fmax
lo,hi=D(0),D(2)
assert g(lo)<0 and g(hi)>0
for _ in range(250):
    mid=(lo+hi)/2
    if g(mid)<0:lo=mid
    else:hi=mid
T=(lo+hi)/2
threshold=fmax*T.exp()
assert abs(g(T))<D('1e-60')
assert D('0.248783897092')<threshold<D('0.248783897095')
assert threshold<D(1)/D(4)
assert fmax*T-(D(1)/4)*(D(1)-(-T).exp())<-c
# An entirely rational choice of t=4/5 also certifies extinction.
t=D(4)/D(5)
assert fmax*t-(D(1)/4)*(D(1)-(-t).exp())<-c

# Finite numerical trajectories illustrate the two rigorously proved claims.
a,phi,eps=0.5,0.8,0.1
def velocity(u,v):
    return u*((1-phi*u)*(u-a)-v)/eps, v*(u-1)
def rk4(u,v,h):
    k1=velocity(u,v)
    k2=velocity(u+h*k1[0]/2,v+h*k1[1]/2)
    k3=velocity(u+h*k2[0]/2,v+h*k2[1]/2)
    k4=velocity(u+h*k3[0],v+h*k3[1])
    return (u+h*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6,
            v+h*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6)

for vstart,outcome in [(0.1,'coexistence'),(0.25,'extinction')]:
    u,v=0.8,vstart
    h=0.001
    for n in range(70000):
        u,v=rk4(u,v,h)
        assert u>=0 and v>=0
    if outcome=='coexistence':
        assert abs(u-1)<1e-6 and abs(v-0.1)<1e-6
    else:
        assert u<1e-12 and v<1e-12
print('PASS: exact rational cancellation, high-precision basin witnesses, scalar minimizer and illustrative finite trajectories')
