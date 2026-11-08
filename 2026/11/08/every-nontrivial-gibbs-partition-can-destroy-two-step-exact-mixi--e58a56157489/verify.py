"""Exact rational checks for Gibbs compression and finite-time mixing."""
from fractions import Fraction as F
from itertools import product

CHECKS = 0


def check(condition, detail):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(detail)


def mul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def plus(A, B):
    return [[x + y for x, y in zip(row_a, row_b)]
            for row_a, row_b in zip(A, B)]


def diff(A, B):
    return [[x - y for x, y in zip(row_a, row_b)]
            for row_a, row_b in zip(A, B)]


def scale(c, A):
    return [[c * x for x in row] for row in A]


def ip(pi, x, y):
    return sum((pi[i] * x[i] * y[i] for i in range(len(pi))), F(0))


def hs_squared(pi, A):
    return sum((pi[i] * A[i][j] ** 2 / pi[j]
                for i in range(len(pi)) for j in range(len(pi))), F(0))


def partitions(n):
    # Restricted-growth strings enumerate every set partition once.
    def rgs(seq, current_max):
        if len(seq) == n:
            groups = [[] for _ in range(current_max + 1)]
            for index, label in enumerate(seq):
                groups[label].append(index)
            yield groups
            return
        for label in range(current_max + 2):
            yield from rgs(seq + [label], max(label, current_max))
    yield from rgs([0], 0)


def family_test(pi, blocks):
    n = len(pi)
    k = len(blocks)
    if not (1 < k < n):
        return
    Pi = [[pi[j] for j in range(n)] for _ in range(n)]
    G = [[F(0) for _ in range(n)] for _ in range(n)]
    for block in blocks:
        mass = sum((pi[i] for i in block), F(0))
        for i in block:
            for j in block:
                G[i][j] = pi[j] / mass
    first, second = blocks[0], blocks[1]
    mass0 = sum((pi[i] for i in first), F(0))
    mass1 = sum((pi[i] for i in second), F(0))
    a = [F(1) / mass0 if i in first else
         -F(1) / mass1 if i in second else F(0) for i in range(n)]
    large_block = next(block for block in blocks if len(block) > 1)
    b = [F(0) for _ in range(n)]
    b[large_block[0]] = F(1) / pi[large_block[0]]
    b[large_block[1]] = -F(1) / pi[large_block[1]]
    A, B = ip(pi, a, a), ip(pi, b, b)
    u = [a[i] + b[i] for i in range(n)]
    v = [B * a[i] - A * b[i] for i in range(n)]
    maxprod = max(abs(u[i] * v[j]) for i in range(n) for j in range(n))
    eps = F(1, 4) / (1 + maxprod)
    theta = eps * A * B
    P = [[pi[j] * (1 + eps * u[i] * v[j])
          for j in range(n)] for i in range(n)]
    Q = mul(mul(G, P), G)
    R = diff(P, Pi)
    D = diff(Q, Pi)
    H = [[a[i] * pi[j] * a[j] / A for j in range(n)] for i in range(n)]
    check(A > 0 and B > 0 and 0 < theta < 1, 'valid parameters')
    check(all(P[i][j] > 0 for i in range(n) for j in range(n)), 'strictly positive')
    check(all(sum(P[i], F(0)) == 1 for i in range(n)), 'row stochastic')
    check(all(sum((pi[i] * P[i][j] for i in range(n)), F(0)) == pi[j]
              for j in range(n)), 'stationary')
    check(ip(pi, u, v) == 0 and ip(pi, a, b) == 0, 'orthogonal')
    check(mul(P, P) == Pi and R != [[F(0)] * n] * n, 'two-step exact')
    check(D == scale(theta, H), 'nontrivial projected eigenmode')
    check(hs_squared(pi, H) == 1, 'Hilbert-Schmidt normalization')
    check(hs_squared(pi, D) < hs_squared(pi, R), 'one-step contraction')
    for t in range(1, 7):
        M = [[F(int(i == j)) for j in range(n)] for i in range(n)]
        N = [[F(int(i == j)) for j in range(n)] for i in range(n)]
        for _ in range(t):
            M = mul(M, P)
            N = mul(N, Q)
        check(diff(N, Pi) == scale(theta ** t, H), 'exact projected powers')
        check(hs_squared(pi, diff(N, Pi)) == theta ** (2 * t), 'HS power law')
        if t >= 2:
            check(M == Pi and N != Pi, 'loss of finite-step exactness')


def exact_three_state_witness():
    P = [[F(1,4), F(1,2), F(1,4)],
         [F(1,3), F(1,3), F(1,3)],
         [F(5,12), F(1,6), F(5,12)]]
    G = [[F(1,2), F(1,2), F(0)],
         [F(1,2), F(1,2), F(0)],
         [F(0), F(0), F(1)]]
    Pi = [[F(1,3)] * 3 for _ in range(3)]
    Q = [[F(17,48), F(17,48), F(7,24)],
         [F(17,48), F(17,48), F(7,24)],
         [F(7,24), F(7,24), F(5,12)]]
    check(mul(P, P) == Pi, 'explicit P squared')
    check(mul(mul(G, P), G) == Q, 'explicit sandwich')
    check(mul(diff(Q, Pi), diff(Q, Pi)) == scale(F(1,8), diff(Q, Pi)),
          'explicit surviving mode')
    for t in range(1, 13):
        power = [[F(int(i==j)) for j in range(3)] for i in range(3)]
        for _ in range(t):
            power = mul(power, Q)
        check(diff(power, Pi) == scale(F(1,8) ** (t - 1), diff(Q, Pi)),
              'explicit all-power formula')


if __name__ == '__main__':
    exact_three_state_witness()
    for n in range(3, 7):
        for raw in ([1] * n, list(range(1, n + 1))):
            total = sum(raw)
            pi = [F(x, total) for x in raw]
            for blocks in partitions(n):
                family_test(pi, blocks)
    print(f'PASS: {CHECKS} exact rational assertions; no simulation')
