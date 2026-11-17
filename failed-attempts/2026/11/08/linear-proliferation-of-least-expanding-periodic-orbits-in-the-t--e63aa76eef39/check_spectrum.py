#!/usr/bin/env python3
"""Exact finite checks for least expansion of the 3D twisted baker map.

Uses only the Python standard library. Analytical all-period proof is in RESULT.md.
"""
from fractions import Fraction as Q
from collections import Counter
from itertools import product
from math import comb

DIM = 3
L = ((2, 0, 0), (0, 1, 0), (0, 0, 1))
R = ((0, 0, -2), (1, 0, 0), (0, 1, 0))
I = tuple(tuple(int(i == j) for j in range(3)) for i in range(3))


def mm(U, V):
    return tuple(tuple(sum(U[i][k]*V[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def mv(U, v):
    return tuple(sum(U[i][j]*v[j] for j in range(3)) for i in range(3))


def solve(U, v):
    A = [[Q(U[i][j]) for j in range(3)]+[Q(v[i])] for i in range(3)]
    for j in range(3):
        i = next(i for i in range(j, 3) if A[i][j])
        A[i], A[j] = A[j], A[i]
        t = A[j][j]
        A[j] = [u/t for u in A[j]]
        for k in range(3):
            if k != j:
                t = A[k][j]
                A[k] = [a-t*b for a, b in zip(A[k], A[j])]
    return tuple(A[i][3] for i in range(3))


def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))


def scalar_power_two(k):
    return k > 0 and (k & (k-1)) == 0


def main():
    tests = 0
    for n in range(1, 10):
        counts = Counter()
        minimizing = []
        for letters in product('LR', repeat=n):
            w = ''.join(letters)
            if w == 'L'*n:
                continue
            A, b = I, (Q(0), Q(0), Q(0))
            phase, visits = 0, [0, 0, 0]
            for letter in w:
                B = L if letter == 'L' else R
                A, b = mm(B, A), mv(B, b)
                b = (b[0]+1, b[1], b[2])
                if letter == 'L':
                    visits[phase] += 1
                else:
                    phase = (phase+1)%3
            E = tuple(tuple(int(i == j)-A[i][j] for j in range(3)) for i in range(3))
            x = solve(E, b)
            assert -1 < x[0] <= 1 and all(0 <= v <= 1 for v in x[1:])
            for letter in w:
                assert (x[0] < 0) == (letter == 'L')
                x = (1+2*x[0], x[1], x[2]) if letter == 'L' else (1-2*x[2], x[0], x[1])
                tests += 1
            assert mv(A, solve(E, b)) == tuple(u-v for u,v in zip(solve(E,b), b))
            tests += 1
            t = w.count('R')
            assert t > 0
            assert abs(det3(A)) == 2**n
            tests += 1
            if t%3:
                assert all(A[i][i] == 0 for i in range(3))
                assert sum(A[i][j]*A[j][i] for i in range(3) for j in range(3)) == 0
                # Trace(A) = Trace(A**2) = 0, hence char(A) = u**3 - det(A).
                counts['nontwist'] += 1
                tests += 2
            else:
                assert all(A[i][j] == 0 for i in range(3) for j in range(3) if i != j)
                exponents = tuple(abs(A[i][i]).bit_length()-1 for i in range(3))
                assert all(scalar_power_two(abs(A[i][i])) for i in range(3))
                assert sum(exponents) == n
                assert sorted(exponents) == sorted(t//3 + v for v in visits)
                tests += 4
                if n >= 4 and min(exponents) == 1:
                    minimizing.append(w)
                counts['twist'] += 1
        if n >= 4:
            assert len(minimizing) == n*(n-3)
            for w in minimizing:
                assert w.count('R') == 3
                assert 'RR' in (w+w)
                tests += 2
            tests += 1
        print(f'n={n}: periodic={2**n-1}, weakest={len(minimizing)}')
    print('CHECK_OK', tests, 'exact assertions')


if __name__=='__main__':
    main()
