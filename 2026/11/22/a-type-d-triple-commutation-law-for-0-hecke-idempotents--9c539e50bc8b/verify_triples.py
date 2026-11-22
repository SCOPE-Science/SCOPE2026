"""Exact certificate for commuting triples of finite type A and D 0-Hecke idempotents.

Pure Python 3; run: python3 verify_triples.py
"""
from itertools import combinations

PAIRS = ((0, 1), (0, 2), (1, 2))


def projection(colour):
    return tuple(((colour >> a) & 1) | (((colour >> b) & 1) << 1)
                 for a, b in PAIRS)


def attach(colour, children):
    """Root component intersections after attaching rooted children."""
    ans = list(projection(colour))
    for child in children:
        for j in range(3):
            if ans[j] and child[j]:
                ans[j] &= child[j]
                if not ans[j]:
                    return None
    return tuple(ans)


def dot(a, b):
    return sum(x*y for x,y in zip(a,b))


def mat_vec(M, v):
    return [dot(row,v) for row in M]


def row_mat(r, M):
    return [sum(r[i]*M[i][j] for i in range(len(r))) for j in range(len(r))]


def add_vectors(*vv):
    return [sum(v[i] for v in vv) for i in range(len(vv[0]))]


def scale(k, v):
    return [k*x for x in v]


leaf = {projection(b) for b in range(8)}
states = set(leaf)
while True:
    next_states = set(states)
    for child in states:
        for colour in range(8):
            result = attach(colour, [child])
            if result is not None:
                next_states.add(result)
    if next_states == states:
        break
    states = next_states
states = sorted(states)
assert len(states) == 17, len(states)
where = {s: i for i,s in enumerate(states)}
N = len(states)
T = [[0]*N for _ in range(N)]
a_leaf = [0]*N
for b in range(8):
    a_leaf[where[projection(b)]] += 1
for j, child in enumerate(states):
    for b in range(8):
        s = attach(b, [child])
        if s is not None:
            T[where[s]][j] += 1
h = [0]*N
for c1 in range(8):
    for c2 in range(8):
        for b in range(8):
            s = attach(b, [projection(c1), projection(c2)])
            if s is not None:
                assert s in where
                h[where[s]] += 1

# Row certificate valid on the full 17-state space:
# u (T^4 - 8 T^3 + 16 T^2 - 12 T + 2 I) = 0.
u = [1]*N
r0 = u
r1 = row_mat(r0, T)
r2 = row_mat(r1, T)
r3 = row_mat(r2, T)
r4 = row_mat(r3, T)
assert add_vectors(r4,scale(-8,r3),scale(16,r2),scale(-12,r1),scale(2,r0)) == [0]*N

# A_n for n >= 1; hub with two leaves starts the type-D spine at 3 vertices.
A = [1]
D = [None]*3
v = a_leaf
w = h
for n in range(1,24):
    A.append(sum(v))
    v = mat_vec(T,v)
for n in range(3,24):
    D.append(sum(w))
    w = mat_vec(T,w)
assert A[0:8] == [1, 8, 46, 254, 1390, 7592, 41452, 226316]
assert [D[n] for n in range(3,9)] == [254, 1420, 7778, 42496, 232052, 1266976]
for seq, start in ((A,0),(D,3)):
    for n in range(start,20):
        assert seq[n+4] == 8*seq[n+3]-16*seq[n+2]+12*seq[n+1]-2*seq[n]
assert [D[n]-A[n] for n in range(4,10)] == [30,186,1044,5736,31356,171228]

# The two generating-function numerators are determined exactly by four
# coefficients and the common fourth-order recurrence.
def numerator(coefficients):
    a,b,c,d = coefficients
    return [a,b-8*a,c-8*b+16*a,d-8*c+16*b-12*a]
assert numerator([D[n] for n in range(4,8)]) == [1420,-3582,2992,-508]
assert numerator([D[n]-A[n] for n in range(4,8)]) == [30,-54,36,0]

# Independent direct subset enumeration using connected components and
# the component-nesting/orthogonality criterion, not the transfer states.
def components(mask, n, edges):
    adjacency = [set() for _ in range(n)]
    for x,y in edges:
        adjacency[x].add(y)
        adjacency[y].add(x)
    remain = {v for v in range(n) if (mask>>v)&1}
    parts = []
    while remain:
        initial = remain.pop()
        block = {initial}
        pending = [initial]
        while pending:
            x = pending.pop()
            for y in adjacency[x] & remain:
                remain.remove(y)
                block.add(y)
                pending.append(y)
        parts.append(block)
    return parts


def pair_ok(a, b, n, edges):
    C = components(a,n,edges)
    E = components(b,n,edges)
    e = {frozenset(x) for x in edges}
    for c in C:
        for d in E:
            if c <= d or d <= c:
                continue
            if not c.isdisjoint(d):
                return False
            if any(frozenset((x,y)) in e for x in c for y in d):
                return False
    return True


def direct_counts(n, edges):
    subsets = list(range(1<<n))
    ok = [[pair_ok(a,b,n,edges) for b in subsets] for a in subsets]
    twos = sum(sum(row) for row in ok)
    threes = sum(1 for a in subsets for b in subsets if ok[a][b]
                   for c in subsets if ok[a][c] and ok[b][c])
    return twos, threes

for n in range(2,7):
    E = [(i,i+1) for i in range(n-1)]
    twos, threes = direct_counts(n,E)
    assert threes == A[n]
    assert twos == [1,4,14,48,164,560,1912][n]
for n in range(4,7):
    # spine: vertices 0,...,n-3; trivalent hub n-3; leaves n-2,n-1
    E = [(i,i+1) for i in range(n-3)] + [(n-3,n-2),(n-3,n-1)]
    twos, threes = direct_counts(n,E)
    assert threes == D[n]
    assert twos == [1,4,14,48,164,560,1912][n]

# The equations alone do not certify priority or newness.
print('HECKE_TYPE_D_TRIPLE_CERTIFICATE_OK')
print('A:', A[1:9])
print('D:', [D[n] for n in range(4,10)])
print('gap:', [D[n]-A[n] for n in range(4,10)])
