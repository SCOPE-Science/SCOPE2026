#!/usr/bin/env python3
"""Exact rational reproduction of a three-state Markov-hole comparison."""
from fractions import Fraction as Q

P = [[Q(z, 10) for z in row] for row in ((8, 1, 1), (3, 3, 4), (1, 7, 2))]
pi = [Q(14, 27), Q(5, 18), Q(11, 54)]

def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q(0))

def mulrow(a, B):
    return [sum((a[i]*B[i][j] for i in range(len(a))), Q(0))
            for j in range(len(B[0]))]

def det3(B):
    a, b, c = B
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
           -a[1]*(b[0]*c[2]-b[2]*c[0])
           +a[2]*(b[0]*c[1]-b[1]*c[0]))

def char_coefficients(B):
    n = len(B)
    assert n == 3
    tr = sum(B[i][i] for i in range(n))
    minors = sum(B[i][i]*B[j][j]-B[i][j]*B[j][i]
                 for i in range(n) for j in range(i+1, n))
    return (Q(1), -tr, minors, -det3(B))

def poly_at(coefficients, z):
    out = Q(0)
    for c in coefficients:
        out = z*out + c
    return out

def remove_edge(i, j):
    B = [r[:] for r in P]
    B[i][j] = Q(0)
    return B

assert all(sum(row, Q(0)) == 1 for row in P)
assert all(x > 0 for row in P for x in row)
assert sum(pi) == 1 and mulrow(pi, P) == pi
assert pi[1]*P[1][0] == Q(1, 12)
assert pi[1]*P[1][2] == Q(1, 9)
# Both holes are prime: first letter differs from the second.
assert 1 != 0 and 1 != 2
B21, B23 = remove_edge(1, 0), remove_edge(1, 2)
c21 = char_coefficients(B21)
c23 = char_coefficients(B23)
assert c21 == (Q(1), Q(-13, 10), Q(17, 100), Q(7, 40))
assert c23 == (Q(1), Q(-13, 10), Q(21, 50), Q(-3, 50))
assert poly_at(c21, Q(9, 10)) == Q(1, 250)
assert poly_at(c23, Q(9, 10)) == Q(-3, 500)
assert poly_at(c23, Q(1)) == Q(3, 50)
# A separate exact count: enumerate all Markov paths through time n,
# removing paths containing the disallowed transition, and compare
# with propagation by the killed transition operator.
for i, j, B in ((1, 0, B21), (1, 2, B23)):
    surviving = pi[:]
    for n in range(1, 12):
        surviving = mulrow(surviving, B)
        matrix_survival = sum(surviving)
        # Independent dynamic-programming calculation from all allowed edges.
        dp = {state: pi[state] for state in range(3)}
        for _ in range(n):
            nxt = {state: Q(0) for state in range(3)}
            for a in range(3):
                for b in range(3):
                    if (a, b) != (i, j):
                        nxt[b] += dp[a]*P[a][b]
            dp = nxt
        assert matrix_survival == sum(dp.values())
        assert 0 < matrix_survival < 1
print('PRIME_MARKOV_ESCAPE_COUNTEREXAMPLE_EXACT_OK')
