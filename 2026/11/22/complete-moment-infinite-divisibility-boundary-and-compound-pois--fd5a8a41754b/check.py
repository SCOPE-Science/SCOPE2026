"""Finite, reproducible tests of exact formulas; not an infinite proof.

Run with Python 3.11+ (standard library only): python check.py
"""
from decimal import Decimal, getcontext
from math import comb

getcontext().prec = 110
D = Decimal
q = D('0.5')


def h(n, N, M):
    return ((1 + M * q**n) / (1 + N * q**n)).ln()


def coeff(k, N, M):
    return ((-1)**(k-1)) * (M**k - N**k) / D(k)


def difference(n, m, N, M):
    # This is (-1)^m Delta^m h_n, using exact binomial coefficients.
    return sum(D((-1)**j * comb(m, j)) * h(n + j, N, M)
               for j in range(m + 1))


def direct_moment(n, N, M, power):
    s = D(0)
    for j in range(n):
        s -= h(j, N, M)
    return (power * s).exp()


def poisson_moment(n, N, M, power, cutoff=720):
    b = [coeff(k, N, M) / (1 - q**k) for k in range(1, cutoff + 1)]
    return (-power * sum(b[k-1] * (1 - q**(k*n))
                         for k in range(1, cutoff + 1))).exp()


def run():
    tests = 0
    for Nstr, Mstr in [('-0.6', '-0.4'), ('-0.6', '0.4'),
                         ('-0.6', '0.6'), ('-0.9', '0.8')]:
        N, M = D(Nstr), D(Mstr)
        for k in range(1, 81):
            assert coeff(k, N, M) >= 0
            tests += 1
        for n in range(1, 18):
            for s in [D('0.2'), D('0.5'), D('1'), D('2.5')]:
                lhs = direct_moment(n, N, M, s)
                rhs = poisson_moment(n, N, M, s)
                assert abs(lhs-rhs) < D('1e-29'), (N, M, n, s, lhs, rhs)
                tests += 1
        for n in range(0, 8):
            for m in range(0, 14):
                assert difference(n, m, N, M) > -D('1e-65')
                tests += 1
    # Outside the wedge, c2 is negative and explicit high-order differences fail.
    N, M = D('-0.3'), D('0.6')
    assert coeff(2, N, M) == D('-0.135')
    assert difference(2, 11, N, M) < -D('0.000003')
    tests += 2
    # Boundary has no even jump intensities.
    N, M = D('-0.6'), D('0.6')
    for j in range(1, 40):
        assert coeff(2*j, N, M) == 0
        tests += 1
    print(f'PASS: {tests} supplementary finite tests')


if __name__ == '__main__':
    run()
