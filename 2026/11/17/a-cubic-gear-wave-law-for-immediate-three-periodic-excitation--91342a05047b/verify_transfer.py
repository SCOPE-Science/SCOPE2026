"""Exact integer-only transfer and spectral check for gear-graph period-3 excitation."""
from itertools import product

PAIRS = list(product(range(3), repeat=2))

def transfer(h, prohibit_successor=False):
    M = [[0] * 9 for _ in range(9)]
    for i, (u, v) in enumerate(PAIRS):
        if prohibit_successor and u == (h + 1) % 3:
            continue
        for j, (u2, v2) in enumerate(PAIRS):
            if (u == (v + 1) % 3 or u2 == (v + 1) % 3) and (h == (u2 + 1) % 3 or v == (u2 + 1) % 3 or v2 == (u2 + 1) % 3):
                M[i][j] = 1
    return M

def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def trace(A):
    return sum(A[i][i] for i in range(len(A)))

def charpoly(M):
    # Exact Newton identities, integer arithmetic; output descending coefficients.
    n = len(M)
    P = identity(n)
    ps = []
    for k in range(1, n + 1):
        P = matmul(P, M)
        ps.append(trace(P))
    coefficients = [1]
    for k in range(1, n + 1):
        numerator = -sum(coefficients[k - j] * ps[j - 1] for j in range(1, k + 1))
        assert numerator % k == 0
        coefficients.append(numerator // k)
    return coefficients

A = transfer(0)
B = transfer(0, True)
assert charpoly(A) == [1, -1, -3, -5, -3, -1, 0, 0, 0, 0] or False, charpoly(A)
assert charpoly(B) == [1, -1, -3, -1, 0, 0, 0, 0, 0, 0] or False, charpoly(B)
print('charpoly_A', charpoly(A))
print('charpoly_B', charpoly(B))
P_A, P_B = identity(9), identity(9)
# Spectral power sums: roots of x^3-2x^2-2x-1, x^2+x+1,
# roots of x^2-2x-1 and -1.
p = [3, 2, 8]
for n in range(3, 65):
    p.append(2 * p[n-1] + 2 * p[n-2] + p[n-3])
r = [2, 2]
for n in range(2, 65):
    r.append(2 * r[n-1] + r[n-2])
expected = []
for n in range(1, 51):
    P_A = matmul(P_A, A)
    P_B = matmul(P_B, B)
    rotational = 2 if n % 3 == 0 else -1
    lhs = trace(P_A) - trace(P_B)
    rhs = p[n] + rotational - r[n] - ((-1)**n)
    assert lhs == rhs, (n, lhs, rhs)
    if n >= 3:
        expected.append((n, 3 * lhs))
print('counts_n3_to_n12', expected[:10])
print('all_trace_and_formula_checks_through_50_PASS')
