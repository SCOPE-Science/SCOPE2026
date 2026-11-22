#!/usr/bin/env python3
"""Independent finite checks of a quadratic near-identity cycle census.

No third-party modules are needed. Brute-force cycles are computed directly
from the defining permutation; moments and type histograms are compared to
independently evaluated exact formulas. Finite tests are not infinite proofs.
"""
from collections import Counter
from fractions import Fraction


def roots(p, j, a):
    if j == 0:
        return 1
    h = 0
    while h < j and a % p**(h+1) == 0:
        h += 1
    if h == j:
        return p**(j//2)
    if h % 2:
        return 0
    unit = (a // p**h) % p
    return 2*p**(h//2) if pow(unit, (p-1)//2, p) == 1 else 0


def predicted(p, n, a):
    L = n-1
    r = [roots(p,j,a) for j in range(L+1)]
    return tuple(([p*r[L]] + [p*r[L-t]-r[L-t+1]
                                    for t in range(1,n)]))


def direct(p, n, a):
    mod = p**n
    seen = bytearray(mod)
    counts = Counter()
    for start in range(mod):
        if seen[start]:
            continue
        x = start
        period = 0
        while not seen[x]:
            seen[x] = 1
            period += 1
            x = (x + p*(x*x-a)) % mod
        assert x == start, (p, n, a, start, x)
        counts[period] += 1
    return tuple(counts[p**t] for t in range(n))


def expected_cov(p, n, s, t):
    L=n-1
    b=Fraction(p-1,p)
    if s>t:
        s,t=t,s
    if s==t==0:
        return p*p*b*L
    if s==t:
        return b*((p-1)**2*(L-t)+1)
    j=L-t
    if s==0:
        return p*b*((p-1)*j-1)
    return b*(p-1)*((p-1)*j-1)


def check_moments(p,n):
    P=p**(n-1)
    v=[predicted(p,n,a) for a in range(P)]
    m=[sum(x[t] for x in v) for t in range(n)]
    means=[Fraction(z,P) for z in m]
    assert means==[p]+[p-1]*(n-1)
    for s in range(n):
        for t in range(n):
            actual=Fraction(sum(x[s]*x[t] for x in v),P)-means[s]*means[t]
            want=expected_cov(p,n,s,t)
            assert actual==want,(p,n,s,t,actual,want)
    types=Counter(v)
    assert len(types)==n+(n-1+1)//2, (p,n,len(types))
    # Every parameter stratum has the predicted frequency.
    L=n-1
    assert types[predicted(p,n,0)]==1
    for h in range(L):
        a=p**h
        if h&1:
            assert types[predicted(p,n,a)]==(p-1)*p**(L-h-1)
        else:
            square=p**h
            nonres=next(u for u in range(1,p) if pow(u,(p-1)//2,p)==p-1)
            assert types[predicted(p,n,square)]==((p-1)//2)*p**(L-h-1)
            assert types[predicted(p,n,nonres*p**h)]==((p-1)//2)*p**(L-h-1)
    return len(types)


def main():
    primes=(3,5,7,11)
    brute_count=0
    moments_count=0
    for p in primes:
        for n in range(2,6):
            if p**n<=50000:
                for a in range(min(p**(n-1),600)):
                    assert direct(p,n,a)==predicted(p,n,a),(p,n,a)
                    brute_count+=1
            if p**(n-1)<=2000:
                check_moments(p,n)
                moments_count+=1
    assert brute_count>=2000 and moments_count>=10
    print('PASS:',brute_count,'direct permutation-cycle checks; ',
          moments_count,'exact parameter moment/type checks')
    for p,n in ((3,5),(5,4)):
        print('Example',p,n,'C(a=0)=',predicted(p,n,0))

if __name__=='__main__':
    main()
