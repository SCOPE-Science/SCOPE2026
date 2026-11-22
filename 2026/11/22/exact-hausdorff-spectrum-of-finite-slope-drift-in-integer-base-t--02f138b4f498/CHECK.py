"""Standalone finite-cell and spectral checks for the stated slope-frequency spectrum."""
from collections import Counter
from math import cosh, sinh, sqrt, log, exp, comb, isclose


def direct_word_counts(base, length):
    """Signs at the midpoint of each elementary half-base cell; integers only."""
    q = base ** (length - 1)
    out = Counter()
    for j in range(2 * q):
        numerator = 2 * j + 1
        denominator = 4 * q
        w = []
        for k in range(length):
            mod = (base**k * numerator) % denominator
            w.append(1 if 2 * mod < denominator else -1)
        out[tuple(w)] += 1
    return out


def predicted_count(base, word):
    same = (base + 1) // 2
    flip = base // 2
    return same ** sum(word[i] == word[i - 1] for i in range(1, len(word))) * flip ** sum(word[i] != word[i - 1] for i in range(1, len(word)))


def rho_formula(base, t):
    a, b = (base + 1) // 2, base // 2
    return a * cosh(t) + sqrt(a * a * sinh(t)**2 + b * b)


def rho_by_iteration(base, t, count=250):
    a, b = (base + 1) // 2, base // 2
    x, y = 0.7, 0.3
    val = None
    for _ in range(count):
        xx = a * exp(t) * x + b * exp(-t) * y
        yy = b * exp(t) * x + a * exp(-t) * y
        val = xx + yy
        x, y = xx / val, yy / val
    return val


def pressure(base, t):
    return log(rho_formula(base, t))


def derivative(base, t):
    eps = 1e-5
    return (pressure(base, t + eps) - pressure(base, t - eps)) / (2 * eps)


def approximate_dimension(base, u):
    lo, hi = -35.0, 35.0
    for _ in range(85):
        mid = (lo + hi) / 2
        if derivative(base, mid) < u:
            lo = mid
        else:
            hi = mid
    t = (lo + hi) / 2
    return (pressure(base, t) - t * u) / log(base)


def main():
    comparisons = 0
    for m in range(2, 8):
        for n in range(1, 7):
            table = direct_word_counts(m, n)
            assert len(table) == 2**n, (m, n, 'missing sign word')
            for w, count in table.items():
                assert count == predicted_count(m, w), (m, n, w, count)
                comparisons += 1
            assert sum(table.values()) == 2 * m**(n - 1)
        for t in [-1.2, -0.5, 0, 0.5, 1.2]:
            assert isclose(rho_formula(m, t), rho_by_iteration(m, t), rel_tol=5e-13)
        assert isclose(pressure(m, 0), log(m), abs_tol=1e-13)
        assert isclose(approximate_dimension(m, 0), 1.0, rel_tol=2e-8)
        assert isclose(approximate_dimension(m, 0.99999), log((m + 1)//2) / log(m), abs_tol=4e-4)
    print('PASS: %d exact sign-word multiplicity comparisons, bases 2..7, lengths 1..6' % comparisons)
    print('PASS: 30 independent Perron eigenvalue power-iteration comparisons')
    print('PASS: midpoint and near-endpoint dimension checks for bases 2..7')
    print('These finite checks do not prove the all-base/all-length or Hausdorff claims.')

if __name__ == '__main__':
    main()
