#!/usr/bin/env python3
"""Exact arithmetic checks for cube--cross-polytope lattice joins."""
from math import comb, factorial


def eulerian(p):
    assert p >= 1
    a = [1]
    for n in range(2, p + 1):
        a = [(k + 1) * (a[k] if k < len(a) else 0)
             + (n - k) * (a[k - 1] if k else 0)
             for k in range(n)]
    return a


def h_star(p, q):
    a = eulerian(p)
    h = [0] * (p + q)
    for k, v in enumerate(a):
        for j in range(q + 1):
            h[k + j] += v * comb(q, j)
    return h


def numerator_coefficients(p, q):
    """Returns d! times the ordinary Ehrhart coefficients, as integers."""
    d = p + q + 1
    totals = [0] * (d + 1)
    for i, weight in enumerate(h_star(p, q)):
        product = [1]
        for r in range(1, d + 1):
            new = [0] * (len(product) + 1)
            for j, value in enumerate(product):
                new[j] += (r - i) * value
                new[j + 1] += value
            product = new
        for k, value in enumerate(product):
            totals[k] += weight * value
    return totals


def cross_count(q, m):
    return sum(2 ** j * comb(q, j) * comb(m, j)
               for j in range(min(q, m) + 1))


def direct_count(p, q, t):
    return sum((t - s + 1) ** p * cross_count(q, s)
               for s in range(t + 1))


def evaluate_integer_polynomial(coefs, t):
    value = 0
    for c in reversed(coefs):
        value = value * t + c
    return value


def main():
    positive_cases = 0
    boundary_negative = []
    coefficient_tests = 0
    counting_tests = 0
    for total in range(2, 18):
        for p in range(1, total):
            q = total - p
            d = total + 1
            coeff = numerator_coefficients(p, q)
            assert len(coeff) == d + 1
            assert coeff[0] == factorial(d)
            assert coeff[d] == factorial(p) * 2 ** q
            bad = [i for i, x in enumerate(coeff) if x <= 0]
            if total <= 16:
                assert not bad, (p, q, bad)
                positive_cases += 1
            else:
                if bad:
                    assert bad == [1], (p, q, bad)
                    boundary_negative.append((p, q))
                else:
                    assert all(x > 0 for x in coeff)
            coefficient_tests += len(coeff)
            # Independent direct count of integer lattice points from join slices.
            for t in list(range(d + 1)) + [d + 3]:
                assert (evaluate_integer_polynomial(coeff, t)
                        == factorial(d) * direct_count(p, q, t)), (p, q, t)
                counting_tests += 1
    assert positive_cases == 120
    assert boundary_negative == [(14, 3), (16, 1)], boundary_negative
    assert coefficient_tests == 1904
    # A reentrant positivity pattern as the cross-polytope dimension increases.
    at14 = {}
    for q in (2, 3, 4, 5):
        coeff = numerator_coefficients(14, q)
        at14[q] = all(x > 0 for x in coeff)
        bad_indices = [k for k, value in enumerate(coeff) if value <= 0]
        assert bad_indices == ([1] if q in (3, 4) else []), (q, bad_indices)
        for t in list(range(14 + q + 2)) + [14 + q + 4]:
            assert evaluate_integer_polynomial(coeff, t) == factorial(14 + q + 1) * direct_count(14, q, t)
            counting_tests += 1
        coefficient_tests += len(coeff)
    assert at14 == {2: True, 3: False, 4: False, 5: True}
    assert numerator_coefficients(14, 3)[1] * 510 == -10397 * factorial(18)
    assert numerator_coefficients(16, 1)[1] * 170 == -897 * factorial(18)
    assert numerator_coefficients(14, 4)[1] * 3990 == -76729 * factorial(19)
    assert numerator_coefficients(14, 5)[1] * 67830 == 618397 * factorial(20)
    print('PASS: 120 strictly positive pairs in total dimension <=17;')
    print('PASS: the only dimension-18 failures are (14,3) and (16,1);')
    print('PASS: reentrant positivity for p=14, q=2,3,4,5;')
    print('PASS: %d integer coefficient sign checks and %d direct-count identities' %
          (coefficient_tests, counting_tests))


if __name__ == '__main__':
    main()
