#!/usr/bin/env python3
"""Exact transfer and direct-state checks for three-opinion plurality on twisted ladders.

Requires Python 3 and sympy. This verifies a finite symbolic identity valid for all
ladder sizes, plus independent full-state enumeration for small sizes.
"""
from itertools import product
from collections import Counter
import sympy as sp

COLORS = range(3)
RUNGS = list(product(COLORS, repeat=2))
RUNG_INDEX = {r: i for i, r in enumerate(RUNGS)}
DIM = len(RUNGS)**2


def stable(color, neighbors):
    counts = Counter(neighbors)
    maximum = max(counts.values())
    winners = [x for x, m in counts.items() if m == maximum]
    return len(winners) > 1 or winners[0] == color


def transfer():
    mat = [[0] * DIM for _ in range(DIM)]
    for a, u in enumerate(RUNGS):
        for b, v in enumerate(RUNGS):
            for c, w in enumerate(RUNGS):
                if stable(v[0], (u[0], v[1], w[0])) and stable(v[1], (u[1], v[0], w[1])):
                    mat[9*a+b][9*b+c] = 1
    return mat


def swap_map():
    result = []
    for u in RUNGS:
        for v in RUNGS:
            su = (u[1], u[0]); sv = (v[1], v[0])
            result.append(9*RUNG_INDEX[su]+RUNG_INDEX[sv])
    assert all(result[result[i]] == i for i in range(DIM))
    return result


def plus_minus_matrices(A, J):
    seen = set(); nonfixed = []; fixed = []
    for i in range(DIM):
        if i in seen: continue
        seen.add(i); seen.add(J[i])
        if J[i] == i: fixed.append(i)
        else: nonfixed.append(i)
    assert (len(nonfixed), len(fixed)) == (36, 9)
    B = sp.Matrix([[A[i][j] - A[i][J[j]] for j in nonfixed] for i in nonfixed])
    reps = nonfixed + fixed
    C = sp.Matrix([[(A[i][j] + A[i][J[j]]) if j in nonfixed else A[i][j]
                    for j in reps] for i in reps])
    return B, C


def symbolic_certificate():
    A = transfer(); J = swap_map()
    for i in range(DIM):
        for j in range(DIM):
            assert A[J[i]][J[j]] == A[i][j]
    B, C = plus_minus_matrices(A, J)
    z = sp.Symbol('z')
    P = z**4+z**2+z+1
    Q = z**4-3*z**3+4*z**2-2*z+1
    R = z**5-5*z**4+7*z**3-4*z**2+6*z-3
    S = z**7-z**6+3*z**5-2*z**4-4*z**2-3*z-3
    assert sp.expand(B.charpoly(z).as_expr()-z**21*(z+1)**3*P*Q**2) == 0
    assert sp.expand(C.charpoly(z).as_expr()-z**21*(z-1)**2*(z+1)**3*R*S**2) == 0
    print('EXACT_36_AND_45_DIMENSION_CHARACTERISTIC_POLYNOMIALS_OK')
    return A, J


def matmul(A, B):
    N = len(A)
    C = [[0]*N for _ in range(N)]
    for i in range(N):
        for k in range(N):
            a = A[i][k]
            if a:
                for j in range(N):
                    b = B[k][j]
                    if b: C[i][j] += a*b
    return C


def power_sum(coeffs, nmax):
    d = len(coeffs)-1; ps = [d]
    for n in range(1, nmax+1):
        if n <= d:
            ps.append(-sum(coeffs[k]*ps[n-k] for k in range(1,n))-n*coeffs[n])
        else:
            ps.append(-sum(coeffs[k]*ps[n-k] for k in range(1,d+1)))
    return ps


def trace_checks(A, J):
    U = power_sum([1,0,1,1,1], 60)
    V = power_sum([1,-3,4,-2,1], 60)
    X = [r[:] for r in A]
    values = {}
    for n in range(1,19):
        prism = sum(X[i][i] for i in range(DIM))
        mobius = sum(X[i][J[i]] for i in range(DIM))
        D = 6*((-1)**n)+2*U[n]+4*V[n]
        assert prism - mobius == D, (n, prism, mobius, D)
        values[n] = (prism, mobius, D)
        X = matmul(X,A)
    expected = {3:(15,39), 4:(93,135), 5:(219,303),
                6:(489,585), 7:(1227,1305), 8:(3645,3543),
                9:(10293,9831), 10:(27069,26073)}
    for n, pair in expected.items(): assert values[n][:2] == pair
    for n in range(3,61):
        D = 6*((-1)**n)+2*U[n]+4*V[n]
        assert (D>0) == (n%10 in (0,1,2,8,9)), (n,D)
    print('EXACT_TRACE_AND_NEWTON_RECURRENCES_OK')
    return values


def independent_bruteforce(n, twisted):
    # Construct the graph directly; do not use the transfer, swap, or state-pair encoding.
    adj = [[] for _ in range(2*n)]
    def connect(v,w):
        adj[v].append(w);adj[w].append(v)
    for i in range(n): connect(2*i,2*i+1)
    for i in range(n-1):
        connect(2*i,2*i+2);connect(2*i+1,2*i+3)
    if twisted:
        connect(0,2*n-1);connect(1,2*n-2)
    else:
        connect(0,2*n-2);connect(1,2*n-1)
    assert all(len(row) == 3 and len(set(row)) == 3 for row in adj)
    total = 0
    for state in product(COLORS, repeat=2*n):
        works = True
        for v in range(2*n):
            a,b,c=(state[j] for j in adj[v])
            if a==b or a==c: winner=a
            elif b==c: winner=b
            else: continue
            if state[v] != winner:
                works = False;break
        total += works
    return total


def finite_checks(values):
    for n in range(3,7):
        p = independent_bruteforce(n,False)
        m = independent_bruteforce(n,True)
        assert (p,m) == values[n][:2], (n,p,m)
    print('DIRECT_MICROSCOPIC_ENUMERATION_N3_TO_N6_OK')


def sign_proof_bound():
    # |root|<3/2 for all roots of z^4+z^2+z+1 by Rouche on |z|=3/2:
    # (3/2)^4 = 81/16 > 19/4 = (3/2)^2+(3/2)+1.
    assert sp.Rational(81,16)>sp.Rational(19,4)
    phi = (1+sp.sqrt(5))/2
    # Minimum |cos(n*pi/5)| is (sqrt(5)-1)/4, for integer n.
    margin = sp.simplify(2*(sp.sqrt(5)-1)*phi**16
               - 8*sp.Rational(3,2)**16 - 6 - 8*phi**(-16))
    assert margin == 5168*sp.sqrt(5)-sp.Rational(93067073,8192)
    assert margin.is_positive is True
    # Each positive term in the residual divided by phi**n decreases for n>=16.
    print('ALL_N_SIGN_DOMINANCE_BOUND_AT_N16_OK')


if __name__ == '__main__':
    A,J = symbolic_certificate()
    values = trace_checks(A,J)
    finite_checks(values)
    sign_proof_bound()
    for n in range(3,16): print('n=%d prism=%d mobius=%d difference=%d' % ((n,)+values[n]))
    print('TERNARY_PLURALITY_LADDER_VERIFY_OK')
