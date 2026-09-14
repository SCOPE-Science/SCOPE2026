"""Standardized 4th moments of 1D log-concave densities (pure stdlib)."""
import math, random


def trapz_xy(x, y):
    s = 0.0
    for i in range(len(x) - 1):
        s += 0.5 * (y[i] + y[i + 1]) * (x[i + 1] - x[i])
    return s


def m4_logconcave(knots, slopes, lo, hi, n=20001):
    """f ~ exp(-phi), phi piecewise linear, slopes increasing for log-concavity."""
    x = [lo + (hi - lo) * i / (n - 1) for i in range(n)]
    k = len(knots)
    phik = [0.0] * k
    for j in range(1, k):
        phik[j] = phik[j - 1] + slopes[j] * (knots[j] - knots[j - 1])
    phi = []
    for v in x:
        # locate segment
        j = 0
        while j < k and v > knots[j]:
            j += 1
        if j == 0:
            p = slopes[0] * (v - knots[0])
        elif j < k:
            p = phik[j - 1] + slopes[j] * (v - knots[j - 1])
        else:
            p = phik[k - 1] + slopes[k] * (v - knots[k - 1])
        phi.append(p)
    m = min(phi)
    f = [math.exp(-(p - m)) for p in phi]
    z = trapz_xy(x, f)
    if not math.isfinite(z) or z <= 0:
        return float("nan")
    m1 = trapz_xy(x, [a * b for a, b in zip(x, f)]) / z
    m2 = trapz_xy(x, [((a - m1) ** 2) * b for a, b in zip(x, f)]) / z
    m4 = trapz_xy(x, [((a - m1) ** 4) * b for a, b in zip(x, f)]) / z
    return m4 / (m2 ** 2) if m2 > 0 else float("nan")


def m4_kink(a, b):
    """Two-sided exponential, slopes -b (left), +a (right). Exact rational formula."""
    z = 1.0 / a + 1.0 / b
    def raw(kk):
        return (math.factorial(kk) / a ** kk * (1.0 / a)
                + ((-1) ** kk) * math.factorial(kk) / b ** kk * (1.0 / b)) / z
    m1, m2, m3, mm4 = raw(1), raw(2), raw(3), raw(4)
    c2 = m2 - m1 ** 2
    c4 = mm4 - 4 * m1 * m3 + 6 * m1 ** 2 * m2 - 3 * m1 ** 4
    return c4 / c2 ** 2


if __name__ == "__main__":
    print("one-sided exp:", m4_logconcave([-1.0], [1.0, 1.0], -1.0, 40.0))
    print("laplace:", m4_logconcave([0.0], [-1.0, 1.0], -40.0, 40.0))
    print("uniform:", m4_logconcave([0.0], [0.0, 0.0], -1.0, 1.0))
    for r in [1, 1.5, 2, 3, 5, 10, 100]:
        print(f"kink ratio {r}: {m4_kink(r, 1.0):.6f}")
    rng = random.Random(0)
    knots = [-1.0, 0.0, 1.0, 2.0]
    best = 0.0
    bestp = None
    for _ in range(1500):
        s = sorted(rng.gauss(0, 2) for _ in range(5))
        a = rng.uniform(-2.0, 0.0)
        if s[-1] <= 0.05:
            continue
        v = m4_logconcave(knots, s, a, 30.0, n=6001)
        if math.isfinite(v) and v > best:
            best, bestp = v, (list(s), a)
    print("best semi-infinite:", best, bestp)
    best = 0.0
    bestp = None
    for _ in range(1500):
        s = sorted(rng.gauss(0, 2) for _ in range(5))
        a = rng.uniform(-3.0, 0.0)
        b = rng.uniform(1.0, 6.0)
        v = m4_logconcave(knots, s, a, b, n=4001)
        if math.isfinite(v) and v > best:
            best, bestp = v, (list(s), a, b)
    print("best finite:", best, bestp)
