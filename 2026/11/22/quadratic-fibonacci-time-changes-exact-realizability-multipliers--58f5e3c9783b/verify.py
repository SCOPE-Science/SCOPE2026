"""Independent finite checks for Fibonacci quadratic-sample realizability theorem.
No numerical test in this file substitutes for the infinite proof.
"""
from math import gcd


def fib_mod(n, m):
    def pair(k):
        if not k:
            return (0,1)
        a,b=pair(k//2)
        c=a*(2*b-a)%m
        d=(a*a+b*b)%m
        return (d,(c+d)%m) if k&1 else (c,d)
    return pair(n)[0]


def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a


def primes_upto(n):
    return [p for p in range(2,n+1) if all(p%d for d in range(2,int(p**.5)+1))]


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]


def mobius(n):
    if n==1:return 1
    ans=1; x=n; p=2
    while p*p<=x:
        if x%p==0:
            x//=p
            if x%p==0:return 0
            ans=-ans
            while x%p==0: x//=p
        p+=1
    if x>1:ans=-ans
    return ans


def test():
    primes=primes_upto(149)
    checked=0
    for a in range(1,11):
        for b in range(0,9):
            for c in range(0,9):
                for p in primes:
                    if p==5:continue
                    x=fib_mod(a*p*p+b*p+c,p)
                    y=fib_mod(a+b+c,p)
                    F=fib_mod(b,p)
                    r=a+c
                    L=(2*fib_mod(r+1,p)-fib_mod(r,p))%p
                    want=0 if p%5 in (1,4) else (-F*L)%p
                    assert (x-y)%p==want,(a,b,c,p,x,y,want)
                    checked+=1
    local=0
    for a in range(1,16):
        for c in range(0,12):
            for p in primes[:8]:
                for k in range(1,5):
                    for n in (1,2,3,5,7):
                        if gcd(n,p)>1:continue
                        m=p**k
                        scalar=1 if a%5==0 else 5
                        x=scalar*fib_mod(a*(n*p**k)**2+c,m)%m
                        y=scalar*fib_mod(a*(n*p**(k-1))**2+c,m)%m
                        assert x==y,(a,c,p,k,n,x,y)
                        local+=1
    dold=0
    for a in range(1,13):
        for c in range(0,8):
            fs={e:fib(a*e*e+c) for e in range(1,81)}
            M=1 if a%5==0 else 5
            for n in range(1,81):
                v=sum(mobius(n//e)*fs[e] for e in divisors(n))
                assert (M*v)%n==0,(a,c,n,v)
                assert v>0,(a,c,n,v)
                dold+=1
            x=(fib_mod(25*a+c,5)-fib_mod(a+c,5))%5
            assert (x==0)==(a%5==0),(a,c,x)
    print(f"PASS prime-index quadratic identities: {checked} cases")
    print(f"PASS prime-power local Dold comparisons: {local} cases")
    print(f"PASS positive integral orbit counts: {dold} cases")
    print("PASS exact fifth-prime multiplier cutoff for 96 coefficient pairs")


if __name__=='__main__': test()
