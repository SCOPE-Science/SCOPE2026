"""Exact-rational finite diagnostics for the Mallows displacement-parity identity.

The theorem is analytic. Finite checks use rigorous tails, not extrapolation.
Run with: python verify_mallows_current.py
"""
from fractions import Fraction


def poch_factors(q, N):
    out = [Fraction(1)]
    p = Fraction(1)
    for j in range(1, N + 1):
        p *= 1 - q ** j
        out.append(p)
    return out


def check(q, N, M):
    assert 0 < q < 1 and M >= N + 1
    P = poch_factors(q, M)
    signed = Fraction(0)
    unsigned = Fraction(0)
    for r in range(N + 1):
        for ell in range(N + 1):
            term = q ** (r * ell + r + ell) / (P[r] * P[ell])
            unsigned += term
            signed += term if (r - ell) % 2 == 0 else -term
    # Approximate the infinite Pochhammer normalization by P[M].
    truncated_parity = (1 - q) * P[M] * signed
    truncated_mass = (1 - q) * P[M] * unsigned
    # Explicit product with M terms.
    finite_product = Fraction(1)
    for j in range(1, M + 1):
        finite_product *= ((1 - q ** j) / (1 + q ** j)) ** 2
    # Marginal R,L both have geometric law (1-q)*q**r. Thus the
    # omitted two-dimensional probability is <= 2*q**(N+1).
    omitted_joint = 2 * q ** (N + 1)
    # The Pochhammer normalization error is bounded by the tail of
    # the product, <= q**(M+1)/(1-q).
    normalization_error = unsigned * q ** (M + 1)
    # Logarithmic infinite-product remainder bound.
    product_error = 4 * q ** (M + 1) / ((1 - q) * (1 - q ** (M + 1)))
    bound = omitted_joint + normalization_error + product_error
    assert 0 < truncated_mass <= 1
    assert 0 < finite_product < 1
    assert abs(truncated_parity - finite_product) <= bound
    print('q=', q, 'N=', N, 'M=', M,
          'finite product=', float(finite_product),
          'finite joint sum=', float(truncated_parity),
          'exact tail bound=', float(bound), 'OK')


if __name__ == '__main__':
    for arg in [(Fraction(1, 4), 25, 45),
                (Fraction(1, 2), 30, 50),
                (Fraction(2, 3), 45, 65),
                (Fraction(3, 4), 50, 75)]:
        check(*arg)
    print('Exact-rational finite diagnostics passed; analytic proof required for all real q.')
