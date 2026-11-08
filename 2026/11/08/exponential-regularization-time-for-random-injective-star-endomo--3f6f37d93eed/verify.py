"""Exact small-star checks and numerical checks for regularization-time law.
Run: python3 verify.py (Python standard library)."""
from itertools import product
from fractions import Fraction
from collections import Counter
from math import comb, factorial, sqrt, exp, log, lgamma

def endomorphisms(n):
    for f in product(range(-1, n), repeat=n):
        vals=[v for v in f if v>=0]
        if len(set(vals))!=len(vals):
            continue
        if f[0]>=0 and any(f[i]>=0 and (f[i]==f[0] or (f[0]!=0 and f[i]!=0)) for i in range(1,n)):
            continue
        yield f

def power(f,g):
    return tuple(g[v] if v>=0 else -1 for v in f)

def regular_criterion(f):
    return f[0]>=0 or 0 not in f or all(v in (-1,0) for v in f)

def chain_len(f):
    predecessors={v:i for i,v in enumerate(f) if v>=0}
    seen=set(); x=0; t=0
    while x in predecessors:
        x=predecessors[x]
        assert x not in seen
        seen.add(x); t+=1
    return t

def has_cycle(f):
    for v in range(1,len(f)):
        seen=set(); x=v
        while x>=0 and x not in seen:
            seen.add(x)
            x=f[x]
        if x>=0:
            return True
    return False

def nth_regular(f):
    g=f
    for r in range(1,len(f)+3):
        if regular_criterion(g):
            return r
        g=power(g,f)
    raise AssertionError('no regular power')

for n in range(2,7):
    m=n-1
    aa=Counter(); tail=Counter(); cyc=Counter(); times=Counter(); total=0; typeB=0; typeC=0
    all_maps=list(endomorphisms(n))
    if n<=4:
        for f in all_maps:
            direct_regular=any(power(power(f,g),f)==f for g in all_maps)
            assert direct_regular==regular_criterion(f),(n,f,direct_regular)
    for f in all_maps:
        total+=1
        times[nth_regular(f)]+=1
        if f[0]>=0:
            if f[0]==0: typeB+=1
            else:typeC+=1
            assert nth_regular(f)==1
            continue
        k=sum(v>=0 for v in f); j=m-k
        aa[k]+=1
        L=chain_len(f); T=nth_regular(f)
        if has_cycle(f):
            assert T==L+1,(f,L,T)
            cyc[k]+=1
        for r in range(1,L+1):
            tail[(k,r)]+=1
    expected_A=sum(comb(m,k)*factorial(m+1)//factorial(m+1-k) for k in range(m+1))
    expected_B=sum(comb(m,k)**2*factorial(k) for k in range(m+1))
    assert (sum(aa.values()),typeB,typeC)==(expected_A,expected_B,m*(m+1))
    for k,count in aa.items():
        assert count==comb(m,k)*factorial(m+1)//factorial(m+1-k)
        for r in range(1,k+2):
            p=Fraction(k,m+1)
            for i in range(1,r):
                p*=Fraction(k-i,m+1-i)
            assert Fraction(tail[k,r],count)==p,(n,k,r,tail[k,r],count,p)
        assert Fraction(count-cyc[k],count)==Fraction(m+1-k,m+1)
    # Exact finite-size survival: hub-chain tail minus unique-center rank-one power.
    for t in range(1,m+1):
        chain_count=Fraction(0)
        for k,count in aa.items():
            if k<t:continue
            p=Fraction(k,m+1)
            for i in range(1,t):p*=Fraction(k-i,m+1-i)
            chain_count+=count*p
        degree=m-t
        coeff=[Fraction(0) for _ in range(degree+1)]
        coeff[0]=Fraction(1)
        for h in range(1,degree+1):
            coeff[h]=sum(r*coeff[h-r] for r in range(1,min(t,h)+1))/h
        exceptional=factorial(m)*coeff[degree]
        calculated=chain_count-exceptional
        observed=sum(v for r,v in times.items() if r>t)
        assert calculated==observed,(n,t,calculated,observed)
    print('STAR_EXHAUSTIVE_OK',n,'total',total,'typeA',expected_A,'typeB',typeB,'typeC',typeC,'max_time',max(times))

# Independent exact log-binomial mixture of conditional hub-chain tails.
def chain_tail_mixture(m,x):
    logs=[lgamma(m+1)-lgamma(j+1)-lgamma(m-j+1)
          +lgamma(m+2)-lgamma(j+2) for j in range(m+1)]
    vmax=max(logs)
    weights=[exp(t-vmax) for t in logs]
    denom=sum(weights)
    r=int(x*sqrt(m))+1
    numer=0.0
    for j,w in enumerate(weights):
        k=m-j
        if r>k: continue
        p=k/(m+1)
        for i in range(1,r):
            p*=(k-i)/(m+1-i)
        numer+=w*p
    return numer/denom
for m in (100,400,1600):
    vals=[chain_tail_mixture(m,x) for x in (0.5,1.0,2.0)]
    print('ASYMPTOTIC_TAIL',m,tuple(round(v,8) for v in vals),'target',tuple(round(exp(-x),8) for x in (0.5,1,2)))
assert abs(chain_tail_mixture(1600,1)-exp(-1))<0.03
print('VERIFY_OK')
