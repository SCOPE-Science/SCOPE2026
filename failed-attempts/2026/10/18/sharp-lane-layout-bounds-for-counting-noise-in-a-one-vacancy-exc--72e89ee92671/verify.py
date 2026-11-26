#!/usr/bin/env python3
"""Exact finite-generator and combinatorial checks for lane-layout count noise.

Uses Python's standard-library Fraction for exact rational arithmetic.
"""
from fractions import Fraction as F
from itertools import combinations


def solve(matrix, vector):
    """Solve a nonsingular rational linear system by Gauss--Jordan elimination."""
    n = len(vector)
    a = [list(matrix[i]) + [vector[i]] for i in range(n)]
    for col in range(n):
        row = next((i for i in range(col, n) if a[i][col]), None)
        assert row is not None, "Singular linear system"
        a[col], a[row] = a[row], a[col]
        pivot = a[col][col]
        a[col] = [x / pivot for x in a[col]]
        for r in range(n):
            if r != col and a[r][col]:
                mul = a[r][col]
                a[r] = [x - mul * y for x, y in zip(a[r], a[col])]
    return [row[-1] for row in a]


def prefix_noise(s, a, b, chi):
    k = len(s)
    assert k % 2 == 0 and sum(s) == 0
    heights = []
    level = 0
    for label in s:
        heights.append(level)
        level += label
    assert level == 0
    avg = F(sum(heights), k)
    spread = sum((F(h) - avg)**2 for h in heights) / k
    v = (a + b) / 2 + (a - b)**2 * spread / (2 * chi)
    return v, spread


def independent_full_generator_noise(s, a, b, chi, columns, p_override=None):
    """An independent direct Poisson-equation calculation on all hole states.

    State = (hole lane, hole column). A particle moving clockwise makes
    the hole move to the preceding column and increments the counted jumps.
    """
    k = len(s)
    size = k * columns
    rates = [a if label > 0 else b for label in s] if p_override is None else list(p_override)
    q = [[F(0) for _ in range(size)] for _ in range(size)]
    counted = [[F(0) for _ in range(size)] for _ in range(size)]
    for lane in range(k):
        for col in range(columns):
            x = lane * columns + col
            transitions = [
                (lane, (col - 1) % columns, rates[lane], True),
                ((lane + 1) % k, col, chi, False),
                ((lane - 1) % k, col, chi, False),
            ]
            for next_lane, next_col, rate, is_counted in transitions:
                y = next_lane * columns + next_col
                assert x != y
                q[x][y] += rate
                q[x][x] -= rate
                if is_counted:
                    counted[x][y] += rate
    assert all(sum(row) == 0 for row in q)
    assert all(sum(q[i][j] for i in range(size)) == 0 for j in range(size))
    reward = [sum(row) for row in counted]
    mean = sum(reward) / size
    coeff = [list(row) for row in q]
    rhs = [mean - x for x in reward]
    coeff[-1] = [F(1) for _ in range(size)]
    rhs[-1] = F(0)
    h = solve(coeff, rhs)
    assert sum(h) == 0
    assert all(sum(q[i][j] * h[j] for j in range(size)) == mean - reward[i]
               for i in range(size))
    # Second derivative of the Perron eigenvalue for the generator tilted
    # by exp(theta) at each longitudinal hop.
    variance = mean + F(2, size) * sum(
        counted[i][j] * h[j]
        for i in range(size) for j in range(size)
    )
    return mean, variance


def general_prefix_noise(rates, chi):
    k = len(rates)
    avg = sum(rates) / k
    partial = []
    height = F(0)
    for value in rates:
        partial.append(height)
        height += value - avg
    assert height == 0
    center = sum(partial) / k
    return avg + F(2, chi * k) * sum((v - center)**2 for v in partial)


def check():
    exact_cases = 0
    for m in (2, 3, 4):
        k = 2 * m
        for selection in (tuple(range(m)), tuple(range(0, k, 2))):
            labels = [1 if i in selection else -1 for i in range(k)]
            for columns in (2, 3):
                a, b, chi = F(5, 3), F(2, 5), F(7, 4)
                expected, spread = prefix_noise(labels, a, b, chi)
                mean, observed = independent_full_generator_noise(
                    labels, a, b, chi, columns)
                assert mean == (a + b) / 2
                assert observed == expected
                if selection == tuple(range(m)):
                    assert spread == F(m * m + 2, 12)
                else:
                    assert spread == F(1, 4)
                exact_cases += 1
    for rates in ((F(1), F(2), F(4)),
                  (F(1, 2), F(5, 2), F(1, 3), F(7, 4), F(3)),
                  (F(1), F(1), F(2), F(3), F(5), F(8))):
        for columns in (2, 3):
            chi = F(11, 5)
            mean, observed = independent_full_generator_noise(
                [1] * len(rates), F(1), F(1), chi, columns,
                p_override=rates)
            assert mean == sum(rates) / len(rates)
            assert observed == general_prefix_noise(rates, chi)
            exact_cases += 1
    arrangements = 0
    for m in range(2, 8):
        k = 2 * m
        for high in combinations(range(k), m):
            labels = [1 if i in high else -1 for i in range(k)]
            _, spread = prefix_noise(labels, F(3), F(1), F(2))
            assert F(1, 4) <= spread <= F(m * m + 2, 12)
            high_set = set(high)
            transitions = sum((i in high_set) != ((i + 1) % k in high_set)
                              for i in range(k))
            # The only lower and upper equality cases are, respectively,
            # alternating lanes and one contiguous block of fast lanes.
            assert (spread == F(1, 4)) == (transitions == k)
            assert (spread == F(m * m + 2, 12)) == (transitions == 2)
            arrangements += 1
    print("VERIFIED: %d complete-state rational generators; "
          "%d exact lane-layout comparisons" % (exact_cases, arrangements))


if __name__ == "__main__":
    check()
