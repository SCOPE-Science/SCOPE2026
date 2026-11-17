"""Independent exact finite-field tests for a reversible wave on crown graphs.
Run: python3 verification/verify_matrix.py
Only standard Python is required; these are tests, not a replacement for proof.
"""
from random import Random

P = 3

def mm(A, B):
    rows, mid, cols = len(A), len(B), len(B[0])
    C = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(mid):
            a = A[i][j]
            if a:
                for k in range(cols):
                    C[i][k] = (C[i][k] + a * B[j][k]) % P
    return C

def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def mpow(A, k):
    R = ident(len(A))
    while k:
        if k & 1:
            R = mm(R, A)
        k //= 2
        if k:
            A = mm(A, A)
    return R

def rank(A):
    B = [row.copy() for row in A]
    rows, cols, r = len(B), len(B[0]), 0
    for j in range(cols):
        p = next((i for i in range(r, rows) if B[i][j]), None)
        if p is None:
            continue
        B[r], B[p] = B[p], B[r]
        if B[r][j] == 2:
            B[r] = [(2 * x) % P for x in B[r]]
        for i in range(r + 1, rows):
            a = B[i][j]
            if a:
                B[i] = [(x - a*y) % P for x,y in zip(B[i], B[r])]
        r += 1
    return r

def wave(n):
    vertices = 2 * n
    T = [[0] * (2 * vertices) for _ in range(2 * vertices)]
    for i in range(vertices):
        for j in range(vertices):
            if (i < n) != (j < n) and (i % n) != (j % n):
                T[i][j] = 1
        T[i][vertices + i] = 2
        T[vertices + i][i] = 1
    return T

def exponent(n, t):
    even, tri, four = t % 2 == 0, t % 3 == 0, t % 4 == 0
    if n % 3 == 0:
        h = 4 if t % 9 == 0 else (3 if tri else 1)
        return (1 + int(even)) * (h + (n-2) * (1 + int(tri)))
    if n % 3 == 1:
        return (n-1) * (1 + int(even)) * (1 + int(tri)) + 4 * int(four)
    return n * (1 + int(even)) * (1 + int(tri))

def apply_direct(n, state):
    vertex_count = 2*n
    u, v = state[:vertex_count], state[vertex_count:]
    new = []
    for i in range(vertex_count):
        opposite = u[n:] if i < n else u[:n]
        new.append((sum(opposite)-opposite[i % n]-v[i]) % P)
    return new + u

rng = Random(20261114)
rank_checks = 0
trajectory_checks = 0
for n in range(5, 11):
    T = wave(n)
    size = 4*n
    clock = {0:18, 1:12, 2:6}[n % 3]
    assert mpow(T, clock) == ident(size), (n, 'global-order')
    for divisor in (2, 3):
        if clock % divisor == 0:
            assert mpow(T, clock // divisor) != ident(size), (n, 'nonminimal-order')
    for t in range(1, 37):
        U = mpow(T, t)
        nullity = size - rank([[(x - int(i == j)) % P for j,x in enumerate(row)] for i,row in enumerate(U)])
        assert nullity == exponent(n,t), (n,t,nullity,exponent(n,t))
        rank_checks += 1
    for test in range(60):
        state = [rng.randrange(P) for _ in range(size)]
        initial = state[:]
        for t in range(1, clock+1):
            state = apply_direct(n, state)
            if t == clock:
                assert state == initial, (n,t,'direct-closed')
        trajectory_checks += 1
    print(f'n={n}, order={clock}, rank_nullities=36, direct_trajectories=60: passed')
print(f'PASS: {rank_checks} exact rank/nullity checks and {trajectory_checks} independent direct trajectories')
