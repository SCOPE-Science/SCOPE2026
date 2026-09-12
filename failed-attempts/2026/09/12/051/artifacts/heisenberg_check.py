"""Explicit 3x3 unitriangular matrix check of the Heisenberg commutator identity.
Verifies [E12(s), E23(s)] = E13(s^2) mod m, hence w_s maps to identity iff m | s^2.
Deterministic; runs in well under a minute."""
import json

def mat_mul(A, B, m):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) % m for j in range(3)] for i in range(3)]

def mat_pow(A, s, m):
    R = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
    for _ in range(s):
        R = mat_mul(R, A, m)
    return R

def mat_inv(A, m):
    # E12(a)E23(b)E13(c) inverse is E13(ac-b+c... ) — brute force over 27 unitriangular candidates
    cands = []
    for a in range(m):
        for b in range(m):
            for c in range(m):
                M = [[1, a, c], [0, 1, b], [0, 0, 1]]
                M = [[x % m for x in row] for row in M]
                cands.append(M)
    for M in cands:
        if mat_mul(A, M, m) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]:
            return M
    raise AssertionError("no inverse")

def comm(A, B, m):
    return mat_mul(mat_mul(mat_mul(A, B, m), mat_inv(A, m), m), mat_inv(B, m), m)

def E12(a, m):
    return [[1, a % m, 0], [0, 1, 0], [0, 0, 1]]

def E23(b, m):
    return [[1, 0, 0], [0, 1, b % m], [0, 0, 1]]

def E13(c, m):
    return [[1, 0, c % m], [0, 1, 0], [0, 0, 1]]

out = {}
for m, S, N in [(4, [4, 6], 3), (9, [6, 9], 5)]:
    A, B = E12(1, m), E23(1, m)
    row = {}
    for s in S + [N]:
        C = comm(mat_pow(A, s, m), mat_pow(B, s, m), m)
        row[f"s={s}"] = {"matrix_equals_E13_s2": C == E13(s * s, m),
                         "is_identity": C == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]}
    out[f"mod_{m}"] = row
print(json.dumps(out, indent=1))
