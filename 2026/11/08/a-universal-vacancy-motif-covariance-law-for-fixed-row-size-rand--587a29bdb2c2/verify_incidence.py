#!/usr/bin/env python3
"""Finite exact checks for a vacancy/motif covariance formula in uniform fixed-row-size incidence models."""
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb

def motif_count(rows, n, right_neighborhoods):
    m = len(rows)
    s = max(max(a) for a in right_neighborhoods) + 1
    total = 0
    for left_injection in permutations(range(m), s):
        allowed = []
        for adj in right_neighborhoods:
            v = set(range(n))
            for index in adj:
                v.intersection_update(rows[left_injection[index]])
            allowed.append(tuple(v))
        def dfs(i, used):
            if i == len(allowed):
                return 1
            return sum(dfs(i + 1, used | (1 << v)) for v in allowed[i] if not (used >> v) & 1)
        total += dfs(0, 0)
    return total

def run_case(n, degrees, right_neighborhoods):
    m = len(degrees)
    k = len(right_neighborhoods)
    assert k < n
    t = [sum(i in a for a in right_neighborhoods)
         for i in range(max(max(a) for a in right_neighborhoods) + 1)]
    assert all(v > 0 for v in t)
    row_choices = [tuple(map(frozenset, combinations(range(n), r))) for r in degrees]
    sz = 1
    for row in row_choices:
        sz *= len(row)
    sums = [0, 0, 0]
    for rows in product(*row_choices):
        used = set().union(*rows)
        z = n - len(used)
        count = motif_count(rows, n, right_neighborhoods)
        sums[0] += z
        sums[1] += count
        sums[2] += z * count
    ez, et, ezt = (Fraction(v, sz) for v in sums)
    assert ez > 0 and et > 0
    cov = ezt - ez * et
    predicted_ratio = (Fraction(n-k,n) *
                      __import__('functools').reduce(lambda a, b: a*b,
                      (Fraction(n,n-d) for d in t), Fraction(1)))
    # Cross-check the formula against direct conditioning on an unused column.
    cond_et = Fraction(0)
    for rows in product(*row_choices):
        if any(0 in x for x in rows):
            continue
        cond_et += motif_count(rows, n, right_neighborhoods)
    valid = 1
    for d in degrees:
        valid *= comb(n-1,d)
    cond_et /= valid
    assert cond_et/et == predicted_ratio, (n,degrees,right_neighborhoods,et,cond_et,predicted_ratio)
    assert cov == ez*et*(predicted_ratio-1)
    return {'n':n,'degrees':degrees,'right_roles':right_neighborhoods,
            'E_empty':str(ez),'E_motif':str(et),'covariance':str(cov),
            'ratio':str(predicted_ratio), 'states':sz}

def cases():
    yield (4, (2,2), ((0,), (1,))) # disjoint matching
    yield (5, (2,3), ((0,), (0,))) # left star, deterministic
    yield (5, (3,3), ((0,1), (0,1))) # biclique
    yield (4, (2,2,1), ((0,), (0,1), (1,))) # path at exact zero
    yield (5, (2,2,1), ((0,), (0,1), (1,))) # path positive
    yield (6, (3,3), ((0,1), (0,), (0,), (1,), (1,))) # double-star negative
    yield (6, (3,3,3), ((0,1), (0,), (0,), (1,), (1,))) # heterogeneous extension

if __name__ == '__main__':
    import json
    for case in cases():
        print(json.dumps(run_case(*case),separators=(',',':')))
    for d in range(2,13):
        for n in range(2*d, d*d+13):
            ratio_minus_one = (Fraction(n-(2*d-1),n) / Fraction(n-d,n)**2) - 1
            assert ratio_minus_one == Fraction(n-d*d,(n-d)**2)
            assert (ratio_minus_one > 0) == (n > d*d)
            assert (ratio_minus_one == 0) == (n == d*d)
    print('PASS: exact finite enumerations and independent conditional totals, plus 638 two-star rational identities')
