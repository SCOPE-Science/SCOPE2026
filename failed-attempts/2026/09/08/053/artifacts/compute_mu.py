"""Exact minimal faithful permutation degree mu(G) for an explicit benchmark
family of 2-groups (orders 32 and 64), from-scratch stdlib Python.

mu(G) = min sum of [G:H_i] over subgroup families with trivial core
intersection (Johnson). Faithfulness <=> intersection of cores is trivial;
kernel of the disjoint-union coset action = intersection of the cores.

Groups are realized as explicit Cayley tables with machine-checked group
axioms (exhaustive associativity, identity, inverses). Subgroups are
enumerated by adjunction-closure DFS (complete: every subgroup is reached).
Cores are brute-force conjugate intersections. mu is an exact shortest-path
(Dijkstra) over the normal-subgroup intersection lattice:
  dist[G]=0; dist[N & C] <= dist[N] + best_index[C].
Optimality is therefore exact, and replayed by verify.py.
"""
import itertools, json, heapq

def check_group(mul):
    n = len(mul)
    assert all(len(r) == n for r in mul)
    # identity: element e with e*g=g*e=g for all g
    ids = [e for e in range(n) if all(mul[e][g] == g and mul[g][e] == g for g in range(n))]
    assert len(ids) == 1, "identity not unique"
    e = ids[0]
    assert e == 0
    inv = [None]*n
    for g in range(n):
        hs = [h for h in range(n) if mul[g][h] == 0 and mul[h][g] == 0]
        assert len(hs) == 1, f"inverse not unique for {g}"
        inv[g] = hs[0]
    for a in range(n):
        for b in range(n):
            ab = mul[a][b]
            for c in range(n):
                assert mul[ab][c] == mul[a][mul[b][c]], f"assoc fails {a},{b},{c}"
    return inv

def build_abelian(cyc):
    elems = list(itertools.product(*[range(m) for m in cyc]))
    idx = {e: i for i, e in enumerate(elems)}
    n = len(elems)
    mul = [[0]*n for _ in range(n)]
    for i, a in enumerate(elems):
        for j, b in enumerate(elems):
            mul[i][j] = idx[tuple((x+y) % m for x, y, m in zip(a, b, cyc))]
    return mul

def build_dihedral_like(m, u, s2):
    """(a,b) = r^a s^b. s r s^-1 = r^u, s^2 = r^s2. Requires u^2=1 mod m,
    u*s2 = s2 mod m (so s^2 central and presentation consistent)."""
    assert (u*u) % m == 1 and (u*s2) % m == s2 % m
    n = 2*m
    def I(a, b): return (a % m) + (b % 2)*m
    mul = [[0]*n for _ in range(n)]
    for a in range(m):
        for b in (0, 1):
            for c in range(m):
                for d in (0, 1):
                    if b == 0:
                        mul[I(a,b)][I(c,d)] = I(a+c, d)
                    else:
                        if d == 0:
                            mul[I(a,b)][I(c,d)] = I(a+u*c, 1)
                        else:
                            mul[I(a,b)][I(c,d)] = I(a+u*c+s2, 0)
    return mul

def build_direct(A, B):
    n1, n2 = len(A), len(B)
    n = n1*n2
    mul = [[0]*n for _ in range(n)]
    for a in range(n1):
        for b in range(n2):
            for c in range(n1):
                for d in range(n2):
                    mul[a*n2+b][c*n2+d] = A[a][c]*n2 + B[b][d]
    return mul

def build_central_product(A, z1, B, z2):
    """(A x B) / diagonal {(1,1),(z1,z2)}; z1,z2 central involutions."""
    n1, n2 = len(A), len(B)
    assert A[z1][z1] == 0 and B[z2][z2] == 0
    for g in range(n1):
        assert A[z1][g] == A[g][z1]
    for g in range(n2):
        assert B[z2][g] == B[g][z2]
    def pmul(p, q): return (A[p[0]][q[0]], B[p[1]][q[1]])
    seen = {}
    reps = []
    for a in range(n1):
        for b in range(n2):
            if (a, b) in seen: continue
            twin = (A[z1][a], B[z2][b])
            cid = len(reps)
            reps.append((a, b))
            seen[(a, b)] = cid
            seen[twin] = cid
    n = len(reps)
    mul = [[0]*n for _ in range(n)]
    for i, p in enumerate(reps):
        for j, q in enumerate(reps):
            mul[i][j] = seen[pmul(p, q)]
    return mul

