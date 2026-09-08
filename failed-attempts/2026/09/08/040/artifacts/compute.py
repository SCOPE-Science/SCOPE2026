"""Exact Hochster + matching certificates (stdlib primary, sympy independent replay)."""
import itertools, json, math, os

ART = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-137/output/artifacts"

def adj(n, edges):
    A = [[False]*n for _ in range(n)]
    for a, b in edges:
        A[a][b] = A[b][a] = True
    return A

def connected(n, edges):
    A = adj(n, edges)
    seen = {0}; st = [0]
    while st:
        u = st.pop()
        for v in range(n):
            if A[u][v] and v not in seen:
                seen.add(v); st.append(v)
    return len(seen) == n

def all_matchings(n, edges):
    m = len(edges); out = []
    for mask in range(1 << m):
        used = set(); ok = True; cur = []
        for i in range(m):
            if (mask >> i) & 1:
                a, b = edges[i]
                if a in used or b in used:
                    ok = False; break
                used.add(a); used.add(b); cur.append((a, b))
        if ok:
            out.append((cur, used))
    return out

def max_matching(n, edges):
    best = 0; wit = []
    for cur, used in all_matchings(n, edges):
        if len(cur) > best:
            best = len(cur); wit = list(cur)
    return best, wit

def min_maximal_matching(n, edges):
    best = None; wit = None
    for cur, used in all_matchings(n, edges):
        maximal = True
        for (a, b) in edges:
            if a not in used and b not in used:
                maximal = False; break
        if maximal and (best is None or len(cur) < best):
            best = len(cur); wit = list(cur)
    return best, wit

def max_induced_matching(n, edges):
    A = adj(n, edges); m = len(edges)
    eset = set(edges) | set((b, a) for (a, b) in edges)
    best = 0; wit = []
    for mask in range(1 << m):
        sel = [edges[i] for i in range(m) if (mask >> i) & 1]
        verts = set(); ok = True
        for a, b in sel:
            if a in verts or b in verts:
                ok = False; break
            verts.add(a); verts.add(b)
        if not ok:
            continue
        for (a, b) in edges:
            if (a, b) in sel or (b, a) in sel:
                continue
            if a in verts and b in verts:
                ok = False; break
        if ok and len(sel) > best:
            best = len(sel); wit = list(sel)
    return best, wit

def rank_frac(mat):
    from fractions import Fraction
    if not mat or not mat[0]:
        return 0
    M = [[Fraction(x) for x in row] for row in mat]
    R, C = len(M), len(M[0])
    r = 0
    for c in range(C):
        piv = None
        for i in range(r, R):
            if M[i][c] != 0:
                piv = i; break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = M[r][c]
        for j in range(c, C):
            M[r][j] /= inv
        for i in range(R):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                for j in range(c, C):
                    M[i][j] -= f * M[r][j]
        r += 1
        if r == R:
            break
    return r

def rank_sympy(mat):
    from sympy import Matrix
    if not mat or not mat[0]:
        return 0
    return int(Matrix(mat).rank())

def reduced_homology_dims(verts, is_indep, rankfn):
    V = list(verts); t = len(V)
    if t == 0:
        return {-1: 1}
    faces = {}
    for mask in range(1, 1 << t):
        S = frozenset(V[i] for i in range(t) if (mask >> i) & 1)
        if is_indep(S):
            d = len(S) - 1
            faces.setdefault(d, []).append(tuple(sorted(S)))
    for d in faces:
        faces[d].sort()
    maxd = max(faces) if faces else -1
    def bmat(d):
        if d <= 0:
            return []
        lo = faces.get(d-1, []); hi = faces.get(d, [])
        if not hi or not lo:
            return []
        pos = {f: i for i, f in enumerate(lo)}
        M = [[0]*len(hi) for _ in lo]
        for j, f in enumerate(hi):
            for k in range(len(f)):
                g = tuple(x for l, x in enumerate(f) if l != k)
                M[pos[g]][j] += 1 if k % 2 == 0 else -1
        return M
    ranks = {}
    for d in range(1, maxd+1):
        ranks[d] = rankfn(bmat(d))
    dims = {}
    n0 = len(faces.get(0, []))
    r1 = ranks.get(1, 0)
    h0 = (n0 - r1 - 1) if n0 > 0 else 0
    if h0:
        dims[0] = h0
    for d in range(1, maxd+1):
        nd = len(faces.get(d, []))
        rd = ranks.get(d, 0); rd1 = ranks.get(d+1, 0)
        hd = nd - rd - rd1
        if hd:
            dims[d] = hd
    return dims

