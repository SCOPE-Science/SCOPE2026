#!/usr/bin/env python3
"""Independent finite-dimensional checks for an explicitly specified quantum master equation.

Requires only the Python standard library. The mathematical theorem is proved in RESULT.md;
finite tests here do not establish its quantified statements.
"""
import cmath
import math
import random

N = 4


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]


def dagger(A):
    return [[A[j][i].conjugate() for j in range(N)] for i in range(N)]


def operator(i, j):
    E = [[0j for _ in range(N)] for _ in range(N)]
    E[i][j] = 1
    return E


def master(R, g, gamma, reset):
    H = [[0j for _ in range(N)] for _ in range(N)]
    H[0][3] = H[3][0] = g
    jumps = [operator(0, 2), operator(1, 3)]  # first-qubit amplitude damping
    jumps += [operator(0, 1), operator(2, 3)]  # second-qubit amplitude damping
    # Each physical jump operator is one of the two matrices below, combining
    # its two nonzero entries before forming J rho J^dagger.
    J1 = [[0j for _ in range(N)] for _ in range(N)]
    J2 = [[0j for _ in range(N)] for _ in range(N)]
    for a, b in ((0, 2), (1, 3)):
        J1[a][b] = 1
    for a, b in ((0, 1), (2, 3)):
        J2[a][b] = 1
    I = [[complex(i == j) for j in range(N)] for i in range(N)]
    out = matmul(H, R)
    rhs = matmul(R, H)
    out = [[-1j * (out[i][j] - rhs[i][j]) - reset * R[i][j]
            for j in range(N)] for i in range(N)]
    out[0][0] += reset * sum(R[i][i] for i in range(N))
    for J in (J1, J2):
        K = matmul(dagger(J), J)
        gain = matmul(matmul(J, R), dagger(J))
        loss1 = matmul(K, R)
        loss2 = matmul(R, K)
        for i in range(N):
            for j in range(N):
                out[i][j] += gamma * (gain[i][j] - (loss1[i][j] + loss2[i][j]) / 2)
    return out


def linear_solve(A, y):
    # Independent complex pivoting solver for the unrestricted 16-by-16 Liouvillian.
    M = [list(row) + [complex(z)] for row, z in zip(A, y)]
    n = len(M)
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(M[i][k]))
        if abs(M[p][k]) < 1e-12:
            raise ArithmeticError('singular Liouvillian')
        M[k], M[p] = M[p], M[k]
        q = M[k][k]
        M[k] = [v / q for v in M[k]]
        for i in range(k + 1, n):
            q = M[i][k]
            if q:
                M[i] = [M[i][j] - q * M[k][j] for j in range(n+1)]
    x = [0j] * n
    for i in range(n - 1, -1, -1):
        x[i] = M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))
    return x


def exact_stationary(g, gamma, reset):
    D = (reset + gamma)**2 + 4*g*g
    a = 2*g*g*(reset+gamma)/((reset+2*gamma)*D)
    b = 2*g*g*gamma/((reset+2*gamma)*D)
    u = g*(reset+gamma)/D
    R = [[0j for _ in range(N)] for _ in range(N)]
    R[0][0] = 1 - a - 2*b
    R[1][1] = R[2][2] = b
    R[3][3] = a
    R[0][3] = 1j*u
    R[3][0] = -1j*u
    return R


def stationary_from_generator(g, gamma, reset):
    A = [[0j] * 16 for _ in range(16)]
    for n in range(16):
        E = operator(n//4, n % 4)
        D = master(E, g, gamma, reset)
        for i in range(N):
            for j in range(N):
                A[4*i+j][n] = D[i][j]
    A[0] = [complex(k in (0, 5, 10, 15)) for k in range(16)]
    rhs = [0j] * 16
    rhs[0] = 1
    x = linear_solve(A, rhs)
    return [x[i*4:i*4+4] for i in range(4)]


def concurrence(g, gamma, reset):
    d = reset + 2*gamma
    q = reset + gamma
    return max(0.0, 2*g * (q*d-2*g*gamma) / (d*(q*q+4*g*g)))


def optimal_g(gamma, reset):
    q = reset + gamma
    d = reset + 2*gamma
    return q * (math.hypot(gamma, d) - gamma) / (2*d)


def optimal_C(gamma, reset):
    d = reset + 2*gamma
    return (math.hypot(gamma, d) - gamma) / (2*d)


def assert_near(a, b, tol=1e-9):
    assert abs(a-b) <= tol * max(1, abs(a), abs(b)), (a,b)


def test():
    count = 0
    rng = random.Random(20261115)
    for _ in range(85):
        g = 10**rng.uniform(-1.1, 1.4)
        gamma = 10**rng.uniform(-1.3, 1.2)
        r = 10**rng.uniform(-1.1, 1.7)
        R = exact_stationary(g, gamma, r)
        Q = stationary_from_generator(g, gamma, r)
        assert max(abs(R[i][j]-Q[i][j]) for i in range(4) for j in range(4)) < 1e-10
        count += 1
        assert max(abs(z) for row in master(R,g,gamma,r) for z in row) < 1e-11
        count += 1
        # Independent partial transpose: its only potentially negative block is
        # [[rho01, rho00,11], [rho11,00, rho10]], giving eigenvalues b +/- |u|.
        b = R[1][1].real
        u = abs(R[0][3])
        ptmin = b-u
        assert (ptmin < -1e-10) == (concurrence(g,gamma,r) > 2e-10)
        count += 1
        assert_near(max(0.0, -2*ptmin), concurrence(g,gamma,r))
        count += 1
        assert R[0][0].real * R[3][3].real + 1e-12 >= u*u
        assert all(R[i][i].real >= 0 for i in range(4))
        count += 2
    for gamma in (0.11, 0.5, 1.0, 3.0):
        for r in (0.03,0.5, 2.0, 8.0, 40.0):
            go = optimal_g(gamma,r)
            assert_near(concurrence(go,gamma,r),optimal_C(gamma,r))
            count += 1
            # Strict global maximum by algebra; grids numerically test the claim.
            for factor in (0.05,0.2,0.6,0.9,1.1,1.5,3.0,9.0):
                assert concurrence(go*factor,gamma,r) < concurrence(go,gamma,r)
                count += 1
            assert optimal_C(gamma,r) < .5
            count += 1
    for gamma in (0.05,0.6,1.5):
        for scale in (1.001,1.1,2.0,10.0):
            g=scale*gamma
            rc=(math.sqrt(gamma*gamma+8*gamma*g)-3*gamma)/2
            assert_near(concurrence(g,gamma,rc),0)
            assert concurrence(g,gamma,rc*0.99) == 0
            assert concurrence(g,gamma,rc*1.01) > 0
            count += 3
    golden=(math.sqrt(5)-1)/4
    for gamma in (0.1, 1.0, 10.0):
        assert_near(optimal_C(gamma,0), golden)
        assert optimal_C(gamma,1e8*gamma) > 0.49999999
        count += 2
    for _ in range(30):
        g,gamma,r = [10**rng.uniform(-2, 2) for j in range(3)]
        s=10**rng.uniform(-2,2)
        assert_near(concurrence(g,gamma,r),concurrence(s*g,s*gamma,s*r))
        count += 1
    print('PASS: %d independent numerical, algebraic-boundary and positivity assertions' % count)

if __name__ == '__main__':
    test()
