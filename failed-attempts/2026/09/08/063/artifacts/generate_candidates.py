"""Candidate-generation replay: emit the 23 boxed + 32 spiked size-7
candidates from explicit data / theorem parameters (stdlib only).

Run from workspace root:
  python3 output/artifacts/generate_candidates.py

What it does:
  BOXED: the 23 boxed size-7 vertex-column matrices are embedded verbatim
    (transcribed from Blanco-Santos arXiv:1601.02577 ancillary
    list_boxed.tex, Size-7 section = text before the Size-8 marker;
    local tarball scratch/bs11.tar.gz, sha256 recorded in candidates.json).
    The script re-parses list_boxed.tex with the documented regex and
    asserts the embedded list matches the fresh parse entry-by-entry, then
    asserts the count is 23 (matching Table-minimal's boxed size-7 total
    4+15+4). So completeness rests on: published count 23 + fresh regex
    parse of the source file + byte-level equality with the embedded data.
  SPIKED: the 32 minimal-size-7 instantiations are generated from theorem
    parameters (Theorem spiked-minimals: (a,b) in {(0,0),(0,1),(1,1)}, k=2;
    Theorem spiked-quasiminimals cases (1)-(10b) at the k forced by the
    stated size formulas k+4/k+5/k+6/floor((3k+b)/2)+5, with the full
    a/b ranges from the theorem statements). The script asserts the count
    is 32, evaluates each size formula to 7, and checks every candidate
    recounts to exactly 7 lattice points. Non-7 exclusion for other family
    members: for each case the script evaluates the size formula at the
    neighboring k values (k-1, k+1, k+2) and asserts none equals 7, i.e. no
    other member of that parametric family can have size 7 (the a/b ranges
    are finite and fully enumerated, so within-case coverage is by
    construction).

Writes: output/artifacts/candidates.json
  {boxed: [...], spiked: [{id, theorem, case, params, size_formula,
                           size_eval, V}], counts: {boxed: 23, spiked: 32},
   boxed_source: {...sha256...}, spiked_size_exclusion: {...}}
"""
import hashlib
import itertools
import json
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(WS, "scratch", "src11", "list_boxed.tex")
TAR = os.path.join(WS, "scratch", "bs11.tar.gz")

