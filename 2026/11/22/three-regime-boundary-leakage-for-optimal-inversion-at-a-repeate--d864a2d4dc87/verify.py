"""Finite diagnostics for repeated-root optimal polynomial residual profiles.

Requires Python 3 and mpmath. Usage: python verify.py
Finite diagnostics are not proofs of the uniform asymptotic theorem.
"""
import mpmath as mp

mp.mp.dps = 65


def constants(m, alpha):
    beta = 1 - mp.mpf(alpha)
    c = (-1) ** (m - 1) * mp.rf(beta, m) / mp.factorial(m - 1)
    d = beta * (mp.rf(beta + 1, m - 1) / mp.factorial(m - 1)) ** 2
    H = mp.matrix([[1 / (beta + i + j) for j in range(m)] for i in range(m)])
    a = mp.lu_solve(H, mp.matrix([1] + [0] * (m - 1)))
    assert mp.almosteq(sum(a), c, rel_eps=mp.mpf('1e-45'), abs_eps=mp.mpf('1e-45'))
    assert mp.almosteq(a[0], d, rel_eps=mp.mpf('1e-45'), abs_eps=mp.mpf('1e-45'))
    return c, d


def residual(m, alpha, L, z):
    alpha = mp.mpf(alpha)
    moment = [sum(k ** j / mp.power(k + 1, alpha) for k in range(L + 1))
              for j in range(2 * m - 1)]
    E = mp.matrix([[moment[i + j] for j in range(m)] for i in range(m)])
    A = mp.lu_solve(E, mp.matrix([1] + [0] * (m - 1)))
    coefs = [mp.power(k + 1, -alpha) *
             sum(A[j] * k ** j for j in range(m)) for k in range(L + 1)]
    for j in range(m):
        lhs = sum(coefs[k] * k ** j for k in range(L + 1))
        assert abs(lhs - (1 if j == 0 else 0)) < mp.mpf('1e-38')
    return sum(coefs[k] * z ** k for k in range(L + 1))


def prediction(m, alpha, L, z):
    c, d = constants(m, alpha)
    alpha = mp.mpf(alpha)
    if alpha < 0:
        return c * z ** (L + 1) / (z - 1), mp.mpf(L)
    if alpha == 0:
        return (c * z ** (L + 1) - d) / (z - 1), mp.mpf(L)
    return d * mp.lerchphi(z, alpha, 1), mp.power(L, 1 - alpha)


def main():
    tests = 0
    for m in (2, 3):
        for alpha in ('-1', '0', '0.5'):
            for z in (mp.exp(mp.j * mp.mpf('0.7')), mp.mpf('-1')):
                prev = None
                for L in (90, 450):
                    r = residual(m, alpha, L, z)
                    pred, scale = prediction(m, alpha, L, z)
                    error = abs(scale * r - pred)
                    assert mp.isfinite(error)
                    if L == 450:
                        assert error < 4, (m, alpha, z, error)
                    prev = error
                    tests += 1
                print('m=', m, 'alpha=', alpha, 'z=', mp.nstr(z, 7),
                      'L=450 scaled discrepancy=', mp.nstr(prev, 9))
    for m in range(2, 7):
        for alpha in ('-2', '-1', '0', '0.5', '0.9'):
            constants(m, alpha)
            tests += 1
    print('PASS:', tests, 'finite moment and asymptotic diagnostics')


if __name__ == '__main__':
    main()
