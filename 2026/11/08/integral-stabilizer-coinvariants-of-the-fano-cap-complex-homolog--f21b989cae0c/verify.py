"""Exact integral chain and subgroup-coinvariant certificate for the Fano cap complex.

Python 3 standard library only. All matrices and coefficients are exact integers,
except for the temporary rational Gaussian elimination of a unimodular matrix.
"""
from fractions import Fraction
from itertools import combinations, product

V = tuple(range(1, 8))
LINES = {frozenset((a, b, a ^ b)) for a, b in combinations(V, 2)}
TRI = list(combinations(V, 3))
TRI = [t for t in TRI if frozenset(t) not in LINES]
CAPS = [c for c in combinations(V, 4)
        if all(frozenset(t) not in LINES for t in combinations(c, 3))]
CHORDS = [e for e in combinations(V, 2) if 1 not in e]
EI = {e: i for i, e in enumerate(CHORDS)}
TI = {t: i for i, t in enumerate(TRI)}
assert (len(LINES), len(TRI), len(CAPS), len(CHORDS)) == (7, 28, 7, 15)

B = [[0] * 28 for _ in range(15)]
for j, (a, b, c) in enumerate(TRI):
    for edge, sign in [((b, c), 1), ((a, c), -1), ((a, b), 1)]:
        if edge in EI:
            B[EI[edge]][j] += sign

PIVOTS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 19]
FREE = [j for j in range(28) if j not in PIVOTS]

# Calculate the inverse of the 15-by-15 chord-boundary minor.
T = [[Fraction(B[i][PIVOTS[j]]) for j in range(15)] +
     [Fraction(i == j) for j in range(15)] for i in range(15)]
for col in range(15):
    pivot = next(i for i in range(col, 15) if T[i][col])
    T[col], T[pivot] = T[pivot], T[col]
    v = T[col][col]
    T[col] = [x / v for x in T[col]]
    for i in range(15):
        if i != col and T[i][col]:
            v = T[i][col]
            T[i] = [x - v*y for x, y in zip(T[i], T[col])]
assert all(T[i][j] == (i == j) for i in range(15) for j in range(15))
INV = [[T[i][15+j] for j in range(15)] for i in range(15)]
# The pivot minor is unimodular: its inverse is integral.
assert all(x.denominator == 1 for row in INV for x in row)
KERNEL = []
for j in FREE:
    c = [0] * 28
    c[j] = 1
    for i, p in enumerate(PIVOTS):
        c[p] = -int(sum(INV[i][k] * B[k][j] for k in range(15)))
    assert all(sum(B[k][q] * c[q] for q in range(28)) == 0 for k in range(15))
    KERNEL.append(c)
assert len(KERNEL) == 13

# 7 tetrahedral boundaries form an integral direct summand in cycle space.
D = [[0] * 7 for _ in range(13)]
for j, cap in enumerate(CAPS):
    for t in range(4):
        face = cap[:t] + cap[t+1:]
        index = TI[face]
        if index in FREE:
            D[FREE.index(index)][j] += (-1)**t
REMOVE = [next(i for i in range(13) if D[i][j]) for j in range(7)]
assert len(set(REMOVE)) == 7
assert all(sum(int(D[i][j] != 0) for j in range(7)) <= 1 for i in range(13))
KEEP = [i for i in range(13) if i not in REMOVE]
assert len(KEEP) == 6

def project(c):
    assert all(sum(B[k][j] * c[j] for j in range(28)) == 0 for k in range(15))
    v = [c[j] for j in FREE]
    for j, i in enumerate(REMOVE):
        assert abs(D[i][j]) == 1
        factor = v[i] // D[i][j]
        v = [v[k] - factor * D[k][j] for k in range(13)]
    assert all(v[i] == 0 for i in REMOVE)
    return [v[i] for i in KEEP]

# Explicit GL(3,2) enumeration by images of ordered binary basis vectors.
G = []
for a, b, c in product(V, repeat=3):
    if len({a, b, c}) == 3 and a ^ b != c:
        G.append(tuple((a if (i & 1) else 0) ^
                       (b if (i & 2) else 0) ^
                       (c if (i & 4) else 0) for i in V))
assert len(G) == len(set(G)) == 168
IDENT = tuple(V)
assert IDENT == G[0]
def compose(a, b):
    return tuple(a[b[x-1]-1] for x in V)
def order(a):
    x = a
    k = 1
    while x != IDENT:
        x = compose(a, x)
        k += 1
        assert k <= 168
    return k

