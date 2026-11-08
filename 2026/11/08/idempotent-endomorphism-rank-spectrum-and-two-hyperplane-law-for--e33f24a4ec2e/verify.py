"""Independent finite-field tests for the idempotent Leibniz-endomorphism rank formula.

Run with: python3 verify.py
The exhaustive matrix enumeration uses prime fields only. The proof covers all prime powers.
"""
from collections import Counter
from itertools import product
from math import prod


def gaussian(n, r, q):
    if not 0 <= r <= n:
        return 0
    numerator = prod(q ** (n - j) - 1 for j in range(r))
    denominator = prod(q ** (j + 1) - 1 for j in range(r))
    assert numerator % denominator == 0
    return numerator // denominator


def projections(n, r, q):
    if not 0 <= r <= n:
        return 0
    return gaussian(n, r, q) * q ** (r * (n - r))


def formula(m, q):
    output = []
    for r in range(m + 3):
        value = projections(m + 1, r, q)
        value += (q ** (2 * r) - q ** r) * projections(m, r, q)
        if r >= 2:
            value += q ** (m - r + 2) * projections(m, r - 2, q)
        output.append(value)
    return output


def product_matrices(a, b, p):
    n = len(a)
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(n)) % p
                       for j in range(n)) for i in range(n))


def matrix_rank(a, p):
    mat = [list(row) for row in a]
    n = len(mat)
    rank = 0
    for j in range(n):
        index = next((i for i in range(rank, n) if mat[i][j] % p), None)
        if index is None:
            continue
        mat[rank], mat[index] = mat[index], mat[rank]
        inverse = pow(mat[rank][j], -1, p)
        mat[rank] = [inverse * v % p for v in mat[rank]]
        for i in range(rank + 1, n):
            factor = mat[i][j]
            mat[i] = [(mat[i][h] - factor * mat[rank][h]) % p for h in range(n)]
        rank += 1
    return rank


def preserves_bracket(a, p):
    """The unique nonzero basis bracket is [e_2,e_1]=e_1."""
    n = len(a)
    for i in range(n):
        for j in range(n):
            actual = a[1][i] * a[0][j] % p
            expected = a[0][0] if (i, j) == (1, 0) else 0
            if actual != expected:
                return False
            # The bracket of images has no components along e_2 or W.
            if (i, j) == (1, 0) and any(a[h][0] for h in range(1, n)):
                return False
    return True


def enumerate_idempotents(p, m):
    n = m + 2
    counts = Counter()
    classes = Counter()
    for cells in product(range(p), repeat=n * n):
        a = tuple(tuple(cells[i * n:(i + 1) * n]) for i in range(n))
        if product_matrices(a, a, p) != a or not preserves_bracket(a, p):
            continue
        r = matrix_rank(a, p)
        counts[r] += 1
        # A: image in span(e_1,W), B: image in span(e_2,W).
        in_left = all(a[1][j] == 0 for j in range(n))
        in_right = all(a[0][j] == 0 for j in range(n))
        if in_left and in_right:
            classes['intersection'] += 1
        elif in_left:
            classes['left_only'] += 1
        elif in_right:
            classes['right_only'] += 1
        else:
            classes['nonabelian'] += 1
    return [counts[k] for k in range(n + 1)], {name: classes[name] for name in ('intersection', 'left_only', 'right_only', 'nonabelian')}


def predicted_classes(p, m):
    a = sum(p ** (2 * r) * projections(m, r, p) for r in range(m + 1))
    b = sum(projections(m + 1, r, p) for r in range(m + 2))
    overlap = sum(p ** r * projections(m, r, p) for r in range(m + 1))
    nonabelian = sum(p ** (m - r) * projections(m, r, p) for r in range(m + 1))
    return {'intersection': overlap, 'left_only': a - overlap,
            'right_only': b - overlap, 'nonabelian': nonabelian}


def run():
    for p, m in ((2, 0), (3, 0), (5, 0), (2, 1), (3, 1), (2, 2)):
        actual, classes = enumerate_idempotents(p, m)
        expected = formula(m, p)
        assert actual == expected, (p, m, actual, expected)
        wanted = predicted_classes(p, m)
        assert classes == wanted, (p, m, classes, wanted)
        print('EXHAUSTIVE_OK', p, m, sum(actual), actual, wanted)

    for p in (2, 3, 5):
        for m in range(0, 20):
            spectrum = formula(m, p)
            classes = predicted_classes(p, m)
            assert sum(spectrum) == sum(classes.values())
            assert spectrum[0] == spectrum[-1] == 1
            assert sum(spectrum) > 0
        print('FORMULA_SANITY_OK', p)

    for p in (2, 3):
        m = 30
        classes = predicted_classes(p, m)
        n = sum(classes.values())
        assert abs((classes['left_only'] / n) - 0.5) < 0.001
        assert abs((classes['right_only'] / n) - 0.5) < 0.001
        assert classes['nonabelian'] / n < 0.001
        print('ASYMPTOTIC_SANITY_OK', p,
              classes['left_only'] / n, classes['right_only'] / n,
              classes['nonabelian'] / n)
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
