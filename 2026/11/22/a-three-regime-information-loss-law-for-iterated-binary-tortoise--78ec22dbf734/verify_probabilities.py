"""Independent composition census and log-fiber asymptotic checks.
Validates source-weighted finite distributions without enumerating strings.
"""
from collections import defaultdict
from math import comb, log2, lgamma, log


def composition_spectrum(n,k):
    assert 1<=k<=n
    counter=defaultdict(int)
    for r in range(k):
        f=comb(n,r)
        counter[f]+=1
    counter[comb(n,k)]+=1
    for H in range(n-k):
        f=comb(H+k,k)
        counter[f]+=1<<(n-k-H-1)
    return counter


def exact_checks():
    num=0
    for n in range(1,101):
        for k in range(1,n+1):
            classes=composition_spectrum(n,k)
            assert sum(m for m in classes.values())==k+(1<<(n-k))
            assert sum(m*size for size,m in classes.items())==(1<<n)
            assert max(classes)==comb(n,min(k,n//2))
            num+=1
    print(f'SPECTRUM_OK {num} (n,k) pairs, n=1..100, all-class mass and extremal fertility')


def entropy(n,k):
    h=composition_spectrum(n,k)
    expectedlog=sum((m*size)*log2(size) for size,m in h.items())/(1<<n)
    return n-expectedlog


def empirical_limits():
    print('n,ratio,shannon_rate,hartley_rate,limit_shannon,limit_hartley')
    for n in (100,200,400,800):
        for a in (.25,.5,.75):
            k=round(a*n)
            shannon=entropy(n,k)/n
            hartley=log2(k+2**(n-k))/n
            print(f'{n},{a:.2f},{shannon:.6f},{hartley:.6f},{max(1-2*a,0):.6f},{1-a:.6f}')

if __name__=='__main__':
    exact_checks()
    empirical_limits()
