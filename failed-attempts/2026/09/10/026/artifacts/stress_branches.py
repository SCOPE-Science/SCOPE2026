"""Stress-test: branch structure, large-box escape, envelope formula.
Target-directed: tests uniformity of bound B. Pure stdlib."""
import json

def lattice_data(G, H, v, box):
    Q = H[0]*(G[0][0]*H[0]+G[0][1]*H[1]) + H[1]*(G[1][0]*H[0]+G[1][1]*H[1])
    r, C, S = v
    def dot(A, B):
        return A[0]*(G[0][0]*B[0]+G[0][1]*B[1]) + A[1]*(G[1][0]*B[0]+G[1][1]*B[1])
    C2 = dot(C, C); v2 = C2 - 2*r*S; N = dot(C, H)
    rows = []
    for d1 in range(-box, box+1):
        for d2 in range(-box, box+1):
            if d1 == 0 and d2 == 0:
                continue
            D = (d1, d2)
            M = dot(D, H); D2 = dot(D, D)
            if (D2+2) % 2 != 0:
                continue
            sa = (D2+2)//2
            den = M*r - N; num = 2*M*S - N*(D2+2)
            if den == 0 or num*den <= 0:
                continue
            Y = num/(Q*den)
            CDOT = dot(C, D)
            b2 = r*D2 - 2*CDOT + (v2 + 2*S + 2*r - 2)
            rows.append({"D": list(D), "M": M, "D2": D2, "den": den,
                         "Y": Y, "b2": b2,
                         "cand": b2 >= -2})
    return {"Q": Q, "v2": v2, "N": N, "C2": C2, "rows": rows}

for name, G, H, v in [
    ("A", [[2, 5], [5, 2]], (1, 0), (2, (1, 0), 0)),
    ("B", [[4, 6], [6, 2]], (1, 0), (2, (1, 0), 0)),
]:
    d = lattice_data(G, H, v, 25)
    rows = d["rows"]
    pos = [w for w in rows if w["den"] > 0]
    neg = [w for w in rows if w["den"] < 0]
    pos_c = [w for w in pos if w["cand"]]
    neg_c = [w for w in neg if w["cand"]]
    print(f"--- {name}: Q={d['Q']} v2={d['v2']} N={d['N']} C2={d['C2']} "
          f"box=25 total_num={len(rows)}")
    print(f"    den>0: num={len(pos)} candidates={len(pos_c)} "
          f"(branch-empty={len(pos_c)==0})")
    print(f"    den<0: num={len(neg)} candidates={len(neg_c)}")
    if neg_c:
        print(f"    den<0 candidates: max|M|={max(abs(w['M']) for w in neg_c)} "
              f"maxY={max(w['Y'] for w in neg_c):.3f} "
              f"minM={min(w['M'] for w in neg_c)}")
        # envelope check: b2 <= den^2/(rQ)+(r-1)(v2/r+2)
        r = v[0]
        bad = 0
        for w in rows:
            env = w["den"]**2/(r*d["Q"]) + (r-1)*(d["v2"]/r + 2)
            if w["b2"] > env + 1e-9:
                bad += 1
        print(f"    envelope violations: {bad}/{len(rows)}")
    if pos_c:
        print("    SURPRISE den>0 candidates:", pos_c[:5])
print("done")
