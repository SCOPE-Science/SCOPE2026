"""Finite corroboration of sharp sixfold covering for reduced prime-power squares."""
from itertools import combinations
from random import Random
from math import isqrt

def primes(limit):
    return [n for n in range(7,limit+1) if all(n%d for d in range(2,isqrt(n)+1))]

def qres(p,a):
    n=p**a
    return sorted({(x*x)%n for x in range(n) if x%p})

def sumcovers(A,n,s=6):
    values={0}
    for _ in range(s):
        values={(u+v)%n for u in values for v in A}
    return len(values)==n

def run():
    deterministic=0
    for p in primes(19):
        Q=qres(p,1); k=len(Q)//2+1
        for A in combinations(Q,k):
            assert sumcovers(A,p), (p,A)
            deterministic+=1
    assert not sumcovers((1,2),7,5)
    assert sumcovers((1,2),7,6)
    rng=Random(20261019)
    stochastic=0
    for p,a,tests in [(7,2,80),(7,3,30),(11,2,80),(13,2,80)]:
        Q=qres(p,a);n=p**a;k=len(Q)//2+1
        for _ in range(tests):
            A=rng.sample(Q,k)
            assert sumcovers(A,n), (p,a,A)
            stochastic+=1
    print(f'CERTIFICATE_OK exhaustive_prime_case={deterministic} sampled_prime_power_case={stochastic} sharpness_mod7=true')

if __name__ == '__main__':
    run()
