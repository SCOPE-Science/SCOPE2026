"""Independent finite tests of a conjugation-quandle medialization formula.
Requires Python 3.9+ only. Run: python verify.py
These tests supplement, rather than replace, the general proof.
"""
from itertools import permutations, product
from math import factorial
from collections import Counter


def inv(p):
    q = [0] * len(p)
    for i, j in enumerate(p):
        q[j] = i
    return tuple(q)


def mul(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2


def make_symmetric(n):
    elements = list(permutations(range(n)))
    # Both composition and inverse below are defined independently of the theorem.
    return elements, mul, inv, [p for p in elements if parity(p) == 0]


def make_dihedral(m=4):
    elements = list(product(range(m), range(2)))
    def mult(a, b):
        return ((a[0] + (1 if a[1] == 0 else -1) * b[0]) % m,
                (a[1] + b[1]) % 2)
    def inverse(a):
        return ((-a[0] * (1 if a[1] == 0 else -1)) % m, a[1])
    # D_8 derived subgroup <r^2>.
    return elements, mult, inverse, [(0, 0), (2, 0)]


def orbit_partition(elements, derived, mult, inverse):
    remaining = set(elements)
    groups = []
    while remaining:
        x = next(iter(remaining))
        orbit = frozenset(mult(mult(inverse(h), x), h) for h in derived)
        assert orbit <= remaining
        remaining -= orbit
        groups.append(orbit)
    return set(groups)


def brute_medial_partition(elements, mult, inverse):
    """Full medial-identity/congruence closure; not using the orbit theorem."""
    idx = {x: i for i, x in enumerate(elements)}
    size = len(elements)
    table = [[idx[mult(mult(inverse(y), x), y)] for y in elements] for x in elements]
    parent = list(range(size))
    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def join(a, b):
        a, b = root(a), root(b)
        if a == b:
            return False
        parent[b] = a
        return True
    while True:
        changed = False
        for a, b, c, d in product(range(size), repeat=4):
            changed |= join(table[table[a][b]][table[c][d]],
                            table[table[a][c]][table[b][d]])
        for a in range(size):
            for b in range(a + 1, size):
                if root(a) == root(b):
                    for c in range(size):
                        changed |= join(table[a][c], table[b][c])
                        changed |= join(table[c][a], table[c][b])
        if not changed:
            break
    classes = {}
    for i, x in enumerate(elements):
        classes.setdefault(root(i), set()).add(x)
    return {frozenset(s) for s in classes.values()}


def partition_count(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for j in range(1, n + 1):
        for k in range(j, n + 1):
            dp[k] += dp[k - j]
    return dp[n]


def odd_distinct_partition_count(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for j in range(1, n + 1, 2):
        for k in range(n, j - 1, -1):
            dp[k] += dp[k - j]
    return dp[n]


def verify_quotient(elements, part, mult, inverse):
    labels = {x: i for i, group in enumerate(part) for x in group}
    # Verify all quotient operations are well-defined, not only via their proof.
    for left_class in part:
        for right_class in part:
            values = {labels[mult(mult(inverse(y), x), y)]
                      for x in left_class for y in right_class}
            assert len(values) == 1
    classes = list(part)
    representatives = [next(iter(c)) for c in classes]
    def op(a, b):
        return labels[mult(mult(inverse(representatives[b]), representatives[a]), representatives[b])]
    # Convert arbitrary class labels into 0,...,k-1.
    indexes = {labels[representatives[i]]: i for i in range(len(classes))}
    table = [[indexes[op(a,b)] for b in range(len(classes))] for a in range(len(classes))]
    for a, b, c, d in product(range(len(classes)), repeat=4):
        assert table[table[a][b]][table[c][d]] == table[table[a][c]][table[b][d]]


def quotient_table(elements, part, mult, inverse):
    classes = sorted(part, key=lambda c: sorted(map(repr,c))[0])
    index = {x: i for i, c in enumerate(classes) for x in c}
    rep = [next(iter(c)) for c in classes]
    return [[index[mult(mult(inverse(rep[b]), rep[a]), rep[b])]
             for b in range(len(classes))] for a in range(len(classes))]


def count_aut(table):
    # Enumerate all bijections and test the entire quandle multiplication table.
    n = len(table)
    total = 0
    for f in permutations(range(n)):
        if all(f[table[a][b]] == table[f[a]][f[b]]
               for a in range(n) for b in range(n)):
            total += 1
    return total


def expected_aut_symmetric(n):
    # Cycle types index S_n conjugacy classes; sign = (-1)^(n - # cycles).
    all_types = set()
    for p in permutations(range(n)):
        visited = set()
        lengths = []
        for i in range(n):
            if i not in visited:
                j = i
                length = 0
                while j not in visited:
                    visited.add(j)
                    length += 1
                    j = p[j]
                lengths.append(length)
        all_types.add(tuple(sorted(lengths)))
    even = sum((n - len(t)) % 2 == 0 for t in all_types)
    odd = len(all_types) - even
    split = sum(len(set(t)) == len(t) and all(x % 2 == 1 for x in t)
                for t in all_types)
    assert split == odd_distinct_partition_count(n)
    return (2 ** split) * factorial(split) * factorial(even - split) * factorial(odd)


def main():
    for n in (3, 4):
        elems, mult, inverse, derived = make_symmetric(n)
        orbit = orbit_partition(elems, derived, mult, inverse)
        universal = brute_medial_partition(elems, mult, inverse)
        assert orbit == universal
        verify_quotient(elems, orbit, mult, inverse)
        expected = partition_count(n) + odd_distinct_partition_count(n)
        assert len(orbit) == expected
        observed_aut = count_aut(quotient_table(elems, orbit, mult, inverse))
        expected_aut = expected_aut_symmetric(n)
        assert observed_aut == expected_aut
        print(f'S_{n}: universal_medial_classes={len(universal)} aut={observed_aut} exact_partition_match=yes')

    elems, mult, inverse, derived = make_dihedral()
    orbit = orbit_partition(elems, derived, mult, inverse)
    universal = brute_medial_partition(elems, mult, inverse)
    assert orbit == universal and len(orbit) == 8
    verify_quotient(elems, orbit, mult, inverse)
    print('D_8: universal_medial_classes=8 exact_partition_match=yes')

    for n in (5, 6):
        elems, mult, inverse, derived = make_symmetric(n)
        orbit = orbit_partition(elems, derived, mult, inverse)
        expected = partition_count(n) + odd_distinct_partition_count(n)
        assert len(orbit) == expected
        # Burnside's lemma checked by independent centralizer counts.
        fixed_sum = sum(sum(mult(mult(inverse(h), x), h) == x for x in elems)
                        for h in derived)
        assert fixed_sum == len(derived) * len(orbit)
        verify_quotient(elems, orbit, mult, inverse)
        if n == 5:
            observed_aut = count_aut(quotient_table(elems, orbit, mult, inverse))
            assert observed_aut == expected_aut_symmetric(n)
            print(f'S_{n}: derived_orbits={len(orbit)} expected={expected} aut={observed_aut} burnside=yes')
        else:
            print(f'S_{n}: derived_orbits={len(orbit)} expected={expected} burnside=yes')
    print('VERIFY_OK finite_groups=5 full_medial_closures=3')

if __name__ == '__main__':
    main()
