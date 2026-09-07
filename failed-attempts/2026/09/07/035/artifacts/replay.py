"""Independent verifier for lane-56 Cayley census. Stdlib only (+numpy iff present).
Reads words.json, re-derives every certificate from the stored mult tables.
Exits 0 iff ALL rows PASS. Diameter/word checks are exact integer work.
Usage: python3 replay.py [path/to/words.json]
"""
import json
import sys

def closure(T, e, gens):
    seen = {e}
    stack = [e]
    while stack:
        g = stack.pop()
        for s in gens:
            h = T[g][s]
            if h not in seen:
                seen.add(h)
                stack.append(h)
    return seen

def bfs(T, src, S):
    n = len(T)
    dist = [-1] * n
    dist[src] = 0
    q = [src]
    i = 0
    while i < len(q):
        g = q[i]
        i += 1
        for s in S:
            h = T[g][s]
            if dist[h] == -1:
                dist[h] = dist[g] + 1
                q.append(h)
    return dist

def check_row(r):
    n = r["order"]
    T = r["mult"]
    assert len(T) == n and all(len(x) == n for x in T), "table shape"
    # identity at 0
    for i in range(n):
        assert T[0][i] == i and T[i][0] == i, "identity"
    # associativity (full, integer)
    for i in range(n):
        for j in range(n):
            ij = T[i][j]
            for k in range(n):
                assert T[ij][k] == T[i][T[j][k]], ("assoc", i, j, k)
    # inverses
    inv = []
    for i in range(n):
        hit = [j for j in range(n) if T[i][j] == 0 and T[j][i] == 0]
        assert len(hit) == 1, ("inverse", i)
        inv.append(hit[0])
    # nonabelian witness
    i, j = r["nonab_wit"]
    assert T[i][j] != T[j][i], "abelian?!"
    # generation
    a, b = r["gen_idx"]
    assert len(closure(T, 0, (a, b))) == n, "not generated"
    # symmetric generating set, no loops
    S = r["S"]
    assert 0 not in S, "loop"
    assert all(inv[s] in S for s in S), "not symmetric"
    assert len(S) == r["degree"], "degree"
    # BFS distances from identity match stored
    d0 = bfs(T, 0, S)
    assert d0 == r["dist0"], "dist0 mismatch"
    assert all(x >= 0 for x in d0), "disconnected"
    # all-pairs diameter exact
    D = 0
    for src in range(n):
        dd = bfs(T, src, S)
        assert all(x >= 0 for x in dd), "disconnected src"
        D = max(D, max(dd))
    assert D == r["diameter"] == max(d0), "diameter"
    # word certificates: letters a/A/b/B over (a,ainv,b,binv); a!=b as group
    # elements (else <a,b> cyclic, contradicting generation of nonabelian group)
    assert a != b, "a==b"
    ai, bi = inv[a], inv[b]
    mp = {'a': a}
    if ai != a:
        mp['A'] = ai
    # b is distinct from a and (cyclicity) from ai; bi may coincide with a/ai
    # only in cyclic case, excluded above, so b gets a fresh letter unless equal
    if b not in mp.values():
        mp['b'] = b
    if bi not in mp.values():
        mp['B'] = bi
    assert set(mp.values()) >= {a, b}, "letters must cover generators"
    for g in range(n):
        w = r["words"][g]
        assert len(w) == d0[g], ("word len", g)
        cur = 0
        for ch in w:
            cur = T[cur][mp[ch]]
        assert cur == g, ("word eval", g)
    w = r["witness_word"]
    assert len(w) == D, "witness length"
    cur = 0
    for ch in w:
        cur = T[cur][mp[ch]]
    assert cur == r["witness"], "witness eval"
    return {"D": D, "d": len(S)}

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "words.json"
    J = json.load(open(path))
    rows = J["rows"]
    ok = 0
    for r in rows:
        info = check_row(r)
        # spectral recheck
        spec = None
        try:
            import numpy as np
            n = r["order"]
            T = r["mult"]
            S = r["S"]
            A = np.zeros((n, n))
            for g in range(n):
                for s in S:
                    A[g, T[g][s]] = 1.0
            assert all(abs(A[g].sum() - r["degree"]) < 1e-12 for g in range(n))
            w, V = np.linalg.eigh(A)
            lam1, lam2 = float(w[-1]), float(w[-2])
            assert abs(lam1 - r["degree"]) < 1e-6, "top eig != degree"
            assert r["gap_lo"] - 1e-9 <= r["degree"] - lam2 <= r["gap_hi"] + 1e-9, "gap outside interval"
            assert abs(lam2 - r["lambda2_eigh"]) < 1e-6, "lambda2 changed"
            v = V[:, -2]
            resid = float(np.linalg.norm(A @ v - lam2 * v))
            assert resid < 1e-6, "residual"
            w2 = np.linalg.eig(A)[0]
            lam2b = sorted((complex(z).real for z in w2), reverse=True)[1]
            assert abs(lam2 - lam2b) < 1e-6, "cross-solver"
            spec = "gapOK"
        except ImportError:
            spec = "numpy-missing-gap-skipped"
        print(f"PASS {r['id']} {r['struct']} n={r['order']} d={info['d']} "
              f"D={info['D']} gap=[{r['gap_lo']:.6f},{r['gap_hi']:.6f}] {spec}")
        ok += 1
    # Lemma check: SD64 (R20) <-> Mod64 (R21) graph iso f(e,k)=(e,(-1)^e k)
    by = {r["id"]: r for r in rows}
    A_, B_ = by["R20"], by["R21"]
    assert A_["order"] == B_["order"] == 64
    TA, TB, SA, SB = A_["mult"], B_["mult"], A_["S"], B_["S"]
    def adj(T, S):
        return [set(T[g][s] for s in S) for g in range(64)]
    AA, BB = adj(TA, SA), adj(TB, SB)
    f = [(e * 32 + ((-k) % 32 if e == 1 else k)) for e in (0, 1) for k in range(32)]
    # note: els order is [(0,k)...,(1,k)...] so index of (e,k) is e*32+k
    assert sorted(f) == list(range(64)), "f bijective"
    for g in range(64):
        assert {f[h] for h in AA[g]} == BB[f[g]], ("iso intertwine", g)
    print("PASS lemma SD64-Mod64 Cayley-graph isomorphism (explicit intertwiner, stdlib check)")
    print(f"ALL {ok}/{len(rows)} rows PASS + lemma PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
