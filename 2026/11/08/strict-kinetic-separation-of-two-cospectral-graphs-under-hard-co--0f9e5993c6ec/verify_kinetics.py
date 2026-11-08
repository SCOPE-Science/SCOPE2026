"""Exact time-resolved expected random sequential adsorption on graph twins.

Every site has an independent exponential(1) attempt time.  Python 3 standard
library only; run: python3 verify_kinetics.py
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import comb

VERT = tuple(range(16))

def edge(a, b, graph):
    if a == b:
        return False
    x, y = divmod(a, 4)
    u, v = divmod(b, 4)
    if graph == 'rook':
        return x == u or y == v
    return ((u-x) % 4, (v-y) % 4) in (
        (1,0), (3,0), (0,1), (0,3), (1,1), (3,3))

def mask_neighborhood(graph):
    return [sum((1 << v) for v in VERT if v == u or edge(u,v,graph))
            for u in VERT]

def expected_by_subset_size(graph):
    closed = mask_neighborhood(graph)
    @lru_cache(None)
    def mean(mask):
        if mask == 0:
            return Fraction(0)
        t = mask
        subtotal = Fraction(0)
        while t:
            bit = t & -t
            t -= bit
            subtotal += mean(mask & ~closed[bit.bit_length()-1])
        return 1 + subtotal / mask.bit_count()
    a = [Fraction(0) for _ in range(17)]
    for mask in range(1 << 16):
        a[mask.bit_count()] += mean(mask)
    return a

def direct_four_subset_sum(graph):
    # No dynamic programming is used here: each induced four-site subgraph is
    # processed in all 24 orders, testing the first distinction separately.
    total = Fraction(0)
    for subset in combinations(VERT,4):
        count = 0
        for perm in permutations(subset):
            accepted = []
            for v in perm:
                if all(not edge(v, u, graph) for u in accepted):
                    accepted.append(v)
            count += len(accepted)
        total += Fraction(count,24)
    return total

if __name__ == '__main__':
    a_r = expected_by_subset_size('rook')
    a_s = expected_by_subset_size('shrikhande')
    difference = [a_r[k] - a_s[k] for k in range(17)]
    expected = [
        Fraction(0), Fraction(0), Fraction(0), Fraction(0),
        Fraction(8), Fraction(64), Fraction(3688,15), Fraction(20736,35),
        Fraction(990), Fraction(3608,3), Fraction(3256,3),
        Fraction(3656,5), Fraction(5464,15), Fraction(392,3),
        Fraction(32), Fraction(24,5), Fraction(1,3)
    ]
    assert difference == expected
    assert all(difference[k] > 0 for k in range(4,17))
    assert a_r[-1] == 4 and a_s[-1] == Fraction(11,3)
    assert direct_four_subset_sum('rook') == a_r[4]
    assert direct_four_subset_sum('shrikhande') == a_s[4]
    # Power basis at p=0, using the exact Bernstein expansion.
    for a, first in ((a_r, -296),(a_s, -304)):
        coefficient = [sum(a[k] * (-1)**(j-k) * comb(16-k,j-k)
                          for k in range(j+1)) for j in range(5)]
        assert coefficient == [0,16,-48,128,first]
    print('k, sum_U of expected occupied sites: rook minus Shrikhande')
    for k,x in enumerate(difference):
        print(f'{k},{x}')
    print('E_rook(p)-E_shrikhande(p) = sum Delta[k]*p^k*(1-p)^(16-k)')
    print('For 0<p<=1 the difference is strictly positive; leading term is 8*p^4')
    print('SHRIKHANDE_ROOK_KINETICS_OK')
