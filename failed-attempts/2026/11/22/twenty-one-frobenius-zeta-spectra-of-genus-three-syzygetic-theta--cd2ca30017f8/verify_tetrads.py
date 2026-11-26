#!/usr/bin/env python3
"""Exact finite permutation certificate for genus-three syzygetic theta tetrads.

The 28 odd theta characteristics of a hyperelliptic genus-three curve
are represented by the unordered pairs of its eight ramification points.
The 315 tetrads are sets of four pairs whose symmetric difference is
empty or all eight labels.  A separate symplectic-plane construction
independently verifies the tetrad action and the Frobenius orbit tables.
Requires only Python 3 standard library; writes a CSV table next to script.
"""
from itertools import combinations, product
from collections import Counter, defaultdict
from math import lcm
from pathlib import Path
import csv

N = 8
ALL = (1 << N) - 1
EDGE_TUPLES = tuple(combinations(range(N), 2))
EDGE_MASKS = tuple((1 << a) | (1 << b) for a, b in EDGE_TUPLES)
E_INDEX = {e: i for i, e in enumerate(EDGE_TUPLES)}


def partitions(n, minimum=1):
    if n == 0:
        yield ()
    for first in range(minimum, n + 1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def representative(p):
    perm = list(range(N))
    start = 0
    for size in p:
        for i in range(size):
            perm[start + i] = start + (i + 1) % size
        start += size
    assert start == N
    return tuple(perm)


def apply_mask(s, permutation):
    out = 0
    for i in range(N):
        if s & (1 << i):
            out |= 1 << permutation[i]
    return out


def canonical(s):
    return min(s, s ^ ALL)


def symplectic(s, t):
    return ((s & t).bit_count() % 2)


def profile(action):
    seen = set()
    result = Counter()
    for start in range(len(action)):
        if start not in seen:
            cur = start
            size = 0
            while cur not in seen:
                seen.add(cur)
                size += 1
                cur = action[cur]
            assert cur == start
            result[size] += 1
    assert sum(length * count for length, count in result.items()) == len(action)
    return tuple(sorted(result.items()))


def format_profile(p):
    return ' '.join(f'{length}^{multiplicity}' for length, multiplicity in p)


def fixed(p, n):
    return sum(length * m for length, m in p if n % length == 0)


# Direct construction: edges of K_8, and four-edge even-degree or
# all-odd-degree graphs.
TETRADS = tuple(q for q in combinations(range(28), 4)
                if (EDGE_MASKS[q[0]] ^ EDGE_MASKS[q[1]] ^
                    EDGE_MASKS[q[2]] ^ EDGE_MASKS[q[3]]) in (0, ALL))
assert len(TETRADS) == 315
T_INDEX = {q: i for i, q in enumerate(TETRADS)}
MATCH = tuple(i for i, q in enumerate(TETRADS)
              if (EDGE_MASKS[q[0]] ^ EDGE_MASKS[q[1]] ^
                  EDGE_MASKS[q[2]] ^ EDGE_MASKS[q[3]]) == ALL)
CYCLE = tuple(i for i in range(315) if i not in MATCH)
assert (len(MATCH), len(CYCLE)) == (105, 210)

# Independent construction: isotropic 2-subspaces of the 6-dimensional
# symplectic space of even 8-subsets modulo the full 8-subset.
V = tuple(s for s in range(256) if s.bit_count() % 2 == 0 and s <= (s ^ ALL))
assert len(V) == 64 and V[0] == 0
PLANES = set()
for a, b in combinations(V[1:], 2):
    if symplectic(a, b) == 0:
        P = tuple(sorted((0, a, b, canonical(a ^ b))))
        assert len(set(P)) == 4
        PLANES.add(P)
PLANES = tuple(sorted(PLANES))
assert len(PLANES) == 315
P_INDEX = {p: i for i, p in enumerate(PLANES)}


def tetrad_to_plane(q):
    first, second, third, fourth = [EDGE_MASKS[i] for i in q]
    a = canonical(first ^ second)
    b = canonical(first ^ third)
    c = canonical(first ^ fourth)
    assert canonical(a ^ b) == c
    assert symplectic(a, b) == 0
    out = tuple(sorted((0, a, b, c)))
    assert out in P_INDEX
    return P_INDEX[out]

T_TO_P = tuple(tetrad_to_plane(t) for t in TETRADS)
assert len(set(T_TO_P)) == 315


def actions_on_both_models(perm):
    ep = [E_INDEX[tuple(sorted((perm[a], perm[b])))] for a, b in EDGE_TUPLES]
    tp = tuple(T_INDEX[tuple(sorted(ep[k] for k in q))] for q in TETRADS)
    sp = tuple(P_INDEX[tuple(sorted(canonical(apply_mask(s, perm))
                                    for s in P))] for P in PLANES)
    assert len(set(tp)) == len(set(sp)) == 315
    assert all(T_TO_P[tp[t]] == sp[T_TO_P[t]] for t in range(315))
    return tp, sp


def restricted_profile(action, ids):
    index = {v: i for i, v in enumerate(ids)}
    return profile(tuple(index[action[v]] for v in ids))


def check_fixed_direct(action, n):
    image = list(range(len(action)))
    for _ in range(n):
        image = [action[i] for i in image]
    return sum(i == j for i, j in enumerate(image))


def irreducible_small_f3(poly):
    """Trial division by every monic polynomial of degree <= half the degree."""
    n = len(poly) - 1
    assert poly[-1] == 1
    for d in range(1, n // 2 + 1):
        for coeffs in product(range(3), repeat=d):
            divisor = list(coeffs) + [1]
            remainder = list(poly)
            for k in range(n - d, -1, -1):
                c = remainder[d + k] % 3
                for j in range(d + 1):
                    remainder[j + k] = (remainder[j + k] - c * divisor[j]) % 3
            if all(x % 3 == 0 for x in remainder[:d]):
                return False
    return True


def check_explicit_f3_examples():
    # The first curve has degree seven: x(x-1)(x+1)(x^4+x+2),
    # so infinity contributes the fourth rational branch point.
    # The second has degree eight and factor degrees 2,2,4.
    q4 = [2, 1, 0, 0, 1]
    q2a = [1, 0, 1]
    q2b = [2, 1, 1]
    assert irreducible_small_f3(q4)
    assert irreducible_small_f3(q2a)
    assert irreducible_small_f3(q2b)
    return True


def run():
    assert check_explicit_f3_examples()
    records = []
    for part in partitions(8):
        t_action, p_action = actions_on_both_models(representative(part))
        assert profile(t_action) == profile(p_action)
        overall = profile(t_action)
        matching = restricted_profile(t_action, MATCH)
        cycling = restricted_profile(t_action, CYCLE)
        period = lcm(*part)
        for n in range(1, period + 1):
            assert fixed(overall, n) == check_fixed_direct(t_action, n)
        records.append({'partition': ','.join(map(str, part)),
                        'full': format_profile(overall),
                        'matching_105': format_profile(matching),
                        'cycle_210': format_profile(cycling),
                        'fixed_1': fixed(overall, 1),
                        'fixed_2': fixed(overall, 2),
                        'fixed_3': fixed(overall, 3),
                        'fixed_4': fixed(overall, 4),
                        'fixed_5': fixed(overall, 5),
                        '_p': overall, '_part': part})
    assert len(records) == 22
    buckets = defaultdict(list)
    prefix4 = defaultdict(list)
    prefix5 = defaultdict(list)
    for r in records:
        buckets[r['_p']].append(r['_part'])
        prefix4[tuple(r[f'fixed_{i}'] for i in range(1, 5))].append(r['_p'])
        prefix5[tuple(r[f'fixed_{i}'] for i in range(1, 6))].append(r['_p'])
    assert len(buckets) == 21
    assert [p for p in buckets.values() if len(p) > 1] == [
        [(1, 1, 1, 1, 4), (2, 2, 4)]]
    assert len(prefix5) == 21
    assert len(prefix4) == 18
    assert [(r['_part'],r['fixed_1']) for r in records if r['_part'] == (8,)] == [((8,), 1)]
    assert tuple(r[f'fixed_{i}'] for r in records for i in range(1, 5)
                 if r['_part'] == (1, 7)) == (0, 0, 0, 0)
    assert tuple(r[f'fixed_{i}'] for r in records for i in range(1, 5)
                 if r['_part'] == (3, 5)) == (0, 0, 0, 0)
    assert [r['fixed_5'] for r in records if r['_part'] == (1, 7)] == [0]
    assert [r['fixed_5'] for r in records if r['_part'] == (3, 5)] == [15]
    path = Path(__file__).resolve().parent / 'tetrad_frobenius_22.csv'
    cols = ['partition', 'full', 'matching_105', 'cycle_210'] + [f'fixed_{n}' for n in range(1, 6)]
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore')
        w.writeheader()
        w.writerows(records)
    print('315_TETRADS_105_MATCHINGS_210_FOUR_CYCLES_22_PARTITIONS_21_SPECTRA_VERIFIED')
    print('FIVE_EXTENSION_RECOVERY_SHARP_ONE_COLLISION_VERIFIED')
    print('table_path:', path)


if __name__ == '__main__':
    run()
