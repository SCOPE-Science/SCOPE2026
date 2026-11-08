"""Exact finite verification for unique-request packing and envy-free welfare.
Runs on Python 3 standard library. Exhaustive tests are finite consistency checks;
they do not substitute for the general packing or Poisson proofs.
"""
from itertools import combinations, product
from collections import Counter
from math import factorial
from fractions import Fraction
from random import Random


def predicted_optimum(m, demands):
    counts = Counter(demands)
    unique = [p for p,c in counts.items() if c == 1]
    masks = [sum(1 << g for g in p) for p in unique]
    def rec(i, used):
        if i == len(masks):
            return 0
        x = rec(i + 1, used)
        if not (used & masks[i]):
            x = max(x, 1 + rec(i + 1, used | masks[i]))
        return x
    return rec(0, 0)


def direct_optimum(m, demands):
    n = len(demands)
    reqs = [sum(1 << g for g in pair) for pair in demands]
    best = 0
    for owners in product(range(n), repeat=m):
        bundles = [0]*n
        for g, agent in enumerate(owners):
            bundles[agent] |= 1 << g
        utilities = [int((bundles[i] & req) == req) for i,req in enumerate(reqs)]
        score = sum(utilities)
        if score <= best:
            continue
        if all(utilities[i] or all((bundle & reqs[i]) != reqs[i] for bundle in bundles)
               for i in range(n)):
            best = score
    return best


def factorial_moment_of_singletons(M,n,j):
    if j > min(M,n): return Fraction(0)
    fall = lambda a,b: factorial(a)//factorial(a-b)
    return Fraction(fall(M,j)*fall(n,j)*(M-j)**(n-j), M**n)


def probability_no_unique_demand(M,n):
    return sum((-1)**j * factorial_moment_of_singletons(M,n,j)/factorial(j)
               for j in range(min(M,n)+1))


def main():
    tested = 0
    cases = [(2,2,[2,3]),(3,2,[3,4]),(4,2,[4,5]),(4,3,[4,5])]
    for m,r,ns in cases:
        options = list(combinations(range(m),r))
        for n in ns:
            for demands in product(options, repeat=n):
                p = predicted_optimum(m, demands)
                d = direct_optimum(m, demands)
                assert p == d, (m,r,n,demands,p,d)
                tested += 1
            print('Exhaustive',m,r,n,len(options)**n)
    rng = Random(20260923)
    for m,r,n,samples in [(5,2,5,100),(5,3,5,100),(5,4,5,100),
                          (5,2,7,60),(6,3,6,20),(6,2,6,20)]:
        options = list(combinations(range(m),r))
        for _ in range(samples):
            demands = [rng.choice(options) for _ in range(n)]
            p = predicted_optimum(m, demands)
            d = direct_optimum(m, demands)
            assert p == d, (m,r,n,demands,p,d)
            tested += 1
        print('Seeded',m,r,n,samples)
    for M,n in [(3,3),(3,4),(4,4),(6,4),(6,5),(6,6)]:
        zero=0;moments={1:0,2:0}
        for outcomes in product(range(M),repeat=n):
            counts=Counter(outcomes)
            s=sum(counts[k]==1 for k in range(M))
            zero+=(s==0)
            for j in (1,2):
                moments[j]+=factorial(s)//factorial(s-j) if s>=j else 0
        assert Fraction(zero,M**n)==probability_no_unique_demand(M,n)
        for j in (1,2):
            assert Fraction(moments[j],M**n)==factorial_moment_of_singletons(M,n,j)
        print('Occupancy identity',M,n)
    print('PASS',tested,'finite demand profiles and six exact occupancy cases')

if __name__=='__main__':main()