# ---------------- group library ----------------
C2 = build_abelian([2]); C4 = build_abelian([4]); C8 = build_abelian([8])
D8 = build_dihedral_like(4, -1, 0)
Q8 = build_dihedral_like(4, -1, 2)   # x^4=1,y^2=x^2 : quaternion order 8
D16 = build_dihedral_like(8, -1, 0)
Q16 = build_dihedral_like(8, -1, 4)
zD8 = 2   # r^2 in (a,b) indexing: (2,0) -> 2
zQ8 = 2   # x^2 -> 2
Ep32 = build_central_product(D8, zD8, D8, zD8)   # extraspecial + (D8*D8)
Em32 = build_central_product(D8, zD8, Q8, zQ8)   # extraspecial - (D8*Q8)

GROUPS = [
    # order 32
    ("C32", build_abelian([32]), "<t|t^32=1>"),
    ("C16xC2", build_abelian([16,2]), "<a,b|a^16=b^2=1,[a,b]=1>"),
    ("C8xC4", build_abelian([8,4]), "<a,b|a^8=b^4=1,[a,b]=1>"),
    ("C8xC2xC2", build_abelian([8,2,2]), "<a,b,c|a^8=b^2=c^2=1,abelian>"),
    ("C4xC4xC2", build_abelian([4,4,2]), "<a,b,c|a^4=b^4=c^2=1,abelian>"),
    ("C4xC2xC2xC2", build_abelian([4,2,2,2]), "<a,b,c,d|a^4=b^2=c^2=d^2=1,abelian>"),
    ("C2xC2xC2xC2xC2", build_abelian([2,2,2,2,2]), "<5 involutions, abelian>"),
    ("D32", build_dihedral_like(16,-1,0), "<r,s|r^16=s^2=1,srs=r^-1> (dihedral, order 32)"),
    ("SD32", build_dihedral_like(16,7,0), "<r,s|r^16=s^2=1,srs=r^7> (semidihedral, order 32)"),
    ("Q32", build_dihedral_like(16,-1,8), "<x,y|x^16=1,y^2=x^8,y^-1xy=x^-1> (generalized quaternion, order 32)"),
    ("D16xC2", build_direct(D16,C2), "D16 x C2"),
    ("Q16xC2", build_direct(Q16,C2), "Q16 x C2"),
    ("D8xC2xC2", build_direct(build_direct(D8,C2),C2), "D8 x C2 x C2"),
    ("Eplus32", Ep32, "(D8 * D8) central product (extraspecial +, order 32)"),
    ("Eminus32", Em32, "(D8 * Q8) central product (extraspecial -, order 32)"),
    # order 64
    ("C64", build_abelian([64]), "<t|t^64=1>"),
    ("C32xC2", build_abelian([32,2]), "<a,b|a^32=b^2=1,abelian>"),
    ("C16xC4", build_abelian([16,4]), "<a,b|a^16=b^4=1,abelian>"),
    ("C8xC8", build_abelian([8,8]), "<a,b|a^8=b^8=1,abelian>"),
    ("C4xC4xC4", build_abelian([4,4,4]), "<a,b,c|a^4=b^4=c^4=1,abelian>"),
    ("C4xC4xC2xC2", build_abelian([4,4,2,2]), "<a,b,c,d|a^4=b^4=c^2=d^2=1,abelian>"),
    ("C2^6", build_abelian([2]*6), "<6 involutions, abelian>"),
    ("D64", build_dihedral_like(32,-1,0), "<r,s|r^32=s^2=1,srs=r^-1> (dihedral, order 64)"),
    ("SD64", build_dihedral_like(32,15,0), "<r,s|r^32=s^2=1,srs=r^15> (semidihedral, order 64)"),
    ("Q64", build_dihedral_like(32,-1,16), "<x,y|x^32=1,y^2=x^16,y^-1xy=x^-1> (gen. quaternion, order 64)"),
    ("D32xC2", build_direct(build_dihedral_like(16,-1,0),C2), "D32 x C2"),
    ("D16xC4", build_direct(D16,C4), "D16 x C4"),
    ("Q32xC2", build_direct(build_dihedral_like(16,-1,8),C2), "Q32 x C2"),
    ("Eplus32xC2", build_direct(Ep32,C2), "(D8*D8) x C2 (order 64)"),
]

