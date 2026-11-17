#!/usr/bin/env python3
"""Check phase lengths and boundary derivative identities; analytic proof is in RESULT.md."""
import math

def angles(r, rho):
    a = 0.0 if rho <= r else math.acos(r/rho)
    b = 0.0 if rho <= 1 else math.acos(1/rho)
    return a,b

def predicted(r,rho):
    m=min(r,1.0); M=max(r,1.0); R=math.hypot(r,1)
    a,b=angles(r,rho)
    if rho<m:
        return [2*math.pi]
    if rho<M:
        return [2*math.pi-2*(a+b)]
    if rho<R:
        return sorted([math.pi*1.5-a-b, math.pi/2-a-b])
    return [math.pi*1.5-a-b]

def numeric_lengths(r,rho,N=180000):
    val=[]
    for j in range(N):
        q=2*math.pi*(j+0.5)/N
        val.append((r+rho*math.cos(q)>0) and (1+rho*math.sin(q)>0))
    # circular run lengths
    if all(val): return [2*math.pi]
    k=next(i for i,z in enumerate(val) if not z)
    run=[]; on=0
    for t in range(1,N+1):
        z=val[(k+t)%N]
        if z: on+=1
        elif on:
            run.append(on*2*math.pi/N);on=0
    return sorted(run)

for r in (0.4,1.0,2.0):
    m=min(r,1);M=max(r,1);R=math.hypot(r,1)
    probes=sorted(set([0.5*m, m+0.23*(M-m) if M>m else m+0.23*(R-m), M+0.2*(R-M),R-0.1*(R-M),R+0.3]))
    for rho in probes:
        p=sorted(predicted(r,rho));n=numeric_lengths(r,rho)
        assert len(p)==len(n),(r,rho,p,n)
        assert max(abs(a-b) for a,b in zip(p,n))<0.0001,(r,rho,p,n)
    h=1e-5
    a1,b1=angles(r,R-h)
    short=2*(math.pi/2-a1-b1)
    assert abs(short/h-2*R/r)<0.01,(r,short/h,2*R/r)
for r in (0.4,1.0,2.0):
    v=1.4;u=0.0
    dx=2*u*(v-1)/2
    dy=2*v*(r-u)/2
    assert dx==0 and abs(dy-r*v)<1e-13
print('GEOMETRIC_MEAN_POSITIVE_ARCS_CHECK_OK')
