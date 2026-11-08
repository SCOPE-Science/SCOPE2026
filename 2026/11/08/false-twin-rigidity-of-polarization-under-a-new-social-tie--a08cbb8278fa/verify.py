"""Exact finite checks for the edge-augmentation polarization theorem.

Requires SymPy (see requirements.txt). The arbitrary-order proof is in RESULT.md;
finite graph enumeration is a supplementary check, not its substitute.
"""
from itertools import combinations
from sympy import Matrix, eye, ones, Rational, zeros


def laplacian(n, edges):
    mat = zeros(n)
    for u, v in edges:
        mat[u, u] += 1
        mat[v, v] += 1
        mat[u, v] -= 1
        mat[v, u] -= 1
    return mat


def connected(n, edges):
    seen = {0}
    while True:
        nxt = seen | {v for u, v in edges if u in seen} | {u for u, v in edges if v in seen}
        if nxt == seen:
            return len(seen) == n
        seen = nxt


def polarity(n, edges, edge):
    u, v = edge
    L = laplacian(n, edges)
    A = (eye(n) + L).inv()
    Q = eye(n) - ones(n) / n
    b = zeros(n, 1)
    b[u] = 1
    b[v] = -1
    t = A * b
    w = A * t
    alpha = 1 / (1 + (b.T * A * b)[0])
    Ap = (eye(n) + L + b * b.T).inv()
    delta = Ap * Q * Ap - A * Q * A
    exact_delta = -alpha * (t * w.T + w * t.T) + alpha**2 * (t.T * t)[0] * (t * t.T)
    assert delta == exact_delta
    neighborhoods = [set(j for i, j in edges if i == k) |
                     set(i for i, j in edges if j == k) for k in range(n)]
    twins = neighborhoods[u] == neighborhoods[v]
    if twins:
        deg = len(neighborhoods[u])
        assert L * b == deg * b
        assert delta == -Rational(2 * (deg + 2), (deg + 3) ** 2) * t * t.T
    else:
        assert L * b != (L * b)[u] * b
        sigma = t - ((t.T * w)[0] / (w.T * w)[0]) * w
        assert (w.T * sigma)[0] == 0
        assert (sigma.T * delta * sigma)[0] > 0
        assert (b.T * delta * b)[0] < 0
    return twins


def polarization(n, edges, s):
    A = (eye(n) + laplacian(n, edges)).inv()
    Q = eye(n) - ones(n) / n
    s = Matrix(s)
    return (s.T * A * Q * A * s)[0]


def main():
    tested = 0
    connected_tested = 0
    connected_with_risk = []
    for n in range(1, 6):
        pairs = list(combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            edges = [e for k, e in enumerate(pairs) if mask & (1 << k)]
            if not connected(n, edges):
                continue
            connected_tested += 1
            for edge in pairs:
                if edge in edges:
                    continue
                tested += 1
                twins = polarity(n, edges, edge)
                if not twins:
                    connected_with_risk.append((n, edges, edge))
                    assert n >= 4
    assert connected_with_risk and connected_with_risk[0][0] == 4
    edges = [(0, 1), (0, 3), (1, 2)]
    opinion = [0, 0, Rational(1, 2), 1]
    before = polarization(4, edges, opinion)
    after = polarization(4, edges + [(0, 2)], opinion)
    assert (before, after, after - before) == (
        Rational(83, 784), Rational(349, 3200), Rational(501, 156800))
    print('PASS: exact symbolic augmentation and sign constructions; '
          f'{connected_tested} connected labeled graphs and {tested} nonedge cases (n<=5).')
    print(f'PASS: connected threshold n=4; rational witness '+
          f'{before} -> {after}, increase {after-before}.')


if __name__ == '__main__':
    main()
