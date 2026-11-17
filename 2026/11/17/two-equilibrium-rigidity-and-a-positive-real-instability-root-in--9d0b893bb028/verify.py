"""Exact-arithmetic spot checks for the common-latency phage equilibrium theorem.

Requires Python 3 standard library only. These are checks, not a replacement
for the arbitrary-parameter proof in RESULT.md or an independent audit.
"""
from fractions import Fraction as R
from math import exp, log, sqrt


def det(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    sign, product = 1, 1
    for i in range(n):
        j = next((j for j in range(i, n) if a[j][i] != 0), None)
        if j is None:
            return 0
        if j != i:
            a[i], a[j] = a[j], a[i]
            sign = -sign
        pivot = a[i][i]
        product *= pivot
        for j in range(i + 1, n):
            t = a[j][i] / pivot
            for l in range(i + 1, n):
                a[j][l] -= t * a[i][l]
            a[j][i] = 0
    return sign * product


def char_matrix(lam, s, alpha, mu, tau, e, k, h, m, b, doses):
    """Characteristic matrix of the unmodified delay system, order S,I,Q_i."""
    n = len(k)
    c = alpha * (1 - e) / mu
    A = [k[i] * (1 - b[i] * e) + h[i] * c for i in range(n)]
    q = [doses[i] / (m[i] + A[i] * s) for i in range(n)]
    w = exp(-lam * tau) if lam != 0 else 1
    J = [[0] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        J[0][i + 2] = -k[i] * s
    J[1][0] = sum(k[i] * q[i] for i in range(n)) * (1 - e * w)
    J[1][1] = -mu
    for i in range(n):
        J[1][i + 2] = k[i] * s * (1 - e * w)
        J[i + 2][0] = k[i] * q[i] * (b[i] * e * w - 1)
        J[i + 2][1] = -h[i] * q[i]
        J[i + 2][i + 2] = -m[i] - k[i] * s - h[i] * c * s + k[i] * b[i] * e * s * w
    return [[(lam if i == j else 0) - J[i][j]
             for j in range(n + 2)] for i in range(n + 2)]


def data(n, s=None, exact=True):
    one = R(1) if exact else 1.0
    k = [one] * n
    h = [2 * one] * n
    m = [one] * n
    b = [2 * one, 6 * one] + [4 * one] * (n - 2)
    extra = [one / (64 * (n - 2))] * (n - 2) if n > 2 else []
    d2 = one / 16
    if s is None:
        d1 = one
    else:
        d1 = (one - d2 / (one - s) - sum(extra)) * (one + s)
        assert d1 > 0
    return k, h, m, b, [d1, d2] + extra


def check_exact():
    checks = 0
    for n in (2, 3, 4, 6):
        for s in (R(1, 16), R(1, 8), R(1, 4), R(1, 2), R(3, 4)):
            k, h, m, b, d = data(n, s)
            A = [1, -1] + [0] * (n - 2)
            a = [m[i] + A[i] * s for i in range(n)]
            fp = -sum(k[i] * d[i] * A[i] / (a[i] ** 2) for i in range(n))
            assert sum(k[i] * d[i] / a[i] for i in range(n)) == 1
            M = char_matrix(0, s, R(1), R(1), 0, R(1, 2), k, h, m, b, d)
            assert det(M) == s * fp * product(a), (n, s, det(M), fp)
            checks += 1
    # The degenerate family with every A_i=0 and flat F(s)=alpha.
    for n in (1, 2, 4):
        s = R(3, 7)
        k = [R(1)] * n; h = [R(2)] * n
        m = [R(1)] * n; b = [R(4)] * n; d = [R(1, n)] * n
        M = char_matrix(0, s, R(1), R(1), 0, R(1, 2), k, h, m, b, d)
        assert det(M) == 0
        checks += 1
    return checks


def product(xs):
    result = 1
    for x in xs:
        result *= x
    return result


def check_real_positive_root():
    count = 0
    for n in (2, 3, 4, 6):
        k, h, m, b, doses = data(n, exact=False)
        extra = 1 / 64 if n > 2 else 0.0
        F = lambda s: 1 / (1 + s) + 1 / (16 * (1 - s)) + extra
        assert F(0) > 1 and F(.6) < 1 and F(.999) > 1
        a, z = 0.0, .6
        for _ in range(70):
            mid = (a + z) / 2
            if F(mid) > 1:
                a = mid
            else:
                z = mid
        s = (a + z) / 2
        assert abs(F(s) - 1) < 5e-15
        fp = -1 / (1 + s) ** 2 + 1 / (16 * (1 - s) ** 2)
        assert fp < 0
        g = lambda lam: det(char_matrix(lam, s, 1., 1., log(2), .5, k, h, m, b, doses))
        assert g(0) < 0
        a, z = 0.0, 1.0
        while g(z) < 0 and z < 256:
            z *= 2
        assert g(z) > 0
        for _ in range(70):
            mid = (a + z) / 2
            if g(mid) < 0:
                a = mid
            else:
                z = mid
        assert 0 < (a + z) / 2 and abs(g((a + z) / 2)) < 1e-7
        print('POSITIVE_CHARACTERISTIC_ROOT', n, f'{(a + z) / 2:.12g}')
        count += 1
    return count


if __name__ == '__main__':
    exact = check_exact()
    roots = check_real_positive_root()
    print('VERIFY_OK exact_determinants', exact, 'positive_real_root_cases', roots)
