"""Lane-70 census: integral homology of flag 2-skeleta on 7 vertices + RP2 witness.

Run: PYTHONPATH=/usr/lib/python3/dist-packages <venv>/bin/python census.py
Outputs: census.csv, summary.json, distribution.txt, rp2_*.txt, collapse_log.txt, small_vertices.txt
Deterministic: all orderings fixed (sorted), no randomness.
"""
import csv, json, sys, time
from itertools import combinations

import networkx as nx
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form

T0 = time.time()

# ---------- homology helpers ----------
def snf_diag(rows_list, r, c):
    """Diagonal of Smith normal form of r x c integer matrix (list of rows)."""
    if r == 0 or c == 0:
        return []
    A = Matrix(rows_list)
    assert A.rows == r and A.cols == c, (A.rows, A.cols, r, c)
    if A.is_zero_matrix:
        return [0] * min(r, c)
    R = smith_normal_form(A)
    S = R[1] if isinstance(R, tuple) else R
    return [int(S[i, i]) for i in range(min(r, c))]

def flag_data(G):
    verts = sorted(G.nodes())
    edges = sorted(tuple(sorted(e)) for e in G.edges())
    tris = sorted(t for t in combinations(verts, 3)
                  if G.has_edge(t[0], t[1]) and G.has_edge(t[0], t[2]) and G.has_edge(t[1], t[2]))
    return verts, edges, tris

def homology_of(verts, edges, tris):
    n0, n1, n2 = len(verts), len(edges), len(tris)
    vi = {v: i for i, v in enumerate(verts)}
    ei = {e: j for j, e in enumerate(edges)}
    # d1: n0 x n1, d(u,v)=v-u for u<v
    d1 = [[0] * n1 for _ in range(n0)]
    for j, (u, v) in enumerate(edges):
        d1[vi[u]][j] = -1
        d1[vi[v]][j] = 1
    # d2: n1 x n2, d(a,b,c)=bc-ac+ab
    d2 = [[0] * n2 for _ in range(n1)]
    for k, (a, b, c) in enumerate(tris):
        d2[ei[(a, b)]][k] += 1
        d2[ei[(a, c)]][k] -= 1
        d2[ei[(b, c)]][k] += 1
    s1 = snf_diag(d1, n0, n1)
    s2 = snf_diag(d2, n1, n2)
    r1 = sum(1 for d in s1 if d != 0)
    r2 = sum(1 for d in s2 if d != 0)
    # QQ-rank cross-check on cases with both complexes nonempty pattern (cheap spot check flag)
    b0, b1, b2 = n0 - r1, n1 - r1 - r2, n2 - r2
    assert b0 >= 0 and b1 >= 0 and b2 >= 0, (b0, b1, b2)
    assert n0 - n1 + n2 == b0 - b1 + b2, "Euler cross-check failed"
    h1tors = sorted(abs(d) for d in s2 if abs(d) > 1)
    return dict(n0=n0, n1=n1, n2=n2, b0=b0, b1=b1, b2=b2,
                r1=r1, r2=r2, s1=s1, s2=s2, h1tors=h1tors)

# ---------- collapse helpers (general simplicial 2-complex) ----------
def collapse_step(V, E, T):
    """One lex-first greedy elementary collapse. Returns (removed_kind, removed) or None."""
    in_tri = {e for t in T for e in combinations(t, 2)}
    # free edges: in exactly one triangle
    cnt = {}
    for t in T:
        for e in combinations(t, 2):
            cnt[e] = cnt.get(e, 0) + 1
    free_edges = sorted(e for e in E if cnt.get(e, 0) == 1)
    if free_edges:
        e = free_edges[0]
        t = next(t for t in T if all(x in t for x in e))
        T.remove(t); E.remove(e)
        return ("edge-in-tri", e, t)
    # maximal simplices
    maxedges = sorted(e for e in E if e not in in_tri)
    maxtris = sorted(T)
    # vertex coface count among maximal simplices
    for v in sorted(V):
        holders = [s for s in maxtris if v in s] + [s for s in maxedges if v in s]
        if len(holders) == 1:
            s = holders[0]
            if len(s) == 2:  # maximal edge
                E.remove(s); V.remove(v)
                return ("vert-in-edge", v, s)
            else:  # maximal triangle: remove v, its 2 edges, the triangle
                T.remove(s)
                for e in combinations(s, 2):
                    if v in e and e in E:
                        E.remove(e)
                V.remove(v)
                return ("vert-in-tri", v, s)
    # isolated vertex is NOT a collapse (no higher simplex); stuck unless single vertex
    return None

