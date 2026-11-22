"""Exact, standard-library verification of the Steiner trihedral-pair lattice.
Usage: python3 verify.py (from the directory containing smith_ops.json).
"""
from itertools import combinations
from collections import Counter
from math import gcd, lcm
from pathlib import Path
import json

E = [('E', i) for i in range(6)]
L = [('L', i, j) for i in range(6) for j in range(i+1, 6)]
Q = [('Q', i) for i in range(6)]
lines = E + L + Q
assert len(lines) == 27 and len(set(lines)) == 27

tritangents = []
for i in range(6):
    for j in range(6):
        if i != j:
            tritangents.append(frozenset((('E', i), ('L', *sorted((i,j))), ('Q', j))))
for x, y, z in combinations(L, 3):
    if len(set(x[1:] + y[1:] + z[1:])) == 6:
        tritangents.append(frozenset((x,y,z)))
tritangents.sort(key=lambda tri: tuple(sorted(tri)))
assert len(tritangents) == len(set(tritangents)) == 45
assert Counter(u for T in tritangents for u in T) == Counter({u:5 for u in lines})

# Rows of a Steiner trihedron are disjoint tritangents; its conjugate
# columns intersect every row in precisely one common surface line.
triads = [a for a in combinations(range(45),3)
          if len(set().union(*(tritangents[i] for i in a))) == 9]
assert len(triads) == 5280
pairs = set()
for a in triads:
    conjugate = [i for i in range(45)
                 if all(len(tritangents[i] & tritangents[j]) == 1 for j in a)]
    for b in combinations(conjugate, 3):
        if len(set().union(*(tritangents[i] for i in b))) == 9:
            pairs.add(tuple(sorted((tuple(a), tuple(b)))))
assert len(pairs) == 120
supports = sorted(tuple(sorted(a+b)) for a,b in pairs)
assert len(set(supports)) == 120
for a,b in pairs:
    assert len(set(a+b)) == 6
    assert all(not tritangents[x] & tritangents[y] for x,y in combinations(a,2))
    assert all(not tritangents[x] & tritangents[y] for x,y in combinations(b,2))
    assert all(len(tritangents[x] & tritangents[y]) == 1 for x in a for y in b)
    assert len(set().union(*(tritangents[i] for i in a+b))) == 9

# Unsigned incidence of 45 planes against 120 unordered pairs.
M = [[int(i in p) for p in supports] for i in range(45)]
assert all(sum(M[i][j] for i in range(45)) == 6 for j in range(120))
assert all(sum(M[i]) == 16 for i in range(45))
gram = [[sum(M[i][k]*M[j][k] for k in range(120)) for j in range(45)]
        for i in range(45)]
assert all(gram[i][i] == 16 for i in range(45))
assert Counter(gram[i][j] for i in range(45) for j in range(i+1,45)) == {1:720,4:270}

# Replay a certificate of elementary unimodular operations. Every listed
# operation is an integral row/column swap, signed row, or shear.
A = [row[:] for row in M]
U = [[int(i == j) for j in range(45)] for i in range(45)]
ops = json.loads(Path(__file__).with_name('smith_ops.json').read_text('utf-8'))
assert len(ops) == 2710
for op in ops:
    code, i, *args = op
    if code == 'rs':
        j = args[0]
        assert 0 <= i < 45 and 0 <= j < 45
        A[i],A[j] = A[j],A[i]
        U[i],U[j] = U[j],U[i]
    elif code == 'cs':
        j = args[0]
        assert 0 <= i < 120 and 0 <= j < 120
        for row in A: row[i],row[j] = row[j],row[i]
    elif code == 'ra':
        j,k = args
        assert 0 <= i < 45 and 0 <= j < 45 and i != j
        A[i] = [x+k*y for x,y in zip(A[i],A[j])]
        U[i] = [x+k*y for x,y in zip(U[i],U[j])]
    elif code == 'ca':
        j,k = args
        assert 0 <= i < 120 and 0 <= j < 120 and i != j
        for row in A: row[i] += k*row[j]
    elif code == 'rn':
        assert not args and 0 <= i < 45
        A[i] = [-x for x in A[i]]
        U[i] = [-x for x in U[i]]
    else: raise ValueError('Unknown certificate operation')
D = [1]*24 + [2]*20 + [12]
assert A == [[(D[i] if i == j else 0) for j in range(120)] for i in range(45)]
# Under the row operations, e_i goes to column i of U. Its order is
# the lcm of d_j / gcd(d_j, U_{j,i}).
orders = [lcm(*(d // gcd(d,U[j][i]) for j,d in enumerate(D))) for i in range(45)]
assert orders == [12]*45
print('VERIFIED: 27 lines; 45 planes; 120 pairs; 2710 unimodular steps')
print('SMITH: 1^24 2^20 12^1; quotient order 12582912; each point order 12')
