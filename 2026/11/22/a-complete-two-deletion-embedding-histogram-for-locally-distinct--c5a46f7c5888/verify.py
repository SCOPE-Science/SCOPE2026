#!/usr/bin/env python3
"""Verify exact two-insertion embedding histograms for locally distinct words.

No external dependencies. Both enumeration methods count indexed embeddings.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb


def predicted(q, m):
    n = m + 2
    n4 = comb(m, 2)
    n3 = 2 * m - 1
    n2 = n * (m * (q - 2) + 1)
    sphere = sum(comb(n, j) * (q - 1)**j for j in range(3))
    n1 = sphere - n2 - n3 - n4
    return Counter({1:n1, 2:n2, 3:n3, 4:n4})


def insertion_histogram(y, q):
    n = len(y) + 2
    multiplicities = defaultdict(int)
    for i, j in combinations(range(n), 2):
        for a in range(q):
            for b in range(q):
                z = list(y)
                z.insert(i, a)
                z.insert(j, b)
                multiplicities[tuple(z)] += 1
    return Counter(multiplicities.values()), multiplicities


def embedding_count(y, x):
    dp = [0] * (len(y) + 1)
    dp[0] = 1
    for a in x:
        for i in range(len(y) - 1, -1, -1):
            if y[i] == a:
                dp[i+1] += dp[i]
    return dp[-1]


def full_host_histogram(y, q):
    return Counter(embedding_count(y, x) for x in product(range(q), repeat=len(y)+2) if embedding_count(y, x) > 0)


def local_distinct(y):
    return all(y[i] != y[j] for i in range(len(y)) for j in range(max(0, i-2), i))


def check():
    total_patterns = total_hosts = total_embeddings = 0
    for q, max_m in [(3, 8), (4, 6), (5, 5)]:
        by_m = []
        for m in range(1, max_m + 1):
            patterns = 0
            for y in product(range(q), repeat=m):
                if not local_distinct(y):
                    continue
                got, indexed = insertion_histogram(y, q)
                want = predicted(q, m)
                assert got == want, (q, m, y, got, want)
                assert sum(k * v for k, v in got.items()) == q*q*comb(m+2, 2)
                assert sum(got.values()) == sum(comb(m+2, j)*(q-1)**j for j in range(3))
                expected_triples = {tuple(y[:i] + (y[i], y[i], y[i]) + y[i+1:]) for i in range(m)}
                expected_abab = {tuple(y[:i] + (y[i],y[i+1],y[i],y[i+1]) + y[i+2:]) for i in range(m-1)}
                expected_doublets = {tuple(y[:i+1]+(y[i],)+y[i+1:j+1]+(y[j],)+y[j+1:]) for i in range(m) for j in range(i+1,m)}
                assert {x for x, e in indexed.items() if e==3} == expected_triples | expected_abab, (q,m,y,'three')
                assert {x for x, e in indexed.items() if e==4} == expected_doublets, (q,m,y,'four')
                # Independently enumerate all potential hosts for small instances.
                if (q==3 and m<=6) or (q==4 and m<=4) or (q==5 and m<=3):
                    actual=full_host_histogram(y,q)
                    assert actual==want,(q,m,y,actual,want)
                    total_hosts+=q**(m+2)
                total_embeddings += q*q*comb(m+2,2)
                total_patterns +=1
                patterns +=1
            by_m.append(patterns)
        print(f'q={q}: validated all local-distinct patterns by m=1..{max_m}; counts {by_m}')
    # Boundary checks show the local hypothesis matters.
    for y in ((0,1,0),(0,0,1)):
        got, _ = insertion_histogram(y, 3)
        assert got != predicted(3, len(y))
        print(f'boundary y={y}: {dict(sorted(got.items()))} differs from local-distinct formula')
    print(f'PASS: {total_patterns} distinct patterns, {total_embeddings} indexed insertion histories, '
          f'{total_hosts} independent full-host DP evaluations.')

if __name__ == '__main__':
    check()
