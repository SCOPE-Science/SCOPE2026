#!/usr/bin/env python3
"""Independent arithmetic checks for two-facility cost comparisons.
Uses only the Python standard library. Execute with: python3 verify.py
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import pi, isclose

def add(*ps):
    out=[F(0)]*max(map(len,ps))
    for p in ps:
        for i,c in enumerate(p):out[i]+=c
    return out

def scale(p,k):return [F(k)*c for c in p]
def prod(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b):out[i+j]+=c*d
    return out

def integral(p,a,b):
    a,b=F(a),F(b)
    return sum((c*(b**(i+1)-a**(i+1))/F(i+1) for i,c in enumerate(p)),F(0))

def at(p,x):
    x=F(x);return sum((c*x**i for i,c in enumerate(p)),F(0))

def exact(profile):
    n=len(profile)
    cost=lambda x,y: sum(min(abs(z-x),abs(z-y)) for z in profile)
    D=sum(abs(profile[i]-profile[j]) for i in range(n) for j in range(i+1,n))
    if not D:return F(0),F(0)
    glob=sum(abs(profile[i]-profile[j])*cost(profile[i],profile[j]) for i in range(n) for j in range(i+1,n))/D
    prop=F(0)
    for i,x in enumerate(profile):
        si=sum(abs(x-y) for y in profile)
        if si:
            for j,y in enumerate(profile):
                prop+=abs(x-y)*cost(x,y)/(si*n)
    return glob,prop

# Independently integrate the closed conditional single-pair service cost on a uniform interval.
# A(t)= integral |t-y| c(t,y) dy; B(t)=integral integral |x-y|min(|t-x|,|t-y|)dxdy.
A=[F(5,48),F(-20,48),F(54,48),F(-68,48),F(34,48)]
B=[F(1,12),F(-4,12),F(12,12),F(-8,12),F(-4,12)] # 0<=t<=1/2
h=[F(1,2),F(-1),F(1)]
N=F(7,120); D=F(1,3); T=F(7,40)
assert integral(A,0,1)==N
# Influence function for conditional pairwise cost, after one-point contamination.
IF_T=scale(add(scale(A,2),B,[-3*N],scale(add(scale(h,2),[-2*D]),-T)),F(1)/D)
assert IF_T==[F(7,40),F(-98,40),F(348,40),F(-420,40),F(130,40)]
assert 2*integral(IF_T,0,F(1,2))==0
IF_R_low=add(scale(IF_T,8),scale([F(1,8),-F(1)],-F(56,5)))
IF_R_high=add(scale(IF_T,8),scale([-F(3,8),F(1)],-F(56,5)))
assert 2*(integral(IF_R_low,0,F(1,4))+integral(IF_R_high,F(1,4),F(1,2)))==0
V=2*(integral(prod(IF_R_low,IF_R_low),0,F(1,4))+integral(prod(IF_R_high,IF_R_high),F(1,4),F(1,2)))
assert V==F(147113,504000),(V,F(147113,504000))
# Analytical polynomial quotient: A/h = (17 t^2-17t)/24 + 1/16 + 7/(96 h).
quot=[F(1,16),-F(17,24),F(17,24)]
assert add(prod(quot,h),[F(7,96)])==A
# Hence P limit is -1/18 + 7*pi/96; G is 7/40. Check strict ordering.
P=-1/18+7*pi/96
G=7/40
assert 0<P<G and isclose(8*P,1.3881512701496017,rel_tol=1e-13)
# Three-point symmetric laws: masses a, 1-2a, a, sites 0,1/2,1.
trials=0
for numerator in range(1,12):
    a=F(numerator,24)
    if a>=F(1,2):continue
    vals=(F(0),F(1,2),F(1))
    # Use rational replication; exact finite mechanism equals the 3-atom functional.
    profile=tuple([vals[0]]*numerator+[vals[1]]*(24-2*numerator)+[vals[2]]*numerator)
    dg,dp=exact(profile)
    expg=a*(1-2*a)/(1-a)
    expp=a*(1-2*a)*(3*a+F(1,2))
    assert (dg/len(profile),dp/len(profile))==(expg,expp),(a,dg,dp,expg,expp)
    diff=a*(1-2*a)**2*(1-3*a)/(2*(1-a))
    assert (dg-dp)/len(profile)==diff
    trials+=1
# Cross-check method formulas in arbitrary finite rational profiles.
for n in range(3,6):
    for v in combinations_with_replacement([F(0),F(1,4),F(1,2),F(3,4),F(1)],n):
        dg,dp=exact(v)
        assert dg>=0 and dp>=0
        if len(set(v))>2:
            # Need not hold per profile; this checks only the deterministic 4-approximation theorem.
            optimum=min(sum(min(abs(z-x),abs(z-y)) for z in v) for x in v for y in v)
            assert dg<=4*optimum and dp<=4*optimum
        trials+=1
# Deterministic midpoint quadrature of independent continuum integrals.
M=300
xx=[(i+0.5)/M for i in range(M)]
num=den=ps=0.0
for x in xx:
    hx=(x*x+(1-x)**2)/2
    for y in xx:
        u,v=sorted((x,y))
        c=(u*u+(1-v)**2)/2+(v-u)**2/4
        w=abs(x-y)
        num+=w*c
        den+=w
        ps+=w*c/hx
assert abs(num/den-G)<3e-5,(num/den,G)
assert abs(ps/M**2-P)<3e-5,(ps/M**2,P)
print('VERIFY_OK: polynomial influence/variance; exact 3-site formulas; rational finite profiles; uniform quadrature')
print('finite cases:',trials,'variance:',V,'uniform mean ratios:',8*P,8*G)
