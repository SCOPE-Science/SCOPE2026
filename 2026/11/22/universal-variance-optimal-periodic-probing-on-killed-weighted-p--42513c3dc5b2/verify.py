"""Exact independent checks for periodic stochastic probing on killed weighted paths.

Python 3 standard library only. Run: python verify.py
"""
from fractions import Fraction as F
from itertools import product

checks = 0

def check(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def inverse(A):
    n = len(A)
    T = [[A[i][j] for j in range(n)] + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for i in range(n):
        p = next(j for j in range(i, n) if T[j][i] != 0)
        T[i], T[p] = T[p], T[i]
        t = T[i][i]
        T[i] = [x / t for x in T[i]]
        for j in range(n):
            if j != i:
                t = T[j][i]
                if t:
                    T[j] = [v - t * w for v, w in zip(T[j], T[i])]
    return [r[n:] for r in T]


def matrix(edge, kill):
    n = len(kill)
    A = [[F(0) for _ in range(n)] for _ in range(n)]
    for i, val in enumerate(kill):
        A[i][i] = val
    for i, val in enumerate(edge):
        A[i][i] += val
        A[i + 1][i + 1] += val
        A[i][i + 1] -= val
        A[i + 1][i] -= val
    return A


def fundamental(edge, kill):
    n = len(kill)
    left = [F(1)]
    for i in range(n - 1):
        term = kill[i] * left[i]
        if i:
            term += edge[i - 1] * (left[i] - left[i - 1])
        left.append(left[i] + term / edge[i])
    right = [F(0)] * (n - 1) + [F(1)]
    for i in range(n - 1, 0, -1):
        term = kill[i] * right[i]
        if i < n - 1:
            term += edge[i] * (right[i] - right[i + 1])
        right[i - 1] = right[i] + term / edge[i - 1]
    omega = edge[0] * (left[1] * right[0] - left[0] * right[1])
    return left, right, omega


def partitions(n):
    def rec(seq, n_classes):
        if len(seq) == n:
            yield tuple(seq)
        else:
            for color in range(n_classes + 1):
                seq.append(color)
                yield from rec(seq, max(n_classes, color + 1))
                seq.pop()
    yield from rec([0], 1)


def score(W, lab):
    return 2 * sum(W[i][j] for i in range(len(lab)) for j in range(len(lab))
                   if i != j and lab[i] == lab[j])


def run_case(n, edge, kill):
    A = matrix(edge, kill)
    G = inverse(A)
    left, right, omega = fundamental(edge, kill)
    check(omega > 0, 'Wronskian')
    check(all(left[i] < left[i + 1] for i in range(n - 1)), 'left increasing')
    check(all(right[i] > right[i + 1] for i in range(n - 1)), 'right decreasing')
    check(all(G[i][j] == left[min(i, j)] * right[max(i, j)] / omega
              for i in range(n) for j in range(n)), 'Green factorization')
    W = [[G[i][j]**2 for j in range(n)] for i in range(n)]
    u = [x*x / (omega * omega) for x in left]
    v = [x*x for x in right]
    du = [u[0]] + [u[i] - u[i - 1] for i in range(1, n)]
    dv = [v[i] - v[i + 1] for i in range(n - 1)] + [v[-1]]
    check(all(x > 0 for x in du + dv), 'interval weights strict')
    for i in range(n):
        for j in range(n):
            total = sum(du[a] * dv[b] for a in range(min(i,j)+1)
                        for b in range(max(i,j), n))
            check(total == W[i][j], 'interval decomposition')
    for lab in partitions(n):
        k = max(lab) + 1
        opt = tuple(i % k for i in range(n))
        gap = score(W, lab) - score(W, opt)
        check(gap >= 0, 'variance min')
        check((gap == 0) == (all(lab[i] == lab[i + k]
                                     for i in range(n - k)) and len(set(lab[:k])) == k),
              'unique color classes')
        gap2 = F(0)
        for a in range(n):
            for b in range(a, n):
                length = b - a + 1
                counts = [sum(lab[i] == col for i in range(a, b + 1)) for col in range(k)]
                t, r = divmod(length, k)
                baseline = r * (t + 1)**2 + (k - r) * t**2
                gap2 += 2 * du[a] * dv[b] * (sum(q*q for q in counts) - baseline)
        check(gap == gap2, 'exact variance excess')
        if k >= 2:
            gap_lb = 4 * sum(du[a] * dv[a + k - 1] for a in range(n - k + 1)
                           if len(set(lab[a:a+k])) < k)
            check(gap >= gap_lb, 'window defect lower bound')


for n in range(2, 8):
    cases = [
        ([F(1) for _ in range(n-1)], [F(1) for _ in range(n)]),
        ([F(i + 2, i + 1) for i in range(n-1)], [F(2*i+1, i+2) for i in range(n)]),
        ([F((i*3+2)%7+1, 3) for i in range(n-1)], [F((i*5+3)%9+1, 4) for i in range(n)]),
    ]
    for edge, kill in cases:
        run_case(n, edge, kill)
print(f'PASS: {checks:,} exact assertions; n=2,...,7, three independent weight patterns each')
