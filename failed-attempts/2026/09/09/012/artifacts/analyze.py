#!/usr/bin/env python3
"""Exact spectral analysis of census graphs + bonus named cubic graphs.

Reads graphs.json (or graphs_n8.json). For each graph:
  * adjacency matrix, exact characteristic polynomial (sympy, integer arithmetic)
  * factorisation over ZZ -> integral verdict (all factors linear)
  * numeric spectrum (numpy), lmin/lmax
  * Hoffman bounds: alpha <= -n*lmin/(lmax-lmin); chi >= 1 - lmax/lmin
  * exact alpha (bitmask MIS), exact chi (k-colouring backtrack)
  * Cauchy interlacing replay on vertex-0-deleted card (numeric, tol 1e-9)
  * cospectral grouping by coefficient tuple
Bonus named graphs (explicit edge lists, NOT part of census):
  * Petersen (n=10), Heawood (n=14, Fano incidence)
Writes analysis.json + prints SUMMARY table.
"""
import json, itertools, math, sys
import numpy as np
import sympy as sp

TOL = 1e-9

def adj_of(n, edges):
    A = [[0]*n for _ in range(n)]
    for u, v in edges:
        A[u][v] += 1
        A[v][u] += 1
    return A

def charpoly_coeffs(A):
    n = len(A)
    x = sp.Symbol('x')
    M = sp.Matrix([[ (x if i == j else 0) - A[i][j] for j in range(n)] for i in range(n)])
    p = M.det()  # exact integer arithmetic
    poly = sp.Poly(p, x)
    return [int(c) for c in poly.all_coeffs()]  # leading..constant

