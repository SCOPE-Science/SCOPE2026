"""Enumerate rank-one spherical Ds on two recorded rank-2 lattices.
Classify numerical walls vs b^2-excluded vs candidate-actual.
Step 3 of target route. Pure stdlib."""
import json

def run_case(name, G, H, v, box):
    Q = H[0]*(G[0][0]*H[0]+G[0][1]*H[1]) + H[1]*(G[1][0]*H[0]+G[1][1]*H[1])
    r, C, S = v
    def dot(A, B):
        return A[0]*(G[0][0]*B[0]+G[0][1]*B[1]) + A[1]*(G[1][0]*B[0]+G[1][1]*B[1])
    C2 = dot(C, C)
    v2 = C2 - 2*r*S
    N = dot(C, H)
    out = {"name": name, "G": G, "Q": Q, "v2": v2, "N": N, "rows": [],
           "n_num": 0, "n_excl": 0, "n_cand": 0}
    for d1 in range(-box, box+1):
        for d2 in range(-box, box+1):
            if d1 == 0 and d2 == 0:
                continue
            D = (d1, d2)
            M = dot(D, H)
            D2 = dot(D, D)
            # Hodge check
            hodge = (M*M - Q*D2)  # >=0 iff D2<=M^2/Q (Q>0); records defect*Q
            # spherical s_a
            if (D2 + 2) % 2 != 0:
                continue  # non-integral s_a: not a Mukai class on K3 (D2 even always; safety)
            sa = (D2 + 2)//2
            den = M*r - N
            num = 2*M*S - N*(D2 + 2)
            if den == 0:
                continue  # no isolated wall (parallel charges)
            if num*den <= 0:
                continue  # Y<=0: no numerical wall at x>0
            Y = num/(Q*den)
            out["n_num"] += 1
            CDOT = dot(C, D)
            b2 = r*D2 - 2*CDOT + (v2 + 2*S + 2*r - 2)
            assert b2 == (C2 - 2*CDOT + D2) - 2*(r-1)*(S - sa), "b2 identity"
            if b2 < -2:
                out["n_excl"] += 1
                status = "excluded(b2<-2)"
            else:
                out["n_cand"] += 1
                status = "candidate-actual"
            out["rows"].append({"D": list(D), "M": M, "D2": D2,
                                "Y": Y, "b2": b2, "hodge_defect_xQ": hodge,
                                "status": status})
    return out

A = run_case("A_disc-21", [[2, 5], [5, 2]], (1, 0), (2, (1, 0), 0), 6)
B = run_case("B_disc-28", [[4, 6], [6, 2]], (1, 0), (2, (1, 0), 0), 6)
for case in (A, B):
    print(case["name"], "Q=", case["Q"], "v2=", case["v2"], "N=", case["N"],
          "num_walls=", case["n_num"], "excluded=", case["n_excl"],
          "candidates=", case["n_cand"])
    assert all(r["hodge_defect_xQ"] >= 0 for r in case["rows"]), "Hodge violated!"
    print("  Hodge OK on", len(case["rows"]), "numerical rows")
with open("output/artifacts/wall_scan.json", "w") as f:
    json.dump({"A": A, "B": B}, f, indent=1)
print("wrote output/artifacts/wall_scan.json")
