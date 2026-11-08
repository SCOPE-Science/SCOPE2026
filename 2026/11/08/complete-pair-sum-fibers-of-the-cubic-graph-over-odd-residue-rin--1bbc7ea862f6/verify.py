#!/usr/bin/env python3
"""Exact arithmetic checks for cubic-graph pair-sum fibers over odd moduli."""
from collections import Counter
from math import prod

def v_p(a,p,k):
    if a==0:return k
    v=0
    while v<k and a%p==0:
        v+=1; a//=p
    return v

def square_roots_count(c,p,j):
    if j<=0:return 1
    z=p**j
    c%=z
    if c==0:return p**(j//2)
    h=v_p(c,p,j)
    if h&1:return 0
    e=h//2
    a=c//p**(2*e)
    if pow(a%p,(p-1)//2,p)!=1:return 0
    return 2*p**e

def local_fiber(p,k,s,t):
    q=p**k
    s%=q;t%=q
    alpha=v_p(3*s,p,k)
    diff=(4*t-s*s*s)%q
    if alpha==k:return q if diff==0 else 0
    power=p**alpha
    if diff%power:return 0
    j=k-alpha
    unit=(3*s//power)%(p**j)
    c=(diff//power)*pow(unit,-1,p**j)%(p**j)
    return power*square_roots_count(c,p,j)

def Q(p,j):
    return 1+sum((p-1)*p**(j-2*h-1)//2 for h in range((j+1)//2))

def size_formula(p,k):
    if p==3:return 3+sum(2*3**j*Q(3,j) for j in range(1,k))
    return 1+(p-1)*sum(p**(j-1)*Q(p,j) for j in range(1,k+1))

def energy_formula(p,k):
    if p==3:return 3**(2*k-1)*(2*k*k+4*k+3)
    return p**(2*k)+(p-1)*p**(2*k-2)*(k*p+(p-1)*k*(k+1)//2)

def direct(p,k):
    q=p**k
    ctr=Counter()
    for x in range(q):
        for y in range(q):
            ctr[((x+y)%q,(x*x*x+y*y*y)%q)]+=1
    for s in range(q):
        for t in range(q):
            a=ctr[(s,t)]
            b=local_fiber(p,k,s,t)
            assert a==b,(p,k,s,t,a,b)
    count=len(ctr)
    energy=sum(v*v for v in ctr.values())
    assert count==size_formula(p,k),(p,k,count,size_formula(p,k))
    assert energy==energy_formula(p,k),(p,k,energy,energy_formula(p,k))
    assert sum(ctr.values())==q*q
    return q,count,energy

cases=[(3,1),(3,2),(3,3),(3,4),(5,1),(5,2),(5,3),(7,1),(7,2),(11,1),(11,2),(13,1),(17,1)]
for p,k in cases:
    print('CASE',p,k,direct(p,k))
# CRT test, not using local convolution: direct generic odd composite moduli
for q,factors in [(15,[(3,1),(5,1)]),(21,[(3,1),(7,1)]),(45,[(3,2),(5,1)]),(75,[(3,1),(5,2)]),(105,[(3,1),(5,1),(7,1)])]:
    c=Counter(((x+y)%q,(x**3+y**3)%q) for x in range(q) for y in range(q))
    expected_size=prod(size_formula(p,k) for p,k in factors)
    expected_energy=prod(energy_formula(p,k) for p,k in factors)
    assert len(c)==expected_size,(q,len(c),expected_size)
    assert sum(v*v for v in c.values())==expected_energy,(q,expected_energy)
    for (s,t),v in c.items():
        assert v==prod(local_fiber(p,k,s,t) for p,k in factors)
    print('CRT',q,expected_size,expected_energy)
print(f'VERIFY_OK local_cases={len(cases)} composite_cases=5 max_modulus={max(p**k for p,k in cases)}')