# Build all integral 6-by-6 homology matrices from signed chain action.
ACTIONS = []
for g in G:
    assert {frozenset(g[x-1] for x in L) for L in LINES} == LINES
    cols = []
    for idx in KEEP:
        cycle = KERNEL[idx]
        image = [0] * 28
        for j, face in enumerate(TRI):
            if not cycle[j]:
                continue
            perm = [g[x-1] for x in face]
            swaps = sum(perm[a] > perm[b] for a in range(3) for b in range(a+1,3))
            image[TI[tuple(sorted(perm))]] += cycle[j] * (-1 if swaps & 1 else 1)
        cols.append(project(image))
    mat = [[cols[j][i] for j in range(6)] for i in range(6)]
    ACTIONS.append(mat)

def determinant(m):
    """Fraction-free Bareiss determinant, allowing row swaps."""
    a = [list(row) for row in m]
    n = len(a)
    prev = 1
    sign = 1
    for k in range(n-1):
        if a[k][k] == 0:
            i = next((i for i in range(k+1, n) if a[i][k]), None)
            if i is None:
                return 0
            a[k], a[i] = a[i], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = a[i][j]*pivot - a[i][k]*a[k][j]
                assert numerator % prev == 0
                a[i][j] = numerator//prev
        for i in range(k+1, n):
            a[i][k] = 0
        prev = pivot
    return sign*a[-1][-1]

assert all(abs(determinant(a)) == 1 for a in ACTIONS)
assert all(ACTIONS[0][i][j] == (i == j) for i in range(6) for j in range(6))
CHARACTER = {}
for g, mat in zip(G, ACTIONS):
    trace = sum(mat[i][i] for i in range(6))
    CHARACTER.setdefault(order(g), set()).add(trace)
assert CHARACTER == {1: {6}, 2: {-2}, 3: {0}, 4: {2}, 7: {-1}}

# Check the integral group action law on all 168^2 pairs.
IX = {g: i for i, g in enumerate(G)}
def mul6(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(6))
             for j in range(6)] for i in range(6)]
for i, g in enumerate(G):
    for j, h in enumerate(G):
        assert mul6(ACTIONS[i], ACTIONS[j]) == ACTIONS[IX[compose(g, h)]]

r = next(g for g in G if order(g) == 7)
C7 = {IDENT}
x = IDENT
for _ in range(6):
    x = compose(x, r)
    C7.add(x)
assert len(C7) == 7
N = {g for g in G if compose(compose(g, r),
       next(h for h in G if compose(g, h) == IDENT)) in C7}
POINT = {g for g in G if g[0] == 1}
LINE = {g for g in G if {g[x-1] for x in (1, 2, 3)} == {1, 2, 3}}
assert (len(POINT), len(LINE), len(N)) == (24, 24, 21)

# The following explicit column selections certify the index of the
# subgroup relation lattice.  (group_index, homology_coordinate_index)
WITNESSES = {
    'point': (POINT, 2, [(18,0),(14,3),(11,2),(16,0),(3,4),(16,2)]),
    'line': (LINE, 2, [(28,2),(49,4),(52,0),(54,4),(53,5),(29,2)]),
    'singer': (C7, 7, [(160,2),(143,5),(67,0),(67,2),(33,3),(143,1)]),
    'normalizer': (N, 1, [(104,3),(158,5),(137,2),(68,4),(85,0),(46,0)]),
    'full': (set(G), 1, [(116,3),(117,2),(142,5),(92,2),(4,4),(85,4)])
}
def relation(i, j):
    return [ACTIONS[i][k][j] - int(k == j) for k in range(6)]
def rank_mod_prime(cols, p):
    a = [[x % p for x in col] for col in cols]
    r = 0
    for col in range(6):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][col], -1, p)
        a[r] = [(x*inv)%p for x in a[r]]
        for i in range(r+1, len(a)):
            c = a[i][col]
            if c:
                a[i] = [(x-c*y)%p for x,y in zip(a[i], a[r])]
        r += 1
        if r == 6:
            break
    return r

for name, (subset, expected_absdet, witness) in WITNESSES.items():
    assert all(G[i] in subset for i,j in witness)
    cols = [relation(i,j) for i,j in witness]
    d = determinant([[cols[j][i] for j in range(6)] for i in range(6)])
    assert abs(d) == expected_absdet, (name, d)
    all_cols = [relation(i,j) for i,g in enumerate(G) if g in subset for j in range(6)]
    if expected_absdet == 2:
        assert rank_mod_prime(all_cols, 2) == 5
    elif expected_absdet == 7:
        assert rank_mod_prime(all_cols, 7) == 5
    print(f'{name}: group_size={len(subset)}, witness_det={d}, '
          f'coinvariants={"Z/"+str(expected_absdet) if expected_absdet>1 else "0"}')
print('Fano: faces=(7,21,28,7), H2=Z^6, GL3(2)=168')
print('VERIFY_OK')
