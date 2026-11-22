#!/usr/bin/env python3
"""Exact integer graph verification for primitive binary six-window cycles."""
from collections import Counter
from math import factorial

N = 6

def primitive(bits):
    return all(any(bits[j] != bits[j % d] for j in range(N)) for d in (1, 2, 3))

def bitword(i, n=N):
    return format(i, f'0{n}b')

def det_bareiss(matrix):
    """Fraction-free exact integer determinant with row pivoting."""
    a = [list(map(int, row)) for row in matrix]
    n = len(a)
    if n == 0: return 1
    prev, sign = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((j for j in range(k + 1, n) if a[j][k]), None)
            if pivot is None: return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        p = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                num = p * a[i][j] - a[i][k] * a[k][j]
                assert num % prev == 0
                a[i][j] = num // prev
            a[i][k] = 0
        prev = p
    return sign * a[-1][-1]

def tree_count(size, edges, root=0):
    lap = [[0]*size for _ in range(size)]
    indeg, outdeg = [0]*size, [0]*size
    for u, v in edges:
        indeg[v]+=1;outdeg[u]+=1
        lap[u][u] += 1
        lap[u][v] -= 1
    assert indeg == outdeg
    matrix = [[lap[i][j] for j in range(size) if j != root]
              for i in range(size) if i != root]
    return det_bareiss(matrix), Counter(outdeg)

words = [i for i in range(64) if primitive(bitword(i))]
assert len(words) == 54
assert words == sorted(words)
full = [(w >> 1, w & 31) for w in words]
t, degrees = tree_count(32, full)
assert t == 389120, t
assert degrees == Counter({2:22, 1:10}), degrees
assert all(factorial(d-1) == 1 for d in degrees.elements())

half = [w for w in words if w < (w ^ 63)]
assert len(half) == 27
quotient = [(w >> 1, min(w & 31, (w & 31)^31)) for w in half]
qt, qdegrees = tree_count(16, quotient)
assert qt == 320, qt
assert qdegrees == Counter({2:11,1:5}),qdegrees
voltage = sum((w & 31) >= 16 for w in half)
assert voltage == 13
pal = [w for w in words if bitword(w) == bitword(w)[::-1]]
anti = [w for w in words if all(a!=b for a,b in zip(bitword(w),bitword(w)[::-1]))]
assert len(pal)==4 and len(anti)==6
fixed_c, fixed_r, fixed_cr = qt, 0, 0
orbits = (t + fixed_c + fixed_r + fixed_cr)//4
assert (t+fixed_c)%4 == 0 and orbits==97360
assert fixed_c//2==160 and (t-fixed_c)//4==97200
print('VERIFY_OK')
print(f'primitive_edges={len(words)}, spanning_trees={t}, quotient_edges={len(half)}, quotient_trees={qt}')
print(f'quotient_voltage_ones={voltage}, reverse_fixed={fixed_r}, reverse_complement_fixed={fixed_cr}')
print(f'complement_fixed={fixed_c}, symmetry_orbits={orbits}, size_2={fixed_c//2}, size_4={(t-fixed_c)//4}')
