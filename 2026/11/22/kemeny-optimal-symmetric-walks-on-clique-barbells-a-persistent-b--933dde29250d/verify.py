"""Reproduce finite exact identities and asymptotic diagnostics for clique-barbell walks.

Requires Python 3.10+ and SymPy 1.10+. Numerical tests supplement, not replace,
the all-size proof in RESULT.md.
"""
from fractions import Fraction as Q
from math import sqrt
import sympy as S


def k_formula(s, u, t, v=None):
    f = Q(s + 1, s) / u + Q(s, 2) / t
    if s >= 3:
        f += Q(2 * (s - 2), 1) / (u + (s - 1) * v)
    return f


def laplacian(s, u, t, v):
    n = 2 * s
    L = S.zeros(n)
    def edge(i, j, weight):
        L[i, i] += weight
        L[j, j] += weight
        L[i, j] -= weight
        L[j, i] -= weight
    for half in range(2):
        offset = half * s
        for j in range(1, s):
            edge(offset, offset + j, u)
        for j in range(1, s):
            for k in range(j + 1, s):
                edge(offset + j, offset + k, v)
    edge(0, s, t)
    return L


def k_matrix(s, u, t, v):
    L = laplacian(s, u, t, v)
    n = 2 * s
    A = L + S.ones(n, n) / n
    inverse = A.inv()
    return sum(inverse[j, j] for j in range(n)) - 1


def f(s, u):
    t = 1 - (s - 1) * u
    return 2 * (s - 2)**2 / (s - 1 - u) + (s + 1) / (s * u) + s / (2 * t)


def deriv(s, u):
    return (2 * (s - 2)**2 / (s - 1 - u)**2
            - (s + 1) / (s * u*u)
            + s * (s - 1) / (2 * (1 - (s - 1) * u)**2))


def optimal_u(s):
    a, b = 0.0, 1.0 / (s - 1)
    for _ in range(110):
        m = (a + b) / 2
        if deriv(s, m) < 0:
            a = m
        else:
            b = m
    return (a + b) / 2


def run():
    total = 0
    for s in range(3, 9):
        for p in (Q(1, 4), Q(1, 3), Q(2, 5)):
            u, t, v = p / s, Q(1, 4), Q(2, 5*s)
            assert (s-1)*u+t <= 1
            assert u + (s-2)*v <= 1
            assert k_formula(s,u,t,v) == k_matrix(s,u,t,v)
            total += 1
        # Maximum-degree walk, including its diagonal holding probabilities.
        u = t = v = Q(1, s)
        assert k_matrix(s,u,t,v) == Q(s*s,2) + 3*s - 3
        total += 1
        u_star = optimal_u(s)
        assert abs(deriv(s,u_star)) <= 1e-8
        assert 0 < u_star < 1/(s-1)
        assert f(s,u_star) < f(s,u_star*.9999)
        assert f(s,u_star) < f(s,u_star*1.0001)
        total += 4
    for s in (30, 100, 1000, 10000, 100000):
        u = optimal_u(s)
        assert abs(s*u-(2-sqrt(2))) < 4/sqrt(s)
        assert abs((1-(s-1)*u)-(sqrt(2)-1)) < 4/sqrt(s)
        assert abs(f(s,u)/s-(3.5+sqrt(2))) < 20/sqrt(s)
        total += 3
    print('PASS:',total,'exact-rational and numerical assertions')
    for s in (3,4,8,64,4096):
        u = optimal_u(s)
        print('s=',s,'gateway-bridge=',round(1-(s-1)*u,9),
              'optimal K=',round(f(s,u),9))

if __name__ == '__main__':
    run()
