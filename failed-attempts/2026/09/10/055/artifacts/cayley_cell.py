"""Cayley cell census for Gamma = Z^2 * C2 with S={a,a^-1,b,b^-1,c}.

Normal form: element = tuple of Z^2 blocks (B0..Bk), k = number of c's,
representing B0 c B1 c ... c Bk. Interior blocks (1..k-1) are nonzero.
Right multiplication by A-generators adds to last block; by c appends a
zero block then reduces (c 0 c merges neighbours).
Stdlib only. Writes cell_census.json next to this script.
"""
import json
from collections import deque

A = (0, 0)

def mul_A(T, dm, dn):
    L = list(T)
    L[-1] = (L[-1][0] + dm, L[-1][1] + dn)
    return tuple(L)

def reduce_blocks(L):
    L = list(L)
    while len(L) >= 3:
        hit = -1
        for i in range(1, len(L) - 1):
            if L[i] == (0, 0):
                hit = i
                break
        if hit < 0:
            break
        L = (L[:hit - 1]
             + [(L[hit - 1][0] + L[hit + 1][0], L[hit - 1][1] + L[hit + 1][1])]
             + L[hit + 2:])
    return tuple(L)

def mul_c(T):
    return reduce_blocks(list(T) + [(0, 0)])

E = ((0, 0),)
GENS = {
    'a': ('A', 1, 0), 'ai': ('A', -1, 0),
    'b': ('A', 0, 1), 'bi': ('A', 0, -1),
    'c': ('C',),
}
INV = {'a': 'ai', 'ai': 'a', 'b': 'bi', 'bi': 'b', 'c': 'c'}
SYMS = ['a', 'ai', 'b', 'bi', 'c']

def apply(T, g):
    s = GENS[g]
    if s[0] == 'A':
        return mul_A(T, s[1], s[2])
    return mul_c(T)

def psi(T):
    return (sum(m + n for (m, n) in T) + (len(T) - 1)) % 2

# sanity: relations
assert apply(apply(E, 'a'), 'ai') == E
assert apply(apply(E, 'b'), 'bi') == E
assert apply(apply(E, 'c'), 'c') == E
t = E
for g in ['a', 'b', 'ai', 'bi']:
    t = apply(t, g)
assert t == E, "commutator [a,b] must be trivial"
assert apply(E, 'a') != E and apply(E, 'c') != E
assert apply(E, 'a') != apply(E, 'ai')

RMAX = 6
dist = {E: 0}
q = deque([E])
while q:
    g = q.popleft()
    if dist[g] >= RMAX:
        continue
    for s in SYMS:
        h = apply(g, s)
        if h not in dist:
            dist[h] = dist[g] + 1
            q.append(h)

balls = {}
for R in range(RMAX + 1):
    balls[R] = sum(1 for d in dist.values() if d <= R)

# edges inside full enumerated ball; bipartition check
verts = set(dist)
edges = set()
bip_ok = True
for g in verts:
    for s in SYMS:
        h = apply(g, s)
        if h in verts:
            e = (g, h) if g <= h else (h, g)
            edges.add(e)
            if psi(g) == psi(h):
                bip_ok = False
# degree check at identity (all 5 neighbours distinct, inside ball)
nbrs_e = {apply(E, s) for s in SYMS}
assert len(nbrs_e) == 5

# adjacency for walk counts
adj = {g: [] for g in verts}
for (g, h) in edges:
    adj[g].append(h)
    adj[h].append(g)

# closed-walk counts at e, lengths 0..6 (all walks + non-backtracking)
# NB state: (vertex, index of generator used to arrive); start: (e, None)
def count_closed(Lmax):
    from collections import defaultdict
    cur = defaultdict(int)
    cur[(E, None)] = 1
    out_all = {0: 1}
    # all-walk DP
    aw = {E: 1}
    all_closed = {0: 1}
    for k in range(1, Lmax + 1):
        nxt = defaultdict(int)
        for v, c in list(aw.items()):
            for w in adj[v]:
                nxt[w] += c
        aw = nxt
        all_closed[k] = aw.get(E, 0)
    nb_closed = {}
    for k in range(1, Lmax + 1):
        nxt = defaultdict(int)
        for (v, gi), c in cur.items():
            for idx, s in enumerate(SYMS):
                if gi is not None and s == INV[SYMS[gi]]:
                    continue
                w = apply(v, s)
                if w in adj and w in adj[v]:
                    nxt[(w, idx)] += c
        cur = nxt
        nb_closed[k] = sum(c for (v, gi), c in cur.items() if v == E)
    return all_closed, nb_closed

all_closed, nb_closed = count_closed(6)

# distinct 4-cycles through e via pairs of length-2 NB paths
paths2 = {}
for i, s1 in enumerate(SYMS):
    m = apply(E, s1)
    for j, s2 in enumerate(SYMS):
        if s2 == INV[s1]:
            continue
        v = apply(m, s2)
        paths2.setdefault(v, []).append((s1, s2))
squares = []
for v, ps in paths2.items():
    if v == E:
        continue
    for x in range(len(ps)):
        for y in range(x + 1, len(ps)):
            squares.append({'apex': list(v), 'p1': ps[x], 'p2': ps[y]})
# dedupe squares by node set
seen = set()
uniq_sq = []
for sq in squares:
    m1 = tuple(sorted([tuple(apply(E, sq['p1'][0])), ]))
    nodes = tuple(sorted([repr(E), repr(apply(E, sq['p1'][0])),
                          repr(sq['apex']), repr(apply(E, sq['p2'][0]))]))
    if nodes not in seen:
        seen.add(nodes)
        uniq_sq.append(sq)

# F2 embedding: u=a, v=cac ; check reduced words up to length 8 != e
u = apply(E, 'a')
v = apply(apply(apply(E, 'c'), 'a'), 'c')
def grp_mul(T, U):
    # multiply T by group element U via block-concat + reduce is wrong in
    # general; instead decompose U into generators once (BFS word) and apply.
    raise AssertionError("unused")
# build generator-words for u,v then BFS over {u,ui,v,vi} words
UWORDS = {'u': ['a'], 'ui': ['ai'], 'v': ['c', 'a', 'c'],
          'vi': ['c', 'ai', 'c']}
INVU = {'u': 'ui', 'ui': 'u', 'v': 'vi', 'vi': 'v'}
WL = 8
bad = []
count = 0
def words(prefix, last):
    global count
    if prefix:
        T = E
        for w in prefix:
            for g in UWORDS[w]:
                T = apply(T, g)
        count += 1
        if T == E:
            bad.append(list(prefix))
    if len(prefix) == WL:
        return
    for w in UWORDS:
        if last is not None and w == INVU[last]:
            continue
        words(prefix + [w], w)
words([], None)

out = {
    'RMAX': RMAX,
    'ball_sizes': balls,
    'n_vertices_R6': len(verts),
    'n_edges_R6': len(edges),
    'bipartition_psi_ok_on_ball': bip_ok,
    'degree_at_e': len(nbrs_e),
    'closed_walks_at_e': all_closed,
    'closed_nonbacktracking_walks_at_e': nb_closed,
    'n_distinct_C4_through_e': len(uniq_sq),
    'sample_C4': uniq_sq[:4],
    'psi_e': psi(E),
    'psi_a': psi(apply(E, 'a')),
    'psi_c': psi(apply(E, 'c')),
    'F2_words_checked': count,
    'F2_trivial_words_up_to_len8': bad,
}
with open('cell_census.json', 'w') as f:
    json.dump(out, f, indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
