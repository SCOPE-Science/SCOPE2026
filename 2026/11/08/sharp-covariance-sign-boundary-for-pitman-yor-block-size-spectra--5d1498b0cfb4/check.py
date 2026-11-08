#!/usr/bin/env python3
"""Independent exact CRP enumeration and analytic consistency tests (stdlib only)."""
from fractions import Fraction as Q
from math import comb, gamma, exp, pi


def rising(x, k):
    z = Q(1)
    for j in range(k):
        z *= x + j
    return z


def recurrence_g(n, alpha, theta):
    z = Q(0)
    for i in range(n):
        if i == 0:
            z = Q(1)
        else:
            z += (theta + alpha*z) / (theta + i)
    return z


def frequency_mean(n, r, alpha, theta):
    return Q(comb(n, r)) * rising(1-alpha, r-1) * rising(theta+alpha, n-r) / rising(theta+1, n-1)


def covariance_formula(n, r, alpha, theta):
    return frequency_mean(n, r, alpha, theta) * (
        1 + recurrence_g(n-r, alpha, theta+alpha) - recurrence_g(n, alpha, theta))


def exact_enumeration(n, alpha, theta):
    """Build each restricted-growth partition by its CRP transition probabilities."""
    E_M = [Q(0)] * (n+1)
    E_MK = [Q(0)] * (n+1)
    E_K = Q(0)
    total = Q(0)
    leaves = 0

    def rec(i, sizes, p):
        nonlocal E_K, total, leaves
        if i == n:
            leaves += 1
            k = len(sizes)
            total += p
            E_K += p*k
            for r in range(1, n+1):
                count = sizes.count(r)
                E_M[r] += p*count
                E_MK[r] += p*count*k
            return
        den = theta + i
        for j in range(len(sizes)):
            b = list(sizes)
            b[j] += 1
            rec(i+1, tuple(b), p*(sizes[j]-alpha)/den)
        rec(i+1, sizes+(1,), p*(theta+alpha*len(sizes))/den)

    rec(1, (1,), Q(1))
    return total, E_K, E_M, E_MK, leaves


def float_g_sequence(n, alpha, theta):
    z = [0.0]*(n+1)
    z[1] = 1.0
    for i in range(1,n):
        z[i+1] = z[i] + (theta + alpha*z[i])/(theta+i)
    return z


def main():
    checks = 0
    params = [(Q(1,2),Q(0)),(Q(1,2),Q(1,2)),(Q(1,3),Q(1)),
              (Q(3,4),Q(-1,2)),(Q(0),Q(2))]
    for alpha, theta in params:
        for n in range(2,9):
            total, ek, em, emk, leaves = exact_enumeration(n, alpha, theta)
            assert total == 1 and leaves > 0
            checks += 2
            gn = recurrence_g(n, alpha, theta)
            assert ek == gn
            checks += 1
            signs = []
            for r in range(1,n+1):
                assert em[r] == frequency_mean(n,r,alpha,theta)
                assert emk[r] - em[r]*ek == covariance_formula(n,r,alpha,theta)
                h = 1 + recurrence_g(n-r,alpha,theta+alpha) - gn
                if r == 1:
                    assert h > 0
                signs.append(1 if h>0 else (-1 if h<0 else 0))
                checks += 3
            assert signs[0] == 1 and signs[-1] == -1
            assert all(signs[i] >= signs[i+1] for i in range(n-1))
            checks += 2
    for alpha, theta in [(0.5,0.0),(0.5,0.5),(0.0,2.0),
                         (0.3333333333333333, 1.0)]:
        n=12000
        gn = float_g_sequence(n,alpha,theta)
        shifted=float_g_sequence(n,alpha,theta+alpha)
        cutoff=max(r for r in range(1,n+1) if 1+shifted[n-r]-gn[n]>0)
        if alpha:
            def aa(t):
                return gamma(t+1)/(alpha*gamma(t+alpha))
            rho=1-(aa(theta)/aa(theta+alpha))**(1/alpha)
        else:
            rho=1-exp(-1/theta)
        assert abs(cutoff/n-rho) < 0.006, (alpha,theta,cutoff/n,rho)
        checks += 1
    assert abs((1-4/pi**2)-(1-(gamma(1)/(0.5*gamma(0.5))/(gamma(1.5)/(0.5*gamma(1))))**2)) < 1e-12
    assert abs((1-pi**2/16)-(1-(gamma(1.5)/(0.5*gamma(1))/(gamma(2)/(0.5*gamma(1.5))))**2)) < 1e-12
    checks += 2
    print('PASS: %d independent exact/analytic assertions; n up to 8, 5 parameter sets; asymptotic cutoff tests' % checks)

if __name__ == '__main__':
    main()
