"""Independent adjacency-list enumeration for deterministic binary majority dynamics.

Run: python3 code/direct_enumeration.py
Only standard Python 3 is needed. Every labeled state is visited.
"""
from math import comb


def update(state, neighbors):
    out = 0
    for vertex, ns in enumerate(neighbors):
        ones = sum((state >> u) & 1 for u in ns)
        old = (state >> vertex) & 1
        bit = int(2 * ones > len(ns)) if 2 * ones != len(ns) else old
        out |= bit << vertex
    return out


def expected(c, s):
    central = comb(c, c // 2) * comb(s, s // 2) if c % 2 == s % 2 == 0 else 0
    imbalance = comb(c, (c - s) // 2) if c > s and (c - s) % 2 == 0 else 0
    periodic_states = 2 * int(s >= c) + 2 * imbalance + central
    return 2, periodic_states // 2


count_cases = count_states = count_two = 0
for c in range(1, 7):
    for s in range(1, 7):
        n = c + s
        neighbors = [tuple(v for v in range(n) if v != u) if u < c
                     else tuple(range(c)) for u in range(n)]
        fixed = periodic2 = 0
        largest_entry = 0
        for state in range(1 << n):
            cur = state
            seq = [cur]
            for _ in range(5):
                cur = update(cur, neighbors)
                seq.append(cur)
            fixed += int(seq[0] == seq[1])
            periodic2 += int(seq[0] == seq[2])
            entry = next((t for t in range(4) if seq[t] == seq[t + 2]), None)
            assert entry is not None, (c, s, state, seq)
            largest_entry = max(largest_entry, entry)
        fexp, cexp = expected(c, s)
        assert (fixed, (periodic2 - fixed) // 2) == (fexp, cexp), (c, s, fixed, periodic2, fexp, cexp)
        if c > s >= 3 and (c - s) % 2 == 0:
            assert largest_entry == 3, (c, s, largest_entry)
        count_cases += 1
        count_states += 1 << n
        count_two += (periodic2 - fixed) // 2
print(f"PASS independent adjacency enumeration: {count_cases} parameter pairs, {count_states} labeled initial states")
print(f"PASS predicted fixed/cycle census and first-periodic-entry <=3; summed primitive orbits: {count_two}")
for c, s in [(2, 2), (4, 2), (5, 3), (6, 4), (5, 6), (8, 8)]:
    print(f"sample c={c}, s={s}, fixed=2, two_cycle_orbits={expected(c,s)[1]}")
