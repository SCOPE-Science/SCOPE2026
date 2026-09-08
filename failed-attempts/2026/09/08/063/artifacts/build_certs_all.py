"""Build full-candidate certificate files for the boxed+spiked size-7 census.

Reads:
  scratch/boxed7.json   (23 boxed candidates from list_boxed.tex parse:
                         V, pts, inter, w, u)
  scratch/spiked7.json  (32 minimal-size-7 spiked instantiations:
                         name, V, npts, ninter, width, u)
Writes:
  output/artifacts/certs_boxed_all.json  (23 entries, full logs)
  output/artifacts/certs_spiked_all.json (32 entries, full logs)

Each entry carries: branch, id, source provenance, V (vertex columns),
pts (all 7 lattice points), inter (interior points), n_interior,
is_hollow, attainer, width (+ rigorous widthlog: upper-bound attainer and
adjugate-box lower-bound scan), facets, ehrhart L(0..3), hstar.

Source provenance:
  boxed: Blanco-Santos arXiv:1601.02577 ancillary list_boxed.tex,
    Size-7 section (parsable block: text before the Size-8 marker),
    parsed by the regex in generate_candidates.py (same regex cross-checked
    here); index = 0-based order of appearance in that section.
    Local tarball scratch/bs11.tar.gz sha256 recorded in candidates.json.
  spiked: Theorems 'spiked-minimals' and 'spiked-quasiminimals' (cases
    (1)-(10b)) of the same paper, minimal k giving size 7 per the stated
    size formulas k+4/k+5/k+6/floor((3k+b)/2)+5; case/key/k recorded per entry.

Stdlib only. Run from workspace root:
  python3 output/artifacts/build_certs_all.py
"""
import itertools
import json
import math
import os
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(os.path.dirname(HERE))
SCR = os.path.join(WS, "scratch")


