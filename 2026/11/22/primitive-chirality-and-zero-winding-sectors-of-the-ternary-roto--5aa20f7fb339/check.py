#!/usr/bin/env python3
"""Exact standard-library comparison of symbolic cyclic-orbit enumerations."""
import itertools
import math

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def mobius(n):
    if n == 1:return 1
    fac=0;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;fac+=1
            if n%p==0:return 0
            while n%p==0:n//=p
        p+=1
    if n>1:fac+=1
    return -1 if fac%2 else 1

def T(n):
    return sum(mobius(n//d)*(2**d+2*(-1)**d) for d in divisors(n))//n

def Z(n):
    return 3*sum(mobius(n//d)*math.comb(d,d//2) for d in divisors(n) if d%2==0)//n

def A(n):
    return 3*sum(mobius(n//d)*2**(d//2) for d in divisors(n) if d%2==0)//2

def canon(a):
    return min(a[k:]+a[:k] for k in range(len(a)))

def winding(a):
    n=len(a)
    return sum(1 if (a[(i+1)%n]-a[i])%3==1 else -1 for i in range(n))//3

def run():
    tests=0
    for n in range(2,13):
        seen=set()
        for a in itertools.product(range(3),repeat=n):
            if any(a[i]==a[(i+1)%n] for i in range(n)):
                continue
            if any(all(a[i]==a[i%d] for i in range(n)) for d in divisors(n) if d<n):
                continue
            seen.add(canon(a))
        ach={a for a in seen if canon(a[::-1])==a}
        zero={a for a in seen if winding(a)==0}
        expected=(T(n),Z(n),A(n))
        actual=(len(seen),len(zero),len(ach))
        assert expected==actual,(n,expected,actual)
        assert ach<=zero,(n,'reversal implies zero winding')
        if n==8: assert (len(seen),len(zero),len(ach),len(zero-ach))==(30,24,18,6)
        print(n,expected)
        tests+=3
    print('PASS: 33 independently enumerated orbit-population comparisons across n=2..12')

if __name__=='__main__':run()
