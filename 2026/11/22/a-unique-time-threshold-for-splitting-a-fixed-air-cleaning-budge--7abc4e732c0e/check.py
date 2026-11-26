"""Reproducible numerical checks for a constant-budget two-zone pulse model.
These are supplementary finite checks, not a substitute for the analytic proof.
"""
import math, random

def remaining_source(k,F,a,t,z):
    v=math.hypot(k,z)
    return math.exp(-(a+k+F/2)*t)*(math.cosh(v*t)-z*math.sinh(v*t)/v)

def remaining_remote(k,F,a,t,z):
    v=math.hypot(k,z)
    return math.exp(-(a+k+F/2)*t)*k*math.sinh(v*t)/v

def eq(t,k,z):
    v=math.hypot(k,z)
    r=z/v
    u=t*v
    return u*r*(1-r/math.tanh(u))-(1-r*r)

def tcrit(k,F):
    z=F/2
    lo=1e-12
    hi=1.
    while eq(hi,k,z)<=0:hi*=2
    for _ in range(75):
        mid=(lo+hi)/2
        if eq(mid,k,z)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2

def optimum(k,F,t):
    hi=F/2
    if t <= tcrit(k,F):return hi
    lo=0.
    for _ in range(75):
        mid=(lo+hi)/2
        if eq(t,k,mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2

def run():
    rng=random.Random(11444)
    assertions=0
    assert abs(tcrit(1,2)-1.7653315356634109)<1e-11;assertions+=1
    for i in range(3500):
        k=10**rng.uniform(-1,0.4)
        F=10**rng.uniform(-1,0.55)
        a=10**rng.uniform(-1,0.55)
        tc=tcrit(k,F)
        t=tc*rng.uniform(0.25,2.0)
        z=optimum(k,F,t)
        assert -1e-10<=z<=F/2+1e-10;assertions+=1
        # Direct source concentration comparison against 21 alternative allocations
        best=remaining_source(k,F,a,t,z)
        for j in range(21):
            zz=-F/2+F*j/20
            other=remaining_source(k,F,a,t,zz)
            assert best <= other +1e-10*max(1,best,other);assertions+=1
        # Remote minimum always at exactly equal allocation
        remote=remaining_remote(k,F,a,t,0)
        for j in range(21):
            zz=-F/2+F*j/20
            other=remaining_remote(k,F,a,t,zz)
            assert remote<=other+1e-10*max(1,remote,other);assertions+=1
        # Strict phase classification away from the boundary
        if t<tc*(1-1e-7): assert abs(z-F/2)<1e-10;assertions+=1
        elif t>tc*(1+1e-7): assert 0<z<F/2;assertions+=1
    # Asymptotic check, no claim of symbolic proof from numerics
    for k,F in [(0.5,1),(1,2),(2,3)]:
        for t in [50,100,200]:
            z=optimum(k,F,t)
            assert abs(t*z-1)<0.12;assertions+=1
    print('PASS',assertions,'deterministic supplementary assertions', 'tcrit(k=1,F=2)=',tcrit(1,2))
if __name__=='__main__':run()
