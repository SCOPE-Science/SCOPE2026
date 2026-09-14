#!/usr/bin/env python3
"""Lane-1816 TARGET work (stdlib only): search for a triangle-free 5-chromatic
finite unit-distance graph (|P| <= 800), route A = explicit construction.

Contents:
  controls : C5 pentagon (triangle-free, chi=3), Moser spindle (chi=4, triangles),
             abstract Mycielski M4/M5 (triangle-free, chi=4/5 abstractly).
  attempt 1: random triangle-free rotation/rhombus assembly + exact 4-color tests.
  attempt 2: numeric (simulated annealing) embedding of abstract triangle-free
             5-chromatic M5 (23v) and 4-chromatic M4 (11v) as unit-distance graphs.
  recovery : same pipeline must re-certify the small controls (proves tooling works).
Writes exp1_results.json next to this script.
"""
import math
import random
import json
import sys
import time
from collections import deque

sys.setrecursionlimit(1000000)
TOL = 1e-6
SQ3 = math.sqrt(3.0)
T0 = time.time()


def log(msg):
    print("[%6.1fs] %s" % (time.time() - T0, msg), flush=True)


# ---------------- geometry ----------------
def unit_adj(pts, tol=TOL):
    n = len(pts)
    adj = [set() for _ in range(n)]
    for i in range(n):
        xi, yi = pts[i]
        for j in range(i + 1, n):
            if abs(math.hypot(pts[j][0] - xi, pts[j][1] - yi) - 1.0) <= tol:
                adj[i].add(j)
                adj[j].add(i)
    return adj


def find_triangle(adj):
    n = len(adj)
    for i in range(n):
        Ai = adj[i]
        for j in Ai:
            if j > i:
                both = Ai & adj[j]
                for k in both:
                    if k > j:
                        return (i, j, k)
    return None


def n_edges(adj):
    return sum(map(len, adj)) // 2


