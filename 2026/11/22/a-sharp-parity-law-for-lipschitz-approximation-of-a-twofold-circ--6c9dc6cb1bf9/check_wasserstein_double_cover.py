"""Independent exact-rational diagnostics for circle-cover transport formulas.

This verifies finite samples of the explicit continuous constructions. The
all-parameter theorem is proved mathematically, not by this checker.
Requires only Python 3 standard library.
"""
from fractions import Fraction as F


def circle_distance(a, b):
    v = abs((a-b) % 2)
    return min(v, 2-v)


def w1_two_fibers(positions):
    """Exact two-source transport LP, optimized by sorting reduced costs."""
    m = len(positions)
    cap = F(1, m)
    terms = [(circle_distance(0, p)-circle_distance(1, p),
              circle_distance(1, p)) for p in positions]
    base = sum((cap*b for _, b in terms), F(0))
    remaining = F(1, 2)
    for a, _ in sorted(terms):
        mass = min(cap, remaining)
        base += mass*a
        remaining -= mass
        if not remaining:
            break
    assert remaining == 0
    return base


def positions(m, t):
    """Relative atom paths of the odd single-move/even paired-move construction."""
    assert 0 <= t <= 1
    if m % 2:
        k = m//2
        starts = [F(0)]*(k+1) + [F(1)]*k
        order = [j for i in range(k) for j in (i, k+1+i)] + [k]
        progress = [F(0) for _ in range(m)]
        for n, j in enumerate(order):
            progress[j] = max(F(0), min(F(1), m*t-n))
        return [starts[j]-progress[j] for j in range(m)]
    k = m//2
    starts = [F(j % 2) for j in range(m)]
    progress = [max(F(0), min(F(1), k*t-j)) for j in range(k)]
    return [starts[j]-progress[j//2] for j in range(m)]


def run():
    count = 0
    for m in range(1, 21):
        expected = F(1, 2*m) if m%2 else F(1, m)
        start = positions(m, F(0))
        end = positions(m, F(1))
        assert all(end[j] == start[j]-1 for j in range(m))
        count += m
        max_cost = F(0)
        for t_num in range(0, 8*m*17 + 1):
            t = F(t_num, 8*m*17)
            vals = positions(m, t)
            cost = w1_two_fibers(vals)
            assert cost <= expected, (m, t, cost, expected)
            if m%2:
                assert cost == expected, (m, t, cost)
            else:
                assert cost >= 0
            max_cost = max(max_cost, cost)
            count += 1
        assert max_cost == expected, (m, max_cost, expected)
        count += 1
    print('DOUBLE_COVER_W1_EXACT_RATIONAL_OK', count)

if __name__ == '__main__':
    run()
