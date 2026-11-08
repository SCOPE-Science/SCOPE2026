"""Reproduce exact matching-polynomial and root-multiplicity checks for bouquets.
Only standard Python libraries are required. Run with: python3 verify.py
"""
from functools import lru_cache
from itertools import combinations_with_replacement
from math import prod

def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a): c[i] += v
    for i, v in enumerate(b): c[i] += v
    while len(c) > 1 and c[-1] == 0: c.pop()
    return c

def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b): c[i + j] += u * v
    return c

def shift(a): return [0] + a

def path_polys(n):
    p = [[1], [1]]
    for m in range(2, n + 1): p.append(add(p[-1], shift(p[-2])))
    return p

def flower_formula(lengths):
    p = path_polys(max(lengths) - 1)
    out = [1]
    for l in lengths: out = mul(out, p[l - 1])
    for i, l in enumerate(lengths):
        term = mul([0, 2], p[l - 2])
        for j, other in enumerate(lengths):
            if i != j: term = mul(term, p[other - 1])
        out = add(out, term)
    return out

def bouquet_edges(lengths):
    edges = []
    next_vertex = 1
    for l in lengths:
        path = list(range(next_vertex, next_vertex + l - 1))
        next_vertex += l - 1
        vertices = [0] + path
        edges += [tuple(sorted((vertices[i], vertices[(i + 1) % l]))) for i in range(l)]
    return edges

def independent_matching_enumerator(edges):
    # Edge-subset recursion independent of the hub decomposition.
    n = len(edges)
    incident = []
    for i, e in enumerate(edges):
        incident.append(sum(1 << j for j, f in enumerate(edges) if set(e) & set(f)))
    @lru_cache(None)
    def rec(mask):
        if not mask: return (1,)
        bit = mask & -mask
        i = bit.bit_length() - 1
        a = list(rec(mask ^ bit))
        b = [0] + list(rec(mask & ~incident[i]))
        return tuple(add(a, b))
    return list(rec((1 << n) - 1))

def at_minus_one(c): return sum(v * (-1)**i for i, v in enumerate(c))

def div_one_plus_x(c):
    assert len(c) > 1
    q = [0] * (len(c) - 1)
    q[-1] = c[-1]
    for i in range(len(c) - 2, 0, -1): q[i - 1] = c[i] - q[i]
    assert c[0] == q[0]
    return q

def order_and_lead(c):
    order = 0
    while at_minus_one(c) == 0:
        c = div_one_plus_x(c)
        order += 1
    return order, at_minus_one(c)

def expected_lead(lengths):
    zero = [l // 3 for l in lengths if l % 3 == 0]
    rest = [l for l in lengths if l % 3]
    p = path_polys(max(lengths))
    if not zero:
        return prod(at_minus_one(p[l - 1]) for l in lengths) * (1 - 2 * sum(l % 3 == 2 for l in lengths))
    # A denominator-free sum for the first nonzero Taylor coefficient.
    from fractions import Fraction
    lead = -2 * prod((-1)**(k - 1) * k for k in zero)
    lead *= prod(at_minus_one(p[l - 1]) for l in rest)
    return int(lead * sum((Fraction(1, k) for k in zero), Fraction(0)))

def main():
    count = 0
    for r in range(1, 5):
        for lengths in combinations_with_replacement(range(3, 10), r):
            if sum(lengths) > 19: continue
            q = flower_formula(lengths)
            brute = independent_matching_enumerator(bouquet_edges(lengths))
            assert q == brute, (lengths, q, brute)
            k = sum(l % 3 == 0 for l in lengths)
            mult, lead = order_and_lead(q)
            assert mult == max(k - 1, 0), (lengths, mult, k)
            assert lead == expected_lead(lengths), (lengths, lead, expected_lead(lengths))
            count += 1
    print('FULL_POLYNOMIAL_DIRECT_MATCHING_CHECK_OK', count, 'mixed-cycle bouquets')
    for r in range(1, 13):
        for l in range(3, 31):
            lengths = (l,) * r
            q = flower_formula(lengths)
            mult, lead = order_and_lead(q)
            assert mult == (r - 1 if l % 3 == 0 else 0)
            assert lead == expected_lead(lengths)
    print('ALL_EQUAL_LENGTH_FAMILIES_OK', 12 * 28)
    print('VERIFY_OK')

if __name__ == '__main__': main()
