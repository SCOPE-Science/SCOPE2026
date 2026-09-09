"""Substep 7: geometric smoothness of committed F_101 bidegree-(3,4) curve.
For each of 4 affine charts, f,fx,fy in k[a,b]; certify 1 in (f,fx,fy) by
bounded cofactor search (Macaulay matrix, sound direction)."""
import json, itertools
P = 101
d = json.load(open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-373/output/artifacts/curve_F101.json"))
C = d["coeffs"]  # C[i][j]: s^{3-i} t^i u^{4-j} v^j

def chart(poly_terms):
    # poly_terms: dict {(ea,eb):c}; returns (f, fa, fb)
    def deriv(p, var):
        r = {}
        for (a, b), c in p.items():
            e = a if var == 0 else b
            if e:
                k = (a - 1, b) if var == 0 else (a, b - 1)
                r[k] = (r.get(k, 0) + e * c) % P
        return {k: v % P for k, v in r.items() if v % P}
    return poly_terms, deriv(poly_terms, 0), deriv(poly_terms, 1)

def mons2(B):
    return [(a, b) for a in range(B + 1) for b in range(B + 1 - a)]

def pmul_shift(p, s):
    return {(a + s[0], b + s[1]): c for (a, b), c in p.items()}

def certify(f, fx, fy, B):
    cols = mons2(B)
    ci = {m: k for k, m in enumerate(cols)}
    rows = []
    for p in (f, fx, fy):
        if not p:
            continue
        md = max(a + b for (a, b) in p)
        for s in mons2(B - md):
            r = [0] * len(cols)
            for (a, b), c in pmul_shift(p, s).items():
                if a + b <= B:
                    r[ci[(a, b)]] = (r[ci[(a, b)]] + c) % P
            rows.append(r)
    # is unit monomial (0,0) in row space? RREF on augmented: check e0 in span
    n, m = len(rows), len(cols)
    A = [r[:] + [0] for r in rows]
    # solve A^T? Direct: row-reduce, see if e0 combination exists: reduce rows, check rank increase test
    def rank_of(M):
        M = [r[:] for r in M]
        R, Cc = len(M), len(M[0])
        r = 0
        for cc in range(Cc):
            piv = next((k for k in range(r, R) if M[k][cc] % P != 0), None)
            if piv is None:
                continue
            M[r], M[piv] = M[piv], M[r]
            inv = pow(M[r][cc] % P, -1, P)
            M[r] = [(x * inv) % P for x in M[r]]
            for k in range(R):
                if k != r and M[k][cc] % P != 0:
                    f2 = M[k][cc] % P
                    M[k] = [(a - f2 * b) % P for a, b in zip(M[k], M[r])]
            r += 1
        return r, M
    r0, _ = rank_of(rows)
    e0 = [0] * m
    e0[ci[(0, 0)]] = 1
    r1, _ = rank_of(rows + [e0])
    return r1 == r0, r0, len(rows), m

charts = {
    "s1u1": {(i, j): C[i][j] % P for i in range(4) for j in range(5) if C[i][j] % P},
    "s1v1": {(i, 4 - j): C[i][j] % P for i in range(4) for j in range(5) if C[i][j] % P},
    "t1u1": {(3 - i, j): C[i][j] % P for i in range(4) for j in range(5) if C[i][j] % P},
    "t1v1": {(3 - i, 4 - j): C[i][j] % P for i in range(4) for j in range(5) if C[i][j] % P},
}
out = []
ok = True
for name, terms in charts.items():
    f, fx, fy = chart(terms)
    cert, r0, nr, nc = certify(f, fx, fy, 14)
    if not cert:
        cert, r0, nr, nc = certify(f, fx, fy, 20)
    out.append(f"{name}: certified={cert} rank={r0} rows={nr} cols={nc}")
    ok = ok and cert
    print(out[-1])
open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-373/output/artifacts/substep7_ok.txt", "w").write("\n".join(out) + f"\nSMOOTH_ALL={ok}\n")
print("SMOOTH_ALL =", ok)
