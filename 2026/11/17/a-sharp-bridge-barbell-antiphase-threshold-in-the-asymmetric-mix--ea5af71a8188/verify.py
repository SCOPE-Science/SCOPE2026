"""Exact rational checks for the asymmetric mixed-order Kuramoto antipodal theorem.
All triad summation indices are included, including repetitions.
Finite checks supplement, and do not replace, the all-size analytical proof.
"""
from fractions import Fraction as F
from math import comb


def complete(n):
    return [[int(i != j) for j in range(n)] for i in range(n)]


def barbell(h):
    n = 2 * h
    a = [[0] * n for _ in range(n)]
    for offset in (0, h):
        for i in range(offset, offset + h):
            for j in range(offset, offset + h):
                if i != j:
                    a[i][j] = 1
    a[0][h] = a[h][0] = 1
    return a


def jacobian(a, signs, k1, k2):
    """Differentiate every term of the original finite coupling sums."""
    n = len(signs)
    edges = sum(sum(row) for row in a)
    d = F(edges, n)
    assert d > 0
    j = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for q in range(n):
            if a[i][q]:
                c = k1 / d * a[i][q] * signs[i] * signs[q]
                j[i][q] += c
                j[i][i] -= c
        for q in range(n):
            for ell in range(n):
                # At antipodal phases cos(2theta_q-theta_ell-theta_i) = signs[i]*signs[ell].
                c = k2 / (n * n) * signs[i] * signs[ell]
                j[i][q] += 2 * c
                j[i][ell] -= c
                j[i][i] -= c
    return j


def mul(j, v):
    return [sum(x * y for x, y in zip(row, v)) for row in j]


def eigen_check(j, v, eigen):
    assert mul(j, v) == [eigen * w for w in v]


def quadratic(j, v):
    w = mul(j, v)
    return -sum(x * y for x, y in zip(v, w))


def positive_grounded(j):
    # Principal minor of -J after deleting vertex n-1, exact LDL no pivoting.
    a = [[-j[i][q] for q in range(len(j) - 1)] for i in range(len(j) - 1)]
    n = len(a)
    for k in range(n):
        pivot = a[k][k]
        if pivot <= 0:
            return False
        for i in range(k + 1, n):
            for q in range(i, n):
                a[q][i] -= a[i][k] * a[q][k] / pivot
                a[i][q] = a[q][i]
    return True


def test_complete():
    count = 0
    for n in range(2, 12):
        for q in range(1, n):
            p = n - q
            signs = [1] * p + [-1] * q
            for k1, k2 in [(F(1), F(1)), (F(3, 2), F(17, 7))]:
                j = jacobian(complete(n), signs, k1, k2)
                m = F(p - q, n)
                c = F(n, n - 1) * k1 + k2
                eplus = -m * c
                eminus = m * c
                erel = F(n, n - 1) * k1 + k2 * (2 * m * m - 1)
                eigen_check(j, [F(1)] * n, F(0))
                for i in range(p - 1):
                    v = [F(0)] * n
                    v[i], v[p - 1] = F(1), F(-1)
                    eigen_check(j, v, eplus)
                    count += 1
                for i in range(p, n - 1):
                    v = [F(0)] * n
                    v[i], v[n - 1] = F(1), F(-1)
                    eigen_check(j, v, eminus)
                    count += 1
                a = sum(j[0][p:])
                b = sum(j[p][:p])
                assert -(a + b) == erel
                v = [a] * p + [-b] * q
                if erel != 0:
                    eigen_check(j, v, erel)
                count += 2
    return count


def test_barbell():
    count = 0
    for h in [2, 3, 4, 5, 6, 8]:
        n = 2 * h
        d = F(h * h - h + 1, h)
        threshold = F(2 * h, 1) / (d * (h * h - 2 * h + 2))
        signs = [1] * h + [-1] * h
        a = barbell(h)
        for factor in [F(9, 10), F(1), F(11, 10)]:
            j = jacobian(a, signs, F(1), factor * threshold)
            assert all(x == y for x, y in zip(mul(j, [F(1)] * n), [F(0)] * n))
            for v in ([F(i - h) for i in range(n)],
                      [F(1) if i % 2 else F(0) for i in range(n)],
                      [F((i * i + 3) % 7 - 3) for i in range(n)]):
                pair = sum(F((v[i] - v[q]) ** 2) for i in range(n) for q in range(i + 1, n) if a[i][q])
                pair -= 2 * (v[0] - v[h]) ** 2  # invert sign of unique cross-edge
                analytic = pair / d + (factor * threshold) * sum(signs[i] * v[i] for i in range(n)) ** 2 / n
                assert quadratic(j, v) == analytic
                count += 1
            c = F(h * h, h - 1)
            z = F(2, 1) / (c - 2)
            u, w = z / 2, -z / 2
            v = [F(1, 2) + u] + [F(1, 2) - u / (h - 1)] * (h - 1)
            v += [F(-1, 2) + w] + [F(-1, 2) - w / (h - 1)] * (h - 1)
            qvalue = quadratic(j, v)
            if factor < 1:
                assert qvalue < 0
            elif factor == 1:
                assert qvalue == 0
            else:
                assert qvalue > 0
                assert positive_grounded(j)
            count += 2
    return count


if __name__ == '__main__':
    c = test_complete()
    b = test_barbell()
    print('VERIFY_OK complete_eigenvector_identities=%d barbell_quadratic_and_threshold_checks=%d' % (c, b))
    print('Finite rational checks; the full finite-size classification and asymptotic limit use analytical proofs.')
