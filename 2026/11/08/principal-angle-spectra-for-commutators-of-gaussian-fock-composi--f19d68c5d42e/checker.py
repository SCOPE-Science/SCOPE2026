#!/usr/bin/env python3
"""Exact arithmetic tests for two Gaussian-Fock composition projections.

The n-particle test uses the unnormalized monomials z1^k*z2^(n-k),
whose Gram matrix is diagonal with entries k!*(n-k)!.
No numerical eigensolver or non-standard package is required.
"""
from fractions import Fraction as Q
from math import comb, factorial

checks = 0

def check(condition, label):
    global checks
    assert condition, label
    checks += 1

def mul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def trace(A):
    return sum(A[i][i] for i in range(len(A)))

c, s = Q(3, 5), Q(4, 5)
for n in range(1, 13):
    m = n + 1
    P = [[Q(int(i == j == n)) for j in range(m)] for i in range(m)]
    u = [Q(comb(n, k))*c**k*s**(n-k) for k in range(m)]
    v = [c**k*s**(n-k) for k in range(m)]
    R = [[u[i]*v[j] for j in range(m)] for i in range(m)]
    check(sum(v[k]*u[k] for k in range(m)) == 1, 'rank-one projection')
    check(mul(R, R) == R, 'idempotent')
    weight = [factorial(k)*factorial(n-k) for k in range(m)]
    for i in range(m):
        for j in range(m):
            check(weight[i]*R[i][j] == weight[j]*R[j][i], 'Gram self-adjoint')
    K = [[mul(P,R)[i][j] - mul(R,P)[i][j] for j in range(m)] for i in range(m)]
    K2 = mul(K,K)
    K3 = mul(K2,K)
    delta = c**(2*n)*(1-c**(2*n))
    check(trace(K2) == -2*delta, 'two singular values squared')
    check(trace(mul(K2,K2)) == 2*delta*delta, 'fourth-power trace')
    for i in range(m):
        for j in range(m):
            check(K3[i][j] == -delta*K[i][j], 'minimal polynomial')

# Two independent non-right principal angles: c1=3/5, c2=4/5.
# Compare total-degree truncations of the Hilbert-Schmidt spectral sum
# against the rational generating function of symmetric powers.
r1, r2 = Q(9,25), Q(16,25)
for N in range(20):
    p2 = sum((r1**i*r2**j - r1**(2*i)*r2**(2*j))
             for i in range(N+1) for j in range(N+1-i))
    a = [sum(r1**i*r2**(k-i) for i in range(k+1)) for k in range(N+1)]
    b = [sum(r1**(2*i)*r2**(2*(k-i)) for i in range(k+1)) for k in range(N+1)]
    check(p2 == sum(a[k]-b[k] for k in range(N+1)), 'Hilbert-Schmidt generating function')

exact_total = Q(2)*(Q(1)/(1-r1)/(1-r2) - Q(1)/(1-r1*r1)/(1-r2*r2))
check(exact_total > 0, 'positive exact total')
print('FOCK_PROJECTION_PRINCIPAL_ANGLES_EXACT_OK', checks,
      'rank_one_c=3/5', 'two_angle_S2_squared=', exact_total)
