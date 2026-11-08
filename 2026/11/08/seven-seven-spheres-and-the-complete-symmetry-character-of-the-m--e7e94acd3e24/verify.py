"""Exact checks for the Möbius–Kantor dominance complex.

Run with Python 3.9 or newer; only the standard library is required.
Vertex labels are u_i=i and v_i=8+i for i=0,...,7.
"""
from collections import Counter, defaultdict, deque
from math import factorial

N = 16
ADJ = [0] * N

def add_edge(a, b):
    assert a != b
    ADJ[a] |= 1 << b
    ADJ[b] |= 1 << a

for i in range(8):
    add_edge(i, (i + 1) % 8)
    add_edge(i, 8 + i)
    add_edge(8 + i, 8 + (i + 3) % 8)
assert all(z.bit_count() == 3 for z in ADJ)
assert sum(z.bit_count() for z in ADJ) // 2 == 24
# BFS from each vertex verifies connectedness and girth exactly six.
def bfs_girth(root):
    dist = [-1] * N
    parent = [-1] * N
    dist[root] = 0
    queue = deque([root])
    shortest = 999
    while queue:
        x = queue.popleft()
        for y in range(N):
            if not ((ADJ[x] >> y) & 1):
                continue
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                parent[y] = x
                queue.append(y)
            elif parent[x] != y:
                shortest = min(shortest, dist[x] + dist[y] + 1)
    assert all(d >= 0 for d in dist)
    return shortest
assert min(bfs_girth(x) for x in range(N)) == 6
print('GRAPH_CONNECTED_CUBIC_GIRTH6',N,24)
CLOSED = [ADJ[i] | (1 << i) for i in range(N)]
FULL = (1 << N) - 1

def face_by_forbidden(m):
    return all(m & c != c for c in CLOSED)

def face_by_domination(m):
    available = FULL ^ m
    for v in range(N):
        if (available >> v) & 1:
            continue
        if not any(((available >> w) & 1) for w in range(N) if (ADJ[v] >> w) & 1):
            return False
    return True

FACES = {m for m in range(1 << N) if face_by_forbidden(m)}
assert all(face_by_forbidden(m) == face_by_domination(m) for m in range(1 << N))
assert len(FACES) == 32391
DIM = Counter(m.bit_count() - 1 for m in FACES)
assert [DIM[k] for k in range(-1, 12)] == [1, 16, 120, 560, 1804, 4176, 6976, 8208, 6462, 3136, 832, 96, 4]
print('FACES',len(FACES),'FVECTOR',tuple(DIM[k] for k in range(-1,12)))

# Staged coordinate-toggle matching on the augmented face poset.
REST = set(FACES)
PAIRS = {}
STAGE = []
for i in range(N):
    new = [(m, m | (1 << i)) for m in sorted(REST)
           if not ((m >> i) & 1) and (m | (1 << i)) in REST]
    for a, b in new:
        assert a in REST and b in REST and a not in PAIRS
        REST.remove(a)
        REST.remove(b)
        PAIRS[a] = b
    STAGE.append(len(new))
assert STAGE == [13668, 1357, 564, 315, 215, 49, 17, 7, 0, 0, 0, 0, 0, 0, 0, 0]
assert len(REST) == 7 and all(m.bit_count() == 8 for m in REST)
assert PAIRS.pop(0) == 1
CRITICAL = REST | {1}
assert len(PAIRS) == 16191 and len(CRITICAL) == 8
assert Counter(m.bit_count() - 1 for m in CRITICAL) == {0: 1, 7: 7}
NONEMPTY = FACES - {0}
assert set(PAIRS).isdisjoint(CRITICAL)
assert set(PAIRS.values()).isdisjoint(CRITICAL)
assert (set(PAIRS) | set(PAIRS.values()) | CRITICAL) == NONEMPTY
print('MATCHING_STAGE_COUNTS',tuple(STAGE))
print('MATCHED_PAIRS',len(PAIRS),'CRITICAL_7_MASKS',tuple(sorted(REST)))

# Directed Hasse graph: matched edges are oriented low -> high;
# all other covering edges are high -> low. A full topological sort
# proves there is no closed alternating V-path.
IN = {a: 0 for a in NONEMPTY}
OUT = {a: [] for a in NONEMPTY}
COVERS = 0
for a in NONEMPTY:
    for i in range(N):
        if (a >> i) & 1:
            continue
        b = a | (1 << i)
        if b not in NONEMPTY:
            continue
        COVERS += 1
        x, y = (a, b) if PAIRS.get(a) == b else (b, a)
        OUT[x].append(y)
        IN[y] += 1
queue = deque(a for a in NONEMPTY if IN[a] == 0)
seen = 0
while queue:
    a = queue.popleft()
    seen += 1
    for b in OUT[a]:
        IN[b] -= 1
        if IN[b] == 0:
            queue.append(b)
print("ACTUAL_COUNTS",seen,len(NONEMPTY),COVERS)
assert seen == len(NONEMPTY) and COVERS == 218672
print('ACYCYCLIC_TOPOLOGICAL_SORT',seen,'COVERS',COVERS)

# Completely independent augmented simplicial boundary reductions over F_2.
BYDIM = defaultdict(list)
for a in FACES:
    BYDIM[a.bit_count() - 1].append(a)
