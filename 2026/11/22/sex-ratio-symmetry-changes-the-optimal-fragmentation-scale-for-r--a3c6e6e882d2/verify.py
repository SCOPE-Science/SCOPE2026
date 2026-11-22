#!/usr/bin/env python3
"""Finite reproducibility checks for a two-sex Poisson mating-site benchmark.

Standard library only. Numerical tests supplement, rather than replace, the proof.
"""
import math


def logsumexp(xs):
    m = max(xs)
    if m == float('-inf'):
        return m
    return m + math.log(sum(math.exp(x - m) for x in xs))


def site_probability(L, theta, k):
    t = L / k
    return (-math.expm1(-theta * t)) * (-math.expm1(-(1-theta) * t))


def log_failure(L, theta, k, r):
    if k < r:
        return 0.0
    a = min(theta, 1-theta)
    b = 1-a
    delta = b-a
    t = L/k
    logq = -a*t + math.log1p(math.exp(-delta*t)*(-math.expm1(-a*t)))
    p = site_probability(L, theta, k)
    if p == 0:
        return 0.0
    if logq == float('-inf'):
        return float('-inf')
    terms = []
    for j in range(r):
        terms.append(math.lgamma(k+1)-math.lgamma(j+1)-math.lgamma(k-j+1)
                     + j*math.log(p)+(k-j)*logq)
    return logsumexp(terms)


def recurrence_tail(p, k, r):
    """Distinct dynamic-programming convolution, without binomial coefficients."""
    prob = [1.0]
    for _ in range(k):
        nxt = [0.0]*(len(prob)+1)
        for j, val in enumerate(prob):
            nxt[j] += val*(1-p)
            nxt[j+1] += val*p
        prob = nxt
    return sum(prob[:r])


def verify():
    checks = 0
    for theta in (0.1, 0.3, 0.5, 0.7, 0.9):
        for L in (0.2, 0.7, 3., 11., 37.):
            for k in range(1, 25):
                t = L/k
                p = site_probability(L, theta, k)
                q_alt = (math.exp(-theta*t)+math.exp(-(1-theta)*t)-math.exp(-t))
                assert abs((1-p)-q_alt) < 1e-12
                checks += 1
                for r in (1, 2, 3, 5):
                    logf = log_failure(L, theta, k, r)
                    actual = math.exp(logf)
                    independent = recurrence_tail(p, k, r)
                    assert abs(actual-independent) < 4e-11, (L, theta, k, r, actual, independent)
                    checks += 1
        for L in (0.3, 2., 17., 80.):
            one = 1-math.exp(log_failure(L, theta, 1, 1))
            for k in range(2, 32):
                other = 1-math.exp(log_failure(L, theta, k, 1))
                assert one >= other-1e-12
                checks += 1

    # For small L, the Markov bound kp/r < current success certifies
    # that *every* larger k is inferior without unbounded enumeration.
    for L in (4.0, 9.0):
        for theta in (0.3, 0.5, 0.8):
            for r in (2, 3):
                best = -1.0
                bestk = None
                for k in range(r, 2001):
                    success = -math.expm1(log_failure(L, theta, k, r))
                    if success > best:
                        best, bestk = success, k
                assert best > 0
                assert theta*(1-theta)*L*L/(r*2001) < best
                checks += 1

    for theta in (0.5, 0.3):
        for L in (100., 400., 1600., 6400.):
            r = 2
            cap = max(25, math.ceil(2*L))
            ranks = [(log_failure(L, theta, k, r),k) for k in range(r, cap+1)]
            score, kopt = min(ranks)
            assert log_failure(L, theta, kopt, r) == score
            scaled = kopt/math.sqrt(L) if theta == 0.5 else kopt*math.log(L)/L
            expected = math.sqrt(1/(2*math.log(2))) if theta == 0.5 else 0.4
            if L >= 1600:
                assert abs(scaled-expected) < 0.4
            print('finite optimizer', 'theta=',theta,'L=',L,'k=',kopt,
                  'scaled=',round(scaled, 5),'predicted limit=',round(expected,5))
            checks += 1
    print('PASS:', checks, 'finite analytical-identity and numerical checks')


if __name__ == '__main__':
    verify()
