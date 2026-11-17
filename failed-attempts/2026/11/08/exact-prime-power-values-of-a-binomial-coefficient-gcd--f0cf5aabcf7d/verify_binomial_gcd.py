"""Exact integer verification of the binomial GCD prime-power formula.

Run with Python 3.10+; no third-party packages are required.
Finite tests are consistency checks and are not proofs of the unrestricted theorem.
"""
from math import comb, gcd


def factor(n):
    ans = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            a = 0
            while n % d == 0:
                n //= d
                a += 1
            ans.append((d,a))
        d += 1 if d == 2 else 2
    if n > 1:
        ans.append((n,1))
    return ans


def floor_log(n,p):
    assert n >= 1
    t=0
    while n >= p:
        n //= p
        t += 1
    return t


def valuation_binom_legendre(N,K,p):
    total=0
    power=p
    while power <= N:
        total += N//power-K//power-(N-K)//power
        power *= p
    return total


def valuation_binom_carries(N,K,p):
    left=K
    right=N-K
    carries=0
    incoming=0
    while left or right:
        digit=left%p+right%p+incoming
        incoming=int(digit>=p)
        carries+=incoming
        left//=p
        right//=p
    return carries


def exponent(n,p,a):
    return max(0,a-floor_log(n//p**a,p))


def predicted(n):
    out=1
    for p,a in factor(n):
        out *= p**exponent(n,p,a)
    return out


def witness(n,p,a):
    A=p**a
    b=n//A
    assert A>b
    if b==1:
        return 2
    t=floor_log(b,p)
    s=b%(p**t) if t else 1
    assert 1<=s<=b-1
    q=1+A*s
    assert 2<=q<=n
    return q


def main():
    direct_count=0
    for n in range(3,101):
        k=n-1
        g=0
        for q in range(2,n+1):
            g=gcd(g,comb(q*k,k))
        assert g == predicted(n), (n,g,predicted(n))
        direct_count+=1
    print('DIRECT_GCD_OK n=3..100 cases=',direct_count)

    components=0
    pairs=0
    for n in range(3,701):
        K=n-1
        for p,a in factor(n):
            e=exponent(n,p,a)
            minimum=10**9
            for q in range(2,n+1):
                val=valuation_binom_carries(q*K,K,p)
                if val<minimum:
                    minimum=val
                if n<=60:
                    assert val==valuation_binom_legendre(q*K,K,p),(n,p,q)
                pairs+=1
            assert minimum==e,(n,p,a,e,minimum)
            components+=1
    print('KUMMER_MINIMUM_OK n=3..700 components=',components,'valuation_pairs=',pairs)

    count=0
    for n in range(3,5001):
        for p,a in factor(n):
            e=exponent(n,p,a)
            if e==0:
                continue
            q=witness(n,p,a)
            assert valuation_binom_legendre(q*(n-1),n-1,p)==e,(n,p,q,e)
            count+=1
    print('EXPLICIT_WITNESS_OK n=3..5000 positive_components=',count)
    print('SAMPLES n=12:',predicted(12),'n=24:',predicted(24),'n=36:',predicted(36),'n=72:',predicted(72),'n=100:',predicted(100))
    print('VERIFY_OK exact_integer=yes independent_carry_and_factorial_methods=yes')


if __name__=='__main__':
    main()