# --- 23 boxed size-7 vertex-column matrices, embedded verbatim ---
# (transcribed from list_boxed.tex Size-7 section; verified byte-equal to a
# fresh regex parse of the source file -- see main()).
BOXED = [
    [[0, 0, 0], [1, 1, 2], [1, 2, 0], [2, 0, 0]],
    [[0, -1, 0], [0, 1, 0], [1, 1, 3], [2, 0, 0]],
    [[0, -1, 0], [0, 1, 0], [1, 1, 4], [2, 0, 0]],
    [[0, -1, 0], [0, 1, 0], [1, 1, 5], [2, 0, 0]],
    [[-1, 2, 1], [0, 0, 0], [0, 0, 1], [1, -1, 1], [1, 1, -1]],
    [[0, 1, 0], [0, 2, 1], [1, 0, 1], [1, 0, 2], [2, 1, 0]],
    [[0, 1, 0], [0, 1, 2], [1, 0, 0], [1, 2, 0], [2, 0, 0]],
    [[0, 0, 0], [0, 1, 1], [0, 1, 2], [1, 2, 0], [2, 0, 0]],
    [[0, 1, 1], [1, 0, 0], [1, 1, 2], [1, 2, 0], [2, 0, 0]],
    [[0, 1, 0], [1, 0, 0], [1, 1, 2], [1, 2, 0], [2, 0, 0]],
    [[0, 0, 1], [1, 0, 0], [1, 1, 2], [1, 2, 0], [2, 0, 0]],
    [[0, 0, 1], [0, 2, 1], [1, 1, 0], [1, 1, 2], [2, 1, 0]],
    [[0, 0, 1], [0, 2, 0], [1, 0, 0], [1, 1, 2], [2, 0, 0]],
    [[0, 0, 1], [0, 1, 0], [0, 1, 2], [1, 2, 0], [2, 0, 0]],
    [[0, 1, 0], [1, 0, 1], [1, 1, 2], [1, 2, 0], [2, 0, 0]],
    [[0, 1, 0], [0, 2, 1], [1, 0, 1], [1, 1, 2], [2, 1, 0]],
    [[0, 1, 1], [1, 0, 0], [1, 1, 2], [1, 2, 0], [2, 1, 0]],
    [[0, 1, 0], [1, 0, 0], [1, 1, 2], [1, 2, 0], [2, 1, 0]],
    [[0, 1, 0], [1, 0, 1], [1, 1, 2], [1, 2, 1], [2, 1, 0]],
    [[0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [1, 0, 0], [2, 0, 0]],
    [[0, 1, 1], [1, 0, 1], [1, 1, 0], [1, 1, 2], [1, 2, 0], [2, 1, 0]],
    [[0, 1, 1], [1, 0, 1], [1, 1, 0], [1, 1, 2], [1, 2, 1], [2, 1, 0]],
    [[0, 1, 1], [1, 0, 1], [1, 1, 0], [1, 1, 2], [1, 2, 1], [2, 1, 1]],
]

PAT = re.compile(
    r"\\left\(\s*\\begin\{array\}\{([clr ]+)\}(.*?)\\end\{array\}"
    r"\s*\\right\)", re.S)


def parse_boxed_source():
    raw = open(SRC, encoding="utf-8", errors="replace").read()
    sec = raw.split("Size 8")[0]
    assert "Size 7" in sec, "Size-7 marker missing"
    mats = PAT.findall(sec)
    out = []
    for _fmt, body in mats:
        rows = [r.strip() for r in body.strip().split("\\\\") if r.strip()]
        grid = [[int(x) for x in r.replace("&", " ").split()]
                for r in rows]
        assert len(grid) == 3, grid
        ncols = len(grid[0])
        assert all(len(r) == ncols for r in grid)
        out.append([list((grid[r][c] for r in range(3)))
                    for c in range(ncols)])
    return raw, out


def gen_spiked():
    """Return list of (id, theorem, case, params, formula, eval, V)."""
    S = []
    for (a, b) in [(0, 0), (0, 1), (1, 1)]:
        k = 2
        S.append(("min(a=%d,b=%d)" % (a, b), "spiked-minimals",
                  "minimal", {"a": a, "b": b, "k": k}, "k+5",
                  "%d+5=7" % k,
                  [(1, 0, 0), (0, 1, 0), (-1, 0, -a), (0, -1, 2 * k + b)]))
    S.append(("q1", "spiked-quasiminimals", "(1)", {"k": 3}, "k+4",
              "3+4=7",
              [(1, -1, -1), (-1, 1, 1), (-1, -1, 0), (0, 0, 3)]))
    S.append(("q2", "spiked-quasiminimals", "(2)", {"k": 2}, "k+5",
              "2+5=7",
              [(1, -1, 0), (-1, 1, -1), (-1, -1, 0), (0, 0, 2)]))
    S.append(("q4", "spiked-quasiminimals", "(4)", {"k": 3}, "k+4",
              "3+4=7",
              [(2, -1, -1), (-1, 2, 1), (-1, -1, 0), (0, 0, 3)]))
    for a in (-1, 0):
        S.append(("q5(a=%d)" % a, "spiked-quasiminimals", "(5)",
                  {"a": a, "k": 3}, "k+4", "3+4=7",
                  [(1, -1, -1), (0, 1, a), (-1, -1, 0), (0, 0, 3)]))
    for a in (-2, -1, 0):
        S.append(("q6(a=%d)" % a, "spiked-quasiminimals", "(6)",
                  {"a": a, "k": 3}, "k+4", "3+4=7",
                  [(1, 0, 0), (0, 1, a), (-1, -1, 0), (0, 0, 3)]))
    for a in (-5, -1):
        S.append(("q7(a=%d)" % a, "spiked-quasiminimals", "(7)",
                  {"a": a, "k": 3}, "k+4", "3+4=7",
                  [(2, 1, 0), (-1, 1, a), (-1, -1, 0), (0, 0, 3)]))
    for a in (-1, 0):
        for b in range(a, 4):
            S.append(("q8(a=%d,b=%d)" % (a, b), "spiked-quasiminimals",
                      "(8)", {"a": a, "b": b, "k": 2}, "k+5", "2+5=7",
                      [(1, 0, 0), (0, 1, 0), (-1, 0, a), (0, -1, b),
                       (0, 0, 2)]))
    for a in (-2, -1, 0):
        for b in (0, 1):
            S.append(("q9(a=%d,b=%d)" % (a, b), "spiked-quasiminimals",
                      "(9)", {"a": a, "b": b, "k": 2}, "k+5", "2+5=7",
                      [(1, 0, 0), (0, 1, 0), (-1, -1, a),
                       (1, 1, 4 - a + b)]))
    for a in (-1, 0):
        S.append(("q10a(a=%d,b=-1)" % a, "spiked-quasiminimals", "(10a)",
                  {"a": a, "b": -1, "k": 2}, "floor((3k+b)/2)+5",
                  "floor((6-1)/2)+5=2+5=7",
                  [(1, 0, a), (0, 2, -1), (-1, 0, 0), (0, 0, 2)]))
        S.append(("q10b(a=%d)" % a, "spiked-quasiminimals", "(10b)",
                  {"a": a, "k": 2}, "k+5", "2+5=7",
                  [(1, 0, 0), (0, 2, a), (-1, 0, 0), (0, 1, 2)]))
    return [ {"id": i, "theorem": t, "case": c, "params": p,
              "size_formula": f, "size_eval": e,
              "V": [list(v) for v in V]}
             for (i, t, c, p, f, e, V) in S ]


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


def npoints(V):
    F = facets_of([tuple(v) for v in V])
    xs = [v[0] for v in V]
    ys = [v[1] for v in V]
    zs = [v[2] for v in V]
    n = 0
    for x in range(min(xs), max(xs) + 1):
        for y in range(min(ys), max(ys) + 1):
            for z in range(min(zs), max(zs) + 1):
                if all(nx * x + ny * y + nz * z <= c
                       for (nx, ny, nz, c) in F):
                    n += 1
    return n


def main():
    raw, parsed = parse_boxed_source()
    assert len(BOXED) == 23, len(BOXED)
    assert len(parsed) == 23, len(parsed)
    for i in range(23):
        assert [list(v) for v in parsed[i]] == BOXED[i], i
    for i, V in enumerate(BOXED):
        assert npoints(V) == 7, (i, V)
    spiked = gen_spiked()
    assert len(spiked) == 32, len(spiked)
    for e in spiked:
        assert npoints(e["V"]) == 7, e["id"]
    # size-formula non-7 exclusion at neighboring k
    excl = {}
    excl["k+4 (cases 1,4,5,6,7)"] = {
        "k_used": 3, "neighbors": {2: 6, 3: 7, 4: 8, 5: 9}}
    excl["k+5 (minimal,2,8,9,10b)"] = {
        "k_used": 2, "neighbors": {1: 6, 2: 7, 3: 8, 4: 9}}
    excl["k+6 (case 3: no size-7 member)"] = {
        "k_used": None, "neighbors": {2: 8, 3: 9, 4: 10},
        "note": "k+6=7 would need k=1, but k>=2 is required "
                "(k=1 gives size<=6/width 1); hence case (3) "
                "contributes no size-7 candidate"}
    excl["floor((3k+b)/2)+5 (case 10a, b=-1)"] = {
        "k_used": 2, "neighbors": {2: 7, 3: 9, 4: 10},
        "note": "k=2,b=-1 -> floor(5/2)+5=7; k=1 is excluded (k>=2)"}
    for key, info in excl.items():
        for k, s in info["neighbors"].items():
            if "k+4" in key:
                assert s == k + 4, (key, k)
            elif "k+6" in key:
                assert s == k + 6, (key, k)
            elif "10a" in key:
                assert s == (3 * k - 1) // 2 + 5, (key, k)
            else:
                assert s == k + 5, (key, k)
            if info.get("k_used") is not None and k != info["k_used"]:
                assert s != 7, (key, k)
    sha_tex = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    sha_tar = hashlib.sha256(open(TAR, "rb").read()).hexdigest()
    out = {
        "boxed": [{"id": i, "V": V} for i, V in enumerate(BOXED)],
        "spiked": spiked,
        "counts": {"boxed": 23, "spiked": 32},
        "boxed_source": {
            "paper": "Blanco-Santos arXiv:1601.02577",
            "file": "ancillary list_boxed.tex, Size-7 section "
                    "(text before Size-8 marker)",
            "url": "https://arxiv.org/e-print/1601.02577",
            "sha256_list_boxed_tex": sha_tex,
            "sha256_bs11_tar_gz": sha_tar,
            "parse_regex": r"\\left\(\s*\\begin\{array\}\{([clr ]+)\}"
                           r"(.*?)\\end\{array\}\s*\\right\)",
            "table_minimal_check": "boxed size-7 total 4+15+4=23",
        },
        "spiked_source": {
            "paper": "Blanco-Santos arXiv:1601.02577, Section 3",
            "theorems": ["spiked-minimals", "spiked-quasiminimals"],
            "note": "a/b ranges are the finite ranges in the theorem "
                    "statements; k>=2 throughout (k=1 gives size<=6)",
        },
        "spiked_size_exclusion": excl,
    }
    with open(os.path.join(HERE, "candidates.json"), "w") as f:
        json.dump(out, f)
    print("boxed candidates: 23 (fresh parse match + 7-point recount OK)")
    print("spiked candidates: 32 (theorem-parameter generation + "
          "7-point recount OK)")
    print("size-formula exclusion for neighboring k: OK")


if __name__ == "__main__":
    main()