def integral_verdict(coeffs):
    x = sp.Symbol('x')
    n = len(coeffs) - 1
    p = sum(c * x**(n - i) for i, c in enumerate(coeffs))
    fac = sp.factor_list(p)[1]  # [(factor, mult)]
    linear = all(sp.Poly(f, x).degree() == 1 for f, _ in fac)
    roots = []
    if linear:
        for f, m in fac:
            r = sp.Poly(f, x).all_coeffs()
            # r = [a, b] -> root -b/a
            roots.extend([-int(r[1]) // int(r[0])] * m)
        roots.sort()
        roots = [int(r) for r in roots]
    return linear, [[str(f.as_expr()), int(m)] for f, m in fac], roots

def spectrum(A):
    return sorted(np.linalg.eigvalsh(np.array(A, dtype=float)).tolist())

def exact_alpha(n, edges):
    adj = [0]*n
    for u, v in edges:
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    best = 0
    for mask in range(1 << n):
        s = bin(mask).count('1')
        if s <= best:
            continue
        ok = True
        for u in range(n):
            if (mask >> u) & 1:
                if adj[u] & mask:
                    ok = False
                    break
        if ok:
            best = s
    return best

def exact_chi(n, edges):
    adj = [[False]*n for _ in range(n)]
    for u, v in edges:
        adj[u][v] = adj[v][u] = True
    order = sorted(range(n), key=lambda u: -sum(adj[u]))
    col = [-1]*n
    def can(k):
        def rec(i):
            if i == n:
                return True
            u = order[i]
            used = {col[w] for w in range(n) if adj[u][w] and col[w] >= 0}
            for c in range(k):
                if c not in used:
                    col[u] = c
                    if rec(i+1):
                        return True
                    col[u] = -1
            return False
        return rec(0)
    for k in range(1, n+1):
        for i in range(n):
            col[i] = -1
        if can(k):
            return k
    return n

def interlacing_ok(full, card):
    # full: ascending length n; card: ascending length n-1
    # need full[i] <= card[i] <= full[i+1]
    return all(full[i] - TOL <= card[i] <= full[i+1] + TOL for i in range(len(card)))

def analyze_one(name, n, edges):
    A = adj_of(n, edges)
    assert all(sum(r) == 3 for r in A), f"{name}: not cubic"
    coeffs = charpoly_coeffs(A)
    integ, fac, iroots = integral_verdict(coeffs)
    spec = spectrum(A)
    lmin, lmax = spec[0], spec[-1]
    assert abs(lmax - 3) < 1e-9, f"{name}: lmax={lmax}"
    hb_alpha = -n * lmin / (lmax - lmin)
    hb_chi = 1 - lmax / lmin
    alpha = exact_alpha(n, edges)
    chi = exact_chi(n, edges)
    assert alpha <= hb_alpha + 1e-9, f"{name}: Hoffman alpha violated"
    assert chi >= hb_chi - 1e-9, f"{name}: Hoffman chi violated"
    # interlacing: delete vertex 0
    idx = list(range(1, n))
    Ac = [[A[i][j] for j in idx] for i in idx]
    cardspec = spectrum(Ac)
    assert interlacing_ok(spec, cardspec), f"{name}: interlacing failed"
    return {
        "name": name, "n": n, "edges": edges,
        "charpoly_coeffs": coeffs,
        "factors": fac, "integral": integ,
        "integer_roots": iroots,
        "spectrum": [round(float(s), 10) for s in spec],
        "lmin": float(lmin), "lmax": float(lmax),
        "hoffman_alpha_bound": float(hb_alpha),
        "hoffman_chi_bound": float(hb_chi),
        "alpha": alpha, "chi": chi,
        "alpha_gap": float(hb_alpha - alpha),
        "chi_gap": float(chi - hb_chi),
        "card0_spectrum": [round(float(s), 10) for s in cardspec],
        "interlacing_ok": True,
    }

def petersen():
    e = []
    for i in range(5):
        e.append([i, (i+1) % 5])            # outer C5
        e.append([i, 5 + i])                # spokes
        e.append([5 + i, 5 + (i+2) % 5])    # inner star
    return 10, e

def heawood():
    # Fano plane lines (7 triples); bipartite point-line incidence, n=14
    lines = [[0,1,3],[1,2,4],[2,3,5],[3,4,6],[4,5,0],[5,6,1],[6,0,2]]
    e = []
    for j, L in enumerate(lines):
        for p in L:
            e.append([p, 7 + j])
    return 14, e

def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "graphs.json"
    data = json.load(open(src))
    rows = []
    for n in sorted(data, key=int):
        for i, e in enumerate(data[n]):
            rows.append(analyze_one(f"n{int(n)}-c{i}", int(n), e))
    for name, fn in (("Petersen-10", petersen), ("Heawood-14", heawood)):
        n, e = fn()
        rows.append(analyze_one(name, n, e))
    # cospectral classes over ALL rows
    cls = {}
    for r in rows:
        cls.setdefault(tuple(r["charpoly_coeffs"]), []).append(r["name"])
    for r in rows:
        r["cospectral_class"] = sorted(cls[tuple(r["charpoly_coeffs"])])
    ncos = sum(1 for v in cls.values() if len(v) > 1)
    json.dump(rows, open("analysis.json", "w"), indent=1)
    print(f"{'name':12s} {'n':>2s} integral spectrum(rounded)  alpha<=Hb  chi>=Hb", flush=True)
    for r in rows:
        print(f"{r['name']:12s} {r['n']:2d} {str(r['integral']):5s} "
              f"{r['spectrum']}  {r['alpha']}<= {r['hoffman_alpha_bound']:.4f}  "
              f"{r['chi']}>= {r['hoffman_chi_bound']:.4f}  class={r['cospectral_class']}", flush=True)
    print(f"CENSUS_ROWS={len([r for r in rows if r['n'] <= 8])} "
          f"INTEGRAL_IN_CENSUS={sum(1 for r in rows if r['n'] <= 8 and r['integral'])} "
          f"MULTI_COSPECTRAL_CLASSES={ncos}", flush=True)
    print("wrote analysis.json", flush=True)

if __name__ == "__main__":
    main()
