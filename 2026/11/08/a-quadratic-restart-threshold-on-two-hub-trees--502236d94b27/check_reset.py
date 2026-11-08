"""Exact checks of the continuous-time reset hitting-time formulas.

Pure Python 3 standard library.  An absorbing finite-state generator is
solved by Fraction Gaussian elimination, independently of orbit reduction.
"""
from fractions import Fraction as Q


def graph(a, b):
    assert a >= 1 and b >= 1
    n = a + b + 3
    adj = [set() for _ in range(n)]
    def edge(u, v):
        adj[u].add(v)
        adj[v].add(u)
    edge(0, 2)  # initial leaf -> first hub
    edge(1, 2)  # target leaf -> first hub
    edge(2, 3)  # bridge between hubs
    for v in range(4, 4 + a - 1):
        edge(2, v)
    for v in range(4 + a - 1, n):
        edge(3, v)
    assert len(adj[2]) == a + 2 and len(adj[3]) == b + 1
    assert sum(map(len, adj)) == 2*(n-1)
    return adj


def gaussian(A, rhs):
    n = len(rhs)
    A = [list(row) + [v] for row, v in zip(A, rhs)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if A[i][col]), None)
        assert pivot is not None
        A[col], A[pivot] = A[pivot], A[col]
        factor = A[col][col]
        A[col] = [z / factor for z in A[col]]
        for i in range(n):
            if i != col and A[i][col]:
                factor = A[i][col]
                A[i] = [x - factor*y for x, y in zip(A[i], A[col])]
    return [A[i][-1] for i in range(n)]


def labeled_mean(a, b, reset):
    reset = Q(reset)
    adj = graph(a, b)
    alive = [i for i in range(len(adj)) if i != 1]
    index = {v: i for i, v in enumerate(alive)}
    A = [[Q(0) for _ in alive] for _ in alive]
    rhs = [Q(1)]*len(alive)
    for v in alive:
        i = index[v]
        A[i][i] += 1
        for w in adj[v]:
            if w != 1:
                A[i][index[w]] -= Q(1, len(adj[v]))
        if v != 0 and reset:
            A[i][i] += reset
            A[i][index[0]] -= reset
    return gaussian(A, rhs)[index[0]]


def formula(a, b, reset):
    r = Q(reset)
    return (r+2)*(a+2+Q(b, 1)/(1+(b+1)*r*(r+2)))


def derivative(a, b, reset):
    r = Q(reset)
    den = 1+(b+1)*r*(r+2)
    return a+2+Q(b, 1)*(1-(b+1)*(r+2)**2)/den**2


def second_derivative(a, b, reset):
    r = Q(reset)
    u = r+2
    den = 1+(b+1)*r*u
    return Q(2*b*(b+1), 1)*((b+1)*u**3-3*u+2)/den**3


def run():
    checks = 0
    for a in range(1, 6):
        for b in range(1, 6):
            for r in [Q(0), Q(1, 5), Q(2, 3), Q(7, 4)]:
                got = labeled_mean(a, b, r)
                expected = formula(a, b, r)
                assert got == expected, (a, b, r, got, expected)
                checks += 1
                assert second_derivative(a, b, r) > 0
                assert derivative(a, b, 0) == a - 4*b*b - 3*b + 2
    # Boundary at b=1, a=5; both adjacent strict regimes are nonempty.
    assert derivative(4, 1, 0) < 0
    assert derivative(5, 1, 0) == 0
    assert derivative(6, 1, 0) > 0
    # Rational-exact cancellation behind all-parameter proof:
    # E - (a+2)(r+2) = b(r+2)/[1+(b+1)r(r+2)].
    print('PASS: %d fully labeled rational generator solves; convexity and boundary checks passed' % checks)


if __name__ == '__main__':
    run()
