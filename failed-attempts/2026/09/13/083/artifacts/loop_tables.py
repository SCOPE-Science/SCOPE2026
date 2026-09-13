"""Install train loops as flipper TEMPS peripheral data; exact intersections; classification.

Corner-weight rule for a train loop (oriented closed walk):
In triangle (tet T, cusp-corner v), walk arcs join side midpoints. For side s (face)
and corner o (o != s side's... periph layout: periph[side][other], side=v, other=w):
entry E[v][w] = signed turn weight. Rule (SnapPy kernel convention, "dual corner
weights"): a strand passing through the triangle from side s_in to side s_out turns
LEFT (+1) or RIGHT (-1) at the corner it cuts. Our triangle orientation: corners W
sorted CCW (link orientation). Arc s_in -> s_out: consider cyclic order; the arc cuts
exactly one corner? NO -- an arc joining two side midpoints cuts the corner BETWEEN them
along the boundary... The two sides s_in, s_out share exactly one corner c (sides as sets
of corners: side j contains corners W\{j}; two sides share one corner). The arc cuts
corner c. Turn sign: traveling s_in -> s_out, with triangle interior on ... : left turn
(+1) iff corner c is on the LEFT of travel direction. Left of travel: computed from
CCW order: travel s_in->s_out; corners: shared corner c; the arc veers toward c.
Hmm, precisely: midpoint of s_in to midpoint of s_out; c = shared corner. Direction of
travel d; normal toward c: n. Turn sign = sign of cross(d, n)? If c is left of d, left turn.
Compute in complex coords (CCW triangle) explicitly. Each arc contributes +/-1 to
E[v][c]. Multiple arcs add. Antisymmetry across gluing must hold for a genuine closed
oriented curve -- VERIFY (this validates the rule!); then intersections via flipper.
"""
import pickle, cmath, math
from itertools import product
import snappy, flipper
import flipper.kernel.triangulation3 as T3m
from flipper.kernel.triangulation3 import MERIDIANS, LONGITUDES, TEMPS

WDIR = "output/artifacts"
D = pickle.load(open(f"{WDIR}/track_data.pkl", "rb"))
branches, switches, NV = D["branches"], D["switches"], D["NV"]
NB = len(branches)
M = snappy.Manifold('10_145')
mono = flipper.monodromy_from_bundle(M)
B = mono.bundle(veering=True)
V = snappy.Manifold(B.snappy_string())
data = V._get_tetrahedra_gluing_data()
NT = len(data)
T3 = B.triangulation3
WSTAR = {0: 2, 1: 3, 2: 0, 3: 1}
bkey = {}
for b, members in enumerate(branches):
    for s in members:
        bkey[s] = b

# directed route graph
states = {}
slist = []
for b, members in enumerate(branches):
    ((i1, v1), j1), ((i2, v2), j2) = members
    for (tb, sb) in [((i1, v1), j1), ((i2, v2), j2)]:
        L = WSTAR[tb[1]]
        smalls = [j for j in range(4) if j != tb[1] and j != L]
        exits = smalls if sb == L else [L]
        st = (b, tb, sb)
        states[st] = []
        slist.append(st)
        for se in exits:
            b2 = bkey[(tb, se)]
            m2 = branches[b2]
            nxt = m2[1] if m2[0] == (tb, se) else m2[0]
            states[st].append((b2, (nxt[0][0], nxt[0][1]), nxt[1], se))  # include exit side se

# turn sign: CCW triangle corners W[0],W[1],W[2] at complex roots; arc mid(s_in)->mid(s_out);
# shared corner c; sign = sign of Im(conj(d) * (c - mid_arc))? left => +1.
CORN = {0: 1 + 0j, 1: cmath.exp(2j * math.pi / 3), 2: cmath.exp(4j * math.pi / 3)}
def turn_sign(W, s_in, s_out):
    P = [CORN[W.index(w)] for w in W]
    mid = lambda s: sum(P[W.index(w)] for w in W if w != s) / 2
    a, b = mid(s_in), mid(s_out)
    cset = set(w for w in W if w != s_in) & set(w for w in W if w != s_out)
    assert len(cset) == 1
    c = CORN[W.index(next(iter(cset)))]
    d = b - a
    n = c - (a + b) / 2
    cr = (d.real * n.imag - d.imag * n.real)
    assert abs(cr) > 1e-9
    return 1 if cr > 0 else -1

