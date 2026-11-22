"""Independent finite-state checks for a biased cycle with complete Poisson resetting.

No external packages are needed. Exhaustive claims in the accompanying proof
are analytic; the computations only verify selected rational test cases.
"""
from fractions import Fraction as F
from math import sqrt


def solve(a, b):
    """Exact rational Gaussian elimination with columnwise pivoting."""
    n = len(b)
    aug = [list(a[i]) + [b[i]] for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if aug[i][k])
        aug[k], aug[pivot] = aug[pivot], aug[k]
        value = aug[k][k]
        aug[k] = [z / value for z in aug[k]]
        for i in range(n):
            if i != k:
                value = aug[i][k]
                if value:
                    aug[i] = [v - value * w for v, w in zip(aug[i], aug[k])]
    return [row[-1] for row in aug]


def stationary_exact(n, p, q, r):
    # Column generator: clockwise p, counterclockwise q, reset to 0 at r.
    gen = [[F(0) for _ in range(n)] for _ in range(n)]
    for k in range(n):
        gen[(k + 1) % n][k] += p
        gen[(k - 1) % n][k] += q
        gen[0][k] += r
        gen[k][k] -= p + q + r
    mat = [gen[i][:] for i in range(n - 1)] + [[F(1)] * n]
    target = [F(0)] * (n - 1) + [F(1)]
    ans = solve(mat, target)
    assert all(z > 0 for z in ans)
    assert sum(ans) == 1
    assert all(sum(gen[i][j] * ans[j] for j in range(n)) == 0 for i in range(n))
    return ans


def roots(n, p, q, r):
    total = p + q + r
    small = 2 * p / (total + sqrt(total * total - 4 * p * q))
    return small, p / (q * small)


def profile(n, p, q, r):
    x, y = roots(n, p, q, r)
    vals = [y ** j / (y ** n - 1) + x ** j / (1 - x ** n)
            for j in range(n)]
    z = sum(vals)
    return [v / z for v in vals]


def ratio(n, j, p, q, r):
    x, h = roots(n, p, q, r)[0], p / q
    return (h ** (j + 1) * x ** (n - 2 * j - 1) *
            (1 - x) * (1 - x ** n) /
            ((h - x) * (h ** n - x ** n)))


def rate(n, j, p, q):
    assert j >= (n + 1) // 2
    lo, hi = 1e-10, 1.0
    while ratio(n, j, p, q, hi) < 1:
        hi *= 2
    for _ in range(100):
        mid = (lo + hi) / 2
        if ratio(n, j, p, q, mid) < 1:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def test():
    count = 0
    for n in range(3, 13):
        for p, q in [(F(3, 2), F(1)), (F(5), F(2)), (F(11, 10), F(1))]:
            for r in [F(1, 20), F(1, 2), F(3), F(30)]:
                pi = stationary_exact(n, p, q, r)
                predicted = profile(n, float(p), float(q), float(r))
                assert max(abs(float(a) - b) for a, b in zip(pi, predicted)) < 2e-10
                for j in range(n):
                    current = p * pi[j] - q * pi[(j + 1) % n]
                    rr = ratio(n, j, float(p), float(q), float(r))
                    # The comparison has a generous numerical boundary allowance.
                    if abs(rr - 1) > 1e-8:
                        assert (current > 0) == (rr < 1)
                    if j <= (n - 1) // 2:
                        assert current > 0
                count += 1
    for n in range(3, 14):
        p, q = 1.5, 1.0
        js = list(range((n + 1) // 2, n))
        rates = [rate(n, j, p, q) for j in js]
        assert all(rates[i] > rates[i + 1] for i in range(len(rates) - 1))
        for j, rr in zip(js, rates):
            assert abs(ratio(n, j, p, q, rr) - 1) < 1e-8
        count += len(rates)
    n = 6
    observed = [rate(n, j, 1.5, 1) for j in [5, 4, 3]]
    expected = [0.226733124762156, 0.48473926750432633, 3.4356203222419124]
    assert max(abs(a - b) for a, b in zip(observed, expected)) < 1e-8
    for n in range(3, 10):
        for j in range((n + 1) // 2, n):
            delta = 1e-5
            t = rate(n, j, 1 + delta, 1)
            leading = 2 * delta / (2 * j + 1 - n)
            assert abs(t - leading) < 0.001 * leading
            count += 1
    print('PASS:', count, 'exact finite-state test families and rate/asymptotic comparisons')
    print('n=6, p=3/2, q=1; thresholds j=5,4,3:', observed)


if __name__ == '__main__':
    test()
