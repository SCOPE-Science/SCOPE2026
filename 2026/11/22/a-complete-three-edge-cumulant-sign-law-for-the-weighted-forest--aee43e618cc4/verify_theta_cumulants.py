#!/usr/bin/env python3
"""Exact small-instance verification of three-edge cumulants in weighted theta forests.

Uses only Python's standard library. This is supplementary to the all-size
mathematical proof; it neither samples parameters nor certifies infinitely many graphs.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import prod


def has_cycle(nverts, edge_pairs, mask):
    parent = list(range(nverts))
    def root(u):
        while parent[u] != u:
            u = parent[u]
        return u
    for t, (u, v) in enumerate(edge_pairs):
        if not ((mask >> t) & 1):
            continue
        ru, rv = root(u), root(v)
        if ru == rv:
            return True
        parent[ru] = rv
    return False


def run_case(lengths, rates):
    assert len(lengths) >= 2 and min(lengths) >= 2
    n = sum(lengths)
    assert len(rates) == n
    b = [Q(p, d) for p, d in rates]
    assert all(0 < x < 1 for x in b)
    arms, edge_pairs, owner = [], [], []
    vertex = 2
    for i, length in enumerate(lengths):
        indices = []
        curr = 0
        for j in range(length):
            nxt = 1 if j == length - 1 else vertex
            if j < length - 1:
                vertex += 1
            indices.append(len(edge_pairs))
            edge_pairs.append((curr, nxt))
            owner.append(i)
            curr = nxt
        arms.append(indices)
    assert len(edge_pairs) == n
    p = [prod(b[e] for e in arm) for arm in arms]
    odds = [x / (1 - x) for x in p]
    pi = [s / (1 + sum(odds)) for s in odds]
    assert all(0 < z < prob for z, prob in zip(pi, p))
    # Independently decide acyclicity using union/find on the actual graph.
    unnorm = {}
    for mask in range(1 << n):
        full_paths = sum(all(mask & (1 << e) for e in arm) for arm in arms)
        assert has_cycle(vertex, edge_pairs, mask) == (full_paths >= 2)
        if full_paths >= 2:
            continue
        unnorm[mask] = prod(x if mask & (1 << t) else 1-x for t, x in enumerate(b))
    Z = sum(unnorm.values())
    expected_Z = prod(1-pi0 for pi0 in p) * (1 + sum(odds))
    assert Z == expected_Z
    probs = {mask: weight / Z for mask, weight in unnorm.items()}
    moments = {}
    for sz in (1, 2, 3):
        for idx in combinations(range(n), sz):
            bits = sum(1 << e for e in idx)
            moments[idx] = sum(w for mask, w in probs.items() if (mask & bits) == bits)
    def m(*indices):
        return moments[tuple(sorted(indices))]
    types = {'three_paths': 0, 'two_paths': 0, 'one_path': 0}
    for a, c, d in combinations(range(n), 3):
        ia, ic, id_ = owner[a], owner[c], owner[d]
        ids = (ia, ic, id_)
        if len(set(ids)) == 3:
            exp = 2 * pi[ia] * pi[ic] * pi[id_] * prod(
                (1-b[e])/(1-p[owner[e]]) for e in (a,c,d))
            case = 'three_paths'
        elif len(set(ids)) == 2:
            i = next(j for j in set(ids) if ids.count(j) == 2)
            j = next(j for j in set(ids) if ids.count(j) == 1)
            exp = (pi[i]*pi[j]*(2*pi[i]-1-p[i]) * prod(
                (1-b[e])/(1-p[owner[e]]) for e in (a,c,d)))
            case = 'two_paths'
        else:
            i = ia
            odds_other = sum(odds[j] for j in range(len(p)) if j != i)
            r = p[i] * odds_other / (1 + odds_other)
            exp = -r*(1+r)*prod(1-b[e] for e in (a,c,d))/(1-r)**3
            case = 'one_path'
        actual = (m(a,c,d)-m(a,c)*m(d)-m(a,d)*m(c)
                  -m(c,d)*m(a)+2*m(a)*m(c)*m(d))
        assert actual == exp, (lengths, (a,c,d), actual, exp)
        assert actual > 0 if case == 'three_paths' else actual < 0
        types[case] += 1
    assert sum(types.values()) == n*(n-1)*(n-2)//6
    return n, types


def main():
    examples = [
        ([2, 2], 2),
        ([3, 4], 3),
        ([2, 2, 2], 4),
        ([3, 3, 2], 5),
        ([2, 3, 4], 3),
        ([2, 2, 2, 2], 7),
        ([3, 3, 3, 2], 5),
    ]
    total = 0
    for lengths, offset in examples:
        n = sum(lengths)
        rates = [(1+(i+offset)%5, 7+(i+offset)%5) for i in range(n)]
        size, counts = run_case(lengths, rates)
        total += sum(counts.values())
        print('OK', lengths, counts)
    print('THETA_CUMULANT_EXACT_CHECKS_PASSED', len(examples), total)

if __name__ == '__main__':
    main()
