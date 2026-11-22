#!/usr/bin/env python3
"""Independent finite checks for exact random-shift harmonic aliasing and robust scale formula."""
import math, cmath, random

def wabs2(c,a,s,mu=0.):
    return ((c-mu)**2+(a-s)**2)/((c-mu)**2+(a+s)**2)

def robust(a,b,c):
    thresh=a*(b-a)/2.0
    if c*c<=thresh:
        s=math.sqrt(a*b-c*c)
        r2=(a+b-2*s)/(a+b+2*s)
    else:
        s=math.hypot(a,c)
        r2=(s-a)/(s+a)
    return s,r2

def cauchy(x,c,a):return a/(math.pi*((x-c)**2+a*a))
def sampleq(n,s,c,a,u):
    tot=0.0
    for j in range(n):
        z=((j+u)/n)
        x=s*math.tan(math.pi*(z-0.5))
        tot+=cauchy(x,c,a)/cauchy(x,0,s)
    return tot/n

def direct_moments(n,s,c,a,phase_grid=2048):
    qs=[sampleq(n,s,c,a,(i+0.5)/phase_grid) for i in range(phase_grid)]
    mean=sum(qs)/phase_grid
    var=sum((q-1.)**2 for q in qs)/phase_grid
    return mean,var

rng=random.Random(20261115)
count=0
for _ in range(350):
    a=math.exp(rng.uniform(-1.5,1.5)); b=a*math.exp(rng.uniform(0.03,2.0)); c=rng.uniform(0,4*b)
    s,r2=robust(a,b,c)
    assert s>0 and 0<=r2<1
    # Stable boundary equality, all sampled targets no larger than robust radius.
    x1=wabs2(c,a,s);x2=wabs2(c,b,s)
    assert abs(max(x1,x2)-r2)<6e-13*(1+abs(r2))
    count+=2
    for k in range(30):
        xc=rng.uniform(-c,c); ya=rng.uniform(a,b)
        assert wabs2(xc,ya,s)<=r2+3e-14
        count+=1
    # Global search over noncentered reference locations (not proof).
    for mu in [0.01*s, -0.01*s, 0.2*s, -s, 3*s]:
        rad=max(wabs2(-c,a,s,mu),wabs2(c,a,s,mu),wabs2(-c,b,s,mu),wabs2(c,b,s,mu))
        assert rad >= r2-1e-13
        count+=1
    # Global search over logarithmic grid (not proof).
    for f in [0.35,0.55,0.7,0.85,1.15,1.4,1.8,2.5]:
        sf=s*f
        r_alt=max(wabs2(c,a,sf),wabs2(c,b,sf))
        assert r_alt>=r2-1e-13
        count+=1
    if _<15:
        for n in (1,2,3,6,11):
            # Direct Riemann computation on the randomized shift, unrelated to Fourier-tail algebra.
            cc=rng.uniform(-c,c); aa=rng.uniform(a,b)
            mean,var=direct_moments(n,s,cc,aa)
            r2t=wabs2(cc,aa,s)
            expected=2*(r2t**n)/(1-r2t**n)
            assert abs(mean-1)<1e-10,(mean,a,b,c,s,n)
            assert abs(var-expected)<2e-8*(1+expected),(var,expected,a,b,c,s,n)
            count+=2
for a,b in [(1,4),(1,9),(0.1,1),(3,3.01)]:
    ct=math.sqrt(a*(b-a)/2)
    for factor in (0.0,.5,1,1.5,4):
        c=ct*factor;s,r2=robust(a,b,c)
        assert abs(max(wabs2(c,a,s),wabs2(c,b,s))-r2)<1e-13
        count+=1
# Positive finite mixtures: empirical phase error is bounded by worst singleton variance.
for _ in range(24):
    a=.5+rng.random()*2; b=a+rng.random()*8; c=rng.random()*4
    s,r2=robust(a,b,c)
    n=2+int(7*rng.random())
    targets=[(rng.uniform(-c,c),rng.uniform(a,b)) for _j in range(4)]
    weights=[rng.random() for _j in range(4)]
    weights=[v/sum(weights) for v in weights]
    vals=[]
    for i in range(1024):
        u=(i+.5)/1024
        vals.append(sum(weights[j]*sampleq(n,s,*targets[j],u) for j in range(4)))
    mean=sum(vals)/len(vals)
    var=sum((v-1.)**2 for v in vals)/len(vals)
    upper=2*r2**n/(1-r2**n)
    assert abs(mean-1)<1e-9
    assert var<=upper+2e-9
    count+=2
print('PASS',count,'checks')