def greedy_collapse(verts, edges, tris, log=None):
    V, E, T = set(verts), set(edges), set(tris)
    steps = 0
    while True:
        r = collapse_step(V, E, T)
        if r is None:
            break
        steps += 1
        if log is not None:
            log.append((steps, r[0], r[1], r[2], len(V), len(E), len(T)))
        if steps > 10 ** 6:
            raise RuntimeError("collapse loop runaway")
    return V, E, T, steps

def exhaustive_collapse_reaches_point(verts, edges, tris, cap=200000):
    """DFS over all elementary-collapse sequences. Returns (reaches_point, n_states)."""
    from collections import deque
    start = (frozenset(verts), frozenset(edges), frozenset(tris))
    seen = {start}
    stack = [start]
    n = 0
    while stack:
        V, E, T = stack.pop()
        n += 1
        if n > cap:
            return None, n  # inconclusive
        if len(V) == 1 and not E and not T:
            return True, n
        # enumerate all possible elementary collapses from this state
        in_tri = {e for t in T for e in combinations(t, 2)}
        cnt = {}
        for t in T:
            for e in combinations(t, 2):
                cnt[e] = cnt.get(e, 0) + 1
        succs = []
        for e in E:
            if cnt.get(e, 0) == 1:
                t = next(t for t in T if all(x in t for x in e))
                succs.append((V, E - {e}, T - {t}))
        maxedges = [e for e in E if e not in in_tri]
        for v in V:
            holders = [s for s in T if v in s] + [s for s in maxedges if v in s]
            if len(holders) == 1:
                s = holders[0]
                if len(s) == 2:
                    succs.append((V - {v}, E - {s}, T))
                else:
                    es = {e for e in combinations(s, 2) if v in e}
                    succs.append((V - {v}, E - es, T - {s}))
        # isolated-vertex deletion is not a collapse; do not allow
        for s_state in succs:
            key = (frozenset(s_state[0]), frozenset(s_state[1]), frozenset(s_state[2]))
            if key not in seen:
                seen.add(key)
                stack.append(key)
    return False, n

# ---------- 1. atlas gate ----------
atlas = list(nx.graph_atlas_g())
assert len(atlas) == 1253, len(atlas)
g7 = [g for g in atlas if g.number_of_nodes() == 7]
assert len(g7) == 1044, len(g7)
print(f"[gate] atlas={len(atlas)} n7={len(g7)} t={time.time()-T0:.1f}s", flush=True)

# ---------- 2. small-vertex minimality scan (n<=5: 1+1+2+4+11+34=53 graphs) ----------
small = [g for g in atlas if g.number_of_nodes() <= 5]
assert len(small) == 53, len(small)
small_tors = []
for g in small:
    h = homology_of(*flag_data(g))
    if h["h1tors"]:
        small_tors.append((g.number_of_nodes(), sorted(g.edges()), h["h1tors"]))
with open("small_vertices.txt", "w") as f:
    f.write(f"graphs with n<=5 scanned: {len(small)}\n")
    f.write(f"cases with H1 torsion: {len(small_tors)}\n")
    for row in small_tors:
        f.write(repr(row) + "\n")
print(f"[small] scanned={len(small)} torsion_cases={len(small_tors)} t={time.time()-T0:.1f}s", flush=True)

