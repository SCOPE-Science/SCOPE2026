#!/usr/bin/env python3
"""Standalone finite verification for idempotent nonexpansive chain operators.
The asymptotic theorem depends on the accompanying mathematical proof.
"""
from itertools import product
from math import log, cos, pi


def walks(d, length):
    counts = [0] * (d + 1)
    counts[0] = 1
    vals = [1]
    for _ in range(length):
        counts = [sum(counts[max(0, j - 1):min(d, j + 1) + 1])
                  for j in range(d + 1)]
        vals.append(sum(counts))
    return vals


def idempotent_count(m):
    ans = 0
    for d in range(m + 1):
        b = m - d
        f = walks(d, b)
        ans += sum(f[a] * f[b - a] for a in range(b + 1))
    return ans


def brute_counts(m):
    idem = total = 0
    for tup in product(range(m + 1), repeat=m + 1):
        if all(abs(tup[i+1] - tup[i]) <= 1 for i in range(m)):
            total += 1
            if all(tup[tup[i]] == tup[i] for i in range(m + 1)):
                idem += 1
    return idem, total


def width_counts(m):
    out = {}
    for d in range(m + 1):
        b = m - d
        fs = walks(d, b)
        out[d] = sum(fs[a]*fs[b-a] for a in range(b+1))
    return out


def total_walk_maps(m):
    # Every +/-/0 increment word has exactly m+1-range valid initial values.
    state = {(0, 0, 0): 1}
    for i in range(m):
        nxt = {}
        for (pos, lo, hi), cnt in state.items():
            for s in (-1, 0, 1):
                p = pos + s
                key = (p, min(lo, p), max(hi, p))
                nxt[key] = nxt.get(key, 0) + cnt
        state = nxt
    return sum(cnt*(m+1 - (hi-lo)) for (pos,lo,hi),cnt in state.items() if hi-lo <= m)


def check():
    idem_reference = [1,3,8,21,56,149,395,1042,2741,7205,18961,50021]
    for m, expected in enumerate(idem_reference):
        assert idempotent_count(m) == expected, (m, idempotent_count(m), expected)
        assert sum(width_counts(m).values()) == expected
    all_map_reference = [1,4,17,68,259,950,3387,11814,40503,136946,457795]
    for m,expected in enumerate(all_map_reference[:9]):
        assert total_walk_maps(m) == expected, (m,total_walk_maps(m),expected)
    for m in range(0,6):
        idem, total = brute_counts(m)
        assert idem == idempotent_count(m)
        assert total == total_walk_maps(m)
    for d in range(0,7):
        for t in range(0,13):
            f = walks(d,t)[t]
            # Compare F_d(t) against naive direct enumeration of lazy paths.
            states = [(0,)]
            for _ in range(t):
                states = [p+(j,) for p in states for j in (p[-1]-1,p[-1],p[-1]+1) if 0<=j<=d]
            assert len(states) == f, (d,t)
    c = 1.5*(2*pi*pi/(3*log(3)))**(1/3)*log(3)
    tstar = (2*pi*pi/(3*log(3)))**(1/3)
    assert abs(c - 2.9926577765382154) < 1e-8
    print('ALL_CHAIN_RETRACTION_CHECKS_OK finite_brute_max_m=5 path_strips=7 count_m_11=',idem_reference[11])
    print('REFERENCE_ASYMPTOTIC_CONSTANTS',round(c,12),round(tstar,12))

if __name__ == '__main__':
    check()
