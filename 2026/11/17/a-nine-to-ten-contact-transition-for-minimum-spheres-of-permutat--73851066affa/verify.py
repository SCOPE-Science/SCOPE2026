"""Exact finite-domain certificate for minimum balls of anti-diagonal permutation X-rays.

Requires only Python 3.10+.  All inequalities are tested as integers after
constructing the proposed center with rational arithmetic.  The loop covers
all k! permutations for each k = 2,...,10; there is no sampling.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial


def exact_ball(k):
    h = [(k - j)**2 + j*j for j in range(k)]
    active = list(range(k)) if k <= 9 else [j for j in range(k) if j != 5]
    S = sum((Q(1, h[j]) for j in active), Q(0))
    t = Q(len(active)-2, 1) / S
    weights = {j: (1 - t / h[j]) / 2 for j in active}
    assert all(w > 0 for w in weights.values())
    assert sum(weights.values()) == 1
    assert (k <= 9 and len(active) == k) or (k == 10 and len(active) == 9)
    if k == 10:
        assert h[5] < t
    C = [Q(0) for _ in range(2*k-1)]
    expected = set()
    for j, a in weights.items():
        x = [0] * (2*k-1)
        if j == 0:
            x[k-1] = k
        else:
            x[k-1-j] = k-j
            x[2*k-1-j] = j
        expected.add(tuple(x))
        for s, v in enumerate(x):
            C[s] += a*v
        assert sum(v*v for v in x) == h[j]
    R2 = t + sum(c*c for c in C)
    H = sum(h)
    assert R2 == Q(sum(h[j] for j in active), 4) - Q((len(active)-2)**2, 4) / S
    if k == 10:
        assert R2 == Q(235064670, 3593269)
    L = t.denominator
    U = [int(2*c*L) for c in C]
    assert all(2*c*L == u for c, u in zip(C, U))
    T = int(t*L)
    equality = set()
    seen = 0
    strict = 0
    for p in permutations(range(k)):
        x = [0]*(2*k-1)
        for i, v in enumerate(p):
            x[i+v] += 1
        # L*(||x||^2 - 2 <C,x> - t) <= 0 exactly.
        deficit = T
        for s, v in enumerate(x):
            deficit -= v*(L*v - U[s])
        assert deficit >= 0, (k, p, deficit)
        if deficit == 0:
            equality.add(tuple(x))
        else:
            strict += 1
        seen += 1
    assert seen == factorial(k)
    assert equality == expected, (k, len(equality), len(expected))
    print(f'k={k}: permutations={seen}, exact sphere R^2={R2}, '
          f'contact X-rays={len(equality)}, strict permutations={strict}')
    return R2, C


if __name__ == '__main__':
    for k in range(2, 11):
        exact_ball(k)
    print('PASS: all factorial permutation cases exhaustively certified.')