def install_loop(loop):
    """loop: list of states forming closed walk. Returns E dict {(tet,v,w): int} + antisym check."""
    E = {}
    n = len(loop)
    for k in range(n):
        b, tb, sb = loop[k][0], loop[k][1], loop[k][2]
        b2 = loop[(k + 1) % n][0]
        se = None
        for j in range(4):
            if j != tb[1] and bkey.get((tb, j), -1) == b2:
                se = j
                break
        assert se is not None, (k, tb, b2)
        i, v = tb
        W = sorted(w for w in range(4) if w != v)
        s = turn_sign(W, sb, se)
        cset = set(w for w in W if w != sb) & set(w for w in W if w != se)
        c = next(iter(cset))
        E[(i, v, c)] = E.get((i, v, c), 0) + s
    return E

def check_antisym(E):
    bad = []
    for i, (nbrs, perms) in enumerate(data):
        for v in range(4):
            for w in range(4):
                if w == v:
                    continue
                # corner (i,v,w) lies in sides j != v,w... the corner is shared via face gluings:
                # corner (i,v,w) identified with (i2,p[v],p[w]) for faces j not containing... any face j != v,w
                # gives a gluing; check one: pick j0 = the side... corner (i,v,w) is in triangle (i,v); its
                # partner: via face j (j != v, j != w): (i2, p[v], p[w]).
                js = [j for j in range(4) if j != v and j != w]
                j = js[0]
                i2 = nbrs[j]; p = perms[j]
                e1 = E.get((i, v, w), 0)
                e2 = E.get((i2, p[v], p[w]), 0)
                if e1 + e2 != 0:
                    bad.append(((i, v, w), e1, (i2, p[v], p[w]), e2))
    return bad

import sys
sys.setrecursionlimit(10000)
loops = []
LMAX = 14
def dfs(start, cur, depth, path_states, used_br):
    if depth == LMAX:
        return
    for nxt in states[cur]:
        b2 = nxt[0]
        if (nxt[1], nxt[2]) == (start[1], start[2]) and b2 == start[0] and depth + 1 >= 3:
            loops.append(path_states + [(b2, nxt[1], nxt[2])])
            continue
        if b2 in used_br:
            continue
        dfs(start, (nxt[0], nxt[1], nxt[2]), depth + 1, path_states + [(nxt[0], nxt[1], nxt[2])], used_br | {b2})
for s in slist:
    dfs(s, s, 0, [], set())
print("raw loops:", len(loops), flush=True)
def canon(loop):
    bs = [st[0] for st in loop]
    n = len(bs)
    rots = [tuple(bs[i:] + bs[:i]) for i in range(n)]
    rev = list(reversed(bs))
    rots += [tuple(rev[i:] + rev[:i]) for i in range(n)]
    return min(rots)
uniq = {}
for loop in loops:
    uniq.setdefault(canon(loop), loop)
print("unique:", len(uniq), flush=True)
for c, loop in uniq.items():
    E = install_loop(loop)
    bad = check_antisym(E)
    print(f"loop len {len(loop)} branches {c}: antisym violations: {len(bad)}", flush=True)
    if bad:
        for x in bad[:6]:
            print("   ", x, flush=True)
    # install as TEMPS and intersect
    for t in T3.tetrahedra:
        for s_ in range(4):
            for o in range(4):
                t.peripheral_curves[TEMPS][s_][o] = 0
    for (i, v, w), e in E.items():
        T3.tetrahedra[i].peripheral_curves[TEMPS][v][w] = e
    print("   i(loop,M) =", T3.intersection_number(TEMPS, MERIDIANS),
          " i(loop,L) =", T3.intersection_number(TEMPS, LONGITUDES), flush=True)
