#!/usr/bin/env python3
"""Exact necessary-profile checks for free degree-nine cubic-line arrangements.

This finite arithmetic check does not replace the geometric flex-disjointness
lemma or the published orbifold inequality. It exhausts integer incidence
profiles under those rigorously established necessary constraints.
"""
from math import comb


def necessary_profiles(k, d):
    assert 3*k+d == 9 and k >= 1 and d >= 1
    pair_budget = 9*comb(k, 2)+3*k*d+comb(d, 2)
    profiles = []
    for t in range(pair_budget//3+1):
        for n3 in range(pair_budget//3+1):
            n2 = pair_budget-3*(n3+t)
            if n2 < 0 or n2+4*n3+5*t != 48:
                continue
            # Talar, Theorem 2.2, multiplied by four.
            if 4*(27*k+n2)+3*n3 < 4*d+20*t:
                continue
            profiles.append((n2, n3, t))
    return sorted(profiles)


one = necessary_profiles(1, 6)
two = necessary_profiles(2, 3)
assert one == [(0, 7, 4), (3, 5, 5)], one
assert two == [(0, 2, 8), (3, 0, 9)], two
print('ARITHMETIC_PROFILE_COUNTS_PASS', one, two)

# One cubic: t distinct lines are totally consumed by flex tangencies.
# With at most three lines at each line-only point, a line belongs to
# at most floor((d-1)/2) ordinary triple points of lines.
line_only_bound = 6 * ((6-1)//2) // 3
assert line_only_bound == 4
for n2, n3, t in one:
    nonflex = 6-t
    cubic_two_lines_bound = comb(nonflex, 2)
    bound = line_only_bound+cubic_two_lines_bound
    assert n3 > bound, (n2,n3,t,bound)
    print('ONE_CUBIC_EXCLUDED', (n2,n3,t), 'triple_bound',bound)

# Two cubics: write u for cubic--cubic A5 and v for cubic--line A5.
# Three cubic--cubic contacts and six cubic--line contacts are maxima.
for n2, n3, t in two:
    uv = [(u, t-u) for u in range(4) if 0 <= t-u <= 6]
    assert uv
    if t == 8:
        assert uv == [(2, 6), (3, 5)]
        for u,v in uv:
            # v >= 5 leaves <= 1 nonflex cubic--line pair, so no
            # cubic-plus-two-lines triple can occur.
            assert 6-v <= 1
            # If u=3, all cubic--cubic intersections are used up.
            # If u=2, v=6, leaving no cubic--line transverse incidence.
            assert u==3 or v==6
            print('TWO_CUBICS_TRIPLE_BOUND', (u,v), 1)
        assert n3 > 1
        print('TWO_CUBICS_EIGHT_A5_EXCLUDED', (n2,n3,t))
    else:
        assert t==9 and uv==[(3,6)] and (n2,n3)==(3,0)
        print('SOLE_NECESSARY_PROFILE', (2,3,n2,n3,t), 'u,v',(3,6))
print('DEGREE9_CUBIC_LINE_NECESSARY_CLASSIFICATION_PASS')
