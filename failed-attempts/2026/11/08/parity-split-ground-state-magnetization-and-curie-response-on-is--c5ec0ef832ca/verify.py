"""Independent finite checks for parity-resolved Ising antiprism ground states.

Run: python3 verify.py
Requires Python 3.8+ standard library only.
"""
from collections import defaultdict, Counter
from itertools import product


def predicted(n):
    if n < 3:
        raise ValueError('Antiprism requires n >= 3')
    if n % 2 == 0:
        return {0: 4}, n
    return {-2: n * (n - 1) // 2,
            0: n * (n + 1),
            2: n * (n - 1) // 2}, n + 1


def from_legs(n):
    """Brute-force independent edge-list calculation for modest n."""
    N = 2 * n
    edges = set()
    for i in range(n):
        edges.add(tuple(sorted((i, (i + 1) % n))))
        edges.add(tuple(sorted((n + i, n + (i + 1) % n))))
        edges.add(tuple(sorted((i, n + i))))
        edges.add(tuple(sorted((i, n + (i - 1) % n))))
    assert len(edges) == 4 * n
    best = 10**9
    sector_counts = Counter()
    for s in product((-1, 1), repeat=N):
        broken = sum(s[u] == s[v] for u, v in edges)
        if broken < best:
            best = broken
            sector_counts.clear()
        if broken == best:
            sector_counts[sum(s)] += 1
    return dict(sector_counts), best


def from_cycle_transfer(n):
    """Minimum-energy DP for C_(2n)^2, grouping by magnetization.

    Maintains independent initial and final spin pairs. States retain
    only the smallest broken-bond count within each magnetization class.
    """
    N = 2 * n
    candidates = {}
    for a, b in product((-1, 1), repeat=2):
        states = {(a, b, a + b): (int(a == b), 1)}
        for i in range(2, N):
            new_states = {}
            for (x, y, mag), (cost, ways) in states.items():
                for z in (-1, 1):
                    key = (y, z, mag + z)
                    value = cost + int(y == z) + int(x == z)
                    prev = new_states.get(key)
                    if prev is None or value < prev[0]:
                        new_states[key] = (value, ways)
                    elif value == prev[0]:
                        new_states[key] = (value, prev[1] + ways)
            states = new_states
        for (x, y, mag), (cost, ways) in states.items():
            value = cost + int(y == a) + int(x == a) + int(y == b)
            old = candidates.get(mag)
            if old is None or value < old[0]:
                candidates[mag] = (value, ways)
            elif value == old[0]:
                candidates[mag] = (value, old[1] + ways)
    optimal = min(v[0] for v in candidates.values())
    return {m: ways for m, (cost, ways) in candidates.items() if cost == optimal}, optimal


def test():
    checks = 0
    for n in range(3, 10):
        observed = from_legs(n)
        expected = predicted(n)
        assert observed == expected, ('legs', n, observed, expected)
        checks += 1
    for n in range(3, 81):
        observed = from_cycle_transfer(n)
        expected = predicted(n)
        assert observed == expected, ('transfer', n, observed, expected)
        counts, broken = observed
        assert sum(counts.values()) == (4 if n % 2 == 0 else 2 * n * n)
        assert broken == n + n % 2
        checks += 3
        # Zero-field equal-weight susceptibility: var(total spin)
        var = sum(m*m*ways for m, ways in counts.items())
        assert var * n == (0 if n % 2 == 0 else 2 * (n - 1) * sum(counts.values()))
        checks += 1
    print(f'PASS: {checks} independent exact checks; n=3..80 for transfer and n=3..9 brute force')


if __name__ == '__main__':
    test()
