"""Standalone finite checks for norm-power sampling of scalar projected rows.

Python 3, standard library only. Assertions supplement, not replace, the
analytic all-parameter proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import isclose

exact_checks = 0
floating_checks = 0


def check(statement):
    global exact_checks
    assert statement
    exact_checks += 1


def near(a, b, tol=2e-10):
    global floating_checks
    assert isclose(float(a), float(b), rel_tol=tol, abs_tol=tol), (a, b)
    floating_checks += 1


def moment(s, d, beta, q):
    denominator = sum((x**beta for x in s), F(0))
    return sum((x**(beta-q) * abs(y)**q for x, y in zip(s, d)), F(0)) / denominator


# Exact scalar row-projection distribution, including signed observations.
row_sizes = [F(1), F(1, 2), F(2, 3), F(3, 4)]
observations = [F(-1), F(0), F(1, 3), F(1)]
for beta in range(1, 6):
    for q in range(1, 7):
        for s2 in row_sizes:
            for d1, d2 in product(observations, repeat=2):
                s = [F(1), s2]
                d = [d1, d2]
                z = F(1) + s2**beta
                p1, p2 = F(1)/z, s2**beta/z
                direct = p1 * abs(d1)**q + p2 * abs(d2/s2)**q
                check(direct == moment(s, d, beta, q))

# The concrete 3 x 2 least-squares family has A^T A = I + vv^T,
# v=(1,eps); its eigenvalues are 1 and 2+eps^2, uniformly conditioned.
for beta in range(1, 6):
    for q in range(1, 9):
        for denominator in range(1, 30):
            eps = F(1, denominator)
            a00, a01, a11 = F(2), eps, F(1)+eps*eps
            tr, det = a00+a11, a00*a11-a01*a01
            check(tr == F(3)+eps**2)
            check(det == F(2)+eps**2)
            # Fixed first equation x_1=0; sampled rows set x_2=1 or 1/eps.
            p_bad = eps**beta/(F(1)+eps**beta)
            direct = (F(1)-p_bad) + p_bad*eps**(-q)
            exact = (F(1)+eps**(beta-q))/(F(1)+eps**beta)
            check(direct == exact)
            # Full least-squares target x*=((1-eps),(2+eps))/(2+eps*eps).
            x1 = (F(1)-eps)/(F(2)+eps**2)
            x2 = (F(2)+eps)/(F(2)+eps**2)
            check(a00*x1 + a01*x2 == F(1))
            check(a01*x1 + a11*x2 == F(1)+eps)
            # Worst-tail probability for R=1/eps is exactly 1/(1+R^beta).
            check(p_bad == F(1)/(F(1)+denominator**beta))

# At beta=q the sharp supremum m is approached by m-1 small rows.
for m in range(2, 9):
    for beta in range(1, 5):
        previous = F(0)
        for denominator in [2, 3, 5, 11, 23, 47]:
            eps = F(1, denominator)
            s = [F(1)] + [eps]*(m-1)
            d = [F(1)]*m
            val = moment(s, d, beta, beta)
            check(previous < val < m)
            previous = val

# For beta>q the candidate t is the unique root of
# beta*t^q + q*(m-1)*t^beta = beta-q.
def root(m, beta, q):
    low, high = 0.0, 1.0
    for _ in range(100):
        t = (low+high)/2
        if beta*t**q+q*(m-1)*t**beta < beta-q:
            low = t
        else:
            high = t
    return (low+high)/2

for m in range(2, 12):
    for beta in range(2, 10):
        for q in range(1, beta):
            t = root(m, beta, q)
            near(beta*t**q + q*(m-1)*t**beta, beta-q)
            sharp = (1+(m-1)*t**(beta-q))/(1+(m-1)*t**beta)
            for s in [i/100 for i in range(1, 101)]:
                val = (1+(m-1)*s**(beta-q))/(1+(m-1)*s**beta)
                assert val <= sharp*(1+1e-12), (m, beta, q, t, s)
                floating_checks += 1
            # Jensen upper bound for nonuniform remaining row lengths.
            if m <= 7:
                choices = [0.1, 0.35, 0.7, 1.0]
                for sample in product(choices, repeat=m-1):
                    z = sum(x**beta for x in sample)
                    val = (1 + sum(x**(beta-q) for x in sample))/(1+z)
                    assert val <= sharp*(1+1e-12), (m, beta, q, val, sharp)
                    floating_checks += 1

print(f"PASS: {exact_checks} exact-rational assertions, {floating_checks} floating-point supplementary checks")
