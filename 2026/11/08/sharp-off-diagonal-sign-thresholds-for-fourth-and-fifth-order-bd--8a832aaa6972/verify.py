#!/usr/bin/env python3
"""Exact checker for sharp off-diagonal signs of BDF4/BDF5 fractional weights.

Python standard library only. The finite checks are paired with rigorous analytic
bounds in RESULT.md; running this program alone does not certify an infinite tail.
"""
from fractions import Fraction as Q
from math import comb


def normalized_bdf_symbol(k):
    """Construct sum_{j=1}^k (1-z)^j/j directly, then normalize."""
    coefficients = [sum((Q((-1)**i * comb(j, i), j)
                         for j in range(max(1,i), k+1)), Q(0))
                    for i in range(k+1)]
    return tuple(c / coefficients[0] for c in coefficients)

BDF = {
    4: {
        "alpha": Q(7, 32),
        "p": (Q(1), -Q(48, 25), Q(36, 25), -Q(16, 25), Q(3, 25)),
        "q": (Q(1), -Q(23, 25), Q(13, 25), -Q(3, 25)),
        "R": Q(7, 5),
        "M": Q(8),
        "expected_reflections": (Q(-1029, 3125), Q(726425, 1088348), Q(-1162595, 1814773)),
    },
    5: {
        "alpha": Q(13, 150),
        "p": (Q(1), -Q(300, 137), Q(300, 137), -Q(200, 137), Q(75, 137), -Q(12, 137)),
        "q": (Q(1), -Q(163, 137), Q(1), -Q(63, 137), Q(12, 137)),
        "R": Q(4, 3),
        "M": Q(9),
        "expected_reflections": (Q(1024, 3699), Q(-8905536, 12634025), Q(3865313017488, 4724118603137), Q(-1438423308, 3211002475)),
    },
}


def schur_constants(q, R):
    """For f(w)=w**m*q(R/w), return all exact Schur constants."""
    m = len(q) - 1
    p = [q[m - i] * R ** (m - i) for i in range(m + 1)]
    assert p[-1] == 1
    vals = []
    while len(p) >= 2:
        m = len(p) - 1
        c = p[0]
        assert abs(c) < 1, (m, c)
        vals.append(c)
        if m == 1:
            break
        p = [(p[j + 1] - c * p[m - j - 1]) / (1 - c * c) for j in range(m)]
        assert p[-1] == 1
    return tuple(vals)


def finite_weights(p, a, N):
    w = [Q(1)]
    for n in range(1, N + 1):
        t = sum((((1 + a) * j - n) * p[j] * w[n-j]
                 for j in range(1, min(n, len(p)-1) + 1)), Q(0)) / n
        w.append(t)
    return w


def verify_branch(order, d):
    a, p, q, R, M = (d[k] for k in ('alpha', 'p', 'q', 'R', 'M'))
    assert len(p) == order + 1 and len(q) == order
    assert p == normalized_bdf_symbol(order)
    assert all(p[j] == q[j] - (q[j-1] if j else Q(0)) for j in range(order))
    assert p[order] == -q[-1]
    constants = schur_constants(q, R)
    assert constants == d['expected_reflections']

    # The rational recurrence is an exact identity obtained from p W'=a p' W.
    W = finite_weights(p, a, 999)
    assert W[0] == 1 and W[1] < 0 and W[2] == 0
    assert all(W[n] < 0 for n in range(3, 1000))
    assert W[2] == a * p[2] + a * (a - 1) * p[1]**2 / 2

    # q has no zeros in |z|<=R by the Schur calculation above, so q^a is analytic.
    # The rational inequalities below are the inputs for the all-n>=1000 Cauchy bound.
    q_norm_bound = sum(abs(q[j]) * R**j for j in range(len(q)))
    if order == 4:
        assert q_norm_bound < 4 and a < Q(1, 4) and M == 8
    else:
        assert q_norm_bound < 6 and a < Q(1, 10) and M == 9
    # |q(z)^a|<2 on |z|=R. M>=3/(R-1) implies |eta(z)|<=M.
    assert M >= 3/(R-1)
    q_at_one = sum(q)
    assert 0 < q_at_one < 1
    C1 = M * R / (R-1) * 10 * (1 + a)
    C2 = M * R / (R-1) * (1+a) / (a * (1-a))
    # High-index convolution tail at n=1000. Its normalized bound decreases thereafter.
    assert Q(1001, 999)**2 < R
    assert C2 * 1000 * 999 * (1/R)**500 < Q(1, 100)
    assert C1 / 1000 + Q(1, 100) < q_at_one
    print(f'BDF{order}: exact negative coefficients n=1 and n=3..999; n=2 zero; '
          f'all n>=1000 certified by Cauchy-tail inequalities; '
          f'alpha={a}; Schur constants={len(constants)}; '
          f'C1/1000={float(C1/1000):.6f}; q(1)={q_at_one}')
    return W[3]


for order, d in BDF.items():
    v3 = verify_branch(order, d)
    if order == 4:
        assert v3 == -Q(133, 5000)
    else:
        assert v3 == -Q(676, 56307)

# BDF6 coefficient z^2: a*(150+7200*a)/2401 >0 for all a>0.
p6_1, p6_2 = normalized_bdf_symbol(6)[1:3]
assert p6_1 == -Q(120, 49) and p6_2 == Q(150, 49)
assert p6_2 - p6_1*p6_1/2 == Q(150, 2401)
assert p6_1*p6_1/2 == Q(7200, 2401)
print('BDF6: w_2(a)=a*(150+7200*a)/2401 >0 for every a>0.')
print('ALL EXACT CHECKS PASSED')
