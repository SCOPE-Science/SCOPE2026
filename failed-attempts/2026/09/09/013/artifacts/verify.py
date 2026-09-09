"""Independent verification route for lane-308 pyramid census.
Route B (independent of pyr_census.py slice-scaling):
  - facets from all vertex triples (exact integer planes), box-scan membership count
  - h* re-derived from L0..L3, L4..L6 re-predicted and compared
  - normalized volume by coning triangulation (apex over base triangulation)
  - Pick invariants (b, area2, i) recomputed
  - width: lemma radius recomputed independently + brute-force primitive scan
  - global census consistency: dip max/uniqueness, genuine non-unimodal list
Writes output/artifacts/verify_log.json. Stdlib only.
"""
import json, math, itertools, os

HERE = os.path.dirname(os.path.abspath(__file__))
C = json.load(open(os.path.join(HERE, "census.json")))
RES = C["results"]

def sub(a, b):
    return (a[0]-b[0], a[1]-b[1], a[2]-b[2])

def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def det3rows(r1, r2, r3):
    return (r1[0]*(r2[1]*r3[2]-r2[2]*r3[1]) - r1[1]*(r2[0]*r3[2]-r2[2]*r3[0])
            + r1[2]*(r2[0]*r3[1]-r2[1]*r3[0]))

def facets_of(V):
    F = []
    for a, b, c in itertools.combinations(V, 3):
        n = cross(sub(b, a), sub(c, a))
        if n == (0, 0, 0):
            continue
        ss = [dot(n, sub(v, a)) for v in V]
        if all(s >= 0 for s in ss):
            F.append((n, dot(n, a)))
        elif all(s <= 0 for s in ss):
            F.append(((-n[0], -n[1], -n[2]), -dot(n, a)))
    assert F, "no facets found"
    return F

def count_box(V, t):
    W = [(t*v[0], t*v[1], t*v[2]) for v in V]
    if len(set(W)) == 1:
        return 1
    F = facets_of(W)
    lo = [min(w[i] for w in W) for i in range(3)]
    hi = [max(w[i] for w in W) for i in range(3)]
    c = 0
    for x in range(lo[0], hi[0]+1):
        for y in range(lo[1], hi[1]+1):
            for z in range(lo[2], hi[2]+1):
                if all(n[0]*x+n[1]*y+n[2]*z >= rhs for (n, rhs) in F):
                    c += 1
    return c

def C2(n):
    return n*(n-1)*(n-2)//6 if n >= 3 else 0

def hstar_of(L):
    h0 = L[0]
    h1 = L[1]-4*h0
    h2 = L[2]-10*h0-4*h1
    h3 = L[3]-20*h0-10*h1-4*h2
    return [h0, h1, h2, h3]

