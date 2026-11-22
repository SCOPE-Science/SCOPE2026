"""Supplementary finite diagnostics for two-by-two similarity formulas.

Requires Python 3 standard library only. These tests do not prove the general theorem.
"""
import math
import random

TOL = 2e-8
COUNT = 0


def matrix_mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def matrix_inv(a):
    d = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return [[a[1][1] / d, -a[0][1] / d], [-a[1][0] / d, a[0][0] / d]]


def diag(a, b):
    return [[a, 0.0], [0.0, b]]


def matrix_norm(a):
    s = sum(abs(v)**2 for row in a for v in row)
    det = abs(a[0][0] * a[1][1] - a[0][1] * a[1][0])
    return math.sqrt((s + math.sqrt(max(0.0, s*s - 4*det*det))) / 2)


def cond(a):
    return matrix_norm(a) * matrix_norm(matrix_inv(a))


def diff(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(2) for j in range(2))


def close(a, b):
    global COUNT
    assert abs(a - b) <= TOL * max(1.0, abs(a), abs(b)), (a, b)
    COUNT += 1


rng = random.Random(20261110)
for _ in range(1200):
    alpha = rng.uniform(0.09, math.pi/2)
    beta = rng.uniform(0.09, math.pi/2)
    ca, sa = math.cos(alpha/2), math.sin(alpha/2)
    cb, sb = math.cos(beta/2), math.sin(beta/2)
    ua, vb = [[ca, ca], [sa, -sa]], [[cb, cb], [sb, -sb]]
    a = matrix_mul(matrix_mul(ua, diag(1.0, -2.0)), matrix_inv(ua))
    b = matrix_mul(matrix_mul(vb, diag(1.0, -2.0)), matrix_inv(vb))
    y = diag(cb/ca, sb/sa)
    close(diff(matrix_mul(y, a), matrix_mul(b, y)), 0.0)
    pa = matrix_mul(matrix_mul(ua, diag(1.0, 0.0)), matrix_inv(ua))
    pb = matrix_mul(matrix_mul(vb, diag(1.0, 0.0)), matrix_inv(vb))
    ia = [[2*pa[0][0]-1, 2*pa[0][1]], [2*pa[1][0], 2*pa[1][1]-1]]
    ib = [[2*pb[0][0]-1, 2*pb[0][1]], [2*pb[1][0], 2*pb[1][1]-1]]
    ga, gb = matrix_norm(ia), matrix_norm(ib)
    close(ga, 1/math.tan(alpha/2))
    close(gb, 1/math.tan(beta/2))
    close(cond(y), max(ga/gb, gb/ga))

for _ in range(200):
    t = math.exp(rng.uniform(-3.0, 3.0))
    a = [[0.0, 1.0], [0.0, 0.0]]
    b = [[0.0, t], [0.0, 0.0]]
    y = diag(t, 1.0)
    close(diff(matrix_mul(y, a), matrix_mul(b, y)), 0.0)
    close(cond(y), max(t, 1/t))

print('TWO_BY_TWO_SIMILARITY_DIAGNOSTICS_OK', COUNT)
