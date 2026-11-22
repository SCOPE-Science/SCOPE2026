"""Exact arithmetic consistency checks for a two-cluster cubic opinion cycle.

Run with Python 3: python checker.py. The infinite theorem relies on the
written algebraic proof, not on the finite arithmetic tests below.
"""
from fractions import Fraction as Q


def cubic_step(state, nu, k):
    n = len(state)
    av = sum(state, Q(0)) / n
    return tuple(x - nu * (x - av) + k * (x - av) ** 3 for x in state)


def jacobian_times(state, tangent, nu, k):
    n = len(state)
    av = sum(state, Q(0)) / n
    tv = sum(tangent, Q(0)) / n
    return tuple(t - nu * (t - tv) + 3 * k * (x - av) ** 2 * (t - tv)
                 for x, t in zip(state, tangent))


def family(n, m, beta):
    ell = n - m
    d_geom = m * m - m * ell + ell * ell
    q = Q(d_geom, n * n)
    k = beta / q                     # The constructed gap has magnitude exactly one.
    nu = Q(2) + beta
    h = k * Q(m * ell * (ell - m), n ** 3)
    a = -h / 2 + Q(ell, n)
    b = -h / 2 - Q(m, n)
    state = (a,) * m + (b,) * ell
    lam_d = -1 + 2 * beta
    lam_a = -1 - beta + 3 * beta * Q(ell ** 2, d_geom)
    lam_b = -1 - beta + 3 * beta * Q(m ** 2, d_geom)
    beta_c = Q(2 * d_geom, n * (2 * max(m, ell) - min(m, ell)))
    return state, nu, k, (lam_d, lam_a, lam_b), beta_c


def test():
    checks = 0
    for n in range(3, 13):
        for m in range(1, n):
            ell = n - m
            state, nu, k, (lam_d, lam_a, lam_b), beta_c = family(n, m, Q(1, 4))
            assert cubic_step(state, nu, k) == tuple(-x for x in state)
            assert cubic_step(tuple(-x for x in state), nu, k) == state
            unit = (Q(1),) * n
            assert jacobian_times(state, unit, nu, k) == unit
            if m >= 2:
                tangent = (Q(1), Q(-1)) + (Q(0),) * (n - 2)
                assert jacobian_times(state, tangent, nu, k) == tuple(lam_a * x for x in tangent)
            if ell >= 2:
                tangent = (Q(0),) * m + (Q(1), Q(-1)) + (Q(0),) * (ell - 2)
                assert jacobian_times(state, tangent, nu, k) == tuple(lam_b * x for x in tangent)
            tangent = (Q(ell, n),) * m + (Q(-m, n),) * ell
            acted = jacobian_times(state, tangent, nu, k)
            assert acted[0] - acted[-1] == lam_d * (tangent[0] - tangent[-1])
            # The sharp interval states strict spectral contraction only.
            predicted = (Q(1, 2) < Q(m, ell) < Q(2) and Q(0) < Q(1, 4) < beta_c)
            computed = (Q(-1) < lam_d < Q(1) and
                        (m == 1 or Q(-1) < lam_a < Q(1)) and
                        (ell == 1 or Q(-1) < lam_b < Q(1)))
            assert predicted == computed
            checks += 1

    n, m = 5, 2
    state = (Q(81, 140),) * 2 + (Q(-59, 140),) * 3
    gamma, alpha = Q(9, 5), Q(16, 63)
    c = Q(n, n - 1)
    nu, k = gamma * c, gamma * alpha * c ** 3
    assert (nu, k) == (Q(9, 4), Q(25, 28))
    assert cubic_step(state, nu, k) == tuple(-x for x in state)
    assert cubic_step(tuple(-x for x in state), nu, k) == state
    got, _, _, (ld, la, lb), critical = family(n, m, Q(1, 4))
    assert got == state
    assert (ld, la, lb, critical) == (Q(-1, 2), Q(-2, 7), Q(-23, 28), Q(7, 10))
    assert {ld ** 2, la ** 2, lb ** 2} == {Q(1, 4), Q(4, 49), Q(529, 784)}
    print('PASS:', checks, 'exact two-cluster checks, plus exact five-agent witness and multipliers')


if __name__ == '__main__':
    test()
