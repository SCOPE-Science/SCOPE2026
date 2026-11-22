#!/usr/bin/env python3
"""Reproducibility checks for exact directional widths of two-disk lenses.
Only numpy and Python standard library are required.  All tests use finite
samples as diagnostics, not as substitutes for the analytic theorem.
"""
import math
import numpy as np

PI = math.pi

def params(R,r,d):
    assert R >= r > 0 and R-r < d < R+r
    x0=(d*d+R*R-r*r)/(2*d)
    H=math.sqrt(max(0,R*R-x0*x0))
    a=x0/R
    b=(d-x0)/r
    assert 0<a<1 and -1<b<1 and a+1e-12>=abs(b)
    return x0,H,a,b

def width(R,r,d,x):
    x0,H,a,b=params(R,r,d)
    assert 0<=x<=1
    y=math.sqrt(max(0,1-x*x))
    if b<0 and x<=-b:
        return 2*r
    if b>=0 and x<=b:
        return 2*H*y
    if x<=a:
        return r+H*y-r*b*x
    return R+r-d*x

def inverse(R,r,d,w):
    x0,H,a,b=params(R,r,d)
    lo=R+r-d
    hi=(2*r if b<=0 else 2*H)
    if w<=lo: return 1.
    if w>=hi: return (max(0,-b) if b<0 else 0.)
    wa=R+r-d*a
    if w<=wa:
        return (R+r-w)/d
    wb=2*H*H/r if b>0 else hi
    if b>0 and w>=wb:
        return math.sqrt(max(0,1-(w/(2*H))**2))
    q=w-r
    return (-r*b*q+H*math.sqrt(max(0,r*r-q*q)))/(r*r)

def cdf(R,r,d,w):
    x0,H,a,b=params(R,r,d)
    lo=R+r-d
    hi=2*r if b<=0 else 2*H
    if w<lo: return 0.
    if w>=hi:return 1.
    x=inverse(R,r,d,w)
    return 1-2*math.asin(min(1,max(0,x)))/PI

def invert_features(m,M,c,atom):
    d=8/(PI*PI*c*c)
    S=m+d
    if atom>0:
        r=M/2
        R=S-r
    else:
        H=M/2
        diff_sq=d*d-4*d*d*H*H/(S*S-d*d)
        diff=math.sqrt(max(0,diff_sq))
        R=(S+diff)/2
        r=(S-diff)/2
    return R,r,d

def brute(R,r,d,theta,N=60000):
    grid=np.linspace(0,2*PI,N,endpoint=False)
    q1=np.column_stack((R*np.cos(grid),R*np.sin(grid)))
    q1=q1[((q1[:,0]-d)**2+q1[:,1]**2)<=r*r+1e-12]
    q2=np.column_stack((d+r*np.cos(grid),r*np.sin(grid)))
    q2=q2[(q2[:,0]**2+q2[:,1]**2)<=R*R+1e-12]
    x0,H,a,b=params(R,r,d)
    points=np.concatenate((q1,q2,np.array([[x0,H],[x0,-H]])))
    u=np.array([math.cos(theta),math.sin(theta)])
    s=points@u
    return float(s.max()-s.min())

cases=[(1,1,.5),(2,1,1.1),(2,1,math.sqrt(3)),(2,1,2.),(3,1,2.1),(3,1,2.8),(2.5,2.4,.3)]
rng=np.random.default_rng(192314)
checks=0
for R,r,d in cases:
    x0,H,a,b=params(R,r,d)
    assert abs(a-a*a*0)>0
    assert abs(width(R,r,d,1)-(R+r-d))<1e-10
    assert abs(width(R,r,d,0)-(2*r if b<=0 else 2*H))<1e-10
    for x in np.linspace(0,1,101):
        w=width(R,r,d,float(x))
        assert R+r-d-1e-10<=w<=(2*r if b<=0 else 2*H)+1e-10
        if x > max(0,-b)+1e-9:
            assert abs(inverse(R,r,d,w)-x)<2e-7,(R,r,d,x,w,inverse(R,r,d,w))
        checks+=2
    for w in np.linspace(R+r-d,(2*r if b<=0 else 2*H)-1e-7,101):
        assert abs(width(R,r,d,inverse(R,r,d,float(w)))-w)<1e-8
        checks+=1
    for theta in rng.uniform(0,2*PI,40):
        numeric=brute(R,r,d,float(theta),N=24000)
        analytic=width(R,r,d,abs(math.cos(theta)))
        assert abs(analytic-numeric)<3e-6,(R,r,d,theta,analytic,numeric)
        checks+=1
    eps=1e-8
    c=(2/PI)*math.sqrt(2/d)
    atom=(2/PI)*math.asin(-b) if b<0 else 0.
    R2,r2,d2=invert_features(R+r-d,2*r if b<=0 else 2*H,c,atom)
    assert np.allclose([R2,r2,d2],[R,r,d],rtol=1e-9,atol=1e-9),(R,r,d,R2,r2,d2)
    checks+=3
    # Exact bottom formula for the linear support branch.
    small=min(d*(1-a)*0.5,0.005)
    exact=(2/PI)*math.acos(1-small/d)
    assert abs(cdf(R,r,d,R+r-d+small)-exact)<1e-11
    checks+=1
    if b<0:
        p=(2/PI)*math.asin(-b)
        assert abs((1-cdf(R,r,d,2*r-1e-11))-p)<2e-5
        checks+=1
print('PASS',checks,'deterministic analytic/inverse/independent boundary diagnostics')
