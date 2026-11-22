#!/usr/bin/env python3
"""Exact finite checks for uniform unrooted biclique forests and Cayley cores."""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
from math import comb, factorial


def cayley(n):
    return 1 if n == 1 else n ** (n - 2)


def falling(b, k):
    out = 1
    for j in range(k):
        out *= b - j
    return out if k <= b else 0


def n_two_component_trees(a):
    return sum(comb(a, s) * cayley(s) * cayley(a-s)
               for s in range(1, a)) // 2


def second_coefficient(a):
    ordinary = n_two_component_trees(a)
    triple = 0 if a == 2 else (comb(a, 3) if a == 3
                                  else 3 * comb(a, 3) * a**(a-4))
    return ordinary + triple


def leading(a, b):
    return cayley(a) * falling(b, a-1) * (a+1) ** (b-a+1)


def second(a, b):
    return second_coefficient(a) * falling(b, a-2) * (a+1)**(b-a+2)


@lru_cache(None)
def forests_by_root_component(a, b):
    """Independent component decomposition, anchored at one vertex of first side."""
    if a == 0 or b == 0:
        return 1
    z = 0
    for i in range(1, a+1):
        for j in range(b+1):
            tree = (1 if i == 1 else 0) if j == 0 else i**(j-1) * j**(i-1)
            z += (comb(a-1, i-1) * comb(b, j) * tree
                  * forests_by_root_component(a-i, b-j))
    return z


def acyclic_neighborhoods(a, masks):
    """Union-find check for ordinary B vertices represented by A-neighborhoods."""
    par = list(range(a))
    def root(x):
        while x != par[x]:
            x = par[x]
        return x
    for mask in masks:
        ix = [i for i in range(a) if mask & (1 << i)]
        if len(ix) < 2:
            continue
        roots = [root(i) for i in ix]
        if len(set(roots)) != len(roots):
            return False
        for y in roots[1:]:
            par[y] = roots[0]
    return True


def coefficients_by_special_pattern(a):
    """Independent incidence-hyperforest enumeration of all special B profiles."""
    larger = [m for m in range(1 << a) if m.bit_count() >= 2]
    counts = {0: 1}
    def go(masks):
        k = len(masks)
        if k:
            counts[k] = counts.get(k, 0) + 1
        if k == a-1:
            return
        for mask in larger:
            t = masks + (mask,)
            if acyclic_neighborhoods(a, t):
                go(t)
    go(())
    return counts


def full_neighborhood_count(a, b, counts):
    """For chosen special B labels, count ordered profiles and ordinary choices."""
    return sum(comb(b, k) * t * (a+1)**(b-k)
               for k, t in counts.items() if k <= b)


def direct_graph_brute(a, b):
    """Enumerate every edge subset, including isolated vertices, directly."""
    edges = [(i, a+j) for i in range(a) for j in range(b)]
    total = dominant = near = 0
    for mask in range(1 << len(edges)):
        par = list(range(a+b))
        def rt(i):
            while i != par[i]:
                i = par[i]
            return i
        degb = [0] * b
        ok = True
        for t, (u, v) in enumerate(edges):
            if mask >> t & 1:
                ru, rv = rt(u), rt(v)
                if ru == rv:
                    ok = False
                    break
                par[rv] = ru
                degb[v-a] += 1
        if not ok:
            continue
        total += 1
        k = sum(x >= 2 for x in degb)
        if k == a-1:
            assert sorted(x for x in degb if x >= 2) == [2]*(a-1)
            dominant += 1
        elif k == a-2:
            near += 1
    return total, dominant, near


def main():
    for a in range(2, 6):
        cs = coefficients_by_special_pattern(a)
        assert cs[a-1] == factorial(a-1)*cayley(a), (a, cs)
        assert cs[a-2] == factorial(a-2)*second_coefficient(a), (a, cs)
        for b in range(a-1, 11):
            via_patterns = full_neighborhood_count(a, b, cs)
            via_components = forests_by_root_component(a, b)
            assert via_patterns == via_components, (a, b, via_patterns, via_components)
        print('PATTERN_AND_COMPONENT_ENUMERATIONS_PASS', a, cs)
    for a, b in [(2,1), (2,5), (3,2), (3,4), (4,3), (4,4)]:
        f, w, n = direct_graph_brute(a, b)
        assert f == forests_by_root_component(a, b)
        assert w == leading(a,b)
        assert n == second(a,b)
        print('INDEPENDENT_EDGE_SUBSET_EXHAUSTION_PASS', a, b, f, w, n)
    assert [second_coefficient(a) for a in range(2, 6)] == [1,4,27,260]
    # If F = W + second + O_a(b^{a-3}(a+1)^b), the coefficient
    # of 1/b in 1-W/F is (a+1)*H_a/a^(a-2).
    for a in range(2, 6):
        b = 300
        f = forests_by_root_component(a, b)
        w = leading(a,b)
        from fractions import Fraction
        kappa = Fraction((a+1)*second_coefficient(a),cayley(a))
        observed = Fraction(b*(f-w),f)
        assert abs(observed-kappa) < Fraction(20*a**4,b), (a,observed,kappa)
        print('TV_FIRST_CORRECTION_CONSISTENCY_PASS', a, str(kappa), float(observed))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