def facets_of(V):
    V = list(dict.fromkeys(map(tuple, V)))
    planes = []
    for i, j, k in itertools.combinations(range(len(V)), 3):
        a, b, c = V[i], V[j], V[k]
        ab = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
        ac = (c[0] - a[0], c[1] - a[1], c[2] - a[2])
        nx = ab[1] * ac[2] - ab[2] * ac[1]
        ny = ab[2] * ac[0] - ab[0] * ac[2]
        nz = ab[0] * ac[1] - ab[1] * ac[0]
        if (nx, ny, nz) == (0, 0, 0):
            continue
        v0 = nx * a[0] + ny * a[1] + nz * a[2]
        vals = [nx * v[0] + ny * v[1] + nz * v[2] for v in V]
        mn, mx = min(vals), max(vals)
        if mn == mx:
            continue
        if mn == v0:
            planes.append((-nx, -ny, -nz, -v0))
        elif mx == v0:
            planes.append((nx, ny, nz, v0))
    U = []
    for p in planes:
        nx, ny, nz, c = p
        g = math.gcd(math.gcd(abs(nx), abs(ny)), abs(nz))
        if g > 1 and c % g == 0:
            p = (nx // g, ny // g, nz // g, c // g)
        if p not in U:
            U.append(p)
    return U


def census(V):
    F = facets_of(V)
    xs = [v[0] for v in V]
    ys = [v[1] for v in V]
    zs = [v[2] for v in V]
    pts, inter = [], []
    for x in range(min(xs), max(xs) + 1):
        for y in range(min(ys), max(ys) + 1):
            for z in range(min(zs), max(zs) + 1):
                if all(nx * x + ny * y + nz * z <= c
                       for (nx, ny, nz, c) in F):
                    pts.append((x, y, z))
                    if all(nx * x + ny * y + nz * z < c
                           for (nx, ny, nz, c) in F):
                        inter.append((x, y, z))
    return pts, inter, F


def width_cert(pts, wmax=8):
    base, det = None, 0
    for quad in itertools.combinations(pts, 4):
        M = [[quad[i][j] - quad[0][j] for j in range(3)]
             for i in range(1, 4)]
        d = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
             - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
             + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
        if d != 0:
            base, det = quad, d
            break
    assert base is not None
    M = [[base[i][j] - base[0][j] for j in range(3)] for i in range(1, 4)]

    def d2(a, b, c, d):
        return a * d - b * c

    Cmat = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            r = [x for x in range(3) if x != i]
            cc = [x for x in range(3) if x != j]
            Cmat[i][j] = ((-1) ** (i + j)) * d2(
                M[r[0]][cc[0]], M[r[0]][cc[1]],
                M[r[1]][cc[0]], M[r[1]][cc[1]])
    adj = [[Cmat[j][i] for j in range(3)] for i in range(3)]
    rs = [sum(abs(adj[i][j]) for j in range(3)) for i in range(3)]
    ad = abs(det)
    log = []
    for W in range(0, wmax + 1):
        B = max(int(math.ceil(x * W / ad)) + 1 for x in rs) if W > 0 else 1
        cur, cu, n = None, None, 0
        for u in itertools.product(range(-B, B + 1), repeat=3):
            if u == (0, 0, 0):
                continue
            if math.gcd(math.gcd(abs(u[0]), abs(u[1])),
                         abs(u[2])) != 1:
                continue
            n += 1
            vv = [u[0] * p[0] + u[1] * p[1] + u[2] * p[2] for p in pts]
            w = max(vv) - min(vv)
            if cur is None or w < cur:
                cur, cu = w, u
        log.append({"W": W, "B": B, "checked": n, "min": cur,
                    "u": list(cu)})
        if cur is not None and cur <= W:
            return cur, cu, log, base, det
    raise AssertionError("width exceeded wmax")


def dilate_count(V, F, k):
    xs = [v[0] for v in V]
    ys = [v[1] for v in V]
    zs = [v[2] for v in V]
    n = 0
    for x in range(k * min(xs), k * max(xs) + 1):
        for y in range(k * min(ys), k * max(ys) + 1):
            for z in range(k * min(zs), k * max(zs) + 1):
                if all(nx * x + ny * y + nz * z <= k * c
                       for (nx, ny, nz, c) in F):
                    n += 1
    return n


def hstar(L0, L1, L2, L3):
    def Cnk(n, k):
        if n < k or k < 0:
            return 0
        r = 1
        for i in range(k):
            r = r * (n - i) // (i + 1)
        return r

    M = [[Cnk(t + 3, 3), Cnk(t + 2, 3), Cnk(t + 1, 3), Cnk(t, 3)]
         for t in range(4)]
    b = [L0, L1, L2, L3]
    A = [list(map(Fraction, M[i])) + [Fraction(b[i])] for i in range(4)]
    for c in range(4):
        p = max(range(c, 4), key=lambda r: abs(A[r][c]))
        A[c], A[p] = A[p], A[c]
        assert A[c][c] != 0
        for r in range(4):
            if r != c:
                f = A[r][c] / A[c][c]
                for k2 in range(c, 5):
                    A[r][k2] -= f * A[c][k2]
    return [int(A[i][4] / A[i][i]) for i in range(4)]


BOXED_SRC = ("Blanco-Santos arXiv:1601.02577 ancillary list_boxed.tex, "
             "Size-7 section (block before the Size-8 marker); "
             "0-based order of appearance; local tarball "
             "scratch/bs11.tar.gz")
SPIKED_SRC = ("Blanco-Santos arXiv:1601.02577 Theorems spiked-minimals / "
              "spiked-quasiminimals cases (1)-(10b) at minimal size-7 k")


def build_boxed():
    data = json.load(open(os.path.join(SCR, "boxed7.json")))
    assert len(data) == 23, len(data)
    out = []
    for e in data:
        V = [tuple(v) for v in e["V"]]
        pts, inter, F = census(V)
        assert len(pts) == 7, (e["i"], len(pts))
        assert sorted(map(list, pts)) == sorted(e["pts"]), e["i"]
        assert sorted(map(list, inter)) == sorted(e["inter"]), e["i"]
        w, cu, log, base, det = width_cert(pts)
        assert w == e["w"] and list(cu) == e["u"], e["i"]
        L = [1, len(pts), dilate_count(V, F, 2), dilate_count(V, F, 3)]
        h = hstar(*L)
        assert h[0] == 1 and all(x >= 0 for x in h), (e["i"], h)
        if len(inter) == 0:
            assert h[3] == 0, (e["i"], h)
        else:
            assert len(inter) == 1, (e["i"], inter)
        out.append({
            "branch": "boxed", "id": e["i"], "source": BOXED_SRC,
            "V": [list(v) for v in V],
            "pts": [list(p) for p in pts],
            "inter": [list(p) for p in inter],
            "n_interior": len(inter),
            "is_hollow": len(inter) == 0,
            "width": w, "attainer": list(cu),
            "basedet": det, "facets": [list(f) for f in F],
            "ehrhart": L, "hstar": h, "widthlog": log,
        })
    hol = [c for c in out if c["is_hollow"]]
    non = [c for c in out if not c["is_hollow"]]
    assert len(hol) == 8 and len(non) == 15, (len(hol), len(non))
    assert sorted(c["id"] for c in hol) == [1, 4, 5, 6, 7, 12, 13, 19]
    assert all(c["width"] == 2 for c in out)
    assert all(c["n_interior"] == 1 for c in non)
    return out


# theorem/case metadata for the 32 spiked instantiations
SPIKED_META = {
    "min(a=0,b=0)": {"theorem": "spiked-minimals", "case": "minimal",
                     "params": {"a": 0, "b": 0, "k": 2},
                     "size_formula": "k+5", "size_eval": "2+5=7"},
    "min(a=0,b=1)": {"theorem": "spiked-minimals", "case": "minimal",
                     "params": {"a": 0, "b": 1, "k": 2},
                     "size_formula": "k+5", "size_eval": "2+5=7"},
    "min(a=1,b=1)": {"theorem": "spiked-minimals", "case": "minimal",
                     "params": {"a": 1, "b": 1, "k": 2},
                     "size_formula": "k+5", "size_eval": "2+5=7"},
    "q1": {"theorem": "spiked-quasiminimals", "case": "(1)",
           "params": {"k": 3}, "size_formula": "k+4",
           "size_eval": "3+4=7"},
    "q2": {"theorem": "spiked-quasiminimals", "case": "(2)",
           "params": {"k": 2}, "size_formula": "k+5",
           "size_eval": "2+5=7"},
    "q4": {"theorem": "spiked-quasiminimals", "case": "(4)",
           "params": {"k": 3}, "size_formula": "k+4",
           "size_eval": "3+4=7"},
}
for _a in (-1, 0):
    SPIKED_META["q5(a=%d)" % _a] = {
        "theorem": "spiked-quasiminimals", "case": "(5)",
        "params": {"a": _a, "k": 3}, "size_formula": "k+4",
        "size_eval": "3+4=7"}
for _a in (-2, -1, 0):
    SPIKED_META["q6(a=%d)" % _a] = {
        "theorem": "spiked-quasiminimals", "case": "(6)",
        "params": {"a": _a, "k": 3}, "size_formula": "k+4",
        "size_eval": "3+4=7"}
for _a in (-5, -1):
    SPIKED_META["q7(a=%d)" % _a] = {
        "theorem": "spiked-quasiminimals", "case": "(7)",
        "params": {"a": _a, "k": 3}, "size_formula": "k+4",
        "size_eval": "3+4=7"}
for _a in (-1, 0):
    for _b in range(_a, 4):
        SPIKED_META["q8(a=%d,b=%d)" % (_a, _b)] = {
            "theorem": "spiked-quasiminimals", "case": "(8)",
            "params": {"a": _a, "b": _b, "k": 2},
            "size_formula": "k+5", "size_eval": "2+5=7"}
for _a in (-2, -1, 0):
    for _b in (0, 1):
        SPIKED_META["q9(a=%d,b=%d)" % (_a, _b)] = {
            "theorem": "spiked-quasiminimals", "case": "(9)",
            "params": {"a": _a, "b": _b, "k": 2},
            "size_formula": "k+5", "size_eval": "2+5=7"}
for _a in (-1, 0):
    SPIKED_META["q10a(a=%d,b=-1)" % _a] = {
        "theorem": "spiked-quasiminimals", "case": "(10a)",
        "params": {"a": _a, "b": -1, "k": 2},
        "size_formula": "floor((3k+b)/2)+5",
        "size_eval": "floor((6-1)/2)+5=2+5=7"}
    SPIKED_META["q10b(a=%d)" % _a] = {
        "theorem": "spiked-quasiminimals", "case": "(10b)",
        "params": {"a": _a, "k": 2}, "size_formula": "k+5",
        "size_eval": "2+5=7"}


def build_spiked():
    data = json.load(open(os.path.join(SCR, "spiked7.json")))
    assert len(data) == 32, len(data)
    assert set(e["name"] for e in data) == set(SPIKED_META), \
        set(e["name"] for e in data) ^ set(SPIKED_META)
    out = []
    for e in data:
        V = [tuple(v) for v in e["V"]]
        pts, inter, F = census(V)
        assert len(pts) == 7, (e["name"], len(pts))
        assert len(pts) == e["npts"] and len(inter) == e["ninter"], \
            e["name"]
        w, cu, log, base, det = width_cert(pts)
        assert w == e["width"] and list(cu) == e["u"], e["name"]
        L = [1, len(pts), dilate_count(V, F, 2), dilate_count(V, F, 3)]
        h = hstar(*L)
        assert h[0] == 1 and all(x >= 0 for x in h), (e["name"], h)
        meta = SPIKED_META[e["name"]]
        out.append({
            "branch": "spiked", "id": e["name"], "source": SPIKED_SRC,
            "theorem": meta["theorem"], "case": meta["case"],
            "params": meta["params"],
            "size_formula": meta["size_formula"],
            "size_eval": meta["size_eval"],
            "V": [list(v) for v in V],
            "pts": [list(p) for p in pts],
            "inter": [list(p) for p in inter],
            "n_interior": len(inter),
            "is_hollow": len(inter) == 0,
            "width": w, "attainer": list(cu),
            "basedet": det, "facets": [list(f) for f in F],
            "ehrhart": L, "hstar": h, "widthlog": log,
        })
    hol = [c for c in out if c["is_hollow"]]
    assert sorted(c["id"] for c in hol) == ["q1", "q2"], \
        [c["id"] for c in hol]
    assert all(c["width"] == 2 for c in hol)
    return out


def main():
    boxed = build_boxed()
    spiked = build_spiked()
    with open(os.path.join(HERE, "certs_boxed_all.json"), "w") as f:
        json.dump({"certificates": boxed,
                   "counts": {"total": 23, "hollow": 8, "non_hollow": 15}},
                  f)
    with open(os.path.join(HERE, "certs_spiked_all.json"), "w") as f:
        json.dump({"certificates": spiked,
                   "counts": {"total": 32, "hollow": 2,
                              "non_hollow": 30}}, f)
    print("boxed: total=23 hollow=8 non_hollow=15 "
          "(all width 2; non-hollow all n_interior=1)")
    print("spiked: total=32 hollow=2 non_hollow=30 "
          "(hollow: q1,q2 width 2)")


if __name__ == "__main__":
    main()
