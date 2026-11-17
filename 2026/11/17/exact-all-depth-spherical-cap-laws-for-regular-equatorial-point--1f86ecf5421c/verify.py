#!/usr/bin/env python3
"""Independent deterministic diagnostics for equal-equator spherical cap depths.
Python standard library only. This numerically corroborates, but does not prove,
the all-n all-radius geometric identities in RESULT.md.
"""
import math

PI=math.pi

def endpoint(n,r,j):
    t=j*PI/n
    if t>=r or t>=PI/2: return 0.
    c=math.cos(r)/math.cos(t)
    return math.sqrt(max(0.,1-c*c))

def antiderivative(r,z):
    if z<=0: return 0.
    c=math.cos(r); s=math.sin(r)
    if abs(z-s)<1e-12: return PI*(1-c)/2
    return math.atan2(c*z,math.sqrt(max(0.,s*s-z*z))) - c*math.asin(min(1.,z/s))

def tail(n,r,k):
    if k<=0:return 1.
    if k>n:return 0.
    if r<=0:return 0.
    if r>=PI:return 1.
    if r>PI/2: return 1-tail(n,PI-r,n-k+1)
    if r==PI/2:
        if n%2==0:return float(k<=n//2)
        return 1. if k<=(n-1)//2 else (.5 if k==(n+1)//2 else 0.)
    return (antiderivative(r,endpoint(n,r,k-1))-
            antiderivative(r,endpoint(n,r,k)))/(PI/n)

def num_tail(n,r,k,panels=5000):
    # Independent integration in the *latitude* variable of conditional
    # longitude depth; no use of the closed-form antiderivative.
    dr=1/panels; alpha=PI/n; c=math.cos(r); sr=math.sin(r)
    acc=0.
    for i in range(panels):
        z=(i+.5)*dr
        if z>=sr:continue
        v=min(1.,c/math.sqrt(1-z*z))
        L=math.acos(v)
        acc+=max(0.,min(1.,L/alpha-k+1.))
    return acc*dr

def direct_area(n,r,k,zsteps=160,phisteps=400):
    # Totally separate direct spherical dot-product enumeration; uniform
    # z and azimuth sampling, suitable for coarse independent comparison.
    hit=0
    for iz in range(zsteps):
        z=-1+(iz+.5)*2/zsteps
        xy=math.sqrt(1-z*z)
        for ip in range(phisteps):
            phi=2*PI*(ip+.37)/phisteps
            cnt=sum(xy*math.cos(phi-2*PI*j/n)>=math.cos(r)
                    for j in range(n))
            hit+=cnt>=k
    return hit/(zsteps*phisteps)

checks=0
for n in [3,4,5,6,7,8,10,13]:
    for r in [0.11, 0.39, 0.75, 1.11, 1.41]:
        for k in range(1,(n+1)//2+2):
            a=tail(n,r,k); b=num_tail(n,r,k)
            assert -1.e-10<=a<=1+1.e-10,(n,r,k,a)
            assert abs(a-b)<4.0e-5,(n,r,k,a,b)
            checks+=1
        pm=[(1-tail(n,r,1))]+[tail(n,r,k)-tail(n,r,k+1)
                                      for k in range(1,n+1)]
        assert min(pm)>-1e-10,(n,r,pm)
        assert abs(sum(pm)-1)<1e-10
        assert abs(sum(k*pm[k] for k in range(n+1))-
                   n*(1-math.cos(r))/2)<1e-9
        checks+=3
    for r in [0.42,0.88,1.31,1.81,2.42]:
        for k in range(1,min(n,3)+1):
            a=tail(n,r,k)
            b=direct_area(n,r,k)
            assert abs(a-b)<.012,(n,r,k,a,b)
            checks+=1
    alpha=PI/n
    for k in range(2,(n+1)//2+1):
        r0=(k-1)*alpha
        C=2*math.sqrt(2*math.tan(r0))/(3*alpha)
        for eps in (1e-3,1e-4):
            a=tail(n,r0+eps,k)
            assert abs(a/(C*eps**1.5)-1)<.003,(n,k,eps,a)
            checks+=1
    if n%2==0:
        assert tail(n,PI/2,n//2)==1.
        assert tail(n,PI/2,n//2+1)==0.
    else:
        assert tail(n,PI/2,(n+1)//2)==.5
        assert tail(n,PI/2,(n-1)//2)==1.
    checks+=2
print('ALL_CHECKS_PASSED', checks)