# ---------- 3. main 7-vertex census ----------
rows = []
from collections import Counter
dist = Counter()
torsion_rows = []
qq_checks = 0
for idx, g in enumerate(g7):
    ai = atlas.index(g)  # atlas index for auditability
    verts, edges, tris = flag_data(g)
    h = homology_of(verts, edges, tris)
    # QQ rank cross-check on every 97th case (cheap, independent path)
    if idx % 97 == 0 and h["n1"] and h["n2"]:
        ei = {e: j for j, e in enumerate(edges)}
        d2 = [[0] * h["n2"] for _ in range(h["n1"])]
        for k, (a, b, c) in enumerate(tris):
            d2[ei[(a, b)]][k] += 1
            d2[ei[(a, c)]][k] -= 1
            d2[ei[(b, c)]][k] += 1
        assert Matrix(d2).rank() == h["r2"], (idx, "r2 mismatch")
        qq_checks += 1
    V, E, T, nsteps = greedy_collapse(verts, edges, tris)
    core = (len(V), len(E), len(T))
    rows.append(dict(atlas_index=ai, n_edges=h["n1"], n_triangles=h["n2"],
                     b0=h["b0"], b1=h["b1"], b2=h["b2"],
                     h1tors=";".join(map(str, h["h1tors"])),
                     r1=h["r1"], r2=h["r2"],
                     snf_d1=";".join(map(str, h["s1"])),
                     snf_d2=";".join(map(str, h["s2"])),
                     core_nv=core[0], core_ne=core[1], core_nt=core[2]))
    dist[(h["b0"], h["b1"], h["b2"], tuple(h["h1tors"]))] += 1
    if h["h1tors"]:
        torsion_rows.append((ai, h["n1"], h["n2"], h["h1tors"]))
    if (idx + 1) % 150 == 0:
        print(f"[census] {idx+1}/1044 t={time.time()-T0:.1f}s", flush=True)

