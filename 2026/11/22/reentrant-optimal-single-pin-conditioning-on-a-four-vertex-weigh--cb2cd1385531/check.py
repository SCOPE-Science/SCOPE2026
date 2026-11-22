"""Exact-rational certificate for a four-vertex pinned-Laplacian condition-number reversal.

Run using the Python standard library: python check.py
No floating-point operation is used by the verifier.
"""
from fractions import Fraction as F

WEIGHTS = (1, 25, 5)
SCALE = 10**6
# At each gain, the four rows correspond to pinning vertices 1, 2, 3, 4.
# Each integer is the lower endpoint (in millionths) of one eigenvalue interval;
# its upper endpoint is the next integer in millionths.
ROOT_BRACKETS = {
    10: ((291272, 7255942, 11081821, 53370962),
         (875395, 2357896, 10370399, 58396308),
         (841352, 2736707, 9160804, 59261135),
         (635059, 2367725, 15555499, 53441716)),
    50: ((313978, 7314171, 50832636, 53539213),
         (978997, 3596816, 20394480, 87029705),
         (939348, 4466857, 16540629, 90053164),
         (721495, 2968461, 50338282, 57971760)),
    500: ((319423, 7319191, 53359273, 501002111),
          (997990, 3992385, 29750712, 527258911),
          (958065, 4949567, 24807932, 531284434),
          (741047, 3147307, 53058874, 505052770))
}
EXPECTED_MINIMIZERS = {10: 2, 50: 4, 500: 2}


def characteristic_at(x, pin, gain):
    """Exact det(A_pin(gain)-x I) via the tridiagonal continuant."""
    w = WEIGHTS
    d = [w[0], w[0]+w[1], w[1]+w[2], w[2]]
    d[pin-1] += gain
    prev, cur = F(1), F(d[0])-x
    for k in range(1, 4):
        prev, cur = cur, (F(d[k])-x)*cur - w[k-1]**2*prev
    return cur


def verify():
    total_brackets = 0
    for gain, rows in ROOT_BRACKETS.items():
        kappas = []
        assert len(rows) == 4
        for pin, vals in enumerate(rows, 1):
            assert len(vals) == 4
            intervals = [(F(k, SCALE), F(k+1, SCALE)) for k in vals]
            assert all(0 < l < u for l,u in intervals)
            assert all(intervals[j][1] < intervals[j+1][0] for j in range(3))
            # Four disjoint sign-changing intervals for a degree-four polynomial
            # certify ALL four real roots, and exactly one root in each.
            for lower, upper in intervals:
                assert characteristic_at(lower, pin, gain) * characteristic_at(upper, pin, gain) < 0
                total_brackets += 1
            # Since eigenvalues lie in their isolated intervals,
            # these are exact rational bounds on the 2-norm condition number.
            small_l, small_u = intervals[0]
            large_l, large_u = intervals[-1]
            kappas.append((large_l / small_u, large_u / small_l))
        best = EXPECTED_MINIMIZERS[gain] - 1
        for other in range(4):
            if other != best:
                assert kappas[best][1] < kappas[other][0], (gain, best+1, other+1)
        print('gain', gain, 'unique optimal vertex', best+1)
        for pin,(low,high) in enumerate(kappas,1):
            print(' vertex',pin, 'kappa in', '%.8f'%float(low), 'to', '%.8f'%float(high))
    assert total_brackets == 48
    print('PASS: 48 disjoint exact-rational eigenvalue sign brackets; 9 strict optimality inequalities')


if __name__ == '__main__':
    verify()
