#!/usr/bin/env python3
"""Exact finite checks for the two-row odd-island shift (standard library only)."""
from itertools import product
from fractions import Fraction

STATES = ('E', 'T0', 'T1', 'B0', 'B1', 'D0', 'D1')
LABELS = (0, 1, 2, 3)  # bits: top=1, bottom=2; D=3
# Each outgoing edge is unique for its destination column label.
EDGES = {
    'E': {0: 'E', 1: 'T1', 2: 'B1', 3: 'D0'},
    'T0': {1: 'T1', 3: 'D0'},
    'T1': {0: 'E', 1: 'T0', 2: 'B1', 3: 'D1'},
    'B0': {2: 'B1', 3: 'D0'},
    'B1': {0: 'E', 1: 'T1', 2: 'B0', 3: 'D1'},
    'D0': {1: 'T1', 2: 'B1', 3: 'D0'},
    'D1': {0: 'E', 1: 'T0', 2: 'B0', 3: 'D1'},
}
M = [[sum(x == dst for x in EDGES[src].values()) for dst in STATES] for src in STATES]
W = [[-1, 0, 1], [0, -1, 1], [-1, -1, 1]]

def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))]

def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def trace(A):
    return sum(A[i][i] for i in range(len(A)))

def charpoly(A):
    n = len(A)
    B = ident(n)
    coeff = [1]
    for k in range(1, n + 1):
        B = matmul(A, B)
        c = Fraction(-trace(B), k)
        assert c.denominator == 1
        c = int(c)
        coeff.append(c)
        for i in range(n):
            B[i][i] += c
    return coeff

def conv(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out

assert charpoly(M) == conv([1, 1, -1], [1, -4, 3, -5, 2, 1])
assert charpoly(W) == conv([1, 1], [1, 0, 1])

def finite_components(word, cyclic=False):
    """Check odd size of every finite component of active two-row cells.

    For cyclic words, unfold five copies; components hitting the outer
    copies' edge are infinite in the repeated configuration.
    """
    n = len(word)
    copies = 5 if cyclic else 1
    width = copies*n
    cells = {(j, row) for j in range(width) for row in range(2)
             if word[j % n] & (1 << row)}
    seen = set()
    for start in cells:
        if start in seen:
            continue
        seen.add(start)
        comp = {start}
        queue = [start]
        for x, row in queue:
            for z in ((x-1, row), (x+1, row), (x, 1-row)):
                if z in cells and z not in seen:
                    seen.add(z)
                    comp.add(z)
                    queue.append(z)
        if cyclic:
            # Check only components hitting the central copy, thus avoiding
            # artificial incomplete components near unfolded boundaries.
            if not any(2*n <= x < 3*n for x, _ in comp):
                continue
            if any(x == 0 or x == width-1 for x, _ in comp):
                continue
        if len(comp) % 2 == 0:
            return False
    return True

def count_finite_via_graph(n):
    counts = [0]*len(STATES)
    counts[0] = 1
    for _ in range(n):
        counts = [sum(counts[i]*M[i][j] for i in range(len(STATES)))
                  for j in range(len(STATES))]
    return sum(counts[STATES.index(t)] for t in ('E', 'T1', 'B1', 'D1'))

Mpower = ident(len(M))
Wpower = ident(len(W))
tests = 0
for n in range(1, 9):
    words = product(LABELS, repeat=n)
    pbrute = fbrute = 0
    for word in words:
        fbrute += finite_components(word)
        pbrute += finite_components(word, cyclic=True)
        tests += 2
    Mpower = matmul(Mpower, M)
    Wpower = matmul(Wpower, W)
    assert fbrute == count_finite_via_graph(n), (n, fbrute)
    pformula = trace(Mpower) - trace(Wpower)
    assert pbrute == pformula, (n, pbrute, pformula)
    print('n=%d closed=%d periodic=%d' % (n, fbrute, pbrute))
print('PASS: %d independently tested finite/component decisions, two characteristic polynomials, eight transfer counts, eight periodic-point identities.' % tests)
