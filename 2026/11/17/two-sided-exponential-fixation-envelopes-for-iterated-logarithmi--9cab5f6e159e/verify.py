#!/usr/bin/env python3
"""Numerical diagnostics for finite logarithmic Bernstein binomial chains.

No external packages. The analytic proof is in RESULT.md.
"""
import math

checks = 0

def check(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)

def a(n, beta, x):
    return math.log1p(beta * x / n) / math.log1p(beta / n)

def phi(gamma, x):
    return -math.expm1(-gamma * x) / -math.expm1(-gamma)

def row(n, beta, x):
    p = a(n, beta, x)
    if p <= 0.0:
        return [1.0] + [0.0] * n
    if p >= 1.0:
        return [0.0] * n + [1.0]
    return [math.comb(n, k) * p**k * (1.0-p)**(n-k) for k in range(n+1)]

def solve(A, y):
    A = [row[:] for row in A]
    y = y[:]
    n = len(y)
    for k in range(n):
        pivot = max(range(k, n), key=lambda i: abs(A[i][k]))
        check(abs(A[pivot][k]) > 1e-13, f'singular chain system {k}')
        A[k], A[pivot] = A[pivot], A[k]
        y[k], y[pivot] = y[pivot], y[k]
        v = A[k][k]
        for i in range(k + 1, n):
            f = A[i][k] / v
            for j in range(k + 1, n):
                A[i][j] -= f * A[k][j]
            y[i] -= f * y[k]
            A[i][k] = 0.0
    x = [0.0] * n
    for k in reversed(range(n)):
        x[k] = (y[k] - sum(A[k][j] * x[j] for j in range(k+1, n))) / A[k][k]
    return x

def h_nodes(n, beta):
    if n == 1:
        return [0.0, 1.0]
    Q = [row(n, beta, j/n) for j in range(1, n)]
    A = [[(1.0 if i == j else 0.0) - Q[i][j+1] for j in range(n-1)] for i in range(n-1)]
    v = solve(A, [q[-1] for q in Q])
    return [0.0] + v + [1.0]

def run():
    for beta in (0.1, 0.4, 0.8):
        for n in (1, 2, 3, 5, 8, 12, 20):
            u = h_nodes(n, beta)
            lower = beta / (1 + beta/n)
            for k in range(0, n+1):
                x = k/n
                check(abs(u[k] - sum(row(n, beta, x)[j]*u[j] for j in range(n+1))) < 1e-9, 'harmonic finite node')
            for x in (0.0, 0.03, 0.13, 0.27, 0.51, 0.76, 0.94, 1.0):
                q = row(n, beta, x)
                check(abs(sum(q)-1.0) < 1e-12, 'probability row normalization')
                h = sum(q[j]*u[j] for j in range(n+1))
                lo, hi = phi(lower,x), phi(beta,x)
                if x == 0.0 or x == 1.0:
                    check(abs(h-x) < 1e-12, 'endpoint absorption')
                else:
                    check(lo < h < hi, 'strict exponential envelope')
                    check(hi-h <= beta*beta/(n+beta)+1e-12, 'uniform bound')
                for gamma in (lower, beta):
                    mgf = sum(q[k]*math.exp(-gamma*k/n) for k in range(n+1))
                    exact = (1-a(n,beta,x)*(1-math.exp(-gamma/n)))**n
                    check(abs(mgf-exact) < 1e-12, 'exact binomial moment')
            for x in (0.0, 0.1, 0.4, 0.7, 1.0):
                c = beta/n
                check(c-c/(1+c*x) >= -1e-14, 'upper normalized derivative sign')
                check(c/(1+c)-c/(1+c*x) <= 1e-14, 'lower normalized derivative sign')
    print(f'PASS: {checks} finite diagnostic assertions')

if __name__ == '__main__':
    run()
