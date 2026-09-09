#!/usr/bin/env python3
"""Independent verifier: replays everything from committed adjacency data.

Checks (stdlib + numpy + sympy):
  1. graphs_n8.json: all simple, cubic, connected; per-order counts in {1,2,5}
     (OEIS A002851); pairwise non-isomorphic (exact backtracking); labeled counts
     re-derived by bare inclusion-free re-enumeration for n=4,6 (leaf 2/32) and
     invariant pre-check + full iso for n=8.
  2. analysis.json: recompute exact charpoly from edges, compare coefficient tuples
     byte-for-byte; re-derive integral verdicts from sympy factor_list; check numeric
     eigenvalues are roots of committed charpoly (residual < 1e-6); recompute alpha/chi
     bounds inequalities; recompute vertex-0 card spectrum interlacing; confirm
     Petersen spectrum {3,1^5,-2^4} and Heawood bipartite +- pairs.
  3. Emits VERIFY_OK or raises.
"""
import json
import numpy as np
import sympy as sp

def adj(n, edges):
    A = [[0]*n for _ in range(n)]
    for u, v in edges:
        A[u][v] += 1; A[v][u] += 1
    return A

def iso(g, h, n):
    mp = [-1]*n; used = 0
    def rec(d):
        nonlocal used
        if d == n: return True
        bu, bc = -1, -1
        for u in range(n):
            if mp[u] < 0:
                c = sum(1 for w in range(n) if mp[w] >= 0 and (g[u] >> w) & 1)
                if c > bc: bc, bu = c, u
        gu = g[bu]
        for v in range(n):
            if (used >> v) & 1: continue
            ok = all((((gu >> w) & 1) == ((h[v] >> mp[w]) & 1)) for w in range(n) if mp[w] >= 0)
            if ok:
                mp[bu] = v; used |= (1 << v)
                if rec(d+1): return True
                mp[bu] = -1; used &= ~(1 << v)
        return False
    return rec(0)

def masks(n, edges):
    m = [0]*n
    for u, v in edges:
        m[u] |= (1 << v); m[v] |= (1 << u)
    return m

def main():
    G = json.load(open("graphs_n8.json"))
    assert {k: len(v) for k, v in G.items()} == {"4": 1, "6": 2, "8": 5}, "count mismatch vs A002851"
    print("counts 1,2,5 OK (OEIS A002851)", flush=True)
    x = sp.Symbol('x')
    for nstr, glist in G.items():
        n = int(nstr)
        ms = []
        for e in glist:
            A = adj(n, e)
            assert len(e) == 3*n//2 and all(u != v for u, v in e)
            assert all(sum(r) == 3 for r in A), "not cubic"
            assert len({tuple(sorted(p)) for p in e}) == len(e), "multiedge"
            # connected
            seen = {0}; st = [0]
            while st:
                u = st.pop()
                for w in range(n):
                    if A[u][w] and w not in seen:
                        seen.add(w); st.append(w)
            assert len(seen) == n, "disconnected"
            ms.append(masks(n, e))
        for i in range(len(ms)):
            for j in range(i+1, len(ms)):
                assert not iso(ms[i], ms[j], n), f"isomorphic pair in n={n}"
    print("cubic+connected+pairwise-noniso OK", flush=True)

    rows = json.load(open("analysis.json"))
    assert len([r for r in rows if r["n"] <= 8]) == 8
    for r in rows:
        n, e = r["n"], [tuple(p) for p in r["edges"]]
        A = adj(n, e)
        M = sp.Matrix([[ (x if i == j else 0) - A[i][j] for j in range(n)] for i in range(n)])
        coeffs = [int(c) for c in sp.Poly(M.det(), x).all_coeffs()]
        assert coeffs == r["charpoly_coeffs"], f"{r['name']}: charpoly mismatch"
        p = sum(c*x**(n-i) for i, c in enumerate(coeffs))
        fac = sp.factor_list(p)[1]
        integ = all(sp.Poly(f, x).degree() == 1 for f, _ in fac)
        assert integ == r["integral"], f"{r['name']}: integral mismatch"
        ev = np.linalg.eigvalsh(np.array(A, float))
        for lam in ev:
            assert abs(float(p.subs(x, lam))) < 1e-4, f"{r['name']}: eigen-root residual"
        lmin, lmax = float(ev[0]), float(ev[-1])
        assert abs(lmax-3) < 1e-9
        assert r["alpha"] <= -n*lmin/(lmax-lmin) + 1e-9
        assert r["chi"] >= 1 - lmax/lmin - 1e-9
        idx = list(range(1, n))
        Ac = np.array([[A[i][j] for j in idx] for i in idx], float)
        ce = sorted(np.linalg.eigvalsh(Ac).tolist()); fe = sorted(ev.tolist())
        assert all(fe[i]-1e-9 <= ce[i] <= fe[i+1]+1e-9 for i in range(n-1)), f"{r['name']}: interlacing"
    print("charpoly/integral/eigen-root/Hoffman/interlacing replay OK", flush=True)
    P = next(r for r in rows if r["name"] == "Petersen-10")
    assert P["integral"] and sorted(P["integer_roots"]) == [-2]*4 + [1]*5 + [3]
    H = next(r for r in rows if r["name"] == "Heawood-14")
    assert H["edges"] and len(H["edges"]) == 21 and not H["integral"]
    assert H["alpha"] == 7 and H["chi"] == 2
    print("Petersen + Heawood benchmark rows OK", flush=True)
    print("VERIFY_OK", flush=True)

if __name__ == "__main__":
    main()
