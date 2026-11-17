"""Standalone exact-rational diagnostics for the reported finite coefficients.
The global theorem rests on the separate analytic proof, not this finite test.
"""
from fractions import Fraction as Q


def threshold(a, m):
    value = Q(1)
    for j in range(1, m + 1):
        value *= (j - a) / (j + 1)
    return value


def c_coefficients(a, N):
    c = [Q(0)] * (N + 1)
    c[1] = a
    for n in range(2, N + 1):
        c[n] = c[n - 1] * (n - 1 - a) / n
    return c


def d_coefficients(a, N):
    d = [Q(1)] + [Q(0)] * N
    for n in range(1, N + 1):
        d[n] = d[n - 1] * (a + n - 1) / n
    return d


def f_coefficient(c, m, tau, n):
    if n < m:
        return c[n]
    if n == m:
        return c[n] + tau
    return c[n] - tau * c[n - m]


assertions = 0
for a in map(Q, ['1/4', '1/3', '1/2', '2/3', '3/4', '1']):
    for m in range(2, 13):
        N = m + 120
        c = c_coefficients(a, N)
        T = threshold(a, m)
        tau_values = (Q(0), T / 2, T, (T + 1) / 2, Q(1))
        for tau in tau_values:
            for n in range(1, N + 1):
                v = f_coefficient(c, m, tau, n)
                if tau <= T:
                    assert v >= 0, (a, m, tau, n, v)
                elif n == m + 1:
                    assert v < 0, (a, m, tau, n, v)
                assertions += 1
        if a < 1:
            assert threshold(a, m + 1) / T == (m + 1 - a) / (m + 2)
            assertions += 1

# Explicit example, including the operator inequality failure.
a, m, tau = Q(1, 2), 2, Q(1, 10)
assert tau < threshold(a, m)
d = d_coefficients(a, 3)
k = [sum((tau ** j) * d[n - j * m] for j in range(n // m + 1)) for n in range(4)]
assert k == [Q(1), Q(1, 2), Q(19, 40), Q(29, 80)]
w1sq, w2sq = k[1] / k[2], k[2] / k[3]
assert w1sq == Q(20, 19) and w2sq == Q(38, 29)
assert w1sq * w2sq - 2 * w1sq + 1 == Q(151, 551)
assertions += 5
print(f'PASS: {assertions} finite exact-rational assertions; global conclusions are analytical.')
