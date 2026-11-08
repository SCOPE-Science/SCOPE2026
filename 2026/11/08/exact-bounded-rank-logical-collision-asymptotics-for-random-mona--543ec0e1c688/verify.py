"""Reproduce finite logical-type collision coefficients and the critical scale."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial, lgamma, log, sqrt


def coefficient(M, n, q):
    f = {(a, b): Fraction(1, factorial(a) * factorial(b))
         for a in range(n + 1) for b in range(n + 1)
         if (a == b and a < q) or (a >= q and b >= q)}
    dp = {(0, 0): Fraction(1)}
    for _ in range(M):
        ndp = {}
        for (i, j), weight in dp.items():
            for (a, b), w in f.items():
                if i + a <= n and j + b <= n:
                    key = (i + a, j + b)
                    ndp[key] = ndp.get(key, Fraction(0)) + weight * w
        dp = ndp
    return dp.get((n, n), Fraction(0)) * Fraction(factorial(n)**2, M**(2*n))


def direct(M, n, q):
    buckets = Counter()
    for sample in product(range(M), repeat=n):
        counts = Counter(sample)
        signature = tuple(min(counts[i], q) for i in range(M))
        buckets[signature] += 1
    return Fraction(sum(v*v for v in buckets.values()), M**(2*n))


def rank_one_stirling(M, n):
    prev = [0]*(n+1)
    prev[0] = 1
    for r in range(1, n+1):
        cur = [0]*(n+1)
        for j in range(1, r+1):
            cur[j] = prev[j-1]+j*prev[j]
        prev=cur
    total=sum(comb(M,j)*(factorial(j)*prev[j])**2 for j in range(min(M,n)+1))
    return Fraction(total,M**(2*n))


def log_critical_probability(M):
    n = int(M*log(2))
    prev = [0]*(n+1)
    prev[0] = 1
    for i in range(1,n+1):
        cur = [0]*(n+1)
        for j in range(1,i+1):
            cur[j] = prev[j-1]+j*prev[j]
        prev=cur
    v=[]
    for j in range(1,min(M,n)+1):
        if prev[j]:
            v.append(lgamma(M+1)-lgamma(j+1)-lgamma(M-j+1)+2*(lgamma(j+1)+log(prev[j])))
    mx=max(v)
    from math import exp
    return mx+log(sum(exp(z-mx) for z in v))-2*n*log(M)


def main():
    tests=0
    for M,nmax in [(2,5),(4,5),(8,3)]:
        for n in range(nmax+1):
            for q in (1,2,3):
                exact=direct(M,n,q)
                algebra=coefficient(M,n,q)
                assert exact == algebra, (M,n,q,exact,algebra)
                if q == 1:
                    assert exact == rank_one_stirling(M,n)
                tests+=1
    print('FINITE_LOGICAL_COLLISION_ENUMERATION_PASS cases='+str(tests))
    limit=1/sqrt(1-log(2)**2)
    for M in (32,64,128,256):
        ratio=__import__('math').exp(log_critical_probability(M)+M*log(2))
        print(f'CRITICAL_RATIO M={M} n={int(M*log(2))} observed={ratio:.10f} limit={limit:.10f}')
    assert abs(__import__('math').exp(log_critical_probability(256)+256*log(2))-limit)<0.07
    print('CRITICAL_SCALE_NUMERICAL_CHECK_PASS')
    print('ALL_MONADIC_COLLISION_CHECKS_PASS')

if __name__=='__main__':
    main()
