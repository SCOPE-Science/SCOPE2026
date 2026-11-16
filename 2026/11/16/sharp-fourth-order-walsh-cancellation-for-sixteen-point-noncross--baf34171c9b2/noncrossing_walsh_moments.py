"""Independent exact inclusion-moment checker for noncrossing matching Walsh sums.

Run: python3 noncrossing_walsh_moments.py
This program enumerates Catalan matchings and all chord marginals of degree <=4.
It does not use the signed interval dynamic program of the C++ checker.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations

@lru_cache(None)
def noncrossing(a, b):
    if a == b:
        return ((),)
    return tuple(
        ((a, j),) + left + right
        for j in range(a + 1, b, 2)
        for left in noncrossing(a + 1, j)
        for right in noncrossing(j + 1, b)
    )


def run(n, degree):
    matchings = noncrossing(0, 2*n)
    edges = sorted({e for m in matchings for e in m})
    ix = {e:i for i,e in enumerate(edges)}
    marginals = Counter()
    for matching in matchings:
        positions = tuple(ix[e] for e in matching)
        for k in range(1, degree + 1):
            for sub in combinations(positions, k):
                marginals[sum(1 << j for j in sub)] += 1
    zeros = Counter()
    shapes = Counter()
    all_zeros = []
    for k in range(1, degree + 1):
        for support in combinations(range(len(edges)), k):
            bits = tuple(1 << i for i in support)
            signed = len(matchings)
            for h in range(1, k + 1):
                signed += (-2)**h * sum(
                    marginals[sum(part)] for part in combinations(bits, h)
                )
            if signed == 0:
                zeros[k] += 1
                if k == degree:
                    all_zeros.append(tuple(edges[i] for i in support))
                    deg = Counter(v for i in support for v in edges[i])
                    shapes[tuple(sorted(deg.values(), reverse=True))] += 1
    return len(matchings), len(edges), zeros, shapes, all_zeros

if __name__ == '__main__':
    for n in (4, 6, 8):
        c, e, z, shapes, zeros = run(n, n//2)
        print(f'n={n} Catalan={c} edges={e} zero_counts={dict(z)}')
        if n == 4:
            assert c == 14 and e == 16 and z == {2:32}
        if n == 6:
            assert c == 132 and e == 36 and z == {3:216}
        if n == 8:
            assert c == 1430 and e == 64 and z == {4:544}
            assert shapes == {(4,1,1,1,1):256,(3,2,1,1,1):288}
            print('four-chord support shapes:', dict(shapes))
    print('NONCROSSING_MATCHINGS_MOMENT_PASS')
