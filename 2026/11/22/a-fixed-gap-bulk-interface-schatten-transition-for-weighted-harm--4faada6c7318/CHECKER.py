#!/usr/bin/env python3
"""Finite diagnostics for weighted-harmonic Toeplitz commutators.

Uses only the Python standard library. Finite checks support, but do not
prove, the infinite-dimensional asymptotic statements.
"""
import math


def moment(j, beta):
    return math.exp(math.lgamma(beta + 1) + math.lgamma(j + 1)
                    - math.lgamma(j + beta + 1))


def action(power, j, beta):
    """Coefficient of T_{z^power} e_j on e_{j+power}."""
    if j >= 0:
        return math.sqrt(moment(j + power, beta) / moment(j, beta))
    if j <= -power:
        return math.sqrt(moment(-j, beta) / moment(-j-power, beta))
    return moment(power, beta) / math.sqrt(moment(-j, beta) *
                                             moment(j + power, beta))


def direct_coefficient(m, n, k, beta):
    return (action(n, -k, beta) * action(m, n-k, beta)
            - action(m, -k, beta) * action(n, m-k, beta))


def formula(m, n, k, beta):
    M = m + n
    if k <= n:
        return math.sqrt(moment(M-k, beta) / moment(k, beta)) * (
            moment(n, beta) / moment(n-k, beta)
            - moment(m, beta) / moment(m-k, beta))
    if k < m:
        return moment(m, beta) * (
            math.sqrt(moment(k, beta) / moment(M-k, beta))
            / moment(k-n, beta)
            - math.sqrt(moment(M-k, beta) / moment(k, beta))
            / moment(m-k, beta))
    return math.sqrt(moment(k, beta) / moment(M-k, beta)) * (
        moment(m, beta) / moment(k-n, beta)
        - moment(n, beta) / moment(k-m, beta))


def gamma_g(j, beta):
    return math.exp(math.lgamma(j + beta + 1) - math.lgamma(j+1))


def main():
    checks = 0
    for beta in (0.2, 0.4, 0.7, 0.9):
        for n in range(1, 36):
            for d in range(1, 9):
                m, M = n+d, 2*n+d
                for k in range(1, M):
                    a = direct_coefficient(m, n, k, beta)
                    b = formula(m, n, k, beta)
                    assert abs(a-b) < 3e-11, (beta, n, d, k, a, b)
                    checks += 1
                    c = formula(m, n, M-k, beta)
                    assert abs(b+c) < 3e-11, (beta, n, d, k, b, c)
                    checks += 1
    for beta in (0.2, 0.4, 0.7, 0.9):
        for d in (1, 2, 5):
            for n in (1000, 3000):
                # Isolated gamma boundary modes: relative accuracy improves with n.
                for r in range(-4, d+5):
                    measured = n**beta * formula(n+d, n, n+r, beta)
                    limit = gamma_g(abs(r), beta)-gamma_g(abs(d-r), beta)
                    assert abs(measured-limit) < 0.15, (beta, d, n, r, measured, limit)
                    checks += 1
                singular = [abs(formula(n+d,n,k,beta)) for k in range(1, 2*n+d)]
                maxlimit = gamma_g(d,beta)-gamma_g(0,beta)
                assert abs(n**beta*max(singular) - maxlimit) < 0.15
                checks += 1
    print('NEAR_DIAGONAL_HARMONIC_BERGMAN_DIAGNOSTIC_OK', checks)


if __name__ == '__main__':
    main()
