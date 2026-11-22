#!/usr/bin/env python3
"""Exact, standard-library verification of all prime-characteristic cut ranks.

Each test is finite. The proof for all primes uses the integer-minor
Hadamard bound stated below, not extrapolation from sample primes.
"""
from itertools import combinations
from collections import Counter
from math import comb

N = 12

def graph():
    neighbors = [set() for _ in range(N)]
    def edge(x, y):
        assert x != y
        neighbors[x].add(y)
        neighbors[y].add(x)
    a = lambda i: 1 + i % 5
    b = lambda i: 6 + i % 5
    for i in range(5):
        edge(0, a(i)); edge(11, b(i))
        edge(a(i), a(i+1)); edge(b(i), b(i+1))
        edge(a(i), b(i)); edge(a(i), b(i-1))
    assert all(len(x) == 5 for x in neighbors)
    assert sum(map(len, neighbors)) == 60
    return neighbors

def rank_mod(matrix, p):
    if not matrix: return 0
    arr = [[v % p for v in row] for row in matrix]
    n, nc = len(arr), len(arr[0])
    r = 0
    for j in range(nc):
        i = next((i for i in range(r, n) if arr[i][j]), None)
        if i is None: continue
        arr[r], arr[i] = arr[i], arr[r]
        inv = pow(arr[r][j], -1, p)
        arr[r] = [v * inv % p for v in arr[r]]
        for i in range(r + 1, n):
            if arr[i][j]:
                c = arr[i][j]
                arr[i] = [(v - c*w) % p for v, w in zip(arr[i], arr[r])]
        r += 1
        if r == n: break
    return r

def isprime(k):
    return k >= 2 and all(k % d for d in range(2, int(k ** .5) + 1))

BASE = {
    0: {0: 1}, 1: {1: 12}, 2: {2: 66}, 3: {3: 220},
    4: {3: 15, 4: 480}, 5: {4: 120, 5: 672}
}
BALANCED = {
    2: {4: 172, 5: 240, 6: 512},
    5: {4: 140, 5: 264, 6: 520},
    'other': {4: 140, 5: 252, 6: 532},
}

def main():
    G = graph()
    # Every r-by-r integer 0/1 subdeterminant, r<=6, has
    # |det| <= (sqrt(r))**r <= 216 by Hadamard's inequality.
    # A nonzero rational-rank minor remains nonzero mod any p>216.
    # The prime 223 exceeds 216 and so gives the rational rank.
    primes = [p for p in range(2, 217) if isprime(p)] + [223]
    sums = {p: [Counter() for _ in range(7)] for p in primes}
    for k in range(7):
        for left in combinations(range(N), k):
            L = set(left)
            right = [v for v in range(N) if v not in L]
            M = [[int(j in G[i]) for j in right] for i in left]
            for p in primes:
                sums[p][k][rank_mod(M, p)] += 1
    for p in primes:
        for k in range(6):
            assert dict(sums[p][k]) == BASE[k], (p, k, sums[p][k])
        exp = BALANCED.get(p, BALANCED['other'])
        assert dict(sums[p][6]) == exp, (p, sums[p][6])
        for k in range(7):
            assert sum(sums[p][k].values()) == comb(N, k)
    # The twelve five-primary exceptional cuts are the pentagon of
    # neighbors of a vertex together with its unique antipode.
    pentagonal_cuts = set()
    for v in range(N):
        distance = {v: 0}; frontier = [v]
        for x in frontier:
            for y in G[x]:
                if y not in distance:
                    distance[y] = distance[x] + 1
                    frontier.append(y)
        antipodes = [u for u, d in distance.items() if d == 3]
        assert len(antipodes) == 1
        L = tuple(sorted(G[v] | set(antipodes)))
        pentagonal_cuts.add(L)
        R = [u for u in range(N) if u not in L]
        M = [[int(u in G[w]) for u in R] for w in L]
        assert rank_mod(M, 5) == 5
        assert rank_mod(M, 7) == 6
    assert len(pentagonal_cuts) == 12
    print('PASS: twelve exceptional characteristic-five cuts are antipodal pentagon unions')
    print('PASS: all 4096 labeled bipartitions represented by cuts k<=6')
    print('PASS: exact ranks for all', len(primes), 'primes <=216 and 223')
    print('PASS: Hadamard bound 216 excludes new prime-rank defects above 216')
    for p in (2, 5, 7, 223):
        print('characteristic', p, 'balanced ranks:', sorted(sums[p][6].items()))
    print('PASS: full icosahedral prime-characteristic cut-rank classification')

if __name__ == '__main__': main()