def is_bipartite(adj):
    n = len(adj)
    col = [-1] * n
    for s in range(n):
        if col[s] >= 0:
            continue
        col[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if col[w] < 0:
                    col[w] = col[u] ^ 1
                    q.append(w)
                elif col[w] == col[u]:
                    return False
    return True


# ---------------- coloring ----------------
def greedy_ncolors(adj, order=None):
    n = len(adj)
    if order is None:
        order = sorted(range(n), key=lambda v: -len(adj[v]))
    col = [-1] * n
    used = 0
    for v in order:
        forbid = {col[u] for u in adj[v] if col[u] >= 0}
        c = 0
        while c in forbid:
            c += 1
        col[v] = c
        if c + 1 > used:
            used = c + 1
    return used, col


def greedy_best(adj, trials=20, seed=0):
    rng = random.Random(seed)
    best = None
    n = len(adj)
    base = list(range(n))
    for _ in range(trials):
        rng.shuffle(base)
        # degree-descending stable-ish: sort by degree desc with random tiebreak
        order = sorted(base, key=lambda v: (-len(adj[v]), rng.random()))
        k, _ = greedy_ncolors(adj, order)
        if best is None or k < best:
            best = k
    return best


def dsatur_kcolorable(adj, k, budget=2000000, time_limit=120.0):
    """Exact k-colorability. Returns (True/False/None, nodes). None = over budget/time."""
    n = len(adj)
    color = [-1] * n
    deg = [len(a) for a in adj]
    nodes = 0
    t_start = time.time()
    timed_out = [False]

    def select():
        best = -1
        bs = -1
        bd = -1
        for v in range(n):
            if color[v] < 0:
                seen = 0
                s = 0
                for u in adj[v]:
                    cu = color[u]
                    if cu >= 0 and not (seen >> cu) & 1:
                        seen |= (1 << cu)
                        s += 1
                if s > bs or (s == bs and deg[v] > bd):
                    bs, bd, best = s, deg[v], v
        return best

    def rec(colored):
        nonlocal nodes
        nodes += 1
        if nodes > budget or (nodes & 4095) == 0 and (time.time() - t_start) > time_limit:
            timed_out[0] = True
            return None
        if timed_out[0]:
            return None
        if colored == n:
            return True
        v = select()
        seen = 0
        for u in adj[v]:
            cu = color[u]
            if cu >= 0:
                seen |= (1 << cu)
        for c in range(k):
            if not (seen >> c) & 1:
                color[v] = c
                r = rec(colored + 1)
                color[v] = -1
                if r is True:
                    return True
                if r is None:
                    return None
        return False

    v0 = max(range(n), key=lambda v: deg[v])
    color[v0] = 0  # wlog by color permutation
    r = rec(1)
    return r, nodes


# ---------------- abstract graphs ----------------
def mycielski(adj):
    n = len(adj)
    apex = 2 * n
    nadj = [set() for _ in range(2 * n + 1)]

    def add(a, b):
        nadj[a].add(b)
        nadj[b].add(a)

    for i in range(n):
        for j in adj[i]:
            if j > i:
                add(i, j)
    for i in range(n):
        for j in adj[i]:
            add(n + i, j)
        add(n + i, apex)
    return nadj


# ---------------- numeric embedding (SA) ----------------
def full_stress(coords, adj):
    n = len(coords)
    s = 0.0
    for i in range(n):
        xi, yi = coords[i]
        Ai = adj[i]
        for j in range(i + 1, n):
            dd = math.hypot(coords[j][0] - xi, coords[j][1] - yi)
            if j in Ai:
                e = dd - 1.0
                s += e * e
            else:
                e = abs(dd - 1.0)
                if e < 0.03:
                    t = 0.03 - e
                    s += 80.0 * t * t
                if dd < 0.12:
                    t = 0.12 - dd
                    s += 8.0 * t * t
    return s


def sa_embed(adj, restarts, iters, seed):
    rng = random.Random(seed)
    n = len(adj)
    best_s = float("inf")
    best_coords = None
    for r in range(restarts):
        R = rng.uniform(0.8, 1.6)
        ph = rng.uniform(0, 2 * math.pi)
        coords = [
            (R * math.cos(ph + 2 * math.pi * i / n) + rng.gauss(0, 0.05),
             R * math.sin(ph + 2 * math.pi * i / n) + rng.gauss(0, 0.05))
            for i in range(n)
        ]
        s = full_stress(coords, adj)
        T = 0.03
        cooling = math.exp(math.log(1e-4) / iters)
        sig = 0.12
        sig_cooling = math.exp(math.log(0.02) / iters)
        for _ in range(iters):
            i = rng.randrange(n)
            ox, oy = coords[i]
            coords[i] = (ox + rng.gauss(0, sig), oy + rng.gauss(0, sig))
            ns = full_stress(coords, adj)
            if ns <= s or rng.random() < math.exp(-(ns - s) / T):
                s = ns
                if s < best_s:
                    best_s = s
                    best_coords = [p for p in coords]
                    if s < 1e-14:
                        break
            else:
                coords[i] = (ox, oy)
            T *= cooling
            sig *= sig_cooling
    return best_s, best_coords


def verify_embedding(coords, adj):
    n = len(coords)
    maxdev = 0.0
    missing = 0
    for i in range(n):
        xi, yi = coords[i]
        for j in adj[i]:
            if j > i:
                dd = math.hypot(coords[j][0] - xi, coords[j][1] - yi)
                maxdev = max(maxdev, abs(dd - 1.0))
                if abs(dd - 1.0) > 1e-3:
                    missing += 1
    minextra = 1e9
    extras = 0
    mind = 1e9
    for i in range(n):
        xi, yi = coords[i]
        for j in range(i + 1, n):
            dd = math.hypot(coords[j][0] - xi, coords[j][1] - yi)
            if dd < mind:
                mind = dd
            if j not in adj[i]:
                e = abs(dd - 1.0)
                if e < minextra:
                    minextra = e
                if e < 1e-6:
                    extras += 1
    tri = find_triangle(unit_adj(coords, tol=1e-6))
    ok = (missing == 0 and extras == 0 and tri is None and maxdev < 1e-3)
    return {"max_req_dev": maxdev, "missing_edges": missing,
            "minextra_gap": minextra, "extra_edges": extras,
            "triangle": tri, "min_sep": mind, "success": ok}


# ---------------- triangle-free assembler ----------------
def grow_triangle_free(target_n, seed, double_prob=0.7, stuck_cap=30000):
    rng = random.Random(seed)
    pts = [(0.0, 0.0), (1.0, 0.0)]
    adj = [set([1]), set([0])]
    stuck = 0
    while len(pts) < target_n and stuck < stuck_cap:
        if rng.random() < double_prob and len(pts) >= 2:
            i = rng.randrange(len(pts))
            j = rng.randrange(len(pts) - 1)
            if j >= i:
                j += 1
            xi, yi = pts[i]
            xj, yj = pts[j]
            mx, my = (xi + xj) / 2.0, (yi + yj) / 2.0
            dx, dy = xj - xi, yj - yi
            dd = math.hypot(dx, dy)
            if dd >= 2.0 or dd < 1e-9:
                stuck += 1
                continue
            h = math.sqrt(max(0.0, 1.0 - (dd / 2.0) ** 2))
            ux, uy = -dy / dd, dx / dd
            if rng.random() < 0.5:
                w = (mx + ux * h, my + uy * h)
            else:
                w = (mx - ux * h, my - uy * h)
        else:
            i = rng.randrange(len(pts))
            a = rng.uniform(0, 2 * math.pi)
            w = (pts[i][0] + math.cos(a), pts[i][1] + math.sin(a))
        # distinctness
        dup = False
        for p in pts:
            if math.hypot(p[0] - w[0], p[1] - w[1]) < 1e-3:
                dup = True
                break
        if dup:
            stuck += 1
            continue
        N = [v for v in range(len(pts))
             if abs(math.hypot(pts[v][0] - w[0], pts[v][1] - w[1]) - 1.0) <= TOL]
        tri = False
        for a_ in range(len(N)):
            for b_ in range(a_ + 1, len(N)):
                if abs(math.hypot(pts[N[a_]][0] - pts[N[b_]][0],
                                  pts[N[a_]][1] - pts[N[b_]][1]) - 1.0) <= TOL:
                    tri = True
                    break
            if tri:
                break
        if tri:
            stuck += 1
            continue
        idx = len(pts)
        pts.append(w)
        adj.append(set())
        for v in N:
            adj[idx].add(v)
            adj[v].add(idx)
        stuck = 0
    return pts, adj


def main():
    res = {}
    # ---- controls ----
    log("control: regular pentagon C5")
    R5 = 1.0 / (2 * math.sin(math.pi / 5))
    c5pts = [(R5 * math.cos(2 * math.pi * i / 5), R5 * math.sin(2 * math.pi * i / 5))
             for i in range(5)]
    c5 = unit_adj(c5pts)
    r2, n2 = dsatur_kcolorable(c5, 2, budget=100000)
    r3, n3 = dsatur_kcolorable(c5, 3, budget=100000)
    res["C5"] = {"n": 5, "m": n_edges(c5), "triangle": find_triangle(c5),
                 "not_2color": (r2 is False), "color3": (r3 is True),
                 "bipartite": is_bipartite(c5)}

    log("control: Moser spindle")
    phi = 2 * math.asin(1 / (2 * math.sqrt(3)))

    def rot(p, a):
        c, s = math.cos(a), math.sin(a)
        return (p[0] * c - p[1] * s, p[0] * s + p[1] * c)

    A = (0.0, 0.0)
    B = (1.0, 0.0)
    C = (0.5, SQ3 / 2)
    D = (1.5, SQ3 / 2)
    moser_pts = [A, B, C, D, rot(B, phi), rot(C, phi), rot(D, phi)]
    moser = unit_adj(moser_pts)
    m3, m3n = dsatur_kcolorable(moser, 3, budget=100000)
    m4, m4n = dsatur_kcolorable(moser, 4, budget=100000)
    res["Moser"] = {"n": 7, "m": n_edges(moser),
                    "triangle": find_triangle(moser),
                    "not_3color": (m3 is False), "not_3color_nodes": m3n,
                    "color4": (m4 is True)}

    log("control: abstract Mycielski M4/M5")
    K2 = [set([1]), set([0])]
    M3 = mycielski(K2)
    M4 = mycielski(M3)
    M5 = mycielski(M4)
    t4, t4n = dsatur_kcolorable(M4, 3, budget=2000000)
    c4, c4n = dsatur_kcolorable(M4, 4, budget=2000000)
    g5 = greedy_best(M5, trials=30, seed=1)
    u5, u5n = dsatur_kcolorable(M5, 4, budget=800000, time_limit=90.0)
    res["M4"] = {"n": len(M4), "m": n_edges(M4),
                 "triangle": find_triangle(M4),
                 "not_3color": (t4 is False), "color4": (c4 is True),
                 "bipartite": is_bipartite(M4)}
    res["M5"] = {"n": len(M5), "m": n_edges(M5),
                 "triangle": find_triangle(M5),
                 "greedy_colors": g5, "bipartite": is_bipartite(M5),
                 "dsatur4": ("UNSAT" if u5 is False else
                             ("SAT" if u5 is True else "TIMEOUT/BUDGET")),
                 "dsatur4_nodes": u5n}

    # ---- recovery: SA re-embeds the small controls ----
    log("recovery: SA embed C5")
    s, c = sa_embed(c5, restarts=3, iters=3000, seed=11)
    res["SA_C5"] = {"stress": s, "verify": verify_embedding(c, c5)}
    log("recovery: SA embed Moser")
    s, c = sa_embed(moser, restarts=3, iters=4000, seed=22)
    res["SA_Moser"] = {"stress": s, "verify": verify_embedding(c, moser)}

    # ---- attempt 2: embed abstract triangle-free chromatic graphs ----
    log("attempt: SA embed M4 (11v, triangle-free, chi=4)")
    s, c = sa_embed(M4, restarts=8, iters=8000, seed=33)
    res["SA_M4"] = {"stress": s, "verify": verify_embedding(c, M4)}
    log("attempt: SA embed M5 (23v, triangle-free, chi=5)")
    s, c = sa_embed(M5, restarts=8, iters=12000, seed=44)
    res["SA_M5"] = {"stress": s, "verify": verify_embedding(c, M5)}

    # ---- attempt 1: random triangle-free assembly ----
    log("attempt: random triangle-free assembly")
    grows = []
    cfgs = [(60, 101, 0.7), (60, 102, 0.85), (100, 103, 0.7),
            (100, 104, 0.85), (150, 105, 0.8), (200, 106, 0.8)]
    for target_n, seed, dp in cfgs:
        pts, adj = grow_triangle_free(target_n, seed, double_prob=dp)
        tri = find_triangle(adj)
        g = greedy_best(adj, trials=10, seed=seed)
        d4, d4n = dsatur_kcolorable(adj, 4, budget=300000, time_limit=30.0)
        grows.append({"seed": seed, "target": target_n, "n": len(pts),
                      "m": n_edges(adj), "triangle": tri,
                      "greedy_colors": g, "bipartite": is_bipartite(adj),
                      "dsatur4": ("SAT" if d4 is True else
                                  ("UNSAT" if d4 is False else "TIMEOUT")),
                      "dsatur4_nodes": d4n})
        log("grown n=%d m=%d greedy=%s dsatur4=%s" %
            (len(pts), n_edges(adj), g, grows[-1]["dsatur4"]))
    res["grows"] = grows

    with open("output/artifacts/exp1_results.json", "w") as f:
        json.dump(res, f, indent=1)
    log("done. results -> output/artifacts/exp1_results.json")
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
