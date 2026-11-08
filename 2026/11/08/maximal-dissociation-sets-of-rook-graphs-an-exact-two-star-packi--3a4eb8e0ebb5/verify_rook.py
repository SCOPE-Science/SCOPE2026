"""Direct, finite verification of maximal dissociation polynomials of rook graphs.

Only Python's standard library is required. Run: python verify_rook.py
The exhaustive tests do not replace the all-parameter structural proof.
"""
from collections import Counter
from math import factorial


def predicted(m, n):
    """Independent integer formula using block-type occupancy counts."""
    result = Counter()
    for a in range(min(m, n) + 1):
        for b in range(m + 1):
            for c in range(n + 1):
                rows, cols = a + b + 2 * c, a + 2 * b + c
                if rows > m or cols > n:
                    continue
                if (rows == m and cols == n) or (
                    a == 0 and (rows == m or cols == n)
                ):
                    numerator = factorial(m) * factorial(n)
                    denominator = (
                        factorial(a) * factorial(b) * factorial(c)
                        * (2 ** (b + c)) * factorial(m - rows)
                        * factorial(n - cols)
                    )
                    assert numerator % denominator == 0
                    result[a + 2 * (b + c)] += numerator // denominator
    return result


def direct(m, n):
    """Examine every selected subset, from graph adjacency only."""
    order = m * n
    adjacency = []
    for i in range(m):
        for j in range(n):
            mask = 0
            for ii in range(m):
                for jj in range(n):
                    if (ii != i or jj != j) and (ii == i or jj == j):
                        mask |= 1 << (ii * n + jj)
            adjacency.append(mask)

    def valid(selected):
        for vertex in range(order):
            if (selected >> vertex) & 1:
                if (selected & adjacency[vertex]).bit_count() > 1:
                    return False
        return True

    out = Counter()
    valid_sets = 0
    for mask in range(1 << order):
        if not valid(mask):
            continue
        valid_sets += 1
        maximal = True
        for vertex in range(order):
            if not ((mask >> vertex) & 1):
                if valid(mask | (1 << vertex)):
                    maximal = False
                    break
        if maximal:
            out[mask.bit_count()] += 1
    return out, valid_sets


def main():
    instances = 0
    examined = valid_total = maximal_total = 0
    for m in range(1, 5):
        for n in range(m, 7):
            if m * n > 20:
                continue
            observed, valid_count = direct(m, n)
            expected = predicted(m, n)
            assert observed == expected, (m, n, observed, expected)
            instances += 1
            examined += 1 << (m * n)
            valid_total += valid_count
            maximal_total += sum(observed.values())
    print('VERIFY_OK', 'instances=' + str(instances),
          'vertex_subsets=' + str(examined),
          'dissociation_sets=' + str(valid_total),
          'maximal_sets=' + str(maximal_total),
          'all_coefficients=PASS', 'single_vertex_extensions=PASS')


if __name__ == '__main__':
    main()
