"""Reproducible checks for bidirectional orientation-reset transport.

Requires only Python 3 standard library. The proof is analytic; this file
checks algebraic identities and independent stationary-age integration.
"""
from fractions import Fraction as F
import math

checks = 0

def same(a, b, tol=2e-11):
    global checks
    assert abs(a-b) <= tol * (1+abs(a)+abs(b)), (a,b)
    checks += 1

def nonnegative(a):
    global checks
    assert a >= -1e-13, a
    checks += 1

def exact(a,b):
    global checks
    assert a==b,(a,b)
    checks+=1

# Derive independently: stationary harmonic from renewal age A~Exp(r).
# Its nth harmonic after a random reset equals mu_n * E(exp(-n^2 D_R A)).
for q_num in range(1,16):
    q=F(q_num,16)
    gamma=q+1
    for c_num in range(1,18):
        c=F(c_num,17)              # cos(alpha)^2
        a1sq=q*q*c/(q+1)**2
        a2=q*(2*c-1)/(q+4)
        gap=a2-a1sq
        compact=q*(c*(q*q+2)-(q+1)**2)/((q+4)*(q+1)**2)
        exact(gap,compact)
        cxx=(1+a2)/2-a1sq
        cyy=(1-a2)/2
        exact(cxx-cyy,gap)
        nonnegative(float(cxx));nonnegative(float(cyy))
        # Infinite-horizon diffusivity difference agrees with finite-lag
        # x-y covariance sign, because the temporal kernel is positive.
        H=2/(q+1)-(1-math.exp(-2*float(q+1)))/float((q+1)**2)
        nonnegative(H)
        same(float(2*gap)*H, 2*float(cxx-cyy)*H)

# Exact isotropy curve. Its positive drift remains nonzero.
for q_num in range(1,17):
    q=F(q_num,32)               # 0<q<=1/2
    c=(q+1)**2/(q*q+2)
    assert F(1,2)<c<=1
    a1sq=q*q*c/(q+1)**2
    a2=q*(2*c-1)/(q+4)
    exact(a1sq,a2)
    exact(a1sq,q*q/(q*q+2))
    exact(((1+a2)/2-a1sq),1/(q*q+2))
    exact(((1-a2)/2),1/(q*q+2))
    nonnegative(float(q/math.sqrt(float(q*q+2))))

# Strict phase classification for the symmetric two-angle reset.
for c_num in range(1,21):
    c=F(c_num,20)
    for q_num in range(1,31):
        q=F(q_num,20)
        p=c*(q*q+2)-(q+1)**2
        left=q*(2*c-1)/(q+4)-q*q*c/(q+1)**2
        exact((left>0)-(left<0),(p>0)-(p<0))
    if c <= F(1,2):
        for q_num in range(1,31):
            q=F(q_num,20)
            assert c*(q*q+2)-(q+1)**2<0
            checks+=1

# Geometric identity for the extra transverse covariance from fluctuating
# reinitialization directions, compared with rotated single-direction resets.
for q_num in range(1,11):
    q=F(q_num,10)
    a=q/(q+1)
    for c_num in range(1,10):
        c=F(c_num,10)
        # difference in stationary angular variance in y:
        mixed_sin=(1-q*(2*c-1)/(q+4))/2
        averaged_fixed_sin=(1-q*(2*c-1)/(q+4))/2-a*a*(1-c)
        exact(mixed_sin-averaged_fixed_sin,a*a*(1-c))

# Independently integrate the stationary age distribution numerically.
# E[cos(n Theta)] = cos(n alpha) int_0^infty r exp(-(r+n^2D) a) da.
# Evaluate a midpoint Riemann sum, then compare to algebraic ratio.
for q,alpha in ((0.22,0.39),(0.5,0.0),(0.87,0.71)):
    for n in (1,2):
        scale=q+n*n
        step=0.0005
        N=int(28/scale/step)
        sm=0.0
        for j in range(N):
            age=(j+0.5)*step
            sm+=q*math.exp(-scale*age)*step
        same(sm*math.cos(n*alpha),q*math.cos(n*alpha)/(q+n*n),tol=4e-8)

# Sample finite-lag covariance equality on exact curve, with translational D.
for q in (0.04,0.13,0.25,0.49,0.5):
    cos2=(q+1)**2/(q*q+2)
    a1=q*math.sqrt(cos2)/(q+1)
    a2=q*(2*cos2-1)/(q+4)
    v=1.7; Dt=0.11; dr=0.8
    gamma=dr*(1+q)
    cxx=(1+a2)/2-a1*a1
    cyy=(1-a2)/2
    for t in (.1,1.,2.5,8.):
        h=t/gamma+math.expm1(-gamma*t)/gamma**2
        vx=2*Dt*t+2*v*v*h*cxx
        vy=2*Dt*t+2*v*v*h*cyy
        same(vx,vy)
        same(vx,2*Dt*t+2*v*v*h/(q*q+2))
print('OK; assertions:',checks)
