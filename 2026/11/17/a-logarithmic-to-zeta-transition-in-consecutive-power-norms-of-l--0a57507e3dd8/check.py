"""Finite diagnostics for a weighted lazy backward shift.

Run: python check.py. The checks use Python's standard library only.
They do not establish the limiting theorem.
"""
from fractions import Fraction
from math import comb, exp, lgamma, log, pi, sqrt


def exact_formula(n, alpha, delta):
    probabilities = [Fraction(comb(n, k)) * delta ** k * (1 - delta) ** (n - k)
                     for k in range(n + 1)]
    probabilities = [Fraction(0)] + probabilities + [Fraction(0)]
    differences = [abs(probabilities[k + 1] - probabilities[k]) for k in range(n + 2)]
    columns = []
    for j in range(1, n + 3):
        columns.append(delta * sum(
            differences[k] * Fraction(j, j - k) ** alpha
            for k in range(min(j, n + 2))))
    return max(columns)


def exact_iteration(n, alpha, delta):
    m = n + 2

    def transform(vec):
        out = [(1 - delta) * v for v in vec]
        for j in range(1, m):
            out[j - 1] += delta * Fraction(j + 1, j) ** alpha * vec[j]
        return out

    norms = []
    for j in range(m):
        v = [Fraction(int(i == j)) for i in range(m)]
        for _ in range(n):
            v = transform(v)
        next_v = transform(v)
        norms.append(sum(abs(a - b) for a, b in zip(next_v, v)))
    return max(norms)


def finite_norm(n, alpha, delta):
    """Direct positive column evaluation, O(n^2) memory O(n)."""
    log_b = [lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)
             + k * log(delta) + (n - k) * log(1 - delta)
             for k in range(n + 1)]
    b = [0.0] + [exp(v) for v in log_b] + [0.0]
    d = [abs(b[k + 1] - b[k]) for k in range(n + 2)]
    best, best_j = 0.0, 1
    for j in range(1, n + 3):
        col = delta * j ** alpha * sum(d[k] / (j - k) ** alpha
                                       for k in range(min(j, n + 2)))
        if col > best:
            best, best_j = col, j
    return best, best_j


def main():
    assertions = 0
    for n in range(0, 7):
        for alpha in (1, 2, 3):
            for delta in (Fraction(1, 3), Fraction(1, 2), Fraction(3, 4)):
                assert exact_formula(n, alpha, delta) == exact_iteration(n, alpha, delta)
                assertions += 1
    gaussian_peak = exp(-0.5) / sqrt(2 * pi)
    for delta in (0.3, 0.5):
        for n in (240, 800, 1600):
            for alpha in (1, 2):
                observed, index = finite_norm(n, alpha, delta)
                if alpha == 1:
                    prediction = delta / (2 * (1 - delta)) * gaussian_peak
                    scaled = observed / log(n)
                    assert 0.6 * prediction < scaled < 2.0 * prediction
                else:
                    prediction = delta ** 2 / (1 - delta) * (pi ** 2 / 6) * gaussian_peak
                    scaled = observed / n
                    assert 0.75 * prediction < scaled < 1.5 * prediction
                sigma = sqrt(n * delta * (1 - delta))
                assert abs((index - n * delta) / sigma) < 1.6
                assertions += 2
                print('n=', n, 'alpha=', alpha, 'delta=', delta,
                      'norm=', round(observed, 7), 'scaled=', round(scaled, 7),
                      'asymptotic=', round(prediction, 7), 'column=', index)
    print('Passed', assertions, 'supplementary exact/numerical assertions.')


if __name__ == '__main__':
    main()
