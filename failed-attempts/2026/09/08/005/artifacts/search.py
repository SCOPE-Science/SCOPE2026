"""Frame-fixed exhaustive complete-arc census for PG(2,5), PG(2,7),
plus maximal witnesses (hyperoval q=8, oval q=9), stabilizers, secant
distributions, blocking-set separation. Stdlib only."""
import json, itertools, os, csv, time

HERE = os.path.dirname(os.path.abspath(__file__))

class Fld:
    def __init__(self, q): self.q = q
    def add(self, a, b):
        q = self.q
        if q in (5, 7): return (a + b) % q
        if q == 8: return a ^ b
        return ((a % 3) + (b % 3)) % 3 + 3 * (((a // 3) + (b // 3)) % 3)
    def neg(self, a):
        q = self.q
        if q in (5, 7): return (-a) % q
        if q == 8: return a
        return ((-(a % 3)) % 3) + 3 * ((-(a // 3)) % 3)
    def sub(self, a, b): return self.add(a, self.neg(b))
    def mul(self, a, b):
        q = self.q
        if q in (5, 7): return (a * b) % q
        if q == 8:
            p = 0
            while b:
                if b & 1: p ^= a
                a <<= 1
                if a & 8: a ^= 0xB  # t^3+t+1
                b >>= 1
            return p & 7
        a0, a1, b0, b1 = a % 3, a // 3, b % 3, b // 3
        return (a0 * b0 + 2 * a1 * b1) % 3 + 3 * ((a0 * b1 + a1 * b0) % 3)
    def inv(self, a):
        assert a != 0
        q = self.q
        if q in (5, 7): return pow(a, -1, q)
        if q == 8:
            for x in range(1, 8):
                if self.mul(a, x) == 1: return x
            raise AssertionError
        a0, a1 = a % 3, a // 3
        n = (a0 * a0 + a1 * a1) % 3
        ni = pow(n, -1, 3)
        return (a0 * ni) % 3 + 3 * ((-a1 * ni) % 3)
    def frob(self, a, s=1):
        for _ in range(s):
            if self.q == 8: a = self.mul(a, a)
            elif self.q == 9: a = (a % 3) + 3 * ((-(a // 3)) % 3)
        return a

def norm(F, v):
    for x in v:
        if x != 0:
            xi = F.inv(x)
            return tuple(F.mul(xi, y) for y in v)
    raise ValueError("zero vector")

def mat_inv(F, M):
    (a, b, c), (d, e, f), (g, h, i) = M
    A = F.sub(F.mul(e, i), F.mul(f, h)); B = F.sub(F.mul(f, g), F.mul(d, i))
    C = F.sub(F.mul(d, h), F.mul(e, g)); D = F.sub(F.mul(c, h), F.mul(b, i))
    E = F.sub(F.mul(a, i), F.mul(c, g)); G = F.sub(F.mul(b, g), F.mul(a, h))
    H = F.sub(F.mul(b, f), F.mul(c, e)); I = F.sub(F.mul(c, d), F.mul(a, f))
    J = F.sub(F.mul(a, e), F.mul(b, d))
    det = F.add(F.add(F.mul(a, A), F.mul(b, B)), F.mul(c, C))
    if det == 0: return None
    di = F.inv(det)
    return ((F.mul(A, di), F.mul(D, di), F.mul(H, di)),
            (F.mul(B, di), F.mul(E, di), F.mul(I, di)),
            (F.mul(C, di), F.mul(G, di), F.mul(J, di)))

def mat_vec(F, M, v):
    return tuple(F.add(F.add(F.mul(M[i][0], v[0]), F.mul(M[i][1], v[1])),
                       F.mul(M[i][2], v[2])) for i in range(3))

def mat_mul(F, A, B):
    return tuple(tuple(F.add(F.add(F.mul(A[i][0], B[0][j]),
                                     F.mul(A[i][1], B[1][j])),
                               F.mul(A[i][2], B[2][j])) for j in range(3))
                 for i in range(3))

def build(q):
    F = Fld(q)
    R = range(q if q in (5, 7) else (8 if q == 8 else 9))
    pts, seen = [], set()
    for x in R:
        for y in R:
            for z in R:
                if x == y == z == 0: continue
                v = norm(F, (x, y, z))
                if v not in seen:
                    seen.add(v); pts.append(v)
    n = len(pts)
    assert n == q * q + q + 1, (q, n)
    idx = {p: i for i, p in enumerate(pts)}
    lines, lseen = [], set()
    for a in R:
        for b in R:
            for c in R:
                if a == b == c == 0: continue
                w = norm(F, (a, b, c))
                if w in lseen: continue
                lseen.add(w)
                m, mem = 0, []
                for i, (x, y, z) in enumerate(pts):
                    if F.add(F.add(F.mul(w[0], x), F.mul(w[1], y)),
                             F.mul(w[2], z)) == 0:
                        m |= (1 << i); mem.append(i)
                assert len(mem) == q + 1, (q, len(mem))
                lines.append((m, mem, w))
    assert len(lines) == n, (q, len(lines))
    masks = [m for m, _, _ in lines]
    members = [mem for _, mem, _ in lines]
    cov = [w for _, _, w in lines]
    lt = [[-1] * n for _ in range(n)]
    for li, mem in enumerate(members):
        for a, b in itertools.combinations(mem, 2):
            assert lt[a][b] == -1 or lt[a][b] == li
            lt[a][b] = lt[b][a] = li
    return {"q": q, "F": F, "pts": pts, "idx": idx, "masks": masks,
            "members": members, "cov": cov, "lt": lt, "n": n,
            "FULL": (1 << n) - 1}

def frame_census(P):
    """Enumerate each arc containing fixed frame F exactly once.

    PGL(3,q) is transitive on ordered frames, so every k-arc (k>=4)
    is equivalent to one containing F; pool points (off all F-secants)
    in increasing-index order give each subset a unique construction path.
    Returns distinct-set counts per k (not tree nodes)."""
    F, n, masks, lt = P["F"], P["n"], P["masks"], P["lt"]
    idx, pts = P["idx"], P["pts"]
    e = [idx[norm(F, v)] for v in
         ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1))]
    cover0 = 0
    for a, b in itertools.combinations(e, 2):
        cover0 |= masks[lt[a][b]]
    pool = [i for i in range(n) if not (cover0 >> i) & 1]
    FULL = P["FULL"]
    arcs, comp, first = {}, {}, {}
    nodes = 0
    stack = [(0, [], cover0)]
    while stack:
        i, cho, cover = stack.pop()
        nodes += 1
        k = 4 + len(cho)
        arcs[k] = arcs.get(k, 0) + 1
        if cover == FULL:
            comp[k] = comp.get(k, 0) + 1
            if k not in first: first[k] = e + cho
        for j in range(i, len(pool)):
            p = pool[j]
            if (cover >> p) & 1:  # p on a secant of F+cho: arc-conflict
                continue
            nc = cover
            for a in e + cho:
                nc |= masks[lt[p][a]]
                if nc == FULL: break
            stack.append((j + 1, cho + [p], nc))
    return {"frame": e, "pool": pool, "nodes": nodes, "arcs": arcs,
            "comp": comp, "first": first}

def cover_map(P, H):
    masks, lt, FULL = P["masks"], P["lt"], P["FULL"]
    cover, wit = 0, {}
    for a, b in itertools.combinations(H, 2):
        li = lt[a][b]
        for t in P["members"][li]:
            if t not in H and t not in wit:
                wit[t] = [a, b]
        cover |= masks[li]
        if cover == FULL: break
    return cover, wit

def stab_order(P, H):
    F, pts, idx = P["F"], P["pts"], P["idx"]
    Hset = set(H)
    E = [pts[h] for h in H[:4]]
    S = ((E[0][0], E[1][0], E[2][0]), (E[0][1], E[1][1], E[2][1]),
         (E[0][2], E[1][2], E[2][2]))
    Sinv = mat_inv(F, S)
    av = mat_vec(F, Sinv, E[3])
    cnt = 0
    for tup in itertools.permutations(H, 4):
        T = [pts[t] for t in tup]
        Tm = ((T[0][0], T[1][0], T[2][0]), (T[0][1], T[1][1], T[2][1]),
              (T[0][2], T[1][2], T[2][2]))
        Tinv = mat_inv(F, Tm)
        bv = mat_vec(F, Tinv, T[3])
        # M = T diag(b) diag(a)^{-1} S^{-1}; D[i][j] = delta_ij b_i / a_i
        D = tuple(tuple((F.mul(bv[i], F.inv(av[i])) if i == j else 0)
                        for j in range(3)) for i in range(3))
        M = mat_mul(F, mat_mul(F, Tm, D), Sinv)
        if all(idx[norm(F, mat_vec(F, M, pts[h]))] in Hset for h in H):
            cnt += 1
    return cnt

def pgamma_stab(P, H, deg):
    F, pts, idx = P["F"], P["pts"], P["idx"]
    total = 0
    for s in range(deg):
        Hs = [idx[norm(F, tuple(F.frob(c, s) for c in pts[h]))] for h in H]
        # count M in PGL with M(Hs)=H via frames: base frame of Hs -> frames of H
        E = [pts[h] for h in Hs[:4]]
        S = ((E[0][0], E[1][0], E[2][0]), (E[0][1], E[1][1], E[2][1]),
             (E[0][2], E[1][2], E[2][2]))
        Sinv = mat_inv(F, S)
        av = mat_vec(F, Sinv, E[3])
        Hset = set(H)
        for tup in itertools.permutations(H, 4):
            T = [pts[t] for t in tup]
            Tm = ((T[0][0], T[1][0], T[2][0]), (T[0][1], T[1][1], T[2][1]),
                  (T[0][2], T[1][2], T[2][2]))
            Tinv = mat_inv(F, Tm)
            bv = mat_vec(F, Tinv, T[3])
            D = tuple(tuple((F.mul(bv[i], F.inv(av[i])) if i == j else 0)
                            for j in range(3)) for i in range(3))
            M = mat_mul(F, mat_mul(F, Tm, D), Sinv)
            if all(idx[norm(F, mat_vec(F, M, pts[h]))] in Hset for h in Hs):
                total += 1
    return total

def secant_dist(P, H):
    Hmask = sum(1 << h for h in H)
    d = {0: 0, 1: 0, 2: 0, "max": 0}
    skew = []
    for li, m in enumerate(P["masks"]):
        c = bin(m & Hmask).count("1")
        d[c] = d.get(c, 0) + 1
        d["max"] = max(d["max"], c)
        if c == 0: skew.append(li)
    return d, skew

def count_arcs_in_set(P, S, target):
    """Count target-sized arcs contained in point set S (plain DFS)."""
    S = sorted(S)
    lt, masks = P["lt"], P["masks"]
    cnt, nodes = [0], [0]
    stack = [(0, [], 0)]
    while stack:
        pos, cho, forbid = stack.pop()
        nodes[0] += 1
        if len(cho) == target:
            cnt[0] += 1
            continue
        if pos == len(S): continue
        if len(cho) + (len(S) - pos) < target: continue
        stack.append((pos + 1, cho, forbid))
        p = S[pos]
        if not (forbid >> p) & 1:
            nf = forbid
            for a in cho: nf |= masks[lt[p][a]]
            stack.append((pos + 1, cho + [p], nf))
    return cnt[0], nodes[0]

def main():
    t0 = time.time()
    out = {"planes": {}, "spectra": {}}
    built = {}
    for q in (5, 7, 8, 9):
        t = time.time()
        built[q] = build(q)
        print(f"built PG(2,{q}): n={built[q]['n']} "
              f"lines={len(built[q]['masks'])} t={time.time()-t:.1f}s", flush=True)
    for q in (5, 7):
        P = built[q]
        t = time.time()
        c = frame_census(P)
        S = sorted(c["comp"])
        e1 = P["idx"][norm(P["F"], (1, 0, 0))]
        e2 = P["idx"][norm(P["F"], (0, 1, 0))]
        e3 = P["idx"][norm(P["F"], (0, 0, 1))]
        small_cov = {}
        for k, H in ((1, [e1]), (2, [e1, e2]), (3, [e1, e2, e3])):
            cv, _ = cover_map(P, H)
            small_cov[k] = (cv != P["FULL"])
        reps = {}
        for k in S:
            H = c["first"][k]
            cv, wit = cover_map(P, H)
            assert cv == P["FULL"]
            sd, skew = secant_dist(P, H)
            reps[str(k)] = {
                "idx": H, "coords": [list(P["pts"][h]) for h in H],
                "stabilizer_PGL": stab_order(P, H),
                "secants": {str(i): sd[i] for i in (0, 1, 2)},
                "cover_witness": {str(t): wit[t] for t in wit},
                "n_skew": len(skew)}
        out["spectra"][str(q)] = {
            "n": P["n"], "spectrum": S,
            "frame": c["frame"], "pool_size": len(c["pool"]),
            "dfs_nodes": c["nodes"],
            "arcs_containing_frame_per_k": {str(k): v for k, v in c["arcs"].items()},
            "complete_containing_frame_per_k": {str(k): v for k, v in c["comp"].items()},
            "small_sizes_123_all_incomplete": small_cov,
            "reps": reps,
            "census_time_s": round(time.time() - t, 1)}
        print(f"q={q} S={S} nodes={c['nodes']} pool={len(c['pool'])} "
              f"arcs={c['arcs']} comp={c['comp']} t={time.time()-t:.1f}s", flush=True)
    # ---- maximal witnesses q=8 (hyperoval), q=9 (oval) ----
    for q in (8, 9):
        P = built[q]
        F, idx = P["F"], P["idx"]
        H = set()
        R = range(8 if q == 8 else 9)
        for u in R:
            H.add(idx[norm(F, (F.mul(u, u), u, 1))])
        H.add(idx[norm(F, (1, 0, 0))])
        if q == 8:
            H.add(idx[norm(F, (0, 1, 0))])  # nucleus
        H = sorted(H)
        assert len(H) == 10, (q, len(H))
        cv, wit = cover_map(P, H)
        sd, skew = secant_dist(P, H)
        assert sd["max"] <= 2 and cv == P["FULL"]
        st = stab_order(P, H)
        gst = pgamma_stab(P, H, 3 if q == 8 else 2)
        # blocking sets: line 0, and triangle (X=0,Y=0,Z=0) minus vertices
        B = list(P["members"][0])
        # covector lines X=0,Y=0,Z=0
        li = {}
        for j, w in enumerate(P["cov"]):
            if w in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
                li[w] = j
        l1, l2, l3 = (li[(1, 0, 0)], li[(0, 1, 0)], li[(0, 0, 1)])
        m1, m2, m3 = P["masks"][l1], P["masks"][l2], P["masks"][l3]
        v12, v13, v23 = m1 & m2, m1 & m3, m2 & m3
        assert v12 != v13 and v13 != v23 and v12 != v23
        Tmask = (m1 | m2 | m3) & ~v12 & ~v13 & ~v23 & P["FULL"]
        T = [t for t in range(P["n"]) if (Tmask >> t) & 1]
        # blocking checks
        def hits_all(S):
            Sm = sum(1 << s for s in S)
            return all((m & Sm) != 0 for m in P["masks"])
        assert hits_all(B) and hits_all(T)
        contains_line_T = any((m & ~Tmask & P["FULL"]) == 0 for m in P["masks"])
        assert not contains_line_T
        t = time.time()
        noval, tnodes = count_arcs_in_set(P, T, 10)
        tdt = time.time() - t
        out[f"q{q}"] = {
            "n": P["n"], "H": H, "H_coords": [list(P["pts"][h]) for h in H],
            "complete": True, "secants": {str(i): sd[i] for i in (0, 1, 2)},
            "skew_lines": skew,
            "skew_example_members": P["members"][skew[0]],
            "stabilizer_PGL": st, "stabilizer_PGammaL": gst,
            "cover_witness": {str(x): wit[x] for x in wit},
            "blocking_line": B, "triangle_lines": [l1, l2, l3],
            "triangle_set": T,
            "triangle_coords": [list(P["pts"][x]) for x in T],
            "triangle_contains_line": contains_line_T,
            "triangle_10arcs": noval, "triangle_dfs_nodes": tnodes,
            "triangle_check_s": round(tdt, 1)}
        print(f"q={q} |H|=10 stab={st} pgamma={gst} sec={sd} "
              f"|T|={len(T)} 10arcs_in_T={noval} ({tnodes} nodes, {tdt:.1f}s)",
              flush=True)
    # CSVs
    for q in (5, 7, 8, 9):
        P = built[q]
        with open(os.path.join(HERE, f"points_q{q}.csv"), "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["idx", "x", "y", "z"])
            for i, p in enumerate(P["pts"]):
                w.writerow([i, p[0], p[1], p[2]])
        with open(os.path.join(HERE, f"lines_q{q}.csv"), "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["idx", "a", "b", "c", "members"])
            for j in range(P["n"]):
                w.writerow([j, P["cov"][j][0], P["cov"][j][1], P["cov"][j][2],
                            " ".join(map(str, P["members"][j]))])
    with open(os.path.join(HERE, "witnesses.json"), "w") as f:
        json.dump(out, f)
    print(f"TOTAL t={time.time()-t0:.1f}s; wrote witnesses.json", flush=True)

if __name__ == "__main__":
    main()
