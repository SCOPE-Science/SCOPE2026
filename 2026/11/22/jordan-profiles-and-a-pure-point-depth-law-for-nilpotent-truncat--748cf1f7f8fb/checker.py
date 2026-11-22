#!/usr/bin/env python3
"""Independent finite-field check of truncated substitution Jordan profiles.
Public-domain verification code; no dependencies beyond the standard library.
"""
from itertools import product
from collections import Counter


def matmul(A, B, q):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) % q for j in range(n)] for i in range(n)]


def rank(A, q):
    A = [row[:] for row in A]
    m = len(A)
    n = len(A[0]) if m else 0
    z = 0
    for col in range(n):
        k = next((i for i in range(z, m) if A[i][col] % q), None)
        if k is None:
            continue
        A[z], A[k] = A[k], A[z]
        inv = pow(A[z][col], -1, q)
        A[z] = [(v*inv) % q for v in A[z]]
        for i in range(z+1, m):
            v = A[i][col]
            if v:
                A[i] = [(u-v*w) % q for u, w in zip(A[i], A[z])]
        z += 1
    return z


def convolution(a, b, N, q):
    c = [0]*N
    for i in range(1, N):
        if not a[i]:
            continue
        for j in range(1, N-i):
            c[i+j] = (c[i+j]+a[i]*b[j]) % q
    return c


def substitution_matrix(coeffs, N, q):
    s = N-1
    full = [0] + list(coeffs)
    power = [0]*N
    power[0] = 1
    cols = []
    for _ in range(s):
        power = convolution(power, full, N, q) if len(cols) else full[:]
        cols.append(power[1:])
    return [[cols[j][i] for j in range(s)] for i in range(s)]


def profile_from_matrix(M, q):
    n = len(M)
    ranks = [n]
    P = M
    while True:
        k = rank(P, q)
        ranks.append(k)
        if k == 0:
            break
        if len(ranks) > n+1:
            raise AssertionError('Unexpected nonnilpotent matrix')
        P = matmul(P, M, q)
    ranks.append(0)
    return tuple(ranks[j-1]-2*ranks[j]+ranks[j+1] for j in range(1, len(ranks)-1))


def predicted_profile(N, d):
    r = [N-1]
    if d is None:
        r.append(0)
    else:
        t = d
        while t < N:
            r.append((N-1)//t)
            t *= d
        r.append(0)
    r.append(0)
    return tuple(r[j-1]-2*r[j]+r[j+1] for j in range(1, len(r)-1))


def run_case(N, q):
    s = N-1
    counts = Counter()
    by_profile = Counter()
    for coeffs in product(range(q), repeat=s):
        if coeffs[0] != 0:
            continue
        d = next((i+1 for i,v in enumerate(coeffs) if v), None)
        M = substitution_matrix(coeffs, N, q)
        actual = profile_from_matrix(M, q)
        expected = predicted_profile(N, d)
        if actual != expected:
            raise AssertionError((N,q,coeffs,d,actual,expected))
        counts[d] += 1
        by_profile[actual] += 1
    assert counts[None] == 1
    for d in range(2, N):
        assert counts[d] == (q-1)*q**(N-1-d)
    assert sum(counts.values()) == q**(N-2)
    # Verify the complete Jordan-profile histogram, merging equal shapes.
    formula = Counter({predicted_profile(N,None):1})
    for d in range(2,N):
        formula[predicted_profile(N,d)] += (q-1)*q**(N-1-d)
    assert by_profile == formula, (by_profile,formula)
    return f'PASS N={N} q={q} checked={sum(counts.values())} profiles={len(by_profile)}'

if __name__=='__main__':
    for N,q in [(3,2),(4,2),(5,2),(6,2),(7,2),(8,2),(5,3),(6,3),(7,3),(8,3),(6,5)]:
        print(run_case(N,q))
    print('ALL CHECKS PASSED')
