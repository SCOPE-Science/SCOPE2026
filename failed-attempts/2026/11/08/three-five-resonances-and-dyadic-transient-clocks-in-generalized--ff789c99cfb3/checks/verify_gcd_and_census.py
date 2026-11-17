"""Standalone GF(2) polynomial gcd and small-state first-entry census."""
from collections import Counter

def deg(a): return a.bit_length()-1

def rem(a,b):
    while deg(a)>=deg(b): a^=b<<(deg(a)-deg(b))
    return a

def gcd(a,b):
    while b:a,b=b,rem(a,b)
    return a

def v_rank(n):
    # x^6+x^4+x^3+x^2+1, unit x^-3 gives det(A)
    P=(1<<6)|(1<<4)|(1<<3)|(1<<2)|1
    g=gcd(P,(1<<n)|1)
    return deg(g)

def step(s,n):
    out=0
    for i in range(n):
        u=(s>>((i-1)%n)&1)^(s>>((i+1)%n)&1)^(s>>(n+i)&1)
        v=(s>>i&1)^(s>>(n+(i-2)%n)&1)^(s>>(n+(i+2)%n)&1)
        out|=u<<i|v<<(n+i)
    return out

def expected_d(n,t):
    h=n&-n
    return 2*(n%3==0)*min(t,2*h)+4*(n%5==0)*min(t,h)

for n in range(5,501):
    assert v_rank(n)==2*(n%3==0)+4*(n%5==0),n
print('POLYNOMIAL_GCD_496_CASES_OK')
for n in range(5,9):
    h=n&-n; R=2*n-expected_d(n,2*h)
    T=2*h if n%3==0 else h if n%5==0 else 0
    count=Counter()
    for s in range(1<<(2*n)):
        orbit=[];idx={};v=s
        while v not in idx:
            idx[v]=len(orbit);orbit.append(v);v=step(v,n)
        count[idx[v]]+=1
    assert sum(count.values())==1<<(2*n)
    for t in range(T+1):
        wanted=(1<<R) if t==0 else (1<<R)*((1<<expected_d(n,t))-(1<<expected_d(n,t-1)))
        assert count[t]==wanted,(n,t,count[t],wanted)
    assert max(count)==T,(n,count)
    print('FULL_STATES_OK',n,'total',1<<(2*n),'transient_classes',sorted(count.items()))
print('EXHAUSTIVE_STATE_CENSUS_OK')
