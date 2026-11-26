"""Exact arithmetic spot checks for a Wythoff additive-representation identity.

The infinite distribution and error bounds are proved in the accompanying text,
not inferred from these finite checks.
"""
from math import isqrt


def floor_alpha(n):
    """Exact floor(n*(sqrt(5)-1)/2), n a nonnegative integer."""
    return (isqrt(5*n*n) - n) // 2


def sign_quadratic(a, b):
    """Exact sign of a+b*sqrt(5), with integer a,b."""
    if b == 0:
        return (a > 0) - (a < 0)
    if a == 0:
        return (b > 0) - (b < 0)
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    if a > 0:
        return (a*a > 5*b*b) - (a*a < 5*b*b)
    return (5*b*b > a*a) - (5*b*b < a*a)


def via_rotation(n):
    fn = floor_alpha(n)
    K = n - fn - 1
    A, B = -n-2*fn, n
    position = sign_quadratic(A-3, B+1)
    if position < 0:  # 0 < {n alpha} < beta
        return sum(sign_quadratic(2*A+8*k+6*floor_alpha(k),
                                  2*B-4*k-2*floor_alpha(k)) < 0
                   for k in range(1, K+1))
    if sign_quadratic(A-6, B+2) < 0:  # beta < t < 2 beta
        return sum(sign_quadratic(2*A+8*k+6*floor_alpha(k)-6,
                                  2*B-4*k-2*floor_alpha(k)+2) > 0
                   for k in range(1, K+1))
    return K


def direct(n, lower):
    return sum((n - 2*k - floor_alpha(k)) in lower
               for k in range(1, n - floor_alpha(n)))


def main():
    limit = 2400
    lower = {h + floor_alpha(h) for h in range(1, limit+1)}
    checked = 0
    for n in range(3, limit + 1):
        r = via_rotation(n)
        expected = direct(n, lower)
        assert r == expected, (n, r, expected)
        assert 0 <= r <= n - floor_alpha(n) - 1
        checked += 1
    for n in (2500, 5000, 10000, 20000, 40000):
        r = via_rotation(n)
        K = n-floor_alpha(n)-1
        assert 0 <= r <= K
    print('VERIFY_OK exact_two_way_checks=%d additional_large_checks=5' % checked)


if __name__ == '__main__':
    main()
