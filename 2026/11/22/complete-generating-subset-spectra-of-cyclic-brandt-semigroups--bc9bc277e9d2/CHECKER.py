"""Independent small-instance tests of the cyclic Brandt generating-subset formula.
Run with: python3 brandtgeneration_check.py. Standard library only.
"""
from itertools import product
from collections import Counter
from math import comb
from random import Random


def strong(n, edges):
    reach = [[i == j for j in range(n)] for i in range(n)]
    for i, j in edges:
        reach[i][j] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    reach[i][j] = reach[i][j] or reach[k][j]
    return all(all(row) for row in reach)


def strong_polynomial(n):
    arcs = list(product(range(n), repeat=2))
    counts = Counter()
    for mask in range(1 << len(arcs)):
        active = [edge for a, edge in enumerate(arcs) if (mask >> a) & 1]
        if strong(n, active):
            counts[len(active)] += 1
    return counts


def mobius(k):
    ans = 1
    prime = 2
    while prime * prime <= k:
        if k % prime == 0:
            k //= prime
            if k % prime == 0:
                return 0
            ans = -ans
        prime += 1
    if k > 1:
        ans = -ans
    return ans


def divisors(m):
    return [d for d in range(1, m + 1) if m % d == 0]


def predicted(n, m):
    pol = strong_polynomial(n)
    out = Counter()
    for d in divisors(m):
        scale = mobius(m // d) * (m // d) ** (n - 1)
        for k, multiplicity in pol.items():
            for j in range(k + 1):
                signed = scale * multiplicity * (-1) ** (k - j) * comb(k, j)
                for s in range(j * d + 1):
                    out[s] += signed * comb(j * d, s)
    return {a: b for a, b in out.items() if b != 0}


def generated_semigroup(n, m, subset):
    zero = None
    values = set(subset)
    queue = list(values)
    # independent closure by multiplication; no graph or subgroup tests
    while queue:
        a = queue.pop()
        for b in list(values):
            for left, right in ((a, b), (b, a)):
                if left is None or right is None or left[2] != right[0]:
                    p = zero
                else:
                    p = (left[0], (left[1] + right[1]) % m, right[2])
                if p not in values:
                    values.add(p)
                    queue.append(p)
    return len(values) == n * n * m + 1


def directly_enumerated(n, m):
    elements = [(i, g, j) for i in range(n) for j in range(n) for g in range(m)]
    out = Counter()
    for mask in range(1 << len(elements)):
        if mask.bit_count() < n:
            continue
        subset = [x for j, x in enumerate(elements) if (mask >> j) & 1]
        if generated_semigroup(n, m, subset):
            out[len(subset)] += 1
    return dict(out)


def lifted_path_generates(n, m, subset):
    # Independent positive-word reachability in a gain-expanded digraph.
    by_source = [[] for _ in range(n)]
    for i, g, j in subset:
        by_source[i].append((g, j))
    for start in range(n):
        discovered = set()
        frontier = [(j, g) for g, j in by_source[start]]
        while frontier:
            j, h = frontier.pop()
            if (j, h) in discovered:
                continue
            discovered.add((j, h))
            for g, nxt in by_source[j]:
                if (nxt, (h + g) % m) not in discovered:
                    frontier.append((nxt, (h + g) % m))
        if len(discovered) < n * m:
            return False
    return True


def independently_lifted(n, m):
    elements = [(i, g, j) for i in range(n) for j in range(n) for g in range(m)]
    out = Counter()
    for mask in range(1 << len(elements)):
        if mask.bit_count() < n:
            continue
        subset = [x for j, x in enumerate(elements) if mask >> j & 1]
        if lifted_path_generates(n, m, subset):
            out[len(subset)] += 1
    return dict(out)


def main():
    for n, m in ((2, 1), (2, 2), (2, 3), (2, 4)):
        a, b = predicted(n, m), directly_enumerated(n, m)
        assert a == b, (n, m, a, b)
        expected = __import__('math').factorial(n - 1) * m ** (n - 1) * sum(1 for j in range(1, m + 1) if __import__('math').gcd(j, m) == 1)
        assert a.get(n, 0) == expected
        assert a.get(n * n * m, 0) == 1
        print(f'PASS n={n} m={m}: {sum(a.values())} generating nonzero subsets, all coefficients checked')
    n, m = 3, 2
    a = predicted(n, m)
    assert strong_polynomial(3) == {3: 2, 4: 15, 5: 39, 6: 48, 7: 30, 8: 9, 9: 1}
    assert a.get(3) == 8 and a.get(18) == 1
    b = independently_lifted(n, m)
    assert a == b, (n, m, a, b)
    print(f'PASS n={n} m={m}: {sum(a.values())} generating subsets, all coefficients independently checked')
    rng = Random(3845)
    elements = [(i, g, j) for i in range(n) for j in range(n) for g in range(m)]
    for _ in range(512):
        mask = rng.getrandbits(len(elements))
        subset = [x for j, x in enumerate(elements) if mask >> j & 1]
        if len(subset) < n:
            continue
        # Check a direct no-graph criterion using explicit path-gain closure.
        labels = {(i, g, j) for i, g, j in subset}
        changes = True
        while changes:
            newer = {(i, (g + h) % m, k) for i, g, j in labels for j2, h, k in labels if j == j2}
            changes = not newer.issubset(labels)
            labels |= newer
        assert generated_semigroup(n, m, subset) == (len(labels) == n * n * m)
    print('PASS n=3 m=2: full lifted-path polynomial, strong-digraph histogram, and 512 sampled closures')

if __name__ == '__main__':
    main()
