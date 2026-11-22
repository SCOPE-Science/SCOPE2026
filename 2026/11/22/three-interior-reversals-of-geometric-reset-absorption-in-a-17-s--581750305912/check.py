"""Exact rational sign certificate for a three-extremum reset example.

Run with Python 3: python check.py. All arithmetic uses standard-library integers
and Fraction; no random sampling or floating point enters the assertions.
"""
from fractions import Fraction as F

P_MILLION = (995517, 148739, 992235, 3511, 967337, 5952, 998114,
             839557, 998092, 971199, 963413, 13393, 997802, 40422, 23406)
p = {i + 1: F(a, 1000000) for i, a in enumerate(P_MILLION)}
assert len(p) == 15 and all(0 < x < 1 for x in p.values())

def det_poly(lo, hi):
    """det(I-s P_restricted), represented in t=s^2, on [lo, hi]."""
    previous, current = [F(1)], [F(1)]
    for j in range(lo + 1, hi + 1):
        factor = p[j - 1] * (1 - p[j])
        following = [F(0)] * max(len(current), len(previous) + 1)
        for i, coefficient in enumerate(current):
            following[i] += coefficient
        for i, coefficient in enumerate(previous):
            following[i + 1] -= factor * coefficient
        previous, current = current, following
    return current

def eval_poly(coefficients, t):
    return sum((a * t**i for i, a in enumerate(coefficients)), F(0))

def eval_derivative(coefficients, t):
    return sum((i * a * t**(i - 1) for i, a in enumerate(coefficients) if i), F(0))

L = det_poly(1, 6)
R = det_poly(8, 15)
assert len(L) == 4 and len(R) == 5

def W(t):
    ell, right = eval_poly(L, t), eval_poly(R, t)
    return (ell + t * eval_derivative(L, t)) * right - t * ell * eval_derivative(R, t)

samples = [(F(3, 5), 1), (F(3, 4), -1), (F(19, 20), 1), (F(1), -1)]
for t, sign in samples:
    w = W(t)
    assert sign * w > 0, (t, w)
    assert eval_poly(L, t) > 0 and eval_poly(R, t) > 0
    print(f't={t}: W(t) sign={"+" if w > 0 else "-"}, exact numerator={w.numerator}')

# Independent resolvent check using exact Gaussian elimination at rational s.
def linear_solve(s, left):
    n = 15
    mat = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    rhs = [F(0) for _ in range(n)]
    for i in range(1, 16):
        if i > 1:
            mat[i - 1][i - 2] -= s * (1 - p[i])
        elif left:
            rhs[i - 1] = s * (1 - p[i])
        if i < 15:
            mat[i - 1][i] -= s * p[i]
        elif not left:
            rhs[i - 1] = s * p[i]
    for k in range(n):
        pivot = next(row for row in range(k, n) if mat[row][k] != 0)
        mat[k], mat[pivot] = mat[pivot], mat[k]
        rhs[k], rhs[pivot] = rhs[pivot], rhs[k]
        pivot_val = mat[k][k]
        for j in range(k, n):
            mat[k][j] /= pivot_val
        rhs[k] /= pivot_val
        for i in range(k + 1, n):
            coefficient = mat[i][k]
            for j in range(k, n):
                mat[i][j] -= coefficient * mat[k][j]
            rhs[i] -= coefficient * rhs[k]
    sol = [F(0)] * n
    for i in reversed(range(n)):
        sol[i] = rhs[i] - sum(mat[i][j] * sol[j] for j in range(i + 1, n))
    return sol[6]

C = (F(1) if False else F(1))
for i in range(7, 16):
    C *= p[i]
for i in range(1, 8):
    C /= 1 - p[i]
for s in (F(1, 2), F(3, 4)):
    a, b = linear_solve(s, True), linear_solve(s, False)
    t = s * s
    formula = eval_poly(R, t) / (eval_poly(R, t) + C * t * eval_poly(L, t))
    assert formula == a / (a + b)
    assert a > 0 and b > 0
print('All four rational signs and two independent exact-resolvent comparisons passed.')
