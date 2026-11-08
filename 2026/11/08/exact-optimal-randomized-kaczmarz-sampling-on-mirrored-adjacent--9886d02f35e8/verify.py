#!/usr/bin/env python3
"""Exact-rational checks for the signed adjacent-pair Kaczmarz design."""
from fractions import Fraction as F


def construct(n, a):
    """Return exact primal and dual certificates for 0 < a <= 1/2."""
    assert n >= 3 and F(0) < a <= F(1, 2)
    b = 1 - a
    r = a / b
    q = [1 / a] + [1 - (-r) ** (n - i) for i in range(2, n)]
    y = [1 / a, F(0)] + [1 - (-r) ** (i - 2) for i in range(3, n + 1)]
    Q = 1 / a + (n - 2) + a * (1 - (-r) ** (n - 2))
    return q, y, Q


def check(n, a):
    b = 1 - a
    if a > b:
        return check(n, b)
    q, y, Q = construct(n, a)
    assert all(x >= 0 for x in q + y)
    assert Q == sum(q) == sum(y)
    for i in range(n - 1):
        assert a * y[i] + b * y[i + 1] == 1
    diag = [a * q[0]] + [b * q[i - 1] + a * q[i] for i in range(1, n - 1)] + [b * q[-1]]
    assert min(diag) == 1
    assert all(x >= 1 for x in diag)
    if a < b:
        assert diag[1] > 1
        assert all(x == 1 for j, x in enumerate(diag) if j != 1)
        assert all(x > 0 for x in q)
        assert all(x > 0 for j, x in enumerate(y) if j != 1)
    else:
        assert Q == 2 * ((n + 1) // 2)
    lam = 1 / Q
    p = [x * lam for x in q]
    assert sum(p) == 1
    assert min([x * lam for x in diag]) == lam
    unif = a / (n - 1)
    assert lam >= unif
    return Q


def check_full_matrix(n, t, s):
    """Construct exact normalized signed projector rows and their weighted sum."""
    assert n >= 3 and t >= 1 and s >= 1
    a = F(t * t, t * t + s * s)
    b = 1 - a
    if a > b:
        return check_full_matrix(n, s, t)
    q, y, Q = construct(n, a)
    weights = [v / (2 * Q) for v in q]
    norm = t * t + s * s
    diag = [F(0) for _ in range(n)]
    offdiag = [F(0) for _ in range(n-1)]
    for i in range(n-1):
        for sign in (+1, -1):
            pi = weights[i]
            diag[i] += pi * F(t*t, norm)
            diag[i+1] += pi * F(s*s, norm)
            offdiag[i] += pi * sign * F(t*s, norm)
    assert all(x == 0 for x in offdiag)
    assert min(diag) == 1/Q
    assert sum(diag) == 1
    assert all(x >= 1/Q for x in diag)
    return 1/Q


def check_balanced_cover(n):
    a = F(1,2)
    Q = 2*((n+1)//2)
    selected = list(range(0,n-1,2))
    if n % 2:
        selected += [n-2]
    assert len(selected) == (n+1)//2
    p = [F(1,len(selected)) if i in selected else F(0) for i in range(n-1)]
    d = [a*p[0]]+[a*(p[i-1]+p[i]) for i in range(1,n-1)]+[a*p[-1]]
    assert min(d) == F(1,Q)


def main():
    count = 0
    for n in range(3, 55):
        for d in (3,4,5,7,9,11,19,37):
            for numerator in range(1,d+1):
                a = F(numerator,d+numerator)
                check(n,a)
                count+=1
        check_balanced_cover(n)
        count+=1
    count2=0
    for n in range(3,18):
        for t in range(1,8):
            for s in range(t,9):
                check_full_matrix(n,t,s)
                count2+=1
    print('PASS:',count,'exact primal-dual and edge-cover certificates;',count2,'exact full-matrix projector identities')

if __name__ == '__main__':
    main()
