#!/usr/bin/env python3
"""Finite cross-checks for sharp fixed-step anti-Niven progressions."""
from math import gcd, lcm

def factor_primes(n):
    ans=[]
    k=2
    while k*k<=n:
        if n%k==0:
            ans.append(k)
            while n%k==0:n//=k
        k+=1 if k==2 else 2
    if n>1:ans.append(n)
    return ans

def digit_sum(n,b):
    ans=0
    while n:
        n,r=divmod(n,b)
        ans+=r
    return ans

def case(b,d,p, full=False):
    assert d>=4 and d%2==0 and p>=5 and p not in factor_primes(d)
    assert b%2==1
    h=[p+r*d for r in range(p-1,0,-1)]
    C=h[0]+2
    assert b>C and all(gcd(b-1,x)==1 for x in h)
    smaller=[q for q in range(3,p,2) if len(factor_primes(q))==1 and factor_primes(q)[0]==q and (b-1)%q==0 and d%q!=0]
    assert not smaller
    s=[b-1-x for x in h]
    assert all(1<=x<b for x in s)
    ps=set().union(*(set(factor_primes(x)) for x in s))
    L=1
    for q in ps:
        if b%q:L=lcm(L,q-1)
    m=1+L
    R=b-C
    for j, sj in enumerate(s):
        assert digit_sum(R+j*d,b)==sj-1
        assert gcd(b-1,sj)==1
        assert all((pow(b,m,q)-b)%q==0 for q in factor_primes(sj))
        assert gcd(pow(b,m,sj)+R+j*d,sj)==1
        if full:
            N=pow(b,m)+R+j*d
            assert digit_sum(N,b)==sj
            assert gcd(N,sj)==1
    return m

if __name__=='__main__':
    cases=0
    max_length=0
    full_cases=0
    for p in (5,7,11,13):
        for d in range(4,25,2):
            if d%p==0: continue
            for u in (1,2,3):
                for a in (1,2,3):
                    b=(2**u)*(p**a)+1
                    if b<=p+(p-1)*d+2:continue
                    m=case(b,d,p,full=False)
                    cases+=1
                    max_length=max(max_length,p-1)
                    if b<=101 and m<=1500:
                        case(b,d,p,full=True)
                        full_cases+=1
    # Sieve-condition families that are not restricted to prime-power b-1.
    extra=0
    for b in range(25,4000,2):
        for d,p in ((4,5),(6,5),(4,7),(8,7)):
            if b<=p+(p-1)*d+2 or (b-1)%p:continue
            if any((b-1)%q==0 and d%q for q in (3,5) if q<p):continue
            H=[p+r*d for r in range(1,p)]
            if all(gcd(b-1,h)==1 for h in H):
                case(b,d,p)
                extra+=1
    # Specific symbolic witness, with 991 permitted by the order constraints.
    b,d,p=41,4,5
    h=[21,17,13,9]
    vals=[pow(b,991)+18+4*j for j in range(4)]
    sums=[digit_sum(x,b) for x in vals]
    assert sums==[19,23,27,31]
    assert all(gcd(x,s)==1 for x,s in zip(vals,sums))
    print(f'VERIFY_OK structured_cases={cases} direct_full_cases={full_cases} sieve_cases={extra} max_length={max_length} example_base41_sums={sums} exponent=991')
