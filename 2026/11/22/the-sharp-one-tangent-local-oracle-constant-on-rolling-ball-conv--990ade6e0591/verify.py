#!/usr/bin/env python3
"""Reproduce the sharp one-tangent local-oracle constant in dimension two.
Pure Python, standard library only. Mathematical proof is independent of tests.
"""
import math, random

def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def norm(a): return math.hypot(a[0],a[1])
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def scale(s,a):return (s*a[0],s*a[1])
def oracle_disk(x,d,s,r=1.0):
    y=add(x,scale(s,d))
    if norm(y)<=r+1e-14:
        return y
    xd=dot(x,d)
    tau=-xd+math.sqrt(max(0,xd*xd+r*r-dot(x,x)))
    tau=min(s,max(0.0,tau))
    q=add(x,scale(tau,d))
    n=scale(1/norm(q),q)
    a=max(0.0,min(1.0,dot(n,d)))
    perp=add(d,scale(-a,n))
    b=norm(perp)
    if b < 1e-10:
        p=q
    else:
        u=scale(1/b,perp)
        t=max(0.0,math.sqrt(max(0,s*s-tau*tau*a*a))-tau*b)
        p=add(q,scale(t,u))
    pn=norm(p)
    phat=scale(r/pn,p) if pn>r else p
    assert norm(phat)<=r+2e-10
    assert norm(add(phat,scale(-1,x)))<=s+2e-10
    return phat

def true_disk_cap_optimum(x,d,s,r=1.0):
    y=add(x,scale(s,d))
    if norm(y)<=r: return dot(d,y)
    z=scale(r,d)
    if norm(add(z,scale(-1,x)))<=s:
        return r
    length=norm(x)
    if length<1e-12:
        return r
    h=(r*r+length*length-s*s)/(2*r*length)
    h=min(1.0,max(-1.0,h))
    delta=math.acos(h)
    phix=math.atan2(x[1],x[0])
    phi=math.atan2(d[1],d[0])
    # the accessible circle arc has endpoints phi_x +/- delta;
    # optimize cosine angle by checking both endpoints.
    return r*max(math.cos(phi-(phix+delta)),math.cos(phi-(phix-delta)))

random.seed(2908)
checks=0
maxratio=0
for j in range(3000):
    r=10**random.uniform(-1,1)
    th=random.uniform(-math.pi,math.pi)
    rad=math.sqrt(random.random())*r
    x=(rad*math.cos(th),rad*math.sin(th))
    ang=random.uniform(-math.pi,math.pi)
    d=(math.cos(ang), math.sin(ang))
    s=r*10**random.uniform(-2,0.8)
    phat=oracle_disk(x,d,s,r)
    best=true_disk_cap_optimum(x,d,s,r)
    loss=best-dot(d,phat)
    bound=s*s/(2*r)
    assert -1e-9*r<loss<=bound+2e-9*r,(j,loss,bound,x,d,s,r)
    maxratio=max(maxratio,loss/bound)
    checks+=1

for eps in [0.2,0.1,0.05,0.02,0.01,0.005,0.002]:
    r=1.;s=eps
    b=eps**3;a=math.sqrt(1-b*b)
    x=(1.,0.);d=(a,b)
    phat=oracle_disk(x,d,s,r)
    loss=1-dot(d,phat)
    ratio=loss/(s*s/2)
    assert 0<loss<s*s/2
    assert abs(loss-(1-(a+b*s)/math.sqrt(1+s*s)))<1e-9
    print(f'sharp witness s={s:.5g}: loss/(s^2/2)={ratio:.9f}')
assert ratio>0.999
print(f'PASS: {checks} random disk instances; max observed gap/bound={maxratio:.7f}; sharp witness limit verified numerically.')
