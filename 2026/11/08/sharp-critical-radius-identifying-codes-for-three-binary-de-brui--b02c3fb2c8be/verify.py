#!/usr/bin/env python3
"""Exhaustive finite witness check for binary directed de Bruijn monitoring codes.

Only standard-library Python required. Run beside WITNESSES.json.
"""
from pathlib import Path
import json


def in_ball_by_backward_bfs(v, n, radius):
    """Enumerate predecessors in the closed incoming directed radius ball."""
    frontier = {v}
    seen = {v}
    for _ in range(radius):
        frontier = { (u >> 1) | (a << (n - 1))
                     for u in frontier for a in (0, 1) }
        seen |= frontier
    return seen


def in_ball_by_overlap(v, n, radius):
    """Independent path-overlap characterization of the same directed ball."""
    result = set()
    for u in range(1 << n):
        if u == v:
            result.add(u)
            continue
        for length in range(1, radius + 1):
            if (u & ((1 << (n - length)) - 1)) == (v >> length):
                result.add(u)
                break
    return result


def check(n, radius, hexadecimal):
    N = 1 << n
    indicator = int(hexadecimal, 16)
    assert indicator >> N == 0, 'out of range witness bits'
    code = {i for i in range(N) if indicator & (1 << i)}
    assert len(code) == N // 2, 'not the predicted sharp size'
    # This is the equality condition for the universal prefix-pair lower bound.
    assert all(((2 * a in code) + ((2 * a + 1) in code)) == 1
               for a in range(N // 2)), 'prefix-twin pair not singly represented'
    seen = set()
    min_size = N
    for target in range(N):
        ball = in_ball_by_backward_bfs(target, n, radius)
        assert ball == in_ball_by_overlap(target, n, radius), \
               'two distance implementations disagree'
        identify = frozenset(ball & code)
        assert identify, f'uncovered target {target}'
        assert identify not in seen, f'undistinguished target {target}'
        seen.add(identify)
        min_size = min(min_size, len(identify))
    assert len(seen) == N
    return N, len(code), min_size


def main():
    p = Path(__file__).resolve().with_name('WITNESSES.json')
    record = json.loads(p.read_text(encoding='utf-8'))
    expected = [(5, 3), (7, 4), (9, 5)]
    assert [(a['n'], a['radius']) for a in record['cases']] == expected
    for a in record['cases']:
        print('CASE n=%d radius=%d vertices=%d sensors=%d min_id_size=%d' %
              ((a['n'], a['radius']) + check(a['n'], a['radius'], a['bitset_hex'])))
    print('VERIFY_OK cases=3 all_vertices_and_pairs_separated')


if __name__ == '__main__':
    main()
