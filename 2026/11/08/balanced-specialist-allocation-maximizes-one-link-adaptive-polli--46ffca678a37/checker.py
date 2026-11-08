#!/usr/bin/env python3
"""Exact verification of three-guild adaptive one-edge repair reliability.

Enumerate survival subsets and the associated bipartite matching feasibility;
compare with the closed form and balanced optimality for small populations.
"""
from itertools import combinations
from fractions import Fraction
from math import comb


def matching_exists(hosts, alive, repair_budget=1):
    """Find a distinct-pollinator assignment to each of 3 hosts with <=1 added edge."""
    if len(alive) < 3:
        return False
    for trio in combinations(alive, 3):
        # Every assignment of three pollinators to the three hosts.
        from itertools import permutations
        for assn in permutations(trio):
            new_edges = sum(hosts[j] != h for h, j in enumerate(assn))
            if new_edges <= repair_budget:
                return True
    return False


def direct_probability(sizes, p):
    hosts = tuple(h for h, m in enumerate(sizes) for _ in range(m))
    n = len(hosts)
    q = 1-p
    total = Fraction(0)
    for mask in range(1 << n):
        alive = [j for j in range(n) if (mask >> j) & 1]
        if matching_exists(hosts, alive):
            total += p**len(alive) * q**(n-len(alive))
    return total


def formula_probability(sizes, p):
    n = sum(sizes)
    q = 1-p
    ideal = sum(comb(n, s) * p**s * q**(n-s) for s in range(3,n+1))
    one_class = sum(q**(n-m) * sum(comb(m,s)*p**s*q**(m-s) for s in range(3,m+1)) for m in sizes)
    return ideal - one_class


def all_compositions(n):
    for a in range(1,n-1):
        for b in range(1,n-a):
            yield (a,b,n-a-b)


def run():
    tested=0
    comparisons=0
    for n in range(3,10):
        profiles=list(all_compositions(n))
        bal=tuple(sorted((n//3+(j<(n%3)) for j in range(3))))
        for p in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
            opt=formula_probability(bal,p)
            for sz in profiles:
                actual=direct_probability(sz,p)
                exact=formula_probability(sz,p)
                assert actual==exact, (n,p,sz,actual,exact)
                tested+=1
                assert exact<=opt,(n,p,sz,exact,opt)
                comparisons+=1
                if tuple(sorted(sz))!=bal:
                    assert exact<opt,(n,p,sz)
                else:
                    assert exact==opt
    print(f'PASS {tested} exact matching-enumeration identities; {comparisons} balancing comparisons')
if __name__=='__main__':run()
