#!/usr/bin/env python3
"""Exact-integer checks for Schemmel-totient prime-power sign classification."""
from math import gcd, isqrt


def prime(n):
    if n < 2:
        return False
    for d in range(2,isqrt(n)+1):
        if n%d==0:
            return False
    return True


def primes_up_to(n):
    return [p for p in range(2,n+1) if prime(p)]


def L(m,n):
    if n==0:
        return 0
    if n==1:
        return 1
    out=1
    t=n
    for p in range(2,isqrt(t)+1):
        if t%p==0:
            if p<=m:
                return 0
            e=0
            while t%p==0:
                t//=p
                e+=1
            out*=p**(e-1)*(p-m)
    if t>1:
        if t<=m:
            return 0
        out*=t-m
    return out


def D(m,n):
    if n==1:
        return 0
    total=0
    t=n
    while t>1:
        t=L(m,t)
        total+=t
    return total


def boundary(m):
    out=1
    for p in primes_up_to(3*m):
        if p<=m:
            continue
        e=1
        while p**e*(p-m)<=2*m:
            e+=1
        out*=p**e
    return max(m,out)


def run():
    local=0
    for m in [2,4,6,8,10,12]:
        P=1
        for q in primes_up_to(m):
            P*=q
        B=boundary(m)
        # Reconstruct the critical escape bound: only divisors of T can have tiny positive L.
        for t in range(m+1,2800):
            ell=L(m,t)
            if gcd(t,P)==1 and ell<=2*m:
                assert t<=B, (m,t,B,ell)
                local+=1
        for p in primes_up_to(251):
            if p<=m:
                continue
            t=p-m
            ell=L(m,t)
            if gcd(t,P)>1:
                for a in range(1,4):
                    assert D(m,p**a)<p**a, (m,p,a,D(m,p**a))
                    local+=1
            elif ell>2*m and p>2*m:
                for a in range(1,4):
                    assert D(m,p**a)>p**a,(m,p,a,D(m,p**a))
                    local+=1
            if p>m+B:
                for a in range(1,4):
                    assert (D(m,p**a)>p**a)==(gcd(t,P)==1),(m,p,a)
                    local+=1
    exception=[]
    m4=0
    for p in primes_up_to(701):
        for a in range(1,4):
            v=D(4,p**a)
            assert v!=p**a
            expect=(p>=13 and p%3==2)
            if (v>p**a)!=expect:
                exception.append((p,a,v))
            m4+=1
    assert not exception,exception
    assert D(4,29)==31 and D(4,59)==65
    assert D(4,11)==10
    # Finite direct counting checks for the exact Euler-product numerator.
    density=[]
    for m in [2,4,6,8,10,12]:
        P=1
        den=1
        num=1
        for q in primes_up_to(m):
            P*=q
            if m%q:
                num*=q-2
                den*=q-1
        good=sum(1 for r in range(1,P+1) if gcd(r,P)==1 and gcd(r-m,P)==1)
        phi=sum(1 for r in range(1,P+1) if gcd(r,P)==1)
        assert good*den==phi*num, (m,good,phi,num,den)
        density.append((m,num,den))
    print('VERIFY_OK: local threshold and prime-power signs:',local,'checks; global m=4:',m4,'prime powers; density factors:',density)

if __name__=='__main__':
    run()