RANK = {}
for d in range(12):
    row = {a: i for i, a in enumerate(BYDIM[d-1])}
    pivots = {}
    for a in BYDIM[d]:
        column = 0
        rem = a
        while rem:
            bit = rem & -rem
            rem -= bit
            column ^= 1 << row[a ^ bit]
        while column:
            lead = column.bit_length() - 1
            if lead in pivots:
                column ^= pivots[lead]
            else:
                pivots[lead] = column
                break
    RANK[d] = len(pivots)
assert [RANK[k] for k in range(12)] == [1, 15, 105, 455, 1349, 2827, 4149, 4059, 2396, 740, 92, 4]
BETTI = {d: len(BYDIM[d]) - RANK[d] - RANK.get(d+1, 0) for d in range(12)}
assert {d: v for d, v in BETTI.items() if v} == {7: 7}
print('MOD2_BOUNDARY_RANKS',tuple(RANK[d] for d in range(12)))
print('REDUCED_BETTI_MOD2',tuple(BETTI[d] for d in range(12)))

# Exhaust all graph automorphisms via backtracking that tests adjacency
# and nonadjacency of every new image against every already placed image.
def all_automorphisms():
    complete = []
    def search(mapped, used):
        if len(mapped) == N:
            complete.append(tuple(mapped[i] for i in range(N)))
            return
        best = None
        for x in range(N):
            if x in mapped:
                continue
            choices = [y for y in range(N) if not ((used >> y) & 1)
                       and all(bool((ADJ[x] >> v) & 1) == bool((ADJ[y] >> w) & 1)
                               for v, w in mapped.items())]
            priority = (-sum((ADJ[x] >> v) & 1 for v in mapped), len(choices), x)
            if best is None or priority < best[0]:
                best = (priority, x, choices)
        _, x, choices = best
        for y in choices:
            mapped[x] = y
            search(mapped, used | (1 << y))
            del mapped[x]
    search({}, 0)
    return sorted(complete)

AUT = all_automorphisms()
assert len(AUT) == 96 and len(set(AUT)) == 96
IDENTITY = tuple(range(N))
assert IDENTITY in AUT
A_SET = set(AUT)
def multiply(a, b):
    return tuple(a[b[i]] for i in range(N))
def inverse(a):
    return tuple(a.index(i) for i in range(N))
assert all(inverse(a) in A_SET for a in AUT)
assert all(multiply(a, b) in A_SET for a in AUT for b in AUT)
assert all(((ADJ[i] >> j) & 1) == ((ADJ[p[i]] >> p[j]) & 1)
           for p in AUT for i in range(N) for j in range(N))
print('AUTOMORPHISMS_EXHAUSTIVE',len(AUT))

def cycle_type(p):
    visited = set()
    parts = []
    for i in range(N):
        if i in visited:
            continue
        j = i
        length = 0
        while j not in visited:
            visited.add(j)
            length += 1
            j = p[j]
        parts.append(length)
    return tuple(sorted(parts, reverse=True))

def parity(seq):
    return 1 - 2 * (sum(seq[i] > seq[j]
                        for i in range(len(seq)) for j in range(i+1, len(seq))) % 2)

# Reduced Hopf trace, including the -1 augmentation trace in degree -1.
# Since the Morse proof gives only Htilde_7, its character is minus
# the reduced alternating fixed-chain trace.
TRACE = {}
for p in AUT:
    lef = -1
    for m in NONEMPTY:
        vertices = [i for i in range(N) if (m >> i) & 1]
        images = [p[v] for v in vertices]
        if sum(1 << j for j in images) == m:
            lef += (-1 if len(vertices) % 2 == 0 else 1) * parity(images)
    TRACE[p] = -lef
assert TRACE[IDENTITY] == 7
assert sum(TRACE.values()) == 0
assert sum(x*x for x in TRACE.values()) == 4 * len(AUT)

classes = []
unvisited = set(AUT)
INV = {p: inverse(p) for p in AUT}
while unvisited:
    a = min(unvisited)
    conj = {multiply(multiply(h, a), INV[h]) for h in AUT}
    assert conj <= unvisited
    assert len({TRACE[x] for x in conj}) == 1
    rep = min(conj)
    classes.append((len(conj), cycle_type(rep), TRACE[rep], rep))
    unvisited -= conj
classes.sort(key=lambda r: (r[0],r[1],r[2],r[3]))
assert len(classes) == 13
assert sorted((s, c) for s, _, c, _ in classes) == sorted([
    (1,7),(1,7),(2,-1),(6,3),(6,3),(8,1),(8,1),
    (8,-1),(8,-1),(12,-3),(12,1),(12,-1),(12,-1)
])
assert sum(size for size,*_ in classes) == 96
print('CONJUGACY_CLASSES',len(classes))
for size, typ, character, rep in classes:
    print('CLASS',size,','.join(map(str, typ)),character,','.join(map(str, rep)))
print('INVARIANT_DIMENSION',sum(TRACE.values())//len(AUT))
print('CHARACTER_INNER_PRODUCT',sum(x*x for x in TRACE.values())//len(AUT))
print('MOBIUS_KANTOR_DOMINANCE_CERTIFICATE_PASS')
