import math
import random

def clip(x, lo, hi):
    return min(max(x, lo), hi)

def inertia(r, b0, epsc):
    return clip(1.0-b0/r, 0.0, 1.0-epsc)

def response(r, b0, epsc):
    b=inertia(r,b0,epsc)
    return math.sqrt(r)*(1.0-b)/(1.0+b)

# Direct replay of source recurrence under alternating gradients.
random.seed(610035)
for _ in range(500):
    d=random.randint(2,8)
    G=[10.0**random.uniform(-1.0,1.0) for _ in range(d)]
    b0=random.uniform(0.02,0.3)
    b2=random.uniform(0.0,0.999)
    epsc=10.0**random.uniform(-4.0,-1.0)
    Vbar=sum(g*g for g in G)/d
    rs=[g*g/Vbar for g in G]
    bs=[inertia(r,b0,epsc) for r in rs]
    v=[0.0]*d
    m=[0.0]*d
    prod=[1.0]*d
    for t in range(1,80):
        sign=1.0 if t%2 else -1.0
        gt=[sign*g for g in G]
        v=[b2*v[i]+(1.0-b2)*gt[i]*gt[i] for i in range(d)]
        vh=[v[i]/(1.0-b2**t) if b2 != 1.0 else float("nan") for i in range(d)]
        for i in range(d):
            assert abs(vh[i]-G[i]*G[i]) <= 3e-12*max(1.0,G[i]*G[i])
        meanvh=sum(vh)/d
        bt=[clip(1.0-b0*meanvh/vh[i],0.0,1.0-epsc) for i in range(d)]
        for i in range(d):
            assert abs(bt[i]-bs[i]) < 3e-13
        m=[bt[i]*m[i]+(1.0-bt[i])*gt[i] for i in range(d)]
        prod=[prod[i]*bt[i] for i in range(d)]
        mh=[m[i]/(1.0-prod[i]) for i in range(d)]
        for i in range(d):
            b=bs[i]
            closed=sign*G[i]*(1.0-b)/(1.0+b)*(1.0-(-b)**t)/(1.0-b**t)
            assert abs(mh[i]-closed) <= 5e-11*max(1.0,abs(closed))

# Piecewise formula.
b0=0.1
epsc=0.001
for r in (0.02,0.05,0.1,0.2,0.4,1.0,1.6,20.0,99.0,100.0,200.0):
    direct=response(r,b0,epsc)
    if r <= b0:
        closed=math.sqrt(r)
    elif r < b0/epsc:
        closed=b0*math.sqrt(r)/(2.0*r-b0)
    else:
        closed=epsc*math.sqrt(r)/(2.0-epsc)
    assert abs(direct-closed) < 3e-14*max(1.0,abs(closed))

# Strict interior reversal.
grid=[0.1001 + (99.9-0.1001)*j/1000 for j in range(1001)]
vals=[response(r,b0,epsc) for r in grid]
assert all(vals[i+1] < vals[i] for i in range(len(vals)-1))

# Default exact example G=(2,1).
G1,G2=2.0,1.0
Vbar=(G1*G1+G2*G2)/2.0
r1=G1*G1/Vbar
r2=G2*G2/Vbar
b1=inertia(r1,b0,epsc)
b2i=inertia(r2,b0,epsc)
assert abs(r1-1.6)<1e-15 and abs(r2-0.4)<1e-15
assert abs(b1-15.0/16.0)<1e-15
assert abs(b2i-3.0/4.0)<1e-15
u1=G1*(1.0-b1)/(1.0+b1)
u2=G2*(1.0-b2i)/(1.0+b2i)
assert abs(u1-2.0/31.0)<1e-15
assert abs(u2-1.0/7.0)<1e-15
assert abs((u1/u2)-14.0/31.0)<1e-15

# beta2 erasure: same response for very different beta2 values.
for beta2 in (0.0,0.2,0.99,0.999999):
    t=17
    g=2.0
    v=(1.0-beta2**t)*g*g
    vh=v/(1.0-beta2**t)
    assert abs(vh-g*g)<1e-12

print("verification passed")