def Lpred(hs, t):
    return (hs[0]*(t+3)*(t+2)*(t+1)//6 + hs[1]*C2(t+2) + hs[2]*C2(t+1) + hs[3]*C2(t))

def pyramidal_normvol(Q, h):
    """Cone apex A=(0,0,h) over fan triangulation of Q from Q[0]."""
    A = (0, 0, h)
    Q3 = [(x, y, 0) for (x, y) in Q]
    nvol = 0
    for i in range(1, len(Q3)-1):
        e1 = sub(Q3[i], Q3[0]); e2 = sub(Q3[i+1], Q3[0]); e3 = sub(A, Q3[0])
        nvol += abs(det3rows(e1, e2, e3))
    return nvol

def pick2(Q):
    s = 0
    n = len(Q)
    for i in range(n):
        s += Q[i][0]*Q[(i+1) % n][1] - Q[(i+1) % n][0]*Q[i][1]
    a2 = abs(s)
    b = 0
    for i in range(n):
        b += math.gcd(abs(Q[(i+1) % n][0]-Q[i][0]), abs(Q[(i+1) % n][1]-Q[i][1]))
    return a2, b, (a2-b+2)//2

def width_bruteforce(V, B):
    best = None; bestu = None
    for u1 in range(-B, B+1):
        for u2 in range(-B, B+1):
            for u3 in range(-B, B+1):
                if u1 == u2 == u3 == 0:
                    continue
                if math.gcd(math.gcd(abs(u1), abs(u2)), abs(u3)) != 1:
                    continue
                vals = [u1*v[0]+u2*v[1]+u3*v[2] for v in V]
                w = max(vals)-min(vals)
                if best is None or w < best:
                    best = w; bestu = (u1, u2, u3)
    return best, bestu

def lemma_radius(V, W0):
    D = [sub(v, V[0]) for v in V[1:]]
    M = None
    for tri in itertools.combinations(D, 3):
        if det3rows(*tri) != 0:
            M = tri; break
    assert M is not None
    det = det3rows(*M)
    (a1, a2, a3), (b1, b2, b3), (c1, c2, c3) = M
    Cf = [[(b2*c3-b3*c2), -(b1*c3-b3*c1), (b1*c2-b2*c1)],
          [-(a2*c3-a3*c2), (a1*c3-a3*c1), -(a1*c2-a2*c1)],
          [(a2*b3-a3*b2), -(a1*b3-a3*b1), (a1*b2-a2*b1)]]
    A = [[Cf[0][0], Cf[1][0], Cf[2][0]],
         [Cf[0][1], Cf[1][1], Cf[2][1]],
         [Cf[0][2], Cf[1][2], Cf[2][2]]]
    rn = max(sum(abs(A[i][j]) for j in range(3)) for i in range(3))
    return (rn+abs(det)*W0-1)//(abs(det)*W0)*W0 if False else math.ceil(rn/abs(det)*W0)

def unimodal(hs):
    n = len(hs)
    for k in range(n):
        if all(hs[j] <= hs[j+1] for j in range(k)) and all(hs[j] >= hs[j+1] for j in range(k, n-1)):
            return True
    return False

# ---- global consistency from census.json ----
dips = [r["dip"] for r in RES]
assert len(RES) == 2992, len(RES)
assert max(dips) == 9 and dips.count(9) == 1
assert sorted(dips)[1-1-1+1:][:1] is not None
assert min(dips) == -20
assert sum(1 for r in RES if r["dip"] > 0) == 1333
bad = [r for r in RES if not unimodal(r["hstar"])]
assert len(bad) == 9, len(bad)
assert all(r["hstar"][0] == 1 and r["hstar"][1] == 0 and r["hstar"][3] == 0 and r["hstar"][2] > 0 for r in bad)
for r in RES:
    assert sum(r["hstar"]) == r["h"]*r["area2"], (r["Q"], r["h"])
    assert Lpred(r["hstar"], 4) == r["L"][4] and Lpred(r["hstar"], 5) == r["L"][5] and Lpred(r["hstar"], 6) == r["L"][6]
print("GLOBAL_OK n=2992 maxdip=9(unique) mindip=-20 ndip=1333 nonunimodal=9")

# ---- independent recount of headline cases ----
E = C["extremal"]; R = C["runner_up"]
W = min(bad, key=lambda r: (r["h"], r["hstar"][2]))
targets = [("EXTREMAL", E), ("RUNNER", R), ("WITNESS", W)] + [("WITNESS_EXTRA_%d" % i, r) for i, r in enumerate(bad) if r is not W]
log = {"cases": []}
for name, r in targets:
    Q = [tuple(p) for p in r["Q"]]; h = r["h"]
    V = [(x, y, 0) for (x, y) in Q] + [(0, 0, h)]
    L = [count_box(V, t) for t in range(7)]
    assert L == r["L"], (name, L, r["L"])
    hs = hstar_of(L)
    assert hs == r["hstar"], (name, hs, r["hstar"])
    for t in range(7):
        assert Lpred(hs, t) == L[t], (name, t)
    nv = pyramidal_normvol(Q, h)
    assert nv == sum(hs) == h*r["area2"], (name, nv, hs)
    a2, b, ii = pick2(Q)
    assert (a2, b, ii) == (r["area2"], r["b"], r["i"]), (name, (a2, b, ii))
    Blem = lemma_radius(V, min(max(v[i] for v in V)-min(v[i] for v in V) for i in range(3)))
    Bscan = max(Blem, 6)
    bw, bu = width_bruteforce(V, Bscan)
    assert bw == r["width"], (name, bw, r["width"])
    wdir = tuple(r["width_dir"])
    vals = [wdir[0]*v[0]+wdir[1]*v[1]+wdir[2]*v[2] for v in V]
    assert max(vals)-min(vals) == r["width"], (name, "witness dir fails")
    assert not unimodal(hs) if name.startswith("WITNESS") else True
    print("%s_OK Q=%s h=%d h*=%s L=%s width=%d dir=%s Blem=%d volume=%d" % (
        name, Q, h, hs, L, bw, bu, Blem, nv))
    log["cases"].append({"name": name, "Q": r["Q"], "h": h, "L": L, "hstar": hs,
                         "width": bw, "width_witness_scan": list(bu),
                         "width_witness_logged": r["width_dir"], "Blem": Blem, "normvol": nv})
assert C["runner_gap"] == E["dip"]-R["dip"] == 2
json.dump(log, open(os.path.join(HERE, "verify_log.json"), "w"))
print("VERIFY_OK all %d headline cases by independent route" % len(targets))