# ---------------- subgroup machinery (bitmasks) ----------------
def analyze(mul):
    n = len(mul)
    inv = check_group(mul)
    full = (1 << n) - 1
    def close_mask(mask):
        changed = True
        while changed:
            changed = False
            have = [g for g in range(n) if mask >> g & 1]
            for s in have:
                for t in have:
                    for h in (mul[s][t], inv[s]):
                        if not (mask >> h & 1):
                            mask |= (1 << h); changed = True
        return mask
    subs = {1}  # {identity}
    work = [1]
    while work:
        s = work.pop()
        for g in range(n):
            if s >> g & 1: continue
            t = close_mask(s | (1 << g))
            if t not in subs:
                subs.add(t); work.append(t)
    subs = sorted(subs, key=lambda m: (bin(m).count("1"), m))
    conj = [[mul[mul[g][h]][inv[g]] for h in range(n)] for g in range(n)]
    def conjugate_mask(mask, g):
        out = 0
        m = mask
        while m:
            lsb = m & (-m)
            h = lsb.bit_length()-1
            out |= (1 << conj[g][h])
            m ^= lsb
        return out
    def core(mask):
        c = full
        for g in range(n):
            c &= conjugate_mask(mask, g)
            if c == 1: break
        return c
    cores = {}
    for s in subs:
        cores[s] = core(s)
    return {"n": n, "inv": inv, "subs": subs, "cores": cores}

def min_degree(n, subs, cores):
    full = (1 << n) - 1
    pop = {s: bin(s).count("1") for s in subs}
    best = {}   # core -> (min index, witness subgroup)
    for s in subs:
        if s == full: continue
        idx = n // pop[s]
        c = cores[s]
        if c not in best or idx < best[c][0]:
            best[c] = (idx, s)
    INF = 10**18
    dist = {full: 0}
    prev = {}
    pq = [(0, full)]
    while pq:
        d, N = heapq.heappop(pq)
        if d != dist[N]: continue
        if N == 1: break
        for C, (idx, w) in best.items():
            M = N & C
            nd = d + idx
            if nd < dist.get(M, INF):
                dist[M] = nd; prev[M] = (N, C)
                heapq.heappush(pq, (nd, M))
    assert 1 in dist
    # reconstruct
    fam = []
    N = 1
    while N != full:
        P, C = prev[N]
        fam.append({"core": C, "index": best[C][0], "witness": best[C][1]})
        N = P
    return dist[1], fam

def mask_gens(mask, mul, inv):
    els = [g for g in range(len(mul)) if mask >> g & 1]
    for r in (1, 2, 3):
        for combo in itertools.combinations(els, r):
            if combo[0] != 0 and 0 in combo: continue
            m = 1
            changed = True
            while changed:
                changed = False
                have = [g for g in range(len(mul)) if m >> g & 1]
                for s in have:
                    for t in list(combo) + have:
                        for h in (mul[s][t], mul[t][s], inv[t]):
                            if not (m >> h & 1):
                                m |= (1 << h); changed = True
            if m == mask:
                return list(combo)
    return els

def main():
    out = {"groups": []}
    for name, mul, pres in GROUPS:
        n = len(mul)
        A = analyze(mul)
        mu, fam = min_degree(n, A["subs"], A["cores"])
        idxs = sorted(f["index"] for f in fam)
        inter = (1 << n) - 1
        for f in fam: inter &= f["core"]
        assert inter == 1, f"family not faithful for {name}"
        normals = sum(1 for s in A["subs"] if A["cores"][s] == s)
        fam_out = []
        for f in fam:
            fam_out.append({
                "index": f["index"],
                "order": n // f["index"],
                "gens": mask_gens(f["witness"], mul, A["inv"]),
                "witness_mask": f["witness"],
                "core_mask": f["core"],
                "core_order": bin(f["core"]).count("1"),
            })
        out["groups"].append({
            "name": name, "order": n, "presentation": pres,
            "n_subgroups": len(A["subs"]), "n_normal": normals,
            "mu": mu, "family_indices": idxs, "family": fam_out,
            "mul_flat": [c for row in mul for c in row],
        })
        print(f"{name:12s} order={n:3d} nsub={len(A['subs']):5d} nnormal={normals:4d} mu={mu:3d} idx={idxs}", flush=True)
    with open("output/artifacts/mu_results.json", "w") as f:
        json.dump(out, f)
    print("wrote output/artifacts/mu_results.json")

if __name__ == "__main__":
    main()
