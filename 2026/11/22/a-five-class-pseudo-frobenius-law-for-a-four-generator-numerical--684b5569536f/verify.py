"""Independent exact-integer checks for a four-generator numerical semigroup family.

Usage: python verify.py. This verifies finite ranges only; it is not an
infinite proof and does not rely upon the candidate Apéry formula for paths.
"""
from heapq import heappush, heappop


def table(m):
    gens = [m, m + 1, 2 * m + 3, 3 * m + 5]
    dist = [None] * m
    dist[0] = 0
    hp = [(0, 0)]
    while hp:
        d, r = heappop(hp)
        if d != dist[r]:
            continue
        for g in gens:
            rr, dd = (r + g) % m, d + g
            if dist[rr] is None or dd < dist[rr]:
                dist[rr] = dd
                heappush(hp, (dd, rr))
    return gens, dist


def h(i):
    return (3 * i + 4) // 5


def genus_closed(m):
    q, r = divmod(m, 5)
    cr = (0, 0, 1, 3, 5)[r]
    return (15 * q * (q - 1)) // 2 + 8 * q + 3 * q * r + cr


def predicted_pf_indices(m):
    return sorted(set(
        [m - 1] +
        [i for i in [m - 3, m - 2] if i % 5 in (2, 4)] +
        [i for i in [m - 5, m - 4] if i % 5 == 2]
    ))


def full_gap_check(m, d):
    gens = [m, m + 1, 2 * m + 3, 3 * m + 5]
    frob = max(d) - m
    inside = [n >= d[n % m] for n in range(frob + max(gens) + 1)]
    pf = []
    for x in range(frob + 1):
        if not inside[x] and all(inside[x + g] for g in gens):
            pf.append(x)
    return pf, sum(not inside[x] for x in range(frob + 1))


aperies = 0
full = 0
for m in range(6, 1001):
    gens, d = table(m)
    expected = [m * h(i) + i for i in range(m)]
    assert d == expected, ('Apery', m)
    aperies += 1
    assert max(d) - m == m * h(m - 1) - 1, ('Frobenius', m)
    target = [d[i] - m for i in predicted_pf_indices(m)]
    actual = [d[i] - m for i in range(1, m) if all(
        d[i] + g > d[(i + g) % m] for g in gens[1:]
    )]
    assert sorted(actual) == sorted(target), ('PF', m)
    assert len(actual) == (2, 3, 3, 1, 2)[m % 5], ('type', m)
    assert genus_closed(m) == sum(h(i) for i in range(1, m)), ('closed genus', m)
    assert (2 * genus_closed(m) == max(d) - m + 1) == (m % 5 == 3), ('symmetric', m)
    if m <= 160:
        brute_pf, brute_genus = full_gap_check(m, d)
        assert sorted(brute_pf) == sorted(target), ('PF brute gaps', m)
        assert brute_genus == sum(h(i) for i in range(1, m)), ('genus', m)
        full += 1
print('PASS: independent shortest-path Apéry checks for', aperies, 'parameters (6..1000)')
print('PASS: independent exhaustive gap/PF/genus checks for', full, 'parameters (6..160)')