def betti_hochster(n, edges, rankfn):
    A = adj(n, edges)
    def indep(S):
        L = list(S)
        for i in range(len(L)):
            for j in range(i+1, len(L)):
                if A[L[i]][L[j]]:
                    return False
        return True
    betti = {}
    for mask in range(1 << n):
        W = [v for v in range(n) if (mask >> v) & 1]
        j = len(W)
        H = reduced_homology_dims(W, indep, rankfn)
        for k, d in H.items():
            i = j - k - 1
            if i < 0 or d == 0:
                continue
            betti[(i, j)] = betti.get((i, j), 0) + d
    betti[(0, 0)] = 1
    return betti

def euler_replay(n, edges):
    A = adj(n, edges)
    def indep(S):
        L = list(S)
        for i in range(len(L)):
            for j in range(i+1, len(L)):
                if A[L[i]][L[j]]:
                    return False
        return True
    bad = 0; tot = 0
    for mask in range(1 << n):
        W = [v for v in range(n) if (mask >> v) & 1]
        if not W:
            continue
        f = 0
        for m2 in range(1, 1 << len(W)):
            S = frozenset(W[i] for i in range(len(W)) if (m2 >> i) & 1)
            if indep(S):
                f += (-1) ** (len(S) - 1)
        H = reduced_homology_dims(W, indep, rank_frac)
        h = sum(((-1) ** k) * d for k, d in H.items())
        tot += 1
        if f - 1 != h:
            bad += 1
    return tot, bad

if __name__ == "__main__":
    os.makedirs(ART, exist_ok=True)
    K7 = [(a, b) for a in range(7) for b in range(a+1, 7)]
    K8 = [(a, b) for a in range(8) for b in range(a+1, 8)]
    G7 = [(0, 1), (2, 3), (4, 5), (6, 1), (6, 3), (6, 5)]
    G8 = [(0, 1), (2, 3), (4, 5), (6, 1), (6, 3), (6, 5), (7, 0)]
    graphs = {"K7": (7, K7), "K8": (8, K8), "G7reg": (7, G7), "G8reg": (8, G8)}
    out = {}
    for name, (n, E) in graphs.items():
        im, imw = max_induced_matching(n, E)
        mm, mmw = max_matching(n, E)
        mmm, mmmw = min_maximal_matching(n, E)
        B1 = betti_hochster(n, E, rank_frac)
        B2 = betti_hochster(n, E, rank_sympy)
        agree = (B1 == B2)
        reg = max((j - i for (i, j), v in B1.items() if v), default=0)
        pd = max((i for (i, j) in B1), default=0)
        tot, bad = euler_replay(n, E)
        rec = {"n": n, "edges": E, "connected": connected(n, E),
               "im": im, "im_witness": imw, "matching_number": mm,
               "matching_witness": mmw, "min_match": mmm,
               "min_match_witness": mmmw,
               "betti": sorted([[i, j, v] for (i, j), v in B1.items()]),
               "reg": reg, "pd": pd,
               "hochster_two_pipeline_agree": agree,
               "euler_subsets": tot, "euler_mismatches": bad}
        out[name] = rec
        print(name, "conn=", rec["connected"], "im=", im, "match=", mm,
              "minmatch=", mmm, "reg=", reg, "pd=", pd,
              "agree=", agree, "euler_bad=", bad)
        print("  betti:", rec["betti"])
    # closed form check for complete graphs
    for name, n in (("K7", 7), ("K8", 8)):
        expect = {(i, i+1): math.comb(n, i+1) * i for i in range(1, n)}
        got = {(i, j): v for [[i, j, v]] in
               [[[a, b, c]] for [a, b, c] in out[name]["betti"]][0:0]} if False else \
              {(i, j): v for [i, j, v] in out[name]["betti"] if not (i == 0 and j == 0)}
        ok = all(got.get(k, 0) == v for k, v in expect.items()) and \
             all(expect.get(k, 0) == v for k, v in got.items())
        out[name]["closed_form_match"] = ok
        print(name, "closed-form match:", ok)
    with open(os.path.join(ART, "betticensus.json"), "w") as f:
        json.dump(out, f, indent=1)
    print("wrote betticensus.json")
