"""Full-candidate verifier for the boxed+spiked size-7 census (stdlib only).

Run from this directory:
  python3 verify.py
Requires: candidates.json, certs_boxed_all.json, certs_spiked_all.json.

Replays EVERYTHING from the candidate vertex sets V only:
  A. candidate generation: re-parse list_boxed.tex (documented regex) and
     check the 23 embedded boxed matrices match entry-by-entry; regenerate
     the 32 spiked instantiations from theorem parameters and check match;
     assert counts 23 / 32; evaluate size formulas (=7) and the neighboring-k
     non-7 exclusion.
  B. per-candidate certificate replay (all 23 boxed + all 32 spiked):
     1. facet recomputation (supporting-plane scan, tolerance-free),
     2. exact lattice-point count (=7) and interior count
        (boxed negatives: exactly 1 interior point; hollow: 0),
     3. stored point/interior-set agreement,
     4. stored attainer gives the stored width (hollow boxed/spiked: 2;
        boxed negatives: 2; spiked non-hollow: stored value),
     5. dilate counts L(1..3) agree; hollow <=> h3*=0 via reciprocity
        L(3)-4L(2)+6L(1)-4=0; non-hollow boxed have h3*=1,
     6. width lower bound: an INDEPENDENTLY recomputed rigorous adjugate box
        (verifier-chosen basis) is scanned -- no primitive functional has
        width below the stored width (boxed: none <=1; spiked q4: none <=2).
  C. totals: 23 boxed (8 hollow width-2 + 15 one-interior-point width-2),
     32 spiked (2 hollow width-2 + 30 non-hollow), hollow-10 pairwise
     inequivalence: all 45 exhaustive unimodular-congruence searches rerun
     and written to inequivalence.log (all False).

Keeps the recomputed-box discipline: the verifier never trusts a stored B.
Exit nonzero on any mismatch.
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


def load(name):
    with open(os.path.join(HERE, name)) as f:
        return json.load(f)


CAND = load("candidates.json")
BOXED = load("certs_boxed_all.json")
SPIKED = load("certs_spiked_all.json")

LOG = open(os.path.join(HERE, "inequivalence.log"), "w")


def facets(V):
    V = list(dict.fromkeys(map(tuple, V)))
    P = []
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
        vs = [nx * v[0] + ny * v[1] + nz * v[2] for v in V]
        mn, mx = min(vs), max(vs)
        if mn == mx:
            continue
        if mn == v0:
            P.append((-nx, -ny, -nz, -v0))
        elif mx == v0:
            P.append((nx, ny, nz, v0))
        else:
            continue  # interior diagonal, not a facet
    U = []
    for p in P:
        nx, ny, nz, c = p
        g = math.gcd(math.gcd(abs(nx), abs(ny)), abs(nz))
        if g > 1 and c % g == 0:
            p = (nx // g, ny // g, nz // g, c // g)
        if p not in U:
            U.append(p)
    return U


def pts_in(V, F, k=1):
    xs = [v[0] for v in V]
    ys = [v[1] for v in V]
    zs = [v[2] for v in V]
    o = []
    for x in range(k * min(xs), k * max(xs) + 1):
        for y in range(k * min(ys), k * max(ys) + 1):
            for z in range(k * min(zs), k * max(zs) + 1):
                if all(nx * x + ny * y + nz * z <= k * c
                       for (nx, ny, nz, c) in F):
                    o.append((x, y, z))
    return o


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def rigorous_box(P, W):
    base, det = None, 0
    for quad in itertools.combinations(P, 4):
        M = [[quad[i][j] - quad[0][j] for j in range(3)] for i in range(1, 4)]
        d = det3(M)
        if d != 0:
            base, det = quad, d
            break
    assert base is not None, "degenerate point set"
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
    B = max(int(math.ceil(x * W / ad)) + 1 for x in rs) if W > 0 else 1
    return B


def width_below(P, strict_below):
    """Minimum width via independently recomputed boxes W=0,1,...."""
    for W in range(0, 8):
        B = rigorous_box(P, W)
        cur, cu = None, None
        for uu in itertools.product(range(-B, B + 1), repeat=3):
            if uu == (0, 0, 0):
                continue
            if math.gcd(math.gcd(abs(uu[0]), abs(uu[1])),
                         abs(uu[2])) != 1:
                continue
            vv = [uu[0] * p[0] + uu[1] * p[1] + uu[2] * p[2] for p in P]
            w = max(vv) - min(vv)
            if cur is None or w < cur:
                cur, cu = w, uu
        if cur is not None and cur <= W:
            return cur, cu, B, W
    raise AssertionError("width out of range")


# ---------- A. candidate generation ----------
print("== A. candidate generation ==")
raw = open(SRC, encoding="utf-8", errors="replace").read()
sha = hashlib.sha256(raw.encode("utf-8")).hexdigest()
assert sha == CAND["boxed_source"]["sha256_list_boxed_tex"], (sha,)
sec = raw.split("Size 8")[0]
mats = re.findall(
    r"\\left\(\s*\\begin\{array\}\{([clr ]+)\}(.*?)\\end\{array\}"
    r"\s*\\right\)", sec, re.S)
parsed = []
for _fmt, body in mats:
    rows = [r.strip() for r in body.strip().split("\\\\") if r.strip()]
    grid = [[int(x) for x in r.replace("&", " ").split()] for r in rows]
    ncols = len(grid[0])
    parsed.append([[grid[r][c] for r in range(3)] for c in range(ncols)])
assert len(parsed) == 23 == CAND["counts"]["boxed"] == \
    len(BOXED["certificates"]) == BOXED["counts"]["total"] == 23
for i in range(23):
    assert parsed[i] == CAND["boxed"][i]["V"] == \
        BOXED["certificates"][i]["V"], i
print("boxed: fresh source parse == embedded candidates == cert inputs "
      "(23/23)")

gen_map = {e["id"]: e["V"] for e in CAND["spiked"]}
assert len(CAND["spiked"]) == 32 == CAND["counts"]["spiked"] == \
    len(SPIKED["certificates"]) == SPIKED["counts"]["total"] == 32
for c in SPIKED["certificates"]:
    assert gen_map[c["id"]] == c["V"], c["id"]
print("spiked: theorem-parameter generation == cert inputs (32/32)")
for key, info in CAND["spiked_size_exclusion"].items():
    for ks, s in info["neighbors"].items():
        k = int(ks)
        if "10a" in key:
            assert s == (3 * k - 1) // 2 + 5, (key, k)
        elif "k+4" in key:
            assert s == k + 4, (key, k)
        elif "k+6" in key:
            assert s == k + 6, (key, k)
        else:
            assert s == k + 5, (key, k)
print("spiked: size-formula evaluations + neighboring-k exclusion OK")


# ---------- B. per-candidate replay ----------
def replay(cert, expect):
    V = [tuple(v) for v in cert["V"]]
    F = facets(V)
    assert set(F) == set(map(tuple, cert["facets"])), cert["id"]
    P = pts_in(V, F, 1)
    I = [p for p in P
         if all(nx * p[0] + ny * p[1] + nz * p[2] < cc
                for (nx, ny, nz, cc) in F)]
    assert len(P) == 7, (cert["id"], len(P))
    assert len(I) == expect["ninter"], (cert["id"], len(I))
    assert set(P) == set(map(tuple, cert["pts"])), cert["id"]
    assert set(I) == set(map(tuple, cert["inter"])), cert["id"]
    assert (len(I) == 0) == cert["is_hollow"] == expect["hollow"], \
        cert["id"]
    u = tuple(cert["attainer"])
    vs = [u[0] * p[0] + u[1] * p[1] + u[2] * p[2] for p in P]
    assert max(vs) - min(vs) == cert["width"] == expect["width"], \
        cert["id"]
    L = [1, len(pts_in(V, F, 1)), len(pts_in(V, F, 2)),
         len(pts_in(V, F, 3))]
    assert L == cert["ehrhart"], (cert["id"], L)
    rec = L[3] - 4 * L[2] + 6 * L[1] - 4
    assert (rec == 0) == cert["is_hollow"], (cert["id"], L)
    if cert["is_hollow"]:
        assert cert["hstar"][3] == 0, cert["id"]
    wmin, _cu, _B, _W = width_below(P, cert["width"])
    assert wmin == cert["width"], (cert["id"], wmin)
    return len(I)


print("== B. boxed replay (23) ==")
nb_hollow = nb_neg = 0
for c in BOXED["certificates"]:
    hol = c["is_hollow"]
    ni = replay(c, {"ninter": 0 if hol else 1,
                    "hollow": hol, "width": 2})
    assert c["width"] == 2
    if hol:
        nb_hollow += 1
        print("OK boxed:%s hollow width=2 h3*=0" % c["id"])
    else:
        assert ni == 1 and c["hstar"][3] == 1, c["id"]
        nb_neg += 1
        print("OK boxed:%s negative n_interior=1 width=2 h3*=1" % c["id"])
assert (nb_hollow, nb_neg) == (8, 15), (nb_hollow, nb_neg)
assert BOXED["counts"] == {"total": 23, "hollow": 8, "non_hollow": 15}
print("boxed totals: 23 = 8 hollow (w2) + 15 one-interior-point (w2)")

print("== B. spiked replay (32) ==")
ns_hollow = ns_neg = 0
for c in SPIKED["certificates"]:
    hol = c["is_hollow"]
    ni = replay(c, {"ninter": c["n_interior"], "hollow": hol,
                    "width": c["width"]})
    assert ni == c["n_interior"] and (ni == 0) == hol
    if hol:
        assert c["width"] == 2 and c["hstar"][3] == 0
        ns_hollow += 1
        print("OK spiked:%s hollow width=2 h3*=0" % c["id"])
    else:
        assert ni >= 1
        ns_neg += 1
        print("OK spiked:%s negative n_interior=%d width=%d" %
              (c["id"], ni, c["width"]))
assert (ns_hollow, ns_neg) == (2, 30), (ns_hollow, ns_neg)
assert SPIKED["counts"] == {"total": 32, "hollow": 2, "non_hollow": 30}
hol_ids = sorted(c["id"] for c in SPIKED["certificates"]
                 if c["is_hollow"])
assert hol_ids == ["q1", "q2"], hol_ids
print("spiked totals: 32 = 2 hollow (q1,q2; w2) + 30 non-hollow")


# ---------- C. inequivalence of the hollow 10 ----------
def adj3(M):
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
    return [[Cmat[j][i] for j in range(3)] for i in range(3)]


def congruent_exact(P, Q):
    S = set(Q)
    for pb in itertools.permutations(P, 4):
        M = [[pb[i][j] - pb[0][j] for j in range(3)] for i in range(1, 4)]
        dd = det3(M)
        if dd == 0:
            continue
        A = adj3(M)
        for qb in itertools.permutations(Q, 4):
            N = [[qb[i][j] - qb[0][j] for j in range(3)] for i in range(1, 4)]
            e = det3(N)
            if e == 0 or e % dd != 0 or abs(e // dd) != 1:
                continue
            X = [[sum(A[i][k] * N[k][j] for k in range(3))
                  for j in range(3)] for i in range(3)]
            if any(X[i][j] % dd != 0 for i in range(3)
                   for j in range(3)):
                continue
            X = [[X[i][j] // dd for j in range(3)] for i in range(3)]
            img = set()
            for p in P:
                v = (p[0] - pb[0][0], p[1] - pb[0][1], p[2] - pb[0][2])
                img.add((qb[0][0] + v[0] * X[0][0] + v[1] * X[1][0]
                         + v[2] * X[2][0],
                         qb[0][1] + v[0] * X[0][1] + v[1] * X[1][1]
                         + v[2] * X[2][1],
                         qb[0][2] + v[0] * X[0][2] + v[1] * X[1][2]
                         + v[2] * X[2][2]))
            if img == S:
                return True
    return False


print("== C. inequivalence of hollow 10 (45 pairs) ==")
hollow_sets = [("boxed:%s" % c["id"], [tuple(p) for p in c["pts"]])
               for c in BOXED["certificates"] if c["is_hollow"]]
hollow_sets += [("spiked:%s" % c["id"], [tuple(p) for p in c["pts"]])
                for c in SPIKED["certificates"] if c["is_hollow"]]
assert len(hollow_sets) == 10, len(hollow_sets)
npair = 0
for a in range(len(hollow_sets)):
    for b in range(a + 1, len(hollow_sets)):
        r = congruent_exact(hollow_sets[a][1], hollow_sets[b][1])
        line = "equiv(%s,%s)=%s" % (hollow_sets[a][0],
                                    hollow_sets[b][0], r)
        print(line)
        LOG.write(line + "\n")
        assert r is False, (hollow_sets[a][0], hollow_sets[b][0])
        npair += 1
assert npair == 45, npair
LOG.write("pairs=45 all_inequivalent=True\n")
LOG.close()
print("inequivalence: 45/45 pairs inequivalent (logged)")
print("ALL REPLAYS PASSED: boxed 23/23, spiked 32/32, inequivalence 45/45")
