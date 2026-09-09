"""Edge cut-point certificate: D_1 regular tetrahedron, source = centroid of face 012,
target edge = t-edge (1,2) in face 123. Proves (exactly, stdlib only) that the two
valid unfold paths seqA=(0,1,3) and seqB=(0,2,3) are the two shortest at both
rational endpoints u=11/20 and u=14/25 with FLIPPED order, hence (IVT on exact
quadratics) a cut point u* in (11/20,14/25) exists on this skeleton edge.
Also derives the exact quadratics from geometry and the closed form u*=(-13+sqrt(1429))/45.
Writes cert_edge_bisect.json. Run: python3 edge_bisect.py (from output/artifacts/).
"""
import json
import sys
from fractions import Fraction as Fr

sys.path.insert(0, ".")
from cert_exact import (FACES, S3, Pt, bary, ref_layout, unfold_paths,
                        valid_and_dist, true_dists)

Fs = (0, 1, 2)
Ft = (1, 2, 3)
seqA = (0, 1, 3)
seqB = (0, 2, 3)

sxy = bary(Fs, Fr(1, 3), Fr(1, 3), Fr(1, 3))
R = ref_layout(Ft)
A, B = R[1], R[2]

def yof(u):
    return Pt(A.x + (B.x - A.x) * S3(u), A.y + (B.y - A.y) * S3(u))

def qfit(pts):
    (x0, y0), (x1, y1), (x2, y2) = pts
    M = [[x0 * x0, x0, Fr(1), y0], [x1 * x1, x1, Fr(1), y1], [x2 * x2, x2, Fr(1), y2]]
    for c in range(3):
        piv = M[c][c]
        assert piv != 0
        for r in range(3):
            if r != c and M[r][c] != 0:
                f = M[r][c] / piv
                for k in range(4):
                    M[r][k] -= f * M[c][k]
    return [M[i][3] / M[i][i] for i in range(3)]

def main():
    # (1) Derive exact distance-squared quadratics along the edge from geometry.
    fit_us = [Fr(1, 10), Fr(1, 2), Fr(9, 10)]
    data = {}
    for seq in (seqA, seqB):
        pts = []
        for u in fit_us:
            d2 = valid_and_dist(sxy, Fs, yof(u), Ft, seq)
            assert d2 is not None, f"fit point u={u} invalid for {seq}"
            assert d2.b == 0, f"non-rational d2 {d2}"
            pts.append((u, d2.a))
        data[seq] = pts
    cA = qfit(data[seqA])
    cB = qfit(data[seqB])
    # (2) Difference quadratic and its discriminant.
    c = [cA[i] - cB[i] for i in range(3)]
    assert c == [Fr(3, 4), Fr(13, 30), Fr(-7, 15)], f"diff coef changed: {c}"
    D = c[1] * c[1] - 4 * c[0] * c[2]
    assert D == Fr(1429, 900), f"discriminant changed: {D}"
    # 1429 is not a perfect square (37^2=1369 < 1429 < 1444=38^2) -> sqrt irrational.
    assert 37 * 37 < 1429 < 38 * 38
    import math
    ustar = (-Fr(13, 30) + math.sqrt(float(D))) / Fr(3, 2)
    assert Fr(11, 20) < ustar < Fr(14, 25), f"root not bracketed: {ustar}"
    # (3) Exact order-flip check at rational endpoints with FULL path enumeration.
    endpts = {}
    for u in (Fr(11, 20), Fr(14, 25)):
        ds = true_dists(sxy, Fs, yof(u), Ft)
        assert len(ds) >= 2
        tab = [(str(d), list(s)) for d, s in ds]
        top2 = [tuple(s) for _, s in ds[:2]]
        assert set(top2) == {seqA, seqB}, f"top2 changed at u={u}: {tab}"
        endpts[str(u)] = tab
    firstA = endpts["11/20"][0][1] == list(seqA)  # A strictly shorter at left end
    secondA = endpts["14/25"][0][1] == list(seqA)  # A still first at right end?
    assert firstA and not secondA, "no order flip"
    # (4) ustar closed form: (-13+sqrt(1429))/45 in (11/20, 14/25), irrational.
    lo, hi = (-13 + math.sqrt(1429)) / 45, (-13 + math.sqrt(1429)) / 45
    assert 0.55 < lo < 0.56 and 0.55 < hi < 0.56
    cert = {
        "t": 1, "source": {"face": list(Fs), "bary": ["1/3", "1/3", "1/3"]},
        "edge": {"face": list(Ft), "verts": [1, 2]},
        "quadA": [str(x) for x in cA], "quadB": [str(x) for x in cB],
        "diff": [str(x) for x in c], "discriminant": str(D),
        "ustar_closed_form": "(-13+sqrt(1429))/45", "ustar_float": ustar,
        "bracket": ["11/20", "14/25"],
        "endpoint_paths": endpts,
        "order": "A<B at 11/20; B<A at 14/25 (squared distances, exact)",
    }
    with open("cert_edge_bisect.json", "w") as f:
        json.dump(cert, f, indent=1)
    print("quadA:", cA)
    print("quadB:", cB)
    print("diff:", c, "disc:", D)
    print("ustar ~", ustar)
    print("EDGE-BISECT CERT OK")

if __name__ == "__main__":
    main()
