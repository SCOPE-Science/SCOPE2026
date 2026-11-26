#!/usr/bin/env python3
"""Reproduce the exact 32-square length-10 superstring computation.

Requires NumPy 2.3.5 and SciPy 1.17.0 (with bundled HiGHS MILP).
The proof uses an explicit small 0/1 integer program, not randomized search.
"""
import json
from functools import lru_cache
from pathlib import Path

import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix


def squares(m):
    return [format(i, f'0{m}b') * 2 for i in range(1 << m)]


def shift(a, b):
    n = len(a)
    return next(d for d in range(1, n + 1) if a[d:] == b[:n-d])


def small_exact(m):
    words = squares(m)
    n = len(words)
    weights = [[shift(words[i], words[j]) for j in range(n)] for i in range(n)]
    @lru_cache(None)
    def remaining(mask, previous):
        if mask == (1 << n) - 1:
            return 0
        return min(weights[previous][j] + remaining(mask | (1 << j), j)
                   for j in range(n) if not mask & (1 << j))
    return 2*m + min(remaining(1 << i, i) for i in range(n))


def run():
    cert = json.loads(Path(__file__).with_name('certificate.json').read_text(encoding='utf8'))
    m = cert['half_length']
    assert m == 5 and cert['required_words'] == (1 << m)
    words = squares(m)
    n = len(words)
    v = n + 1
    dummy = n
    observed = cert['witness_linear_word']
    route = cert['witness_root_order']
    assert len(observed) == 82 and set(observed) <= {'0','1'}
    assert len(route) == n and sorted(route) == list(range(n))
    assert all(w in observed for w in words)
    recomposed = words[route[0]]
    for i, j in zip(route, route[1:]):
        recomposed += words[j][-shift(words[i], words[j]):]
    assert recomposed == observed

    arcs = [(i, j) for i in range(v) for j in range(v) if i != j]
    indices = {p: k for k, p in enumerate(arcs)}
    t = len(arcs)
    costs = np.asarray([2*m if i == dummy else
                        0 if j == dummy else
                        shift(words[i], words[j]) for i,j in arcs], dtype=np.float64)
    assert all(int(x) == x for x in costs)
    cuts = cert['subtour_cuts']
    assert cuts and all(0 < len(S) < v and len(S) == len(set(S))
                        and all(0 <= x < v for x in S) for S in cuts)
    A = lil_matrix((2*v+len(cuts), t), dtype=float)
    lower = np.full(2*v+len(cuts), -np.inf)
    upper = np.full(2*v+len(cuts), np.inf)
    for a,(i,j) in enumerate(arcs):
        A[i,a] = 1
        A[v+j,a] = 1
    lower[:2*v] = upper[:2*v] = 1
    for k,S in enumerate(cuts):
        S = set(S)
        for i in S:
            for j in S:
                if i != j:
                    A[2*v+k,indices[(i,j)]] = 1
        upper[2*v+k] = len(S)-1

    result = milp(costs, integrality=np.ones(t),
                  bounds=Bounds(np.zeros(t),np.ones(t)),
                  constraints=LinearConstraint(A.tocsr(),lower,upper),
                  options={'mip_rel_gap':0, 'time_limit':120})
    assert result.status == 0, result.message
    assert result.mip_gap < 1e-8
    assert abs(result.mip_dual_bound-82) < 1e-7, result.mip_dual_bound
    assert abs(result.fun-82) < 1e-7, result.fun
    assert max(abs(x-round(x)) for x in result.x) < 1e-7
    # Directly verify the resulting integer solution, not just optimizer logs.
    chosen = [arcs[i] for i,x in enumerate(result.x) if x > 0.5]
    assert len(chosen) == v
    successor = dict(chosen)
    assert len(successor) == v and len(set(successor.values())) == v
    seen = set(); cur = dummy
    for _ in range(v):
        assert cur not in seen
        seen.add(cur); cur = successor[cur]
    assert cur == dummy and len(seen) == v
    assert sum(int(costs[indices[(i,j)]]) for i,j in chosen) == 82
    # The listed witness is a feasible tour of length 82 in the full, unrelaxed problem.
    r = [dummy] + route + [dummy]
    assert sum(int(costs[indices[(i,j)]]) for i,j in zip(r,r[1:])) == 82
    for msmall, answer in cert['known_shorter_orders'].items():
        assert small_exact(int(msmall)) == answer
    print('VERIFY_OK square_superstring_n5=82 all_32_factors=present '
          'integer_program_optimal=yes small_orders=4,12,24,48')


if __name__ == '__main__':
    run()
