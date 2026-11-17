"""Exact finite checks of generalized windmill Lipschitz variance formulas.

Requires only the Python standard library. This is corroborative,
not a substitute for the all-parameter proof.
"""
from fractions import Fraction
from itertools import combinations, product
from math import floor


def discrepancy(sizes):
    reachable = {0}
    for a in sizes:
        reachable = {z + a for z in reachable} | {z - a for z in reachable}
    return min(map(abs, reachable))


def predicted(sizes):
    total = sum(sizes)
    n = total + 1
    d = discrepancy(sizes)
    correction = max(0, 2 * d - n)
    return Fraction(n * total - d * d + correction * correction // 4, n * n)


def exact_vertexwise(sizes):
    # Enumerates ALL integral anchored feasible values, rather than
    # the aggregate signed capacities used in the mathematical proof.
    domains = []
    for a in sizes:
        domains.append(tuple(x for x in product((-1, 0, 1), repeat=a)
                             if max(x) - min(x) <= 1))
    n = 1 + sum(sizes)
    best = Fraction(-1)
    maximizers = []
    for blocks in product(*domains):
        values = (0,) + tuple(x for block in blocks for x in block)
        t = sum(x*x for x in values)
        s = sum(values)
        var = Fraction(n*t - s*s, n*n)
        if var > best:
            best, maximizers = var, [blocks]
        elif var == best:
            maximizers.append(blocks)
    return best, maximizers


def exact_aggregate(sizes):
    n = sum(sizes) + 1
    domains = [[(0,0)] + [(i,i) for i in range(1,a+1)] +
               [(i,-i) for i in range(1,a+1)] for a in sizes]
    best = Fraction(-1)
    for state in product(*domains):
        count = sum(t for t,s in state)
        balance = sum(s for t,s in state)
        best = max(best, Fraction(n*count-balance*balance,n*n))
    return best


def verify():
    vcount = 0
    for r in range(2,5):
        for sizes in combinations(range(1,9),r):
            if sum(sizes) > 9:
                continue
            expected = predicted(sizes)
            got, optimizers = exact_vertexwise(sizes)
            assert got == expected, (sizes, expected, got)
            assert optimizers
            vcount += 1
    print('INDEPENDENT_EXHAUSTIVE_VERTEXWISE_VALUES_OK', vcount)

    acount = 0
    for r in range(2,6):
        for sizes in combinations(range(1,10),r):
            if sum(sizes) > 13:
                continue
            assert exact_aggregate(sizes) == predicted(sizes), sizes
            acount += 1
    print('INDEPENDENT_EXACT_SIGNED_CAPACITY_STATES_OK', acount)

    allcases = 0
    for a in range(1,100):
        for b in range(1,100):
            total = a+b
            n = total+1
            d=abs(a-b)
            delta=max(0,2*d-n)
            expected=Fraction(n*total-d*d+delta*delta//4,n*n)
            best=Fraction(-1)
            for k in range(a+1):
                for l in range(b+1):
                    best=max(best,Fraction(n*(k+l)-(k-l)**2,n*n))
            assert best==expected,(a,b,best,expected)
            allcases+=1
    print('EXACT_TWO_BLADE_PHASE_IDENTITIES_OK',allcases)

    monotone=0
    for n in range(2,400):
        def numerator(d):
            v=max(0,2*d-n)
            return n*(n-1)-d*d+v*v//4
        for d in range(n-1):
            assert numerator(d)>numerator(d+1),(n,d)
            monotone+=1
    print('DISCREPANCY_ENVELOPE_STRICT_MONOTONICITY_OK',monotone)
    print('ALL_WINDMILL_PARTITION_DISCREPANCY_CHECKS_OK')

if __name__ == '__main__':
    verify()
