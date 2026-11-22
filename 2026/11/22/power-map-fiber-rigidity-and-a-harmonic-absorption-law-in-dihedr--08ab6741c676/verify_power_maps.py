"""Independent finite checks of power-map formulas for rank-two 0-Hecke monoids.

Run with standard Python 3: python dih_power_checker.py
A pair (length, initial_letter) indexes an alternating Coxeter word; the
longest word has the unique representative (m,0).
"""
from collections import Counter
from math import ceil, log


def elements(m):
    return [(0, 0), (m, 0)] + [(ell, a) for ell in range(1, m) for a in (0, 1)]


def multiply(m, x, y):
    """Demazure/right-descent multiplication, without using a power formula."""
    if x[0] == m or y[0] == m:
        return (m, 0)
    if x[0] == 0:
        return y
    if y[0] == 0:
        return x
    ell, start = x
    right_length, right_start = y
    for i in range(right_length):
        right_letter = (right_start + i) % 2
        current_last_letter = (start + ell - 1) % 2
        if right_letter != current_last_letter:
            ell += 1
        if ell == m:
            return (m, 0)
    return (ell, start)


def expected_power_length(m, ell, r):
    if ell == 0 or ell == m:
        return ell
    return min(m, r * ell if ell % 2 == 0 else r * (ell - 1) + 1)


def expected_fiber_at_longest(m, r):
    return 2 * m - 3 - 2 * ((m - 1) // (2 * r) + (m - 2) // (2 * r))


def expected_image_size(m, r):
    return 4 + 2 * ((m - 1) // (2 * r) + (m - 2) // (2 * r))


def expected_depth(m, ell):
    if ell == m:
        return 1
    if ell % 2 == 0:
        return (m + ell - 1) // ell
    if ell >= 3:
        return (m + ell - 3) // (ell - 1)
    return None


checks = 0
for m in range(3, 81):
    es = elements(m)
    assert len(es) == 2 * m and len(set(es)) == 2 * m
    for r in range(1, m + 6):
        targets = []
        for x in es:
            y = (0, 0)
            for _ in range(r):
                y = multiply(m, y, x)
            assert y[0] == expected_power_length(m, x[0], r), (m, x, r)
            if y[0] < m and y[0] > 0:
                assert y[1] == x[1], (m, x, r)
            targets.append(y)
            checks += 1
        counts = Counter(targets)
        assert len(counts) == expected_image_size(m, r), (m, r, len(counts))
        assert counts[(m, 0)] == expected_fiber_at_longest(m, r)
        assert all(mult == 1 for y, mult in counts.items() if y != (m, 0))
    for x in es:
        if x[0] in (0, 1):
            continue
        y = (0, 0)
        for r in range(1, m + 2):
            y = multiply(m, y, x)
            if y == (m, 0):
                assert r == expected_depth(m, x[0])
                break
        else:
            raise AssertionError((m, x, "failed to absorb"))
    sqroot_count = sum(multiply(m, x, x) == (m, 0) for x in es)
    predicted = m if m % 2 else (m + 1 if m % 4 == 0 else m - 1)
    assert sqroot_count == predicted
    if m <= 9:
        for x in es:
            for y in es:
                for z in es:
                    assert multiply(m, multiply(m, x, y), z) == multiply(m, x, multiply(m, y, z))

for m in (1000, 10000, 100000):
    depths = [expected_depth(m, ell) for ell in range(2, m)]
    mean = sum(depths) / (m - 2)
    p2 = sum(t == 2 for t in depths) / (m - 2)
    p3 = sum(t == 3 for t in depths) / (m - 2)
    print(f"m={m}, mean_minus_log_m={mean-log(m):.8f}, P(T=2)={p2:.7f}, P(T=3)={p3:.7f}")
    assert abs(p2 - 0.5) < 4 / m
    assert abs(p3 - 1/6) < 4 / m
print(f"PASS: every power at 3<=m<=80 and 1<=r<=m+5, {checks} element-power checks; all power fibers, depths, square roots; associativity m<=9")
