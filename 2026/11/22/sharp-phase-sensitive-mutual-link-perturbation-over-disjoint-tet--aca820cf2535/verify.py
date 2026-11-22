#!/usr/bin/env python3
"""Direct finite-diagram enumeration and coefficient checks for matched-triple bases.
Requires Python standard library only.
"""
from itertools import combinations
from math import comb, exp, log, isclose

Q = .75
A = 160/147
B = 1600/1323
LOCAL = (49,49,40,25)

def formula(n, t):
    blocks=[set(range(3*b,3*b+3)) for b in range(t)]
    out=[0]*(n+1)
    pairs=comb(n,2)
    for bits in range(1<<n):
        S={i for i in range(n) if (bits>>i)&1}
        k=len(S)
        local_inside=sum(comb(len(S&b),2) for b in blocks)
        cross_inside=comb(k,2)-local_inside
        cross_outside=pairs-3*t-cross_inside
        x=3**cross_inside*4**cross_outside
        for b in blocks:
            x*=LOCAL[len(S&b)]
        out[k]+=x
    return out

def brute(n,t):
    pairs=list(combinations(range(n),2))
    block_edges=[tuple(pairs.index(p) for p in combinations(range(3*b,3*b+3),2)) for b in range(t)]
    out=[0]*(n+1)
    # Every assignment of old-pair links at x,y, and mutual-link bits.
    for x in range(1<<len(pairs)):
        if any(all(x&(1<<i) for i in indices) for indices in block_edges):
            continue
        for y in range(1<<len(pairs)):
            if any(all(y&(1<<i) for i in indices) for indices in block_edges):
                continue
            # More direct forbidden-pair set for all possible S.
            for mask in range(1<<n):
                if any((x&(1<<i)) and (y&(1<<i)) and (mask&(1<<a)) and (mask&(1<<b)) for i,(a,b) in enumerate(pairs)):
                    continue
                out[mask.bit_count()]+=1
    return out

def polynomial_conditional(n,t,kmax):
    # Coefficients of (1+3z+3A z^2+B z^3)^t(1+z)^(n-3t),
    # normalized by binomial(n,k).
    c=[0.]*(kmax+1);c[0]=1.
    v=(1.,3.,3*A,B)
    for _ in range(t):
        new=[0.]*(kmax+1)
        for k in range(kmax+1):
            new[k]=sum(v[s]*c[k-s] for s in range(min(3,k)+1))
        c=new
    for _ in range(n-3*t):
        for k in range(kmax,0,-1): c[k]+=c[k-1]
    return [c[k]/comb(n,k) if k<=n else 0. for k in range(kmax+1)]

def check_distribution(n,t):
    w=[1.]
    for k in range(n):
        v=w[-1]*(n-k)/(k+1)*Q**k
        w.append(v)
    denom=sum(w)
    p=[x/denom for x in w]
    # Suppress terms whose mass is already negligible in both measures.
    kmax=min(n,max(i for i,v in enumerate(p) if v>1e-15)+22)
    h=polynomial_conditional(n,t,kmax)
    z=sum(p[k]*h[k] for k in range(kmax+1))
    pt=[p[k]*h[k]/z for k in range(kmax+1)]
    tv=sum(abs(pt[k]-p[k]) for k in range(kmax+1))/2
    mu2=sum(p[k]*k*(k-1) for k in range(kmax+1))
    leading_tv=(13/49)*(t/(n*(n-1)))*sum(p[k]*abs(k*(k-1)-mu2) for k in range(kmax+1))/2
    leading_count=(13/49)*(t/(n*(n-1)))*mu2
    print(f'n={n} t={t} ratio_minus_one={z-1:.9g} leading_ratio={leading_count:.9g} tv={tv:.9g} leading_tv={leading_tv:.9g}')
    assert z>=1 and tv<1
    return tv

for n in range(1,5):
    for t in range(min(n//3,1)+1):
        a=brute(n,t);b=formula(n,t)
        assert a==b,(n,t,a,b)
        print(f'brute n={n} t={t} coefficients={a} total={sum(a)}')
for t in (0,1,2):
    n=6
    p=formula(n,t)
    print(f'formula n={n} t={t} coefficients={p} total={sum(p)}')
for n in (300,1200,6000,15000):
    check_distribution(n,n//3)
for n in (300,1200,6000):
    check_distribution(n,1)
print('VERIFY_OK')
