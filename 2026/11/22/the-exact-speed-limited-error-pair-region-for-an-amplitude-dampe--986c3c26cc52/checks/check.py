#!/usr/bin/env python3
"""Standalone arithmetic consistency checks for a bounded-speed qubit inversion theorem.

Checks are finite sanity tests, not a substitute for the analytic proof.
Standard library only. Run: python3 check.py
"""
import math
import random

PI = math.pi
RNG = random.Random(20261111)
COUNT = 0

def close(a, b, tol=1e-9):
    global COUNT
    COUNT += 1
    assert abs(a-b) <= tol*max(1.0,abs(a),abs(b)), (a,b)

def require(condition):
    global COUNT
    COUNT += 1
    assert condition

def mix(h,q):
    """Mass at -1 and at b realizing first two moments h,q."""
    if h <= -1+1e-12:
        return 1.0, -1.0
    b = (q+h)/(1+h)
    a = (b-h)/(1+b)
    return a,b

def normalized_errors(h,q):
    return 1+2*h+q, 1-2*h+q

def verify_envelope(u,v):
    return 2+(u-v)**2/8 <= u+v+1e-10 and u+v <= 4+1e-10

# Exact moment region and its constructive two-point representation.
for i in range(550):
    h = RNG.uniform(-.98,.98)
    q = h*h + RNG.random()*(1-h*h)
    a,b = mix(h,q)
    require(-1-1e-10 <= b <= 1+1e-10)
    require(-1e-10 <= a <= 1+1e-10)
    close(-a+(1-a)*b,h)
    close(a+(1-a)*b*b,q)
    u,v = normalized_errors(h,q)
    require(verify_envelope(u,v))
    # Converse from measured errors to moments.
    close((u-v)/4,h)
    close((u+v)/2-1,q)

for h,q in [(1,1),(-1,1),(0,0),(0,1),(.4,.16),(-.7,.49),(.2,1)]:
    u,v=normalized_errors(h,q)
    require(verify_envelope(u,v))
    a,b=mix(h,q)
    close(a+(1-a)*b*b,q)

# Every nonmonotone meridian path obeys the same speed-limited occupation
# lower bounds. Integrals of the quadratic trigonometric loss are exact.
def segment_integrals(a,b,omega):
    low,high=sorted((a,b))
    d=high-low
    common=1.5*d+0.25*(math.sin(2*high)-math.sin(2*low))
    odd=2*(math.sin(high)-math.sin(low))
    return (common+odd)/omega,(common-odd)/omega

for i in range(280):
    omega=RNG.uniform(.2,4)
    a,b=RNG.uniform(0,PI), RNG.uniform(0,PI)
    route=[0,a,b,PI]
    plus=minus=0.0
    length=0.0
    for lo,hi in zip(route,route[1:]):
        x,y=segment_integrals(lo,hi,omega)
        plus+=x;minus+=y
        length+=abs(hi-lo)/omega
    waits=[RNG.uniform(0,4) for _ in range(4)]
    for theta,t in zip(route,waits):
        z=math.cos(theta)
        plus+=t*(1+z)**2
        minus+=t*(1-z)**2
    T=length+sum(waits)
    C=1.5*PI/omega
    extra=T-PI/omega
    u=(plus-C)/extra
    v=(minus-C)/extra
    require(verify_envelope(u,v))
    ratio=plus/minus
    upper=1+4*extra/C
    require(ratio <= upper+1e-9)

# Sharp one-sided-pole dwell / speed-limited flip attains the ratio.
for omega in [.2,1,5]:
    C=1.5*PI/omega
    for extra in [0,.1,1,4,20]:
        k_minus=(C+4*extra)/4
        k_plus=C/4
        close(k_minus/k_plus,1+8*(omega*(PI/omega+extra)-PI)/(3*PI))

# A high-order integration check on the physical GKSL amplitude damping
# equation. During a meridian drive, the x,z Bloch equations are
# dx/dt = omega*z - gamma*x/2,
# dz/dt = -omega*x + gamma*(1-z).
def simulate(omega,intervals,sign,gamma,step=.001):
    x,z=0.,float(sign)
    def f(x,z,w):return w*z-gamma*x/2,-w*x+gamma*(1-z)
    for duration,w in intervals:
        N=max(1,math.ceil(duration/step));dt=duration/N
        for _ in range(N):
            ax,az=f(x,z,w)
            bx,bz=f(x+dt*ax/2,z+dt*az/2,w)
            cx,cz=f(x+dt*bx/2,z+dt*bz/2,w)
            dx,dz=f(x+dt*cx,z+dt*cz,w)
            x+=dt*(ax+2*bx+2*cx+dx)/6
            z+=dt*(az+2*bz+2*cz+dz)/6
    # sign=+1 => ideal terminal -z; sign=-1 => ideal terminal +z
    error=(1+sign*z)/2
    return error

for omega,wait_north,wait_south in [(2,.4,.2),(1,2.,0),(3,0.,.8)]:
    C=1.5*PI/omega
    durations=[(wait_north,0),(PI/omega,omega),(wait_south,0)]
    # minus input is antipodal and experiences the same nominal drive.
    kplus=(C+4*wait_south)/4
    kminus=(C+4*wait_north)/4
    for sign,expected in [(1,kplus),(-1,kminus)]:
        e1=simulate(omega,durations,sign,0.0001)
        e2=simulate(omega,durations,sign,0.00005)
        # Richardson cancellation removes the linear finite-noise effect.
        approx=2*e2/.00005-e1/.0001
        close(approx,expected,3e-5)

print(f'PASS: {COUNT} numerical and algebraic checks; analytical proof required for general theorem')