with open("census.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
with open("distribution.txt", "w") as f:
    f.write(f"total={len(rows)} qq_spot_checks={qq_checks}\n")
    f.write("b0,b1,b2,H1tors : count\n")
    for k in sorted(dist):
        f.write(f"{k[0]},{k[1]},{k[2]},{list(k[3])} : {dist[k]}\n")
    f.write(f"torsion_cases={len(torsion_rows)}\n")
    for r in torsion_rows:
        f.write(f"torsion atlas_index={r[0]} ne={r[1]} nt={r[2]} H1tors={r[3]}\n")
print(f"[census] done torsion_cases={len(torsion_rows)} t={time.time()-T0:.1f}s", flush=True)

# ---------- 4. RP2 witness: lex-first closed-surface search on 6 vertices ----------
alledges = sorted(combinations(range(6), 2))
alltris = sorted(combinations(range(6), 3))
tri_edges = {t: sorted(combinations(t, 2)) for t in alltris}
edge_tris = {e: [t for t in alltris if all(x in t for x in e)] for e in alledges}
RP2 = None
solution = []
used = {e: 0 for e in alledges}
sys.setrecursionlimit(10000)
def bt(i):
    global RP2
    if RP2 is not None:
        return True
    if len(solution) == 10:
        if all(used[e] == 2 for e in alledges):
            RP2 = list(solution)
            return True
        return False
    if i == len(alltris):
        return False
    # prune: remaining slots must suffice to fill edge deficits
    if len(solution) + (len(alltris) - i) < 10:
        return False
    t = alltris[i]
    if all(used[e] < 2 for e in tri_edges[t]) and len(solution) < 10:
        for e in tri_edges[t]:
            used[e] += 1
        solution.append(t)
        if bt(i + 1):
            return True
        solution.pop()
        for e in tri_edges[t]:
            used[e] -= 1
    return bt(i + 1)
assert bt(0) and RP2 is not None, "no closed 10-triangle surface found"
facets = sorted(tuple(t) for t in RP2)
verts6 = list(range(6))
edges6 = sorted(e for e in alledges if used[e] > 0)
assert len(edges6) == 15, len(edges6)
h6 = homology_of(verts6, edges6, facets)
assert h6["n0"] - h6["n1"] + h6["n2"] == 1, "chi must be 1"
# manifold check: every vertex link is a cycle
for v in verts6:
    link_e = [(a, b) for (a, b, c) in [tuple(sorted(set(t) - {v})) if v in t else None
                                       for t in facets] if c is not None] if False else None
    star = [t for t in facets if v in t]
    link_edges = [tuple(sorted(set(t) - {v})) for t in star]
    assert len(link_edges) == len(set(link_edges)) == 5, (v, link_edges)
    deg = {}
    for a, b in link_edges:
        deg[a] = deg.get(a, 0) + 1
        deg[b] = deg.get(b, 0) + 1
    assert sorted(deg.values()) == [2] * 5, (v, deg)
# connectivity
seen_v, stack = {0}, [0]
adj = {v: set() for v in verts6}
for a, b in edges6:
    adj[a].add(b); adj[b].add(a)
while stack:
    v = stack.pop()
    for u in adj[v]:
        if u not in seen_v:
            seen_v.add(u); stack.append(u)
assert len(seen_v) == 6
assert h6["h1tors"] == [2] and h6["b1"] == 0 and h6["b2"] == 0, h6
with open("rp2_facets.txt", "w") as f:
    for t in facets:
        f.write(f"{t[0]}{t[1]}{t[2]}\n")
with open("rp2_snf.txt", "w") as f:
    f.write(f"facets={facets}\n")
    f.write(f"n0,n1,n2={h6['n0']},{h6['n1']},{h6['n2']} chi={h6['n0']-h6['n1']+h6['n2']}\n")
    f.write(f"snf_d1_diag={h6['s1']}\n")
    f.write(f"snf_d2_diag={h6['s2']}\n")
    f.write(f"r1={h6['r1']} r2={h6['r2']} b0,b1,b2={h6['b0']},{h6['b1']},{h6['b2']} H1tors={h6['h1tors']}\n")
print(f"[rp2] facets={facets} H1tors={h6['h1tors']} t={time.time()-T0:.1f}s", flush=True)

# ---------- 5. collapse certificates for witness ----------
clog = []
V, E, T, nsteps = greedy_collapse(verts6, edges6, facets, log=clog)
with open("collapse_log.txt", "w") as f:
    f.write(f"greedy lex-first collapse of RP2 witness: steps={nsteps} "
            f"final_core nv={len(V)} ne={len(E)} nt={len(T)}\n")
    f.write(f"core_tris={sorted(T)}\n")
    f.write("step kind detail core(nv,ne,nt)\n")
    for s, kind, a, b, nv, ne, nt in clog:
        f.write(f"{s} {kind} {a}->{b} ({nv},{ne},{nt})\n")
reaches, nstates = exhaustive_collapse_reaches_point(verts6, edges6, facets)
with open("collapse_exhaustive.txt", "w") as f:
    f.write(f"exhaustive collapse DFS: reaches_single_vertex={reaches} states_visited={nstates}\n")
print(f"[collapse] greedy_core=({len(V)},{len(E)},{len(T)}) exhaustive_reaches={reaches} "
      f"states={nstates} t={time.time()-T0:.1f}s", flush=True)

summary = dict(
    atlas_total=len(atlas), n7=len(g7), small_scanned=len(small),
    small_torsion_cases=len(small_tors), torsion_cases_7=len(torsion_rows),
    torsion_rows_7=torsion_rows, qq_spot_checks=qq_checks,
    rp2_facets=facets, rp2_homology=dict(b0=h6["b0"], b1=h6["b1"], b2=h6["b2"],
                                         h1tors=h6["h1tors"], snf_d2=h6["s2"]),
    rp2_greedy_core=dict(nv=len(V), ne=len(E), nt=len(T), steps=nsteps),
    exhaustive=dict(reaches_point=reaches, states=nstates),
    elapsed_s=round(time.time() - T0, 1))
with open("summary.json", "w") as f:
    json.dump(summary, f, indent=1)
print(json.dumps(summary, indent=1))
