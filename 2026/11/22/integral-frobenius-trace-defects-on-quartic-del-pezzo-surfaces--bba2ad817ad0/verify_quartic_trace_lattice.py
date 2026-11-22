"""Exact quartic del Pezzo exceptional-curve trace lattice computation.

Python 3 standard library only.  With no arguments prints a CSV certificate.
All calculations use integer arithmetic; no floating-point or finite-field sampling.
"""
import csv
import itertools
import math
import sys
from collections import deque, Counter
from fractions import Fraction

N = 6
DIAG = (1, -1, -1, -1, -1, -1)
EYE = tuple(tuple(int(i == j) for j in range(N)) for i in range(N))


def mm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(N))
                       for j in range(N)) for i in range(N))


def mv(A, v):
    return tuple(sum(A[i][j] * v[j] for j in range(N)) for i in range(N))


def pairing(a, b):
    return sum(a[i] * DIAG[i] * b[i] for i in range(N))


def reflect(root):
    return tuple(tuple(EYE[i][j] + root[i] * root[j] * DIAG[j]
                       for j in range(N)) for i in range(N))


def perm_compose(a, b):
    return tuple(a[b[i]] for i in range(16))


def perm_inverse(a):
    b = [None] * 16
    for i, x in enumerate(a):
        b[x] = i
    return tuple(b)


def orbit_cycles(p):
    seen = set()
    result = []
    for j in range(16):
        if j not in seen:
            c = []
            x = j
            while x not in seen:
                seen.add(x)
                c.append(x)
                x = p[x]
            assert x == j
            result.append(c)
    return result


def matrix_rank(A):
    if not A or not A[0]:
        return 0
    B = [[Fraction(x) for x in row] for row in A]
    m, n = len(B), len(B[0])
    r = 0
    for j in range(n):
        pivot = next((i for i in range(r, m) if B[i][j]), None)
        if pivot is None:
            continue
        B[r], B[pivot] = B[pivot], B[r]
        z = B[r][j]
        B[r] = [v / z for v in B[r]]
        for i in range(r + 1, m):
            z = B[i][j]
            if z:
                B[i] = [u - z * v for u, v in zip(B[i], B[r])]
        r += 1
        if r == m:
            break
    return r


def determinant(B):
    n = len(B)
    if n == 0:
        return 1
    a = [list(row) for row in B]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            i = next((i for i in range(k+1,n) if a[i][k]), None)
            if i is None:
                return 0
            a[k], a[i] = a[i], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num = a[i][j] * p - a[i][k] * a[k][j]
                assert num % prev == 0
                a[i][j] = num // prev
        for i in range(k+1,n):
            a[i][k] = 0
        prev = p
    return sign * a[-1][-1]


def saturation_index(A, rank):
    # gcd of all rank-by-rank minors equals index in rational saturation.
    if rank == 0:
        return 1
    k = len(A[0])
    g = 0
    for rows in itertools.combinations(range(6), rank):
        for cols in itertools.combinations(range(k), rank):
            val = abs(determinant([[A[i][j] for j in cols] for i in rows]))
            g = math.gcd(g, val)
            if g == 1:
                return 1
    assert g > 0
    return g


def main():
    C = []
    for j in range(1, 6):
        C.append(tuple(int(i == j) for i in range(6)))
    for j, k in itertools.combinations(range(1, 6), 2):
        C.append(tuple(1 if i == 0 else -1 if i in (j, k) else 0 for i in range(6)))
    C.append((2, -1, -1, -1, -1, -1))
    assert len(C) == 16 and len(set(C)) == 16
    K = (-3, 1, 1, 1, 1, 1)
    assert all(pairing(c, c) == -1 and pairing(c, K) == -1 for c in C)
    roots = [(1, -1, -1, -1, 0, 0)]
    for j in range(1, 5):
        roots.append(tuple(1 if i == j else -1 if i == j + 1 else 0 for i in range(6)))
    assert all(pairing(r,r) == -2 and pairing(r,K) == 0 for r in roots)
    gens = [reflect(r) for r in roots]
    for M in gens:
        assert mv(M, K) == K
        assert all(pairing(mv(M, a), mv(M, b)) == pairing(a,b) for a in C for b in C)
    pos = {c:i for i,c in enumerate(C)}
    genp = [tuple(pos[mv(g,c)] for c in C) for g in gens]
    I = tuple(range(16))
    group = {I:(EYE, ())}
    todo = deque([I])
    while todo:
        p = todo.popleft()
        M, word = group[p]
        for j, (gp, gm) in enumerate(zip(genp, gens)):
            z = perm_compose(gp, p)
            if z not in group:
                group[z] = (mm(gm,M), word + (j,))
                todo.append(z)
    assert len(group) == 1920
    rem = set(group)
    classes = []
    while rem:
        p = min(rem)
        conj = {p}
        stack = [p]
        while stack:
            v = stack.pop()
            for gp in genp:
                x = perm_compose(perm_compose(gp, v), perm_inverse(gp))
                if x not in conj:
                    conj.add(x)
                    stack.append(x)
        assert conj <= rem
        rem.difference_update(conj)
        classes.append((p, len(conj)))
    assert len(classes) == 18
    assert sum(n for _, n in classes) == 1920
    data = []
    for p, cardinal in classes:
        M, word = group[p]
        orbs = orbit_cycles(p)
        A = [[sum(C[j][i] for j in orb) for orb in orbs] for i in range(6)]
        r = matrix_rank(A)
        assert r == 6 - matrix_rank([[M[i][j] - EYE[i][j] for j in range(6)] for i in range(6)])
        idx = saturation_index(A, r)
        sizes = sorted(map(len, orbs))
        order = math.lcm(*sizes)
        data.append(dict(class_size=cardinal, order=order, invariant_rank=r,
                         line_orbits='.'.join(map(str, sizes)), index=idx,
                         reflection_word=''.join(str(j+1) for j in word) or 'identity'))
    data.sort(key=lambda a:(a['order'],a['invariant_rank'],a['line_orbits'],a['index'],a['class_size'],a['reflection_word']))
    assert sorted(x['index'] for x in data) == [1]*12+[2]*3+[4]*2+[16]
    quarter = [x for x in data if x['order'] == 4 and x['line_orbits'] == '4.4.4.4']
    assert len(quarter) == 4 and sorted(x['index'] for x in quarter) == [1,2,4,16]
    writer = csv.DictWriter(sys.stdout, fieldnames=list(data[0].keys()), lineterminator='\n')
    writer.writeheader()
    writer.writerows(data)
    print('EXACT_CERTIFICATE group=1920 classes=18 nonunit=6 max_index=16 same_line_orbits_indices=1,2,4,16', file=sys.stderr)


if __name__ == '__main__':
    main()
