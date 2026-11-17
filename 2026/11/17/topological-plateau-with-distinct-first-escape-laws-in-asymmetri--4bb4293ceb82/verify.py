#!/usr/bin/env python3
"""Exact-rational finite checks for nested critical-hole first-hit laws.

Run with Python 3.10+; only the standard library is required.
"""
from fractions import Fraction as Q


def forbidden_right(length):
    return '11' + ''.join('0' if j % 2 == 0 else '1' for j in range(length - 2))


def series_coefficients(k, even, terms):
    # G(z)=N(z)/D(z); all coefficient operations use exact rational arithmetic.
    exponent = 2 * k + 1
    D = [Q(0)] * max(3, exponent + 1)
    D[0], D[1], D[2], D[exponent] = Q(1), Q(-1, 2), Q(-1, 4), Q(1, 2**exponent)
    N = [Q(0)] * max(3, exponent + 1)
    if even:
        N[0] = Q(1, 4) + Q(1, 2**(2*k+2))
        N[1] = Q(1, 2**(2*k+3))
        N[2*k+1] += Q(1, 2**(2*k+3))
    else:
        N[0] = Q(1, 4) + Q(1, 2**(2*k+1))
        N[1] = Q(1, 2**(2*k+2))
        N[2*k] -= Q(1, 2**(2*k+2))
    result = []
    for i in range(terms):
        v = N[i] if i < len(N) else Q(0)
        v -= sum(D[j]*result[i-j] for j in range(1,min(i+1,len(D))))
        result.append(v)
    return result


def direct_escape(k, even, horizon):
    length = 2*k+2 if even else 2*k+1
    steps = length + horizon + 1
    scale = 2**steps
    counter = [0] * (horizon + 1)
    left, right = Q(1,4), Q(1,2)+Q(1,2**length)
    for p in range(scale):
        x = Q(2*p+1,2*scale)
        for j in range(horizon+1):
            if left < x < right:
                counter[j] += 1
                break
            x = (-2*x) % 1
    return [Q(v,scale) for v in counter]


def matrix_and_absorption(length):
    pats = ('00',forbidden_right(length))
    states = list(dict.fromkeys([''] + [w[:i] for w in pats for i in range(1,len(w))]))
    r = len(states)
    M = [[Q(0) for _ in range(r)] for _ in range(r)]
    B = [[Q(0),Q(0)] for _ in range(r)]
    for i,word in enumerate(states):
        for b in '01':
            v = word+b
            hit = [j for j,pat in enumerate(pats) if v.endswith(pat)]
            if hit:B[i][hit[0]] += Q(1,2)
            else:
                w = max((s for s in states if v.endswith(s)),key=len)
                M[i][states.index(w)] += Q(1,2)
    return M,B


def solve(M, b):
    n = len(M)
    A = [[(Q(i==j)-M[i][j]) for j in range(n)] + [b[i]] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j,n) if A[i][j] != 0)
        A[j],A[pivot] = A[pivot],A[j]
        fac = A[j][j]
        A[j] = [v/fac for v in A[j]]
        for i in range(n):
            if i==j: continue
            fac = A[i][j]
            A[i] = [a-fac*c for a,c in zip(A[i],A[j])]
    return [A[i][-1] for i in range(n)]


for k in range(1,6):
    for even in (False,True):
        length = 2*k+2 if even else 2*k+1
        M,B = matrix_and_absorption(length)
        Et = solve(M, [Q(1)]*len(M))[0]
        pR = solve(M, [r[1] for r in B])[0]
        expected_R = Q(3,2*(4**k+2)) if even else Q(3,4**k+2)
        assert pR == expected_R
        # Completion time in bits -> first-hit index in map iterates.
        Ehit = Et - (2-1)*(1-pR) - (length-1)*pR - 1
        expected = Q(4**(k+1)-1-(3 if even else 6)*k,4**k+2)
        assert Ehit == expected, (k,even,Ehit,expected)
        assert series_coefficients(k,even,5) == direct_escape(k,even,4)
    assert forbidden_right(2*k+2) == forbidden_right(2*k+1)+'1'
    print(f'k={k}: exact PGF coefficients, means and right-hole probabilities verified')

print('VERIFY_OK exact_rational_patterns=10 means=10 winning_probabilities=10 direct_time_probabilities=50')
