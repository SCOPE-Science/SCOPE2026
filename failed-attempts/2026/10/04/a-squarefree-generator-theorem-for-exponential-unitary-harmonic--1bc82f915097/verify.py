#!/usr/bin/env python3
from math import gcd, isqrt

def factor(n):
    out={}; d=2
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1; n//=d
        d += 1 if d==2 else 2
    if n>1: out[n]=out.get(n,0)+1
    return out

def is_prime(n):
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

def squarefree(n): return all(e==1 for e in factor(n).values())
def unitary_divisors(a):
    return [d for d in range(1,a+1) if a%d==0 and gcd(d,a//d)==1]
def tau_eu_exp(a): return len(unitary_divisors(a))
def E(a,p): return sum(p**(a-d) for d in unitary_divisors(a))
def criterion(a,p,m):
    ee=E(a,p); t=tau_eu_exp(a); M=ee//gcd(ee,t)
    return squarefree(M) and m%M==0

def direct_harmonic_integer(a,p,m):
    ds=unitary_divisors(a)
    # divisors are m*p^d; H = count / sum reciprocal, tested by exact divisibility
    ee=sum(p**(a-d) for d in ds)
    return (p**a*m*len(ds))%ee==0

primes=[p for p in range(2,40) if is_prime(p)]
checked=0; hits=[]
for a in range(2,13):
    for p in primes:
        for m in range(1,501):
            if gcd(p,m)!=1 or not squarefree(m): continue
            d=direct_harmonic_integer(a,p,m)
            c=criterion(a,p,m)
            assert d==c,(a,p,m,E(a,p),tau_eu_exp(a),d,c)
            checked+=1
            if d and len(hits)<20: hits.append((a,p,m,p**a*m))
# exact spot checks
spots=[]
for a,p in [(2,2),(2,3),(4,2),(4,3),(6,2),(6,3),(8,2),(10,2)]:
    ee=E(a,p);t=tau_eu_exp(a);M=ee//gcd(ee,t)
    spots.append((a,p,ee,t,M,squarefree(M)))
assert spots[0][:6]==(2,2,3,2,3,True)
assert spots[1][:6]==(2,3,4,2,2,True)
assert spots[2][:6]==(4,2,9,2,9,False)
assert spots[3][:6]==(4,3,28,2,14,True)
assert spots[4][:6]==(6,2,57,4,57,True)
print('VERIFY_OK checked=%d hits=%s spots=%s' % (checked,hits[:12],spots))
