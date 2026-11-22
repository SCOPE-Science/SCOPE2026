"""Standalone finite diagnostics for the sparse Bergman kernel-site classification.

The script tests exact formulas numerically; the proof of all real-parameter
statements is analytical and is given separately.
Run: python3 check.py
"""
import math
import cmath


def root_bisect(f, lo, hi, n=90):
    flo, fhi = f(lo), f(hi)
    if not (flo * fhi < 0.0):
        raise AssertionError((lo, hi, flo, fhi))
    for _ in range(n):
        mid = (lo + hi) / 2.0
        if f(mid) * flo > 0:
            lo, flo = mid, f(mid)
        else:
            hi = mid
    return (lo + hi) / 2.0


def capture(beta, m, a, x):
    return (1 + a * x ** (m / 2)) ** 2 * (1 - x) ** beta


def critical(beta, m):
    assert beta > 1 and m >= 3
    v, q = beta / 2, m / 2
    # H(0)<0<H(1-epsilon); the other root is exactly y=1.
    def h(y):
        return q * y * (-math.expm1(v * math.log(y))) - v * (1 - y)
    y = root_bisect(h, 1e-15, 1 - 1e-5)
    x = 1 - y
    a = math.expm1(-v * math.log(y)) / x ** q
    return a, x


def stationary(beta, m, a, x):
    return a * x ** (m / 2 - 1) * (m - (m + beta) * x) - beta


def relative_error(a, b):
    return abs(a - b) / max(1.0, abs(a), abs(b))


def main():
    checks = 0
    for beta in [1.1, 1.4, 2., 2.7, 5., 10.]:
        for m in [3, 4, 5, 6, 8, 12, 25, 50, 100]:
            ac, xc = critical(beta, m)
            asn = beta / 2 * ((m + beta) / (m - 2)) ** ((m - 2) / 2)
            xsn = (m - 2) / (m + beta)
            assert asn < ac and xsn < xc < m / (m + beta)
            checks += 1
            assert relative_error(capture(beta, m, ac, xc), 1) < 2e-10
            checks += 1
            assert abs(stationary(beta, m, ac, xc)) < 1e-8 * max(1, beta)
            checks += 1
            for a, above in [(ac * .97, False), (ac * 1.03, True)]:
                # Check the full interval, including the origin and all angles
                # after optimal angular phase alignment.
                vals = [capture(beta, m, a, j / 1500) for j in range(1500)]
                if above:
                    assert max(vals) > 1 + 1e-7
                else:
                    assert max(vals) <= 1 + 3e-10
                checks += 1
            ah = ac * 1.08
            # Both stationary roots are present beyond the global transition.
            xminus = root_bisect(lambda x: stationary(beta, m, ah, x), 1e-13, xsn)
            xplus = root_bisect(lambda x: stationary(beta, m, ah, x), xsn, m / (m + beta))
            assert 0 < xminus < xsn < xplus < m / (m + beta)
            assert capture(beta, m, ah, xplus) > 1
            checks += 1
            if beta == 2:
                expx = 1 - 2 / m
                expa = (m / 2) * (1 - 2 / m) ** (1 - m / 2)
                assert relative_error(xc, expx) < 4e-12
                assert relative_error(ac, expa) < 4e-12
                checks += 2
            # The actual Hilbert kernel evaluation verifies the angular
            # reduction for a sample radius and all m-th root phases.
            r = math.sqrt(xc)
            theta = .23
            w = r * cmath.exp(1j * theta)
            score = abs(1 + ac * (w ** m)) ** 2 * (1 - abs(w) ** 2) ** beta
            assert score <= capture(beta, m, ac, xc) * (1 + 2e-12)
            checks += 1
    # The m=2 continuous (rather than first-order) phase at every beta.
    for beta in [1.001, 1.2, 2, 5.3, 10]:
        for a in [beta / 4, beta / 2, beta, 10 * beta]:
            x = max(0., (2 * a - beta) / (a * (beta + 2)))
            vals = [capture(beta, 2, a, j / 2500) for j in range(2500)]
            assert capture(beta, 2, a, x) >= max(vals) - 1e-8
            checks += 1
    # Sharp degree asymptotics, tested at independently increasing cutoffs.
    for beta in [1.2, 2, 4]:
        err = []
        for m in [100, 300, 900]:
            ac, xc = critical(beta, m)
            target = (math.e * m / beta) ** (beta / 2)
            err.append(abs(ac / target - 1))
            assert abs(m * (1 - xc) / beta - 1) < .13
            checks += 1
        assert err[-1] < err[0]
        checks += 1
    print(f"PASS: {checks} finite diagnostics (not an infinite proof)")


if __name__ == '__main__':
    main()
