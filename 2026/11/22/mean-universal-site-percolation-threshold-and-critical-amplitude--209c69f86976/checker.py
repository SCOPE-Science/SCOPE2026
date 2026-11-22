#!/usr/bin/env python3
"""Reproducible exact finite diagnostics for Bernoulli site percolation on grandparent graphs."""
from fractions import Fraction as Q
from itertools import product
from decimal import Decimal, getcontext
from math import sqrt

ASSERTIONS=0
def check(condition, detail=''):
    global ASSERTIONS
    assert condition, detail
    ASSERTIONS += 1

def word_probability(n,p):
    # Root conditioned retained; endpoint retained and no adjacent absent sites.
    if n==0: return Q(1)
    a,b=Q(1),p
    if n==1:return b
    for _ in range(2,n+1):a,b=b,p*b+p*(1-p)*a
    return b

def polynomial_word_probability(n,p):
    from math import comb
    return sum((Q(comb(n-j,j))*p**(n-j)*(1-p)**j for j in range(n//2+1)),Q(0))

# Full binary rooted tree through depth 3: 15 vertices, 2^14 exact configurations.
parents=[-1]
for v in range(7): parents += [v,v]
check(len(parents)==15)
depth=[0]*len(parents)
for v in range(1,len(parents)): depth[v]=depth[parents[v]]+1

def ancestors(v):
    a=[]
    while v>=0:
        a.append(v)
        v=parents[v]
    return list(reversed(a))

for v in range(len(parents)):
    for p in (Q(1,3),Q(1,2),Q(3,5)):
        check(word_probability(depth[v],p)==polynomial_word_probability(depth[v],p))

nbr=[set() for _ in parents]
for v in range(1,len(parents)):
    for w in (parents[v],parents[parents[v]] if parents[v]!=0 else -1):
        if w>=0:
            nbr[v].add(w); nbr[w].add(v)
counts=[0,0,0,0]
for bits in product((0,1),repeat=len(parents)-1):
    retained=(1,)+bits
    reachable={0};stack=[0]
    while stack:
        x=stack.pop()
        for y in nbr[x]:
            if retained[y] and y not in reachable:
                reachable.add(y);stack.append(y)
    for v in range(len(parents)):
        path=ancestors(v)
        # More robust: no two successive closed ancestral vertices, and endpoint retained.
        admissible=bool(retained[v]) and all(retained[path[j]] or retained[path[j+1]] for j in range(len(path)-1))
        check((v in reachable)==admissible, (v,bits))
        counts[depth[v]]+=(v in reachable)
for d in range(4):
    nodes=2**d
    check(Q(counts[d],2**14)==nodes*word_probability(d,Q(1,2)))

# Exact expected-generation and subcritical susceptibility identities.
for m in (Q(3,2),Q(2),Q(3)):
 for p in (Q(1,10),Q(1,5)):
    mu=[m**n*word_probability(n,p) for n in range(10)]
    check(mu[0]==1)
    check(mu[1]==m*p)
    for n in range(2,len(mu)):
      check(mu[n]==m*p*mu[n-1]+m*m*p*(1-p)*mu[n-2])
    R=m*p+m*m*p*(1-p)
    if R<1:
        check(1/(1-R)>sum(mu))

# Verify exact numerical fixed-point survival slopes for same-mean offspring distributions.
getcontext().prec=55
m=Decimal(2)
q=(m+1-((m+1)**2-4).sqrt())/(2*m)
Rprime=m+m*m*(1-2*q)
check(Decimal('0.19098')<q<Decimal('0.19099'))
for eta,pgf in ((Decimal(2),lambda z:z*z),(Decimal(3),lambda z:(z+z**3)/2)):
    K=2*Rprime/(eta*(m*(1-q)*q*q+1/(m*m)))
    for delta in ('0.0005','0.0001','0.00002'):
        p=q+Decimal(delta)
        def f(z):return 1-pgf(1-z)
        def fun(h):return f(p*h+(1-p)*f(p*h))-h
        lo=Decimal('1e-35');hi=Decimal(1)
        check(fun(lo)>0)
        check(fun(hi)<0)
        for _ in range(180):
            mid=(lo+hi)/2
            if fun(mid)>0:lo=mid
            else:hi=mid
        h=(lo+hi)/2
        check(abs(h/Decimal(delta)/K-1)<Decimal('0.03'))
    print('offspring factorial second moment',eta,'near-critical conditional slope',K)
print('PASS',ASSERTIONS,'exact enumeration and arithmetic assertions')
