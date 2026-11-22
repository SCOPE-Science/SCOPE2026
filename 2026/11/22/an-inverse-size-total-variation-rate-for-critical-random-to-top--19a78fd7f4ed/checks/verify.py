#!/usr/bin/env python3
"""Exact finite checks for quantitative fixed-point approximation in uniform move-to-front shuffling."""
from collections import Counter
from fractions import Fraction
from itertools import product, permutations
from math import comb, factorial, exp, floor

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def falling(n, k):
    if k > n: return 0
    z=1
    for j in range(k): z *= n-j
    return z

def pmf_partial_fixed(t,m):
    """Inclusion-exclusion exact law of fixed coordinates in a uniform injective t-word on [m]."""
    assert 0 <= t <= m
    return [sum(((-1)**j)*Fraction(falling(t,h+j), factorial(h)*factorial(j)*falling(m,h+j))
                for j in range(t-h+1)) for h in range(t+1)]

def pmf_perm_fixed(k):
    return pmf_partial_fixed(k,k)

def pmf_fixed_given_k(n,k):
    result = Counter()
    for j in range(n-k+1):
        m=n-j
        pr=Fraction(comb(m-1,k-1),comb(n,k))
        if m==k: pmf=pmf_perm_fixed(k)
        else: pmf=pmf_partial_fixed(k-1,m-1)
        for h,v in enumerate(pmf):
            if v: result[j+h]+=pr*v
    assert sum(result.values())==1
    return result

def law_shuffle(n,r):
    counts=Counter()
    ks=Counter()
    for choices in product(range(1,n+1),repeat=r):
        deck=list(range(1,n+1))
        for x in choices:
            deck.remove(x);deck.insert(0,x)
        counts[sum(x==i+1 for i,x in enumerate(deck))]+=1
        ks[len(set(choices))]+=1
    return {h:Fraction(z,n**r) for h,z in counts.items()}, {k:Fraction(z,n**r) for k,z in ks.items()}

def exact_law(n,r):
    # occupancy K by Stirling numbers of the second kind
    old=[1]+[0]*r
    for t in range(1,r+1):
        new=[0]*(r+1)
        for k in range(1,t+1):new[k]=k*old[k]+old[k-1]
        old=new
    law=Counter()
    for k in range(1,min(n,r)+1):
        prob=Fraction(falling(n,k)*old[k],n**r)
        if not prob: continue
        for f,v in pmf_fixed_given_k(n,k).items():law[f]+=prob*v
    assert sum(law.values())==1
    return law

def lim_pmf(a,max_len=500):
    q=1-a
    return [sum(exp(-a)*a**(h-j)/factorial(h-j)*a*q**j for j in range(h+1)) for h in range(max_len)]

# A. Elementary combinatorial representation against actual histories.
for n in range(2,6):
    for r in range(1,5):
        direct,ks=law_shuffle(n,r)
        mix=Counter()
        for k,w in ks.items():
            for h,v in pmf_fixed_given_k(n,k).items():mix[h]+=w*v
        for h in range(n+1):check(direct.get(h,0)==mix.get(h,0),f'push-to-front n={n},r={r},h={h}')
        independent=exact_law(n,r)
        for h in range(n+1):check(direct.get(h,0)==independent.get(h,0),f'occupancy n={n},r={r},h={h}')

# B. Conditional suffix and factorial-moment formulas through eight labels.
for n in range(2,9):
    for k in range(1,n+1):
        counts=Counter()
        for word in permutations(range(1,n+1),k):
            j=n-max(word)
            h=sum(word[i]==i+1 for i in range(k))
            counts[(j,h)]+=1
        total=falling(n,k)
        for j in range(n-k+1):
            pj=Fraction(comb(n-j-1,k-1),comb(n,k))
            check(Fraction(sum(counts[(j,h)] for h in range(k+1)),total)==pj,f'suffix n={n},k={k},j={j}')
            if j<n-k:
                p=pmf_partial_fixed(k-1,n-j-1)
            else:p=pmf_perm_fixed(k)
            for h in range(k+1):
                check(Fraction(counts[(j,h)],total)==pj*(p[h] if h<len(p) else 0),f'conditional fixed n={n},k={k},j={j},h={h}')

# C. Check analytic partial-permutation Poisson bound for sample sizes.
for m in range(2,45):
    for t in range(1,m+1):
        p=pmf_partial_fixed(t,m)
        lam=t/m
        po=[exp(-lam)*lam**h/factorial(h) for h in range(t+1)]
        tail=max(0.,1-sum(po))
        tv=(sum(abs(float(p[h])-po[h]) for h in range(t+1))+tail)/2
        check(tv <= exp(2)/t+1e-12, f'Poisson TV t={t}, m={m}')

# D. Check that n times the actual total-variation distance stays bounded numerically
# in several critical-time examples, without asserting that this proves any limit.
for c in (0.4,1.0,2.0):
    a=1-exp(-c)
    limit=lim_pmf(a,100)
    for n in (8,12,18,24):
        r=floor(c*n)
        if r==0:continue
        law=exact_law(n,r)
        tv=(sum(abs(float(law.get(i,0))-limit[i]) for i in range(100)) + max(0.,1-sum(limit)))/2
        check(0<=tv<=1,f'total variation invalid for c={c},n={n}')
        print(f'c={c:.1f}, n={n}, r={r}, TV={tv:.9f}, n*TV={n*tv:.6f}')
print(f'PASS: {checks} exact combinatorial and numeric assertions')
