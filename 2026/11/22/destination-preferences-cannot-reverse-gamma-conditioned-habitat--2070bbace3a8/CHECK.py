#!/usr/bin/env python3
"""Independent numerical cross-checks for a gamma-weighted habitat-ring kernel.

Numerical checks supplement, but do not replace, the analytic proof.
Run: python3 gamma_ring_check.py
"""
import math
import random


def stationary(P):
    n = len(P)
    A = [[P[j][i] - (1.0 if i == j else 0.0) for j in range(n)]
         for i in range(n)]
    A[-1] = [1.0] * n
    b = [0.0] * (n - 1) + [1.0]
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(A[i][k]))
        if abs(A[p][k]) < 1e-14:
            raise ValueError('singular stationary system')
        A[k], A[p] = A[p], A[k]
        b[k], b[p] = b[p], b[k]
        pivot = A[k][k]
        A[k] = [v / pivot for v in A[k]]
        b[k] /= pivot
        for i in range(n):
            if i != k:
                v = A[i][k]
                if v:
                    A[i] = [x - v*y for x, y in zip(A[i], A[k])]
                    b[i] -= v*b[k]
    return b


def kernel_plus_and_log_affinity(plus, minus, t):
    # Each edge is (alpha, beta, weight).
    n = len(plus)
    p = []
    F = 0.0
    for a, b in zip(plus, minus):
        def logscore(s):
            alpha, beta, weight = s
            return (math.log(weight) + alpha * math.log(beta)
                    - math.lgamma(alpha) + (alpha - 1) * math.log(t) - beta * t)
        d = logscore(a) - logscore(b)
        F += d
        p.append(1/(1+math.exp(-d)))
    P = [[0.0]*n for _ in range(n)]
    for i in range(n):
        P[i][(i+1)%n] = p[i]
        P[i][(i-1)%n] = 1-p[i]
    return P, F


def zeros_bisect(fn, lo, hi):
    f_lo = fn(lo)
    if f_lo * fn(hi) > 0: raise ValueError('not bracketed')
    for _ in range(100):
        mid = (lo+hi)/2
        if (fn(mid)>0) == (f_lo>0):
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def main():
    rng = random.Random(72024118)
    tested = 0
    for n in range(3, 12):
        for _ in range(240):
            plus = [(rng.uniform(.6, 4.0), rng.uniform(.5, 3.0), rng.uniform(.3, 4.0)) for j in range(n)]
            minus = [(rng.uniform(.6, 4.0), rng.uniform(.5, 3.0), rng.uniform(.3, 4.0)) for j in range(n)]
            t = rng.uniform(.12, 4.5)
            P, F = kernel_plus_and_log_affinity(plus, minus, t)
            pi = stationary(P)
            current = [pi[i]*P[i][(i+1)%n] - pi[(i+1)%n]*P[(i+1)%n][i] for i in range(n)]
            assert max(current)-min(current) < 2e-10
            assert all(x > 0 for x in pi)
            assert abs(sum(pi)-1) < 2e-10
            if abs(F)>1e-6 and abs(current[0])>1e-10:
                assert (F > 0) == (current[0] > 0)
            tested += 1
    # In the destination-only selection specialization, arbitrary habitat
    # qualities change stationary masses but not the sign of circulation.
    for n in (3, 4, 6, 9):
        for _ in range(100):
            q = [rng.uniform(.1, 10.0) for i in range(n)]
            plus_core = [(rng.uniform(.7,3.5),rng.uniform(.4,2.8)) for i in range(n)]
            minus_core = [(rng.uniform(.7,3.5),rng.uniform(.4,2.8)) for i in range(n)]
            plus = [(a,b,q[(i+1)%n]) for i,(a,b) in enumerate(plus_core)]
            minus = [(a,b,q[(i-1)%n]) for i,(a,b) in enumerate(minus_core)]
            unweighted_plus = [(a,b,1) for a,b in plus_core]
            unweighted_minus = [(a,b,1) for a,b in minus_core]
            t = rng.uniform(.1,4.0)
            P, F = kernel_plus_and_log_affinity(plus, minus, t)
            _, F0 = kernel_plus_and_log_affinity(unweighted_plus, unweighted_minus, t)
            assert abs(F-F0) < 1e-10
            pi = stationary(P)
            J = pi[0]*P[0][1]-pi[1]*P[1][0]
            if abs(F)>1e-6 and abs(J)>1e-10:
                assert (J>0)==(F0>0)
            tested += 1
    root1 = zeros_bisect(lambda t: 4*t*math.exp(-t)-1, .1, .9)
    root2 = zeros_bisect(lambda t: 4*t*math.exp(-t)-1, 1.5, 3.0)
    assert abs(root1-.35740295618138895) < 2e-14
    assert abs(root2-2.1532923641103494) < 2e-14
    for n in [3, 4, 5, 9, 20]:
        plus = [(2.0, 2.0, 1.0)]*n
        minus = [(1.0, 1.0, 1.0)]*n
        for t in [0.02, .4, 1, 2, 3, 20]:
            P, F = kernel_plus_and_log_affinity(plus, minus, t)
            pi = stationary(P)
            j = pi[0]*P[0][1]-pi[1]*P[1][0]
            exact = (4*t*math.exp(-t)-1)/(n*(4*t*math.exp(-t)+1))
            assert abs(j-exact) < 2e-12
            tested += 1
    print('PASS: %d independently solved stationary kernels, exact witness, and two roots' % tested)
    print('root_low=%.15f root_high=%.15f' % (root1, root2))


if __name__ == '__main__': main()
