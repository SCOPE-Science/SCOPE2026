"""Exact finite identities for the extreme-vertex permutation-graph model.
Only Python's standard library is required. This is a check, not an asymptotic proof.
"""
from itertools import permutations
from fractions import Fraction
from math import factorial


def inversion_degrees(p):
    n = len(p)
    d = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] > p[j]:
                d[i] += 1
                d[j] += 1
    return d


def corner_data(i, j, n, h):
    left = i <= h
    right = i > n - h
    bottom = j <= h
    top = j > n - h
    if not ((left or right) and (bottom or top)):
        return None
    side_row = 'L' if left else 'R'
    side_col = 'B' if bottom else 'T'
    x = i if left else n + 1 - i
    y = j if bottom else n + 1 - j
    return (side_row + side_col, x, y)


def before_row(a, b):
    ta, xa, _ = a
    tb, xb, _ = b
    sa, sb = ta[0], tb[0]
    if sa != sb:
        return sa == 'L'
    return xa < xb if sa == 'L' else xa > xb


def before_col(a, b):
    ta, _, ya = a
    tb, _, yb = b
    sa, sb = ta[1], tb[1]
    if sa != sb:
        return sa == 'B'
    return ya < yb if sa == 'B' else ya > yb


def checks():
    permutations_checked = 0
    degree_identities = 0
    edge_identities = 0
    four_corner_count_totals = 0
    # Exhaustively check each permutation of [n] for n=2,...,8.
    for n in range(2, 9):
        h = max(1, (n - 1) // 3)
        sum_corner_ll = 0
        sum_corner_ll_pairs = 0
        for p0 in permutations(range(1, n + 1)):
            p = list(p0)
            d = inversion_degrees(p)
            permutations_checked += 1
            cc = [corner_data(i, p[i - 1], n, h) for i in range(1, n + 1)]
            count_ll = sum(c is not None and c[0] == 'LB' for c in cc)
            sum_corner_ll += count_ll
            sum_corner_ll_pairs += count_ll * (count_ll - 1)
            for i in range(1, n + 1):
                j = p[i - 1]
                k = sum(1 for s in range(1, i) if p[s - 1] < j)
                assert d[i - 1] == i + j - 2 - 2 * k
                # Complement-reversal creates the high-degree equation.
                sigma = [n + 1 - v for v in p]
                ks = sum(1 for s in range(1, i) if sigma[s - 1] < sigma[i - 1])
                assert n - 1 - d[i - 1] == i + sigma[i - 1] - 2 - 2 * ks
                degree_identities += 2
            for i in range(n):
                for j in range(i + 1, n):
                    if cc[i] is None or cc[j] is None:
                        continue
                    # Exact inversion graph adjacency from the corresponding
                    # corner coordinates; no residual combinatorial data.
                    predicted = before_col(cc[j], cc[i])
                    assert before_row(cc[i], cc[j])
                    actual = p[i] > p[j]
                    assert predicted == actual
                    edge_identities += 1
        # First two falling-factorial moments of points in an h by h corner.
        observed_e = Fraction(sum_corner_ll, factorial(n))
        observed_ff2 = Fraction(sum_corner_ll_pairs, factorial(n))
        expected_e = Fraction(h * h, n)
        expected_ff2 = Fraction(h * h * (h - 1) ** 2, n * (n - 1))
        assert observed_e == expected_e
        assert observed_ff2 == expected_ff2
        four_corner_count_totals += 2
    print(f'PASS permutations={permutations_checked}; degree_identities={degree_identities}; '
          f'corner_edge_identities={edge_identities}; exact_moment_identities={four_corner_count_totals}')


if __name__ == '__main__':
    checks()
