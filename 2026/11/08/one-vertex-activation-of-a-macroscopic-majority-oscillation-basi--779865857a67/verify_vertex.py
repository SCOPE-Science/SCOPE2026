"""Exhaustive independent vertex-level check of majority dynamics on K(n,n,n+1).
Uses only Python 3 standard library. Run: python verify_vertex.py
"""
from math import comb


def update(bits, adj):
    out = 0
    for v, neighbors in enumerate(adj):
        ones = sum((bits >> w) & 1 for w in neighbors)
        if 2 * ones > len(neighbors):
            new = 1
        elif 2 * ones < len(neighbors):
            new = 0
        else:
            new = (bits >> v) & 1
        out |= new << v
    return out


def graph(n):
    sizes = (n, n, n + 1)
    part = [i for i, size in enumerate(sizes) for _ in range(size)]
    return [[v for v in range(len(part)) if part[u] != part[v]] for u in range(len(part))]


def count_formula(n):
    m = n + 1
    total = 0
    for a in range(n + 1):
        for b in range(n + 1):
            weight = comb(n, a) * comb(n, b)
            for c in range(m + 1):
                if ((a + b < n and c > n - min(a, b))
                        or (a + b > n and c <= n - max(a, b))
                        or (a + b == n and min(a, b) < c <= max(a, b))):
                    total += weight * comb(m, c)
    return total


def run():
    for n in range(1, 6):
        adj = graph(n)
        N = len(adj)
        osc = 0
        fixed_cycles = set()
        two_cycle_states = set()
        for initial in range(1 << N):
            x = initial
            y = update(x, adj)
            z = update(y, adj)
            w = update(z, adj)
            zz = update(w, adj)
            assert zz == z, ('not periodic by time two', n, initial)
            if z != w:
                osc += 1
                if initial == z or initial == w:
                    two_cycle_states.add(initial)
            else:
                fixed_cycles.add(z)
        expected = count_formula(n)
        assert osc == expected, (n, osc, expected)
        assert fixed_cycles == {0, (1 << N) - 1}, (n, fixed_cycles)
        expected_periodic = (1 << (n + 2)) - 2
        assert len(two_cycle_states) == expected_periodic, (n, len(two_cycle_states), expected_periodic)
        print(f'n={n}: states={1<<N}, two_cycle_basin={osc}, periodic_states={len(two_cycle_states)}, fixed_states={len(fixed_cycles)}, CHECK=OK')


if __name__ == '__main__':
    run()
