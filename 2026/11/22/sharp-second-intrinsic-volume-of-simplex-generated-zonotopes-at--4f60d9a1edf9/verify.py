"""Reproduce algebraic and numerical checks for a sharp zonotope V2 bound.

Uses only the Python standard library. The mathematical proof is in RESULT.md;
finite tests here do not establish the inequality in arbitrary dimensions.
"""
from fractions import Fraction as F
from math import comb, isclose, isqrt, sqrt
from random import Random


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def sqtrace(T):
    return sum(t*t for row in T for t in row)


def exact_fixture():
    # These unit vectors span R^3; every pairwise wedge length is rational.
    P = [
        (F(3, 5), F(4, 5), F(0)),
        (F(1), F(0), F(0)),
        (F(0), F(1), F(0)),
        (F(0), F(0), F(1)),
    ]
    n, d = len(P), len(P[0])
    L = F(n)
    A = F(n*(n-1), 2)
    T = [[sum(v[i]*v[j] for v in P) for j in range(d)] for i in range(d)]
    B = (L*L-sqtrace(T))/2
    s_values = [F(4, 5), F(3, 5), F(1), F(1), F(1), F(1)]
    S = sum(s_values)
    H = sum((s-S/A)**2 for s in s_values)
    Q = F(0)
    E = sqtrace(T)-L*L/d
    A_star = L*L*F(n-1, 2*n)
    B_star = L*L*F(d-1, 2*d)
    delta = A_star*B_star-S*S
    assert B == sum(s*s for s in s_values)
    assert delta == (A_star*E+B_star*Q)/2-Q*E/4+A*H
    assert delta > 0
    # The dimension-d regular simplex has exact Gram diagonal 1,
    # off-diagonal -1/d; every pairwise wedge has squared norm 1-1/d^2.
    for d in range(2, 13):
        n = d+1
        gram = [[F(1) if i == j else -F(1, d)
                 for j in range(n)] for i in range(n)]
        assert all(sum(row) == 0 for row in gram)
        assert all(gram[i][j] == gram[j][i] for i in range(n) for j in range(n))
        l2 = F(n*n)
        sstar2 = l2*l2*F(d-1, 4*(d+1))
        actual2 = comb(n, 2)**2 * (F(1)-F(1, d*d))
        assert sstar2 == actual2
    return 11


def numerical_fixture():
    rng = Random(731245)
    cases = 0
    for d in range(2, 11):
        n = d+1
        for k in range(100):
            P = [[rng.uniform(-2, 2) for _ in range(d)] for _ in range(n)]
            if k % 13 == 0:
                P[0] = [0.0]*d  # included degenerate cases
            a = [sqrt(dot(v, v)) for v in P]
            L = sum(a)
            U = [[v[j]/av if av else 0.0 for j in range(d)] for v, av in zip(P, a)]
            T = [[sum(a[t]*U[t][i]*U[t][j] for t in range(n))
                  for j in range(d)] for i in range(d)]
            A = sum(a[i]*a[j] for i in range(n) for j in range(i+1, n))
            S = 0.0
            B_direct = 0.0
            W = []
            for i in range(n):
                for j in range(i+1, n):
                    w = a[i]*a[j]
                    cos = dot(U[i], U[j])
                    sin = sqrt(max(0.0, 1.0-cos*cos))
                    S += w*sin
                    B_direct += w*sin*sin
                    W.append((w, sin))
            B = (L*L-sqtrace(T))/2
            Q = sum((v-L/n)**2 for v in a)
            E = sqtrace(T)-L*L/d
            A_star = L*L*(n-1)/(2*n)
            B_star = L*L*(d-1)/(2*d)
            Sstar2 = A_star*B_star
            H = sum(w*(sin-S/A)**2 for w, sin in W)
            identity = ((A_star*E+B_star*Q)/2-Q*E/4+A*H)
            delta = Sstar2-S*S
            scale = max(1.0, L**4)
            assert abs(A-(A_star-Q/2)) < 2e-12*scale
            assert abs(B-B_direct) < 2e-12*scale
            assert abs(B-(B_star-E/2)) < 2e-12*scale
            assert abs(delta-identity) < 2e-12*scale
            assert delta > -2e-12*scale
            assert delta+2e-12*scale >= max(A_star*E/2, B_star*Q/2)
            cases += 1
    return cases


if __name__ == '__main__':
    e = exact_fixture()
    f = numerical_fixture()
    print('PASS:', e, 'exact rational/simplex-dimensional checks,',
          f, 'reproducible numerical configurations')
