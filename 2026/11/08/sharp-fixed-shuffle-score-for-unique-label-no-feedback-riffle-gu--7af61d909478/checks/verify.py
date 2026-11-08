#!/usr/bin/env python3
"""Independent finite checks for unique-label no-feedback riffle guesses.

Only Python's standard library is required. This checks exact finite marginals,
assignment bounds, and constructive scores; asymptotic assertions follow
from the mathematical argument and are not verified by finite tests.
"""
import itertools
import math
from fractions import Fraction


def binom_pmf(n, p):
    return [Fraction(math.comb(n, x)) * p**x * (1-p)**(n-x)
            for x in range(n+1)]


def marginal_matrix(n, m):
    assert m >= 2 and m & (m-1) == 0
    mat = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(1, n+1):
        for t in range(m):
            a = binom_pmf(n-i, Fraction(t, m))
            b = binom_pmf(i-1, Fraction(t+1, m))
            for x, px in enumerate(a):
                if not px:
                    continue
                for y, py in enumerate(b):
                    if py:
                        mat[i-1][x+y] += px*py/m
    return mat


def round_robin_guess(n, m):
    L, r0 = divmod(n, m)
    out = [None]*n
    for t in range(m):
        for r in range(1, L+1):
            out[m*(r-1)+t] = t*L+r-1
    for r in range(r0):
        out[m*L+r] = m*L+r
    return out


def exact_optimum(mat):
    n = len(mat)
    dp = {0: Fraction(0)}
    for i in range(n):
        nxt = {}
        for mask, score in dp.items():
            for j in range(n):
                if (mask >> j) & 1 == 0:
                    nextmask = mask | (1 << j)
                    value = score + mat[i][j]
                    if nextmask not in nxt or nxt[nextmask] < value:
                        nxt[nextmask] = value
        dp = nxt
    return dp[(1<<n)-1]


def constant(m):
    a = lambda t: math.sqrt((t/m)*(1-t/m))
    return 2/(m*m*math.sqrt(2*math.pi))*sum(1/(a(t)+a(t+1)) for t in range(m))


def check():
    checks = 0
    for m in (2,4,8):
        for n in (max(3,m), max(3,m)+1, 2*m):
            mat = marginal_matrix(n,m)
            checks += 1
            assert all(sum(row) == 1 for row in mat)
            checks += 1
            assert all(sum(mat[i][j] for i in range(n)) == 1 for j in range(n))
            guess = round_robin_guess(n,m)
            checks += 1
            assert sorted(guess) == list(range(n))
            construct = sum(mat[i][guess[i]] for i in range(n))
            colbound = sum(max(mat[i][j] for i in range(n)) for j in range(n))
            opt = exact_optimum(mat)
            checks += 3
            assert 0 <= construct <= opt <= colbound
            assert opt <= n
            assert all(x >= 0 for row in mat for x in row)
        checks += 1
        assert constant(m)>0
    checks += 1
    assert abs(constant(2)-math.sqrt(2/math.pi))<1e-12
    # The finite gap is expected to persist, and the formula predicts its scale.
    for m in (2,4,8):
        n = 4*m
        mat = marginal_matrix(n,m)
        score = sum(mat[i][round_robin_guess(n,m)[i]] for i in range(n))
        checks += 1
        assert score>0 and 0<constant(m)<1
    return checks


if __name__ == '__main__':
    print('Exact checks passed:', check())
    print('Leading constants:', ', '.join(f'm={m}: {constant(m):.12f}' for m in (2,4,8)))
