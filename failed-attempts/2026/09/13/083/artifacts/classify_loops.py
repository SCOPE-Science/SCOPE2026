"""Classify enumerated train loops: homology (a,b), Zung slope, realizability."""
import pickle, math
from collections import Counter
import snappy, flipper
from flipper.kernel.triangulation3 import MERIDIANS, LONGITUDES

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
            states[st].append((b2, (nxt[0][0], nxt[0][1]), nxt[1]))

TAU = 2 * math.pi
def side_angle(W, j, off):
    k = W.index(j)
    return TAU * (k + 1.5) / 3 + off

def chord_cross(p1, p2, q1, q2):
    if len(set([round(p1,9), round(p2,9), round(q1,9), round(q2,9)])) < 4:
        return 0
    def rel(x):
        return (x - p1) % TAU
    r2, r3, r4 = rel(p2), rel(q1), rel(q2)
    if (r3 < r2) != (r4 < r2):
        return 1 if r3 < r2 else -1
    return 0

def curve_arcs(tet_idx, v, P):
    t = T3.tetrahedra[tet_idx]
    W = sorted(w for w in range(4) if w != v)
    return [(w, t.peripheral_curves[P][v][w]) for w in W if t.peripheral_curves[P][v][w] != 0]

def inter_walk_curve(walk_tris, P):
    from collections import defaultdict
    by_tri = defaultdict(list)
    for (tri, se_in, se_out) in walk_tris:
        by_tri[tri].append((se_in, se_out))
    tot = 0
    for tri, warcs in by_tri.items():
        i, v = tri
        W = sorted(w for w in range(4) if w != v)
        carcs = curve_arcs(i, v, P)
        for (se_in, se_out) in warcs:
            p1 = side_angle(W, se_in, 0.02); p2 = side_angle(W, se_out, 0.02)
            for (w, mult) in carcs:
                js = [j for j in W if j != w]
                q1 = side_angle(W, js[0], -0.02); q2 = side_angle(W, js[1], -0.02)
                if mult < 0:
                    q1, q2 = q2, q1
                tot += chord_cross(p1, p2, q1, q2) * abs(mult)
    return tot

import sys
sys.setrecursionlimit(10000)
loops = []
LMAX = 14
def dfs(start, cur, depth, path_states, used_br):
    if depth == LMAX:
        return
    for nxt in states[cur]:
        b2 = nxt[0]
        if nxt == start and depth + 1 >= 3:
            loops.append(path_states + [nxt])
            continue
        if b2 in used_br:
            continue
        dfs(start, nxt, depth + 1, path_states + [nxt], used_br | {b2})
for s in slist:
    dfs(s, s, 0, [], set())
print("raw loops:", len(loops), flush=True)

# canonicalize (rotation + reversal) and dedupe
def canon(loop):
    bs = [st[0] for st in loop]
    n = len(bs)
    rots = [tuple(bs[i:] + bs[:i]) for i in range(n)]
    rev = list(reversed(bs))
    rots += [tuple(rev[i:] + rev[:i]) for i in range(n)]
    return min(rots)
uniq = {}
for loop in loops:
    c = canon(loop)
    uniq.setdefault(c, loop)
print("unique loops:", len(uniq), flush=True)

def walk_tris(loop):
    # loop: list of states; state k: (b, tb, sb) arrived at tb via sb.
    # exits tb via se = side of next state's arrival? next state (b2, tb2, sb2): b2 contains side (tb, se).
    out = []
    n = len(loop)
    for k in range(n):
        b, tb, sb = loop[k]
        b2, tb2, sb2 = loop[(k + 1) % n]
        # find exit side se of tb with bkey[(tb,se)] == b2
        for se in range(4):
            if se != tb[1] and bkey.get((tb, se), -1) == b2:
                out.append((tb, sb, se))
                break
    return out

def zung_slope(a, b):
    # direction a*(-1,0)+b*(6,-1) = (6b-a, -b); t = -b/(6b-a)
    d = 6 * b - a
    if d == 0:
        return float('inf')
    return -b / d

results = Counter()
detail = {}
for c, loop in uniq.items():
    wt = walk_tris(loop)
    if len(wt) != len(loop):
        continue
    iM = inter_walk_curve(wt, MERIDIANS)
    iL = inter_walk_curve(wt, LONGITUDES)
    a, b = -iL, iM
    g = math.gcd(a, b)
    prim = (a // g, b // g) if g else (a, b)
    t = zung_slope(*prim)
    results[(prim, round(t, 6) if abs(t) != float('inf') else 'inf', len(loop))] += 1
    detail.setdefault((prim, len(loop)), []).append((iM, iL))
for k in sorted(results, key=lambda x: (x[1] if isinstance(x[1], float) else 999, x[2])):
    print(f"class {k[0]}  Zung slope {k[1]}  len {k[2]}  count {results[k]}", flush=True)
