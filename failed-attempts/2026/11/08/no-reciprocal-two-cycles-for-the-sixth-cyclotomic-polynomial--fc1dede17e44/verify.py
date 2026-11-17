#!/usr/bin/env python3
"""Independent exact-arithmetic checks for sixth-cyclotomic reciprocal rigidity."""
from math import gcd, isqrt
from fractions import Fraction

def f(a):
    return a*a-a+1

def factors(n):
    d=2; out={}
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1
            n//=d
        d+=1 if d==2 else 2
    if n>1:out[n]=out.get(n,0)+1
    return out

def h(n):
    z=1
    for p,e in factors(n).items():
        z*=(p**(2*e+1)+1)//(p+1)
    return z

def main():
    pairs=0
    for a in range(1,5001):
        N=f(a)
        for d in range(1,isqrt(N)+1):
            if N%d:continue
            for b in {d,N//d}:
                if a!=1 or b!=1:
                    assert f(b)%a != 0
                else:
                    assert a==b==1
                pairs+=1
    print('RECIPROCAL_DIVISORS_OK a<=5000, divisor_pairs=',pairs)
    for n in range(1,351):
        s=sum((Fraction(1,gcd(k,n)) for k in range(1,n+1)),Fraction(0))
        assert s == Fraction(h(n),n),(n,s)
    print('GCD_SUM_IDENTITY_OK n=1..350')
    first=614341
    ff=factors(first)
    assert ff=={7:1,13:1,43:1,157:1},ff
    assert h(first)%first==0
    assert all(p%6==1 for p in ff)
    assert all(any(q!=p and f(q)%p==0 for q in ff) for p in ff)
    print('KNOWN_EXAMPLE_OK n=',first,'prime_factors=',list(ff),'integer_sum=',h(first)//first)
    print('VERIFY_OK exact_integer_and_rational=yes')
if __name__=='__main__': main()
