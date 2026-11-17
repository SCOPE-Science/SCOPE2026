#!/usr/bin/env python3
"""Independent finite checks of an alternating complement-scattered-factor formula.
Requires only the Python standard library; no external inputs.
The mathematical all-parameter statement is proved separately, not by this script.
"""
from itertools import combinations, product
from math import comb


def deletion_complements(w, u):
    """Enumerate every embedding position-set directly, retaining distinct remainders."""
    n = len(w)
    result = set()
    for selected in combinations(range(n), len(u)):
        if ''.join(w[i] for i in selected) != u:
            continue
        keep = set(selected)
        result.add(''.join(w[i] for i in range(n) if i not in keep))
    return result


def shuffle_contains(u, v, w):
    """Independent dynamic program using two sequence pointers, not deletion sets."""
    if len(u) + len(v) != len(w):
        return False
    possible = {(0, 0)}
    for letter in w:
        new = set()
        for i, j in possible:
            if i < len(u) and u[i] == letter:
                new.add((i + 1, j))
            if j < len(v) and v[j] == letter:
                new.add((i, j + 1))
        possible = new
        if not possible:
            return False
    return (len(u), len(v)) in possible


def pair_runs(v):
    if len(v) % 2:
        return None
    previous = False
    count = 0
    for i in range(0, len(v), 2):
        t = v[i:i+2]
        if t not in ('01', '10'):
            return None
        here = t == '10'
        count += int(here and not previous)
        previous = here
    return count


def theoretical(r, k):
    return sum(comb(r+1, 2*j) for j in range(k+1) if 2*j <= r+1)


def checks():
    direct_cases = 0
    for n in range(0, 9):
        for k in range(n+1):
            r = n-k
            observed = deletion_complements('01'*n, '01'*k)
            predicted = {
                ''.join(p) for p in product(('01', '10'), repeat=r)
                if sum(1 for i, x in enumerate(p) if x == '10' and (i == 0 or p[i-1] != '10')) <= k
            }
            assert observed == predicted, ('direct vs run criterion', n, k, observed ^ predicted)
            assert len(observed) == theoretical(r, k), ('direct vs count', n, k)
            direct_cases += 1

    dp_cases = 0
    # Enumerate all balanced words independently, not only pair-coded candidates.
    for r in range(0, 8):
        for k in range(0, 5):
            w = '01'*(r+k)
            u = '01'*k
            for zs in combinations(range(2*r), r):
                zero_positions = set(zs)
                v = ''.join('0' if t in zero_positions else '1' for t in range(2*r))
                actual = shuffle_contains(u, v, w)
                t = pair_runs(v)
                predicted = t is not None and t <= k
                assert actual == predicted, ('independent DP',r,k,v,actual,predicted)
                dp_cases += 1
    assert theoretical(5, 2) == 31
    assert theoretical(6, 2) == 57
    assert theoretical(8, 3) == 247
    print('ALTERNATING_COMPLEMENT_VERIFY_OK', 'direct_pairs', direct_cases, 'independent_dp_words', dp_cases)

if __name__ == '__main__':
    checks()
