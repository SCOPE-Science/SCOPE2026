"""honeycomb_flip.py — stdlib-only exact certification for lane-115 partial theorem.

Constructs an explicit regular unimodular (honeycomb-type, dual core K4)
triangulation T0 of 4*Delta_2, enumerates all its flips mod S3, and certifies
a regular unimodular one-flip neighbour T1 whose skeleton core has a bridge
=> infinite bitangent side (via bridge-contraction in Jacobian, BLMR black box).

Outputs: witness.json (all data needed for independent replay).
"""
import json, random, itertools
from fractions import Fraction as F

# ---------- lattice points of 4*Delta_2 ----------
PTS = [(i, j) for i in range(5) for j in range(5 - i)]
IDX = {p: k for k, p in enumerate(PTS)}
N = len(PTS)
assert N == 15

def area2(a, b, c):
    return abs((b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1]))

def sarea(a, b, c):  # signed double area
    return (b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1])

# boundary lattice segments of 4*Delta_2 (12 of them)
BSEG = set()
corners = [(0,0),(4,0),(0,4)]
edges_c = [((0,0),(4,0)), ((4,0),(0,4)), ((0,4),(0,0))]
for p, q in edges_c:
    for t in range(4):
        a = (p[0]+(q[0]-p[0])*t//4, p[1]+(q[1]-p[1])*t//4)
        b = (p[0]+(q[0]-p[0])*(t+1)//4, p[1]+(q[1]-p[1])*(t+1)//4)
        BSEG.add(frozenset((a,b)))
assert len(BSEG) == 12

# ---------- exact 3x3 solve for lifting plane ----------
def plane(p1, p2, p3):
    """Return (a,b,c) with z = a*x+b*y+c through lifted points (x,y,z as Fractions).
    None if singular."""
    M = [[F(p1[0]), F(p1[1]), F(1)],
         [F(p2[0]), F(p2[1]), F(1)],
         [F(p3[0]), F(p3[1]), F(1)]]
    rhs = [F(p1[2]), F(p2[2]), F(p3[2])]
    # Cramer
    def det3(M):
        return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
                - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
                + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
    D = det3(M)
    if D == 0:
        return None
    out = []
    for col in range(3):
        Mc = [row[:] for row in M]
        for r in range(3):
            Mc[r][col] = rhs[r]
        out.append(det3(Mc) / D)
    return tuple(out)

def lower_triangulation(h):
    """h: list of 15 heights (Fraction-compatible). Return sorted triangle tuple-set
    of the regular subdivision, or None if non-generic / not a triangulation."""
    LP = [(x, y, F(h[IDX[(x,y)]])) for (x, y) in PTS]
    tris = []
    for combo in itertools.combinations(range(N), 3):
        a, b, c = (PTS[i] for i in combo)
        if area2(a, b, c) == 0:
            continue
        pl = plane(LP[combo[0]], LP[combo[1]], LP[combo[2]])
        if pl is None:
            continue
        A, B, C = pl
        ok, eq = True, []
        for m, (x, y) in enumerate(PTS):
            diff = LP[m][2] - (A*F(x) + B*F(y) + C)
            if diff < 0:
                ok = False
                break
            if diff == 0:
                eq.append(m)
        if ok and len(eq) == 3 and set(eq) == set(combo):
            tris.append(tuple(sorted(combo)))
    return tris

def check_triangulation(tris):
    """Verify unimodular triangulation of 4*Delta_2. Return (ok, info)."""
    if len(tris) != 16:
        return False, f"count {len(tris)} != 16"
    for t in tris:
        a, b, c = (PTS[i] for i in t)
        if area2(a, b, c) != 1:
            return False, f"non-unimodular {t}"
    edge_use = {}
    for ti, t in enumerate(tris):
        for e in [frozenset((PTS[t[0]],PTS[t[1]])), frozenset((PTS[t[1]],PTS[t[2]])),
                  frozenset((PTS[t[0]],PTS[t[2]]))]:
            edge_use.setdefault(e, []).append(ti)
    for e, users in edge_use.items():
        if e in BSEG:
            if len(users) != 1:
                return False, f"bdy edge {sorted(e)} used {len(users)}x"
        else:
            if len(users) != 2:
                return False, f"interior edge {sorted(e)} used {len(users)}x"
    # pairwise interior-disjointness (exact orientation test)
    def orient(p, q, r):
        return (q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0])
    def proper_cross(p1,p2,p3,p4):
        d1 = orient(p3,p4,p1); d2 = orient(p3,p4,p2)
        d3 = orient(p1,p2,p3); d4 = orient(p1,p2,p4)
        return ((d1>0)!=(d2>0) and d1!=0 and d2!=0 and (d3>0)!=(d4>0) and d3!=0 and d4!=0)
    T = [[PTS[i] for i in t] for t in tris]
    for i in range(16):
        for j in range(i+1, 16):
            si, sj = set(tris[i]), set(tris[j])
            if len(si & sj) == 2:
                continue  # share an edge (manifold) — fine
            for e1 in itertools.combinations(T[i],2):
                for e2 in itertools.combinations(T[j],2):
                    if proper_cross(e1[0],e1[1],e2[0],e2[1]):
                        return False, f"overlap tris {i},{j}"
    return True, "ok"

# ---------- dual graph / skeleton core ----------
def dual_interior_edges(tris):
    edge_map = {}
    for ti, t in enumerate(tris):
        P = [PTS[i] for i in t]
        for e in [frozenset((P[0],P[1])), frozenset((P[1],P[2])), frozenset((P[0],P[2]))]:
            edge_map.setdefault(e, []).append(ti)
    int_edges = [(users[0], users[1], sorted(e)) for e, users in edge_map.items()
                 if e not in BSEG]
    return int_edges  # (tri_a, tri_b, [pt,pt])

def skeleton_core(tris):
    """Return core multigraph (nodes, edges) after pruning leaves + smoothing 2-valent."""
    ie = dual_interior_edges(tris)
    alive = set(range(len(tris)))
    adj = {v: [] for v in alive}  # v -> list of edge ids
    edges = {}  # eid -> [u,v]
    for eid, (u, v, _) in enumerate(ie):
        edges[eid] = [u, v]
        adj[u].append(eid); adj[v].append(eid)
    def deg(v):
        ds = 0
        for eid in adj[v]:
            u, w = edges[eid]
            ds += 2 if u == w else 1
        return ds
    # prune leaves
    changed = True
    while changed:
        changed = False
        for v in list(alive):
            if deg(v) <= 1:
                for eid in list(adj[v]):
                    u, w = edges[eid]
                    o = w if u == v else u
                    if o in adj:
                        adj[o] = [e for e in adj[o] if e != eid]
                    del edges[eid]
                del adj[v]; alive.discard(v); changed = True
    # smooth degree-2 nodes
    while True:
        found = None
        for v in list(alive):
            if deg(v) == 2:
                eu, ev = adj[v]
                a = edges[eu][1] if edges[eu][0] == v else edges[eu][0]
                b = edges[ev][1] if edges[ev][0] == v else edges[ev][0]
                if not (edges[eu][0] == v and edges[eu][1] == v) and \
                   not (edges[ev][0] == v and edges[ev][1] == v):
                    found = (v, eu, ev, a, b); break
        if not found:
            break
        v, eu, ev, a, b = found
        del edges[eu]; del edges[ev]
        del adj[v]; alive.discard(v)
        nid = max(edges)+1 if edges else 0
        edges[nid] = [a, b]
        adj[a] = [e for e in adj[a] if e not in (eu, ev)] + [nid]
        if b == a:
            pass
        else:
            adj[b] = [e for e in adj[b] if e not in (eu, ev)] + [nid]
    nodes = sorted(alive)
    elist = sorted((u, v) for (u, v) in edges.values())
    return nodes, elist

def genus_check(tris):
    ie = dual_interior_edges(tris)
    return len(ie) - len(tris) + 1

def connectivity(nodes, elist):
    """Brute-force edge-connectivity data: bridges, 2-cuts, components."""
    E = list(elist)
    def comps(skip):
        parent = {v: v for v in nodes}
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        for i, (u, v) in enumerate(E):
            if i in skip:
                continue
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
        return len(set(find(v) for v in nodes))
    if comps(set()) > 1:
        return {"edge_conn": 0, "bridges": [], "two_cuts": []}
    bridges = [i for i in range(len(E)) if comps({i}) > 1]
    two = []
    for i in range(len(E)):
        for j in range(i+1, len(E)):
            if comps({i, j}) > 1:
                two.append([i, j])
    ec = 1 if bridges else (2 if two else 3)
    return {"edge_conn": ec, "bridges": bridges, "two_cuts": two}

def is_K4(nodes, elist):
    if len(nodes) != 4 or len(elist) != 6:
        return False
    degs = {v: 0 for v in nodes}
    seen = set()
    for u, v in elist:
        if u == v:
            return False
        if (u, v) in seen or (v, u) in seen:
            return False
        seen.add((u, v)); degs[u] += 1; degs[v] += 1
    return all(d == 3 for d in degs.values())

# ---------- S3 action on 4*Delta_2 ----------
def s3_images(pt, perm):
    i, j = pt; k = 4 - i - j
    t = [i, j, k]
    nt = [t[perm[0]], t[perm[1]], t[perm[2]]]
    return (nt[0], nt[1])
S3 = list(itertools.permutations([0, 1, 2]))

def canon(tris):
    best = None
    for p in S3:
        img = tuple(sorted(tuple(sorted(IDX[s3_images(PTS[i], p)] for i in t)) for t in tris))
        if best is None or img < best:
            best = img
    return best

# ---------- flips ----------
def all_flips(tris):
    """Yield (edge_pts, new_tris_set) for each flippable interior edge."""
    edge_map = {}
    for ti, t in enumerate(tris):
        P = [PTS[i] for i in t]
        for e in [frozenset((P[0],P[1])), frozenset((P[1],P[2])), frozenset((P[0],P[2]))]:
            edge_map.setdefault(e, []).append(ti)
    out = []
    T = [set(t) for t in tris]
    for e, users in edge_map.items():
        if e in BSEG or len(users) != 2:
            continue
        A, B = T[users[0]], T[users[1]]
        shared = A & B
        if len(shared) != 2:
            continue
        a, b = (IDX[p] for p in e)
        c = (A - shared).pop(); d = (B - shared).pop()
        quad = [PTS[a], PTS[b], PTS[c], PTS[d]]
        # convexity: hull of 4 pts must be 4 pts
        def hull_size(q):
            q = sorted(set(q))
            def cr(o, p, r):
                return (p[0]-o[0])*(r[1]-o[1]) - (p[1]-o[1])*(r[0]-o[0])
            # point-in-triangle strict test for each point vs triangle of others
            for i in range(4):
                o, p, r, s = q[i], q[(i+1)%4], q[(i+2)%4], q[(i+3)%4]
                # check s strictly inside triangle opr
                d1 = cr(o,p,s); d2 = cr(p,r,s); d3 = cr(r,o,s)
                if (d1>0 and d2>0 and d3>0) or (d1<0 and d2<0 and d3<0):
                    return 3
                # check collinear degenerate
            # check all-4 convex via hull
            pts = sorted(q)
            def hull(pts):
                def cr2(o,p,r):
                    return (p[0]-o[0])*(r[1]-o[1])-(p[1]-o[1])*(r[0]-o[0])
                lo = []
                for p in pts:
                    while len(lo)>=2 and cr2(lo[-2],lo[-1],p) <= 0: lo.pop()
                    lo.append(p)
                hi = []
                for p in reversed(pts):
                    while len(hi)>=2 and cr2(hi[-2],hi[-1],p) <= 0: hi.pop()
                    hi.append(p)
                return lo[:-1]+hi[:-1]
            return len(hull(pts))
        if hull_size(quad) != 4:
            continue
        n1 = tuple(sorted((c, d, a))); n2 = tuple(sorted((c, d, b)))
        newT = set(tris)
        newT.discard(tuple(sorted(T[users[0]]))); newT.discard(tuple(sorted(T[users[1]])))
        newT.add(n1); newT.add(n2)
        newT = sorted(newT)
        ok, _ = check_triangulation(newT)
        if ok:
            out.append((sorted(e), newT))
    return out

def find_heights_for(target, h0, tries=4000, seed=0):
    """Perturbation search for heights inducing target triangulation."""
    r = random.Random(seed)
    tc = canon(target)
    for t in range(tries):
        h = [F(h0[i]) + F(r.randint(-9999, 9999), 100) for i in range(N)]
        tris = lower_triangulation(h)
        if tris is None or len(tris) != 16:
            continue
        if canon(tris) == tc and sorted(tris) == sorted(target):
            return [str(x) for x in h]
    # wider search
    for t in range(tries):
        h = [F(h0[i]) + F(r.randint(-39999, 39999), 100) for i in range(N)]
        tris = lower_triangulation(h)
        if tris is None or len(tris) != 16:
            continue
        if sorted(tris) == sorted(target):
            return [str(x) for x in h]
    return None

# ---------- main ----------
def main():
    random.seed(20260908)
    T0 = H0 = None
    info0 = None
    for seed in range(2000):
        r = random.Random(1000 + seed)
        h = [F(x * x + y * y) * 100 + F(r.randint(0, 9999), 100)
             for (x, y) in PTS]
        tris = lower_triangulation(h)
        if tris is None:
            continue
        ok, _ = check_triangulation(tris)
        if not ok:
            continue
        if genus_check(tris) != 3:
            continue
        nodes, elist = skeleton_core(tris)
        if is_K4(nodes, elist):
            T0, H0 = sorted(tris), h
            info0 = (nodes, elist)
            print(f"FOUND T0 at seed {seed}")
            break
    assert T0 is not None, "no K4-core triangulation found"
    print("T0 tris:", T0)
    print("T0 heights:", H0)
    print("T0 core nodes:", info0[0], "edges:", info0[1])

    flips = all_flips(T0)
    print(f"# flippable edges of T0: {len(flips)}")
    # group mod S3 by flipped triangulation
    orbits = {}
    for e, nT in flips:
        c = canon(nT)
        orbits.setdefault(c, []).append((e, nT))
    print(f"# S3-orbits of flips: {len(orbits)}")

    results = []
    witness = None
    for oi, (c, members) in enumerate(orbits.items()):
        e, nT = members[0]
        nodes, elist = skeleton_core(nT)
        conn = connectivity(nodes, elist)
        h1 = find_heights_for(nT, H0, seed=oi)
        entry = {
            "orbit": oi,
            "n_members": len(members),
            "flipped_edge": [[int(a) for a in p] for p in e],
            "new_tris": [[int(x) for x in t] for t in nT],
            "core_nodes": nodes,
            "core_edges": [[int(u) for u in ee] for ee in elist],
            "edge_conn": conn["edge_conn"],
            "n_two_cuts": len(conn["two_cuts"]),
            "regular_cert_heights": h1,
        }
        results.append(entry)
        print(f"orbit {oi}: members={len(members)} edge={e} coreV={len(nodes)} "
              f"coreE={len(elist)} edgeconn={conn['edge_conn']} "
              f"2cuts={len(conn['two_cuts'])} regular={'YES' if h1 else 'NO'}")
        if witness is None and conn["edge_conn"] == 1 and h1 is not None:
            witness = entry

    assert witness is not None, "no bridge flip found"
    print("WITNESS orbit:", witness["orbit"])

    data = {
        "T0_tris_idx": [[int(x) for x in t] for t in T0],
        "T0_heights": [str(F(x)) for x in H0],
        "T0_core_nodes": info0[0],
        "T0_core_edges": [[int(u) for u in ee] for ee in info0[1]],
        "points": [[int(a) for a in p] for p in PTS],
        "flip_orbits": results,
        "witness_orbit": witness["orbit"],
    }
    with open("witness.json", "w") as f:
        json.dump(data, f, indent=1)
    print("wrote witness.json")


if __name__ == "__main__":
    main()
