"""Reproducible finite tests for rare balanced modal count predicates.

Run with Python 3 standard library: python checker.py.
The analytic limit is proved separately; finite tests are not that proof.
"""
import itertools
import math
from fractions import Fraction
from collections import Counter


def category_probability(n, a):
    if abs(a) > n or (n-a) % 2:
        return Fraction(0)
    return Fraction(math.comb(n, (n+a)//2), 2**n)


def exact_comparison(n, a, b, comparator):
    pa, pb = category_probability(n, a), category_probability(n, b)
    if a == b:
        raise ValueError('distinct offsets required')
    q = 1 - pa - pb
    answer = Fraction(0)
    for i in range(n+1):
        for j in range(n+1-i):
            if comparator(i, j):
                coefficient = math.comb(n, i)*math.comb(n-i, j)
                answer += coefficient*pa**i*pb**j*q**(n-i-j)
    return answer


def brute_comparison(n, a, b, comparator):
    successes = 0
    for bits in itertools.product((0, 1), repeat=n*n):
        offsets = [2*sum(bits[i*n:(i+1)*n])-n for i in range(n)]
        successes += comparator(offsets.count(a), offsets.count(b))
    return Fraction(successes, 2**(n*n))


def brute_gated_formula(n):
    successes=0
    for bits in itertools.product((0, 1), repeat=n*n):
        offsets=[2*sum(bits[i*n:(i+1)*n])-n for i in range(n)]
        counts=Counter(offsets)
        works=((counts[0]>=counts[2] and counts[0]>=1)
               or (counts[1]>=counts[3] and counts[1]>=1))
        successes += works
    return Fraction(successes, 2**(n*n))


def exact_gated_formula(n):
    a,b=(0,2) if n%2==0 else (1,3)
    return exact_comparison(n,a,b,lambda i,j:i>=1 and i>=j)


def approx_probability(n, a):
    if abs(a)>n or (n-a)%2:
        return 0.0
    k=(n+a)//2
    return math.exp(math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)-n*math.log(2))


def floating_difference_distribution(n, a, b):
    pa, pb = approx_probability(n, a), approx_probability(n, b)
    q=1-pa-pb
    dist=[1.0]
    for step in range(n):
        nxt=[0.0]*(2*step+3)
        for index,prob in enumerate(dist):
            nxt[index] += pb*prob
            nxt[index+1] += q*prob
            nxt[index+2] += pa*prob
        dist=nxt
    return dist


def main():
    for n in range(1, 5):
        for a, b in [(-2, 0), (0, 2), (-1, 1), (0, 1)]:
            for comparison in [lambda x, y:x == y, lambda x, y:x >= y,
                               lambda x, y:x-y >= 1, lambda x, y:x-y >= 2,
                               lambda x, y:x-y >= -1]:
                exact=exact_comparison(n, a, b, comparison)
                brute=brute_comparison(n, a, b, comparison)
                assert exact==brute, (n,a,b,exact,brute)
    for n in range(1,5):
        assert brute_gated_formula(n)==exact_gated_formula(n)
    c=math.sqrt(2/math.pi)
    tie_constant=1/(2*math.sqrt(math.pi*c))
    weak_constant=tie_constant/2
    # Numeric asymptotic diagnostics for a=0,b=2 on even branching.
    observations=[]
    for n in (100, 400, 1600):
        dist=floating_difference_distribution(n,0,2)
        tie=dist[n]
        weak=sum(dist[n:])
        observations.append((n,n**0.25*tie,n**0.25*(weak-0.5)))
    assert abs(observations[-1][1]-tie_constant) < 0.005
    assert abs(observations[-1][2]-weak_constant) < 0.02
    print('EXACT_FINITE_CASES_OK')
    print('Expected tie constant:', format(tie_constant, '.12f'))
    print('Expected weak-comparison constant:', format(weak_constant, '.12f'))
    for n in (2, 4):
        for h in (-1, 0, 1, 2):
            assert exact_comparison(n, 0, 2, lambda x, y:x-y>=h) == brute_comparison(n, 0, 2, lambda x,y:x-y>=h)
    for n,tie,weak in observations:
        print('n=',n,'scaled tie=',format(tie,'.9f'),'scaled weak excess=',format(weak,'.9f'))
    print('ALL_CHECKS_OK')


if __name__=='__main__':
    main()
