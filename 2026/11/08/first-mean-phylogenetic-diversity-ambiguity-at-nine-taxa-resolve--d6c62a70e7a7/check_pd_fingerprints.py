"""Exact reproducibility checker for nine-tip mean/variance PD fingerprints.

Run: python3 check_pd_fingerprints.py
Uses only the Python standard library; all arithmetic is integer or Fraction.
"""
from functools import lru_cache
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb

LEAF = ()

@lru_cache(None)
def leaf_count(t):
    return 1 if t == LEAF else leaf_count(t[0]) + leaf_count(t[1])

@lru_cache(None)
def shapes(n):
    if n == 1:
        return (LEAF,)
    ans = []
    for a in range(1, n // 2 + 1):
        b = n - a
        for x in shapes(a):
            for y in shapes(b):
                if a < b or x <= y:
                    ans.append((x, y))
    return tuple(ans)

def edge_sizes(t):
    out = []
    def collect(u):
        out.append(leaf_count(u))
        if u != LEAF:
            collect(u[0]); collect(u[1])
    collect(t[0]); collect(t[1])
    return tuple(sorted(out))

def nested_counts(t):
    out = Counter()
    def visit(u, ancestors):
        size = leaf_count(u)
        for big in ancestors:
            out[(big, size)] += 1
        if u != LEAF:
            visit(u[0], ancestors + (size,))
            visit(u[1], ancestors + (size,))
    visit(t[0], ()); visit(t[1], ())
    return out

def clade_masks(t):
    out = []; idx = 0
    def rec(u):
        nonlocal idx
        if u == LEAF:
            bit = 1 << idx; idx += 1
            out.append(bit); return bit
        bit = rec(u[0]) | rec(u[1]); out.append(bit); return bit
    full = rec(t)
    assert full == (1 << leaf_count(t)) - 1
    out.remove(full)  # the root is not an edge
    return out

def polynomial_mean(t):
    coeff = Counter({0: 2 * leaf_count(t) - 2})
    for s in edge_sizes(t):
        coeff[s] -= 1
    return {power: count for power, count in coeff.items() if count}

def polynomial_variance(t):
    # q is the common extinction probability.
    coeff = Counter()
    for s in edge_sizes(t):
        coeff[s] += 1
        coeff[2*s] -= 1
    for (big, small), num in nested_counts(t).items():
        coeff[big] += 2 * num
        coeff[big + small] -= 2 * num
    return {power: count for power, count in coeff.items() if count}

def polydiff(a, b):
    return {k: a.get(k, 0) - b.get(k, 0) for k in set(a) | set(b)
            if a.get(k, 0) != b.get(k, 0)}

def independent_moments_at_half(t):
    # Completely independent 2^n survivor-configuration enumeration.
    masks = clade_masks(t)
    n = leaf_count(t)
    m1 = m2 = 0
    for survivors in range(1 << n):
        value = sum(bool(survivors & c) for c in masks)
        m1 += value
        m2 += value*value
    mean = Fraction(m1, 2**n)
    return mean, Fraction(m2, 2**n) - mean*mean

def main():
    expected_counts = {2: 1, 3: 1, 4: 2, 5: 3, 6: 6, 7: 11, 8: 23, 9: 46}
    pair = None
    for n in range(2, 10):
        all_trees = shapes(n)
        assert len(all_trees) == expected_counts[n]
        assert len(set(all_trees)) == len(all_trees)
        groups = defaultdict(list)
        for t in all_trees:
            groups[tuple(sorted(edge_sizes(t)))].append(t)
        colliding = [group for group in groups.values() if len(group) > 1]
        if n < 9:
            assert not colliding
        else:
            assert len(groups) == 45
            assert sorted(map(len, colliding)) == [2]
            pair = colliding[0]
        print('n=%d shapes=%d mean_fingerprints=%d' % (n, len(all_trees), len(groups)))
    a, b = pair
    assert a != b and leaf_count(a) == leaf_count(b) == 9
    assert edge_sizes(a) == edge_sizes(b) == (1,)*9+(2,)*3+(3,)+(4,)*2+(5,)
    assert polynomial_mean(a) == polynomial_mean(b) == {0: 16, 1: -9, 2: -3, 3: -1, 4: -2, 5: -1}
    assert polydiff(polynomial_variance(a), polynomial_variance(b)) == {7: -2, 8: 2}
    assert nested_counts(a)[(5,2)] == 2 and nested_counts(b)[(5,2)] == 1
    assert nested_counts(a)[(5,3)] == 0 and nested_counts(b)[(5,3)] == 1
    assert all((nested_counts(a)[key]-nested_counts(b)[key]) == 0
               for key in set(nested_counts(a)) | set(nested_counts(b))
               if key not in ((5,2),(5,3)))
    ma, va = independent_moments_at_half(a)
    mb, vb = independent_moments_at_half(b)
    assert ma == mb == Fraction(335, 32)
    assert va == Fraction(6483, 1024)
    assert vb == Fraction(6491, 1024)
    assert va - vb == -Fraction(1, 128)
    print('witness_A=',a)
    print('witness_B=',b)
    print('variance_A_minus_B=-2*q^7*(1-q)')
    print('at_q_half: mean=%s variance_A=%s variance_B=%s' % (ma, va, vb))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
