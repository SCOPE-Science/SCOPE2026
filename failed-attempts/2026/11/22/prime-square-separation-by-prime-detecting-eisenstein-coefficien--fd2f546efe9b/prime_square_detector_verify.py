#!/usr/bin/env python3
"""Independent finite cross-checks of a divisor-sum coefficient trichotomy.

Run: python3 prime_square_detector_verify.py
Uses only Python standard library. All comparisons use integers after squaring,
so no floating point tolerance is involved. Finite checks are not the proof.
"""
from math import isqrt


def primes_up_to(n):
    prime = bytearray(b'\x01')*(n+1)
    prime[0:2] = b'\x00\x00'
    for p in range(2,isqrt(n)+1):
        if prime[p]:
            prime[p*p:n+1:p] = b'\x00'*(((n-p*p)//p)+1)
    return prime


def divisors(n):
    ans=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            ans.append(d)
            if d*d!=n: ans.append(n//d)
    return ans


def coefficient_direct(n,r,s):
    ds=divisors(n)
    return (n**s+1)*sum(d**r for d in ds) - (n**r+1)*sum(d**s for d in ds)


def sigma_multiplicative(n,j):
    # Separately factor n, then form product of finite geometric sums.
    x=n
    p=2
    product=1
    while p*p<=x:
        if x%p==0:
            summand=1
            term=1
            while x%p==0:
                x//=p
                term*=p**j
                summand+=term
            product*=summand
        p+=1 if p==2 else 2
    if x>1: product*=1+x**j
    return product


def coefficient_proper(n,r,s):
    return sum((1+n**s)*d**r - (1+n**r)*d**s for d in range(2,n) if n%d==0)


def square_threshold_comparison(value,n,r,s):
    # Compare value with n**(s+r/2), by squares, all quantities nonnegative.
    return (value*value>n**(2*s+r)) - (value*value<n**(2*s+r))


def prime_square_bound(n,r,s):
    # Equivalent to n^(r/2)*(n^((s-r)/2)-1)*(n^((r+s)/2)-1),
    # tested by integer squaring (r,s odd -> all exponents integral).
    h=s-r
    assert h%2==0 and (r+s)%2==0
    m=n**(h//2)-1
    v=n**((r+s)//2)-1
    # bound^2 = n**r * (m*v)^2
    return n**r*(m*v)**2


def main():
    N=2400
    isprime=primes_up_to(N)
    tested=prime_tests=square_tests=other_tests=0
    first=[]
    for r in range(1,14,2):
        for s in range(r+2,16,2):
            for n in range(2,N+1):
                a=coefficient_direct(n,r,s)
                b=coefficient_proper(n,r,s)
                assert a==b, ('divisor form',r,s,n,a,b)
                c=(n**s+1)*sigma_multiplicative(n,r) - (n**r+1)*sigma_multiplicative(n,s)
                assert a==c, ('independent multiplicative method',r,s,n,a,c)
                p=isqrt(n)
                sq_prime=p*p==n and isprime[p]
                if isprime[n]:
                    assert a==0,(r,s,n,a)
                    prime_tests+=1
                elif sq_prime:
                    formula=p**r*(p**(s-r)-1)*(p**(r+s)-1)
                    assert a==formula,(r,s,n,a,formula)
                    assert 0<a*a<n**(2*s+r),(r,s,n,a)
                    assert a*a==prime_square_bound(n,r,s),(r,s,n,a)
                    square_tests+=1
                else:
                    assert a>0 and square_threshold_comparison(a,n,r,s)==1,(r,s,n,a)
                    assert a*a>prime_square_bound(n,r,s),(r,s,n,a)
                    other_tests+=1
                tested+=1
                if r==1 and s==3 and n<=15:
                    first.append((n,a,'prime' if isprime[n] else ('prime square' if sq_prime else 'other composite')))
    print('VERIFY_OK')
    print('parameter pairs: 28; indices per pair: 2399; tested:',tested)
    print('prime cases:',prime_tests,'prime-square cases:',square_tests,'other composite cases:',other_tests)
    print('sample for (r,s)=(1,3):',first)
    print('Exact integer equality and strict thresholds only; finite checks do not prove the infinite theorem.')

if __name__=='__main__': main()
