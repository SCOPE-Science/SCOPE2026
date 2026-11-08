"""Finite checks for two-point extension witnesses in Kneser graphs."""
from itertools import combinations
from math import comb

def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0

def formula(n, r):
    assert r >= 2 and n >= 3*r
    joint_adjacent = choose(n - 2*r, r)
    mixed = choose(n-r-1, r-1)
    joint_nonadjacent = (choose(n, r) - 2*choose(n-r, r)
                         + choose(n-2*r, r))
    return (joint_adjacent, mixed, joint_nonadjacent)

def counts_for_pair(sets, a, b):
    out = [0, 0, 0, 0]
    for c in sets:
        if c in (a,b):
            continue
        aa = int((a&c) == 0)
        bb = int((b&c) == 0)
        out[2*aa + bb] += 1
    return out

def exhaustive(n, r):
    sets = [sum(1 << j for j in I) for I in combinations(range(n),r)]
    minima = [len(sets)+1]*4
    for i,a in enumerate(sets):
        for b in sets[i+1:]:
            c = counts_for_pair(sets,a,b)
            minima = [min(p,q) for p,q in zip(minima,c)]
    J,M,Z = formula(n,r)
    assert minima == [Z,M,M,J], (n,r,minima,[Z,M,M,J])
    return minima

if __name__ == '__main__':
    cases = 0
    for r, hi in [(2,11),(3,11)]:
        for n in range(3*r,hi+1):
            minima = exhaustive(n,r)
            assert min(minima)==min(formula(n,r))
            print(f'exhaustive r={r} n={n}: patterns (00,01,10,11)={minima}; threshold={min(minima)} PASS')
            cases += 1
    assert [min(formula(n,2)) for n in range(6,15)] == [1,3,4,4,4,4,4,4,4]
    print(f'exhaustive pair parameters: {cases}; r=2 closed phase diagram PASS')
    # Check the three formula branches, positivity, and large-n dominance.
    for r in range(2,9):
        for n in range(3*r,3*r+80):
            J,M,Z = formula(n,r)
            assert min(J,M,Z)>0
            assert choose(n-r-1,r)-choose(n-2*r,r)-1>=0
            assert choose(n-2*r,r-1)>=2
        n=10000
        J,M,Z=formula(n,r)
        assert Z < min(J,M)
    print('formula positivity and eventual joint-nonadjacency bottleneck for 7 widths PASS')
    print('ALL CHECKS PASS')
