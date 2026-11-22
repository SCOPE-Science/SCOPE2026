#!/usr/bin/env python3
"""Direct finite verification of domination and add/delete components on F_2(K_{1,n})."""
from collections import Counter
from itertools import combinations
from math import comb


def graph(n):
    pairs = list(combinations(range(n), 2))
    N = n + len(pairs)
    closed = [1 << i for i in range(N)]
    for j, (a, b) in enumerate(pairs):
        e = n + j
        closed[a] |= 1 << e
        closed[b] |= 1 << e
        closed[e] |= (1 << a) | (1 << b)
    return closed


def predicted_poly(n):
    m = comb(n, 2)
    result = Counter()
    for j in range(m + 1):
        result[n + j] += comb(m, j)
    for j in range(m + 1):
        excluded = comb(m - n + 1, j) if j <= m - n + 1 else 0
        result[n - 1 + j] += n * (comb(m, j) - excluded)
    for r in range(2, n + 1):
        forced = comb(r, 2)
        for j in range(m - forced + 1):
            result[n - r + forced + j] += comb(n, r) * comb(m - forced, j)
    return +result


def predicted_components(n, budget):
    if budget < n - 1:
        return 0
    if budget == n - 1:
        return comb(n, 2)
    if budget == n:
        return comb(n, 2) + comb(n, 3) + 1
    return 1 + sum(comb(n, r) for r in range(4, n + 1)
                   if budget == n - r + comb(r, 2))


def run(n):
    closed = graph(n)
    N = len(closed)
    full = (1 << N) - 1
    dominating = set()
    poly = Counter()
    for mask in range(1 << N):
        reached = 0
        v = mask
        while v:
            bit = v & -v
            reached |= closed[bit.bit_length() - 1]
            v -= bit
        if reached == full:
            dominating.add(mask)
            poly[mask.bit_count()] += 1
    assert poly == predicted_poly(n), (n, poly, predicted_poly(n))
    tested = 0
    for budget in range(n - 1, min(N, n + 7) + 1):
        unseen = {m for m in dominating if m.bit_count() <= budget}
        components = 0
        while unseen:
            cur = [unseen.pop()]
            components += 1
            while cur:
                mask = cur.pop()
                for i in range(N):
                    candidate = mask ^ (1 << i)
                    if candidate in unseen:
                        unseen.remove(candidate)
                        cur.append(candidate)
        assert components == predicted_components(n, budget), (n, budget, components)
        tested += 1
    print('n', n, 'subsets', 1 << N, 'dominating', len(dominating),
          'component_budgets', tested, 'PASS')


if __name__ == '__main__':
    for n in range(2, 6):
        run(n)
    print('VERIFY_OK')
