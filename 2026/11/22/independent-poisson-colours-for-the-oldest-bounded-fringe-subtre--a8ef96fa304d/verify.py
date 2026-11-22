"""Exact consistency checks for early small fringe subtrees in uniform recursive trees.

Standard-library only. Finite computations do not establish the Poisson limit.
"""
from fractions import Fraction
from itertools import product, combinations
from collections import Counter, defaultdict
from math import factorial, isqrt


def falling(a, k):
    v = 1
    for h in range(k):
        v *= a-h
    return v


def p_size(n, i, s):
    if s < 1 or s > n-i+1 or i < 2:
        return Fraction(0)
    return Fraction((i-1)*falling(n-i,s-1),falling(n-1,s))


def trees(n):
    for edges in product(*(range(1, v) for v in range(2,n+1))):
        par = (0,0) + edges
        descendants = [{j} for j in range(n+1)]
        for j in range(n,1,-1):
            descendants[par[j]].update(descendants[j])
        yield par, descendants


def subset_reduced_parent(par, verts):
    rank = {v: k+1 for k,v in enumerate(verts)}
    return tuple(rank[par[j]] for j in verts[1:])


def main():
    checks = 0
    for n in range(2,9):
        marginal = Counter()
        color_sets = defaultdict(Counter)
        outside_trees = defaultdict(Counter)
        inside_trees = defaultdict(Counter)
        total = factorial(n-1)
        for par, desc in trees(n):
            for i in range(2,n+1):
                s = len(desc[i])
                marginal[i,s] += 1
                D = tuple(sorted(desc[i]-{i}))
                color_sets[i,s][D] += 1
                outside = tuple(v for v in range(1,n+1) if v not in desc[i])
                inside = tuple(sorted(desc[i]))
                if len(outside) >= 1:
                    outside_trees[(i,s,D)][subset_reduced_parent(par,outside)] += 1
                inside_trees[(i,s,D)][subset_reduced_parent(par,inside)] += 1
        for i in range(2,n+1):
            for s in range(1,n+1):
                assert Fraction(marginal[i,s], total) == p_size(n,i,s), (n,i,s)
                checks += 1
                if p_size(n,i,s) == 0:
                    continue
                sets = color_sets[i,s]
                assert len(sets)==len(list(combinations(range(i+1,n+1),s-1)))
                assert len(set(sets.values()))==1
                checks += 2
                for D,c in sets.items():
                    outside = outside_trees.get((i,s,D))
                    if outside is not None:
                        assert len(outside)==factorial(n-s-1)
                        assert len(set(outside.values()))==1
                        checks += 2
                    inside = inside_trees[(i,s,D)]
                    assert len(inside)==factorial(s-1)
                    assert len(set(inside.values()))==1
                    checks += 2
    for n in (1000,10000,100000):
        t = 2.0
        m = min(n,int(t*n**0.5))
        for s in (1,2,3,4):
            mu=sum(p_size(n,i,s) for i in range(2,m+1))
            assert abs(float(mu)-2)<(15/n**0.5)
            checks+=1
    print('PASS:',checks,'exact and deterministic analytic consistency assertions')

if __name__=='__main__':
    main()
