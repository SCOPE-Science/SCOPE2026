"""Replay script: re-runs full audit from frozen input output/artifacts/KS3_RefPoly.d3.
Steps: parse (assert 4319), facets, reflexivity, nfac==Nvert header, L(0..3) box counts,
exact h* interpolation, V==sum(h), triangulation fan volume cross-check, unimodality,
2P + 3P decomposition checks, L1==Mpts header. Rebuilds distribution tables.
Stdlib + numpy only. Usage: python3 replay.py [--limit N]
"""
import sys, os, re, math, json, time, hashlib
from fractions import Fraction
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(HERE, "output", "artifacts", "KS3_RefPoly.d3")
if not os.path.exists(ART):
    ART = os.path.join(HERE, "KS3_RefPoly.d3")

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def parse_refpoly(path):
    pat = re.compile(r"^3\s+(\d+)\s+M:(\d+)\s+(\d+)\s+N:(\d+)\s+(\d+)\s+Pic:(-?\d+)\s+Cor:(-?\d+)\s*$")
    polys = []
    with open(path) as f:
        lines = f.read().splitlines()
    i, n = 0, len(lines)
    while i < n:
        if not lines[i].strip():
            i += 1; continue
        m = pat.match(lines[i].strip()); assert m, f"bad header: {lines[i]!r}"
        nv, Mpts, Mvert, Npts, Nvert, Pic, Cor = map(int, m.groups())
        rows = [list(map(int, lines[i+k].split())) for k in (1, 2, 3)]
        assert all(len(r) == nv for r in rows)
        verts = [tuple(rows[r][c] for r in range(3)) for c in range(nv)]
        polys.append(dict(id=len(polys), nv=nv, Mpts=Mpts, Mvert=Mvert, Npts=Npts,
                          Nvert=Nvert, Pic=Pic, Cor=Cor, verts=verts))
        i += 4
    return polys

def cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def dot(a, b): return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def sub(a, b): return (a[0]-b[0], a[1]-b[1], a[2]-b[2])
def g3(v): return math.gcd(math.gcd(abs(v[0]), abs(v[1])), abs(v[2]))

def facets_of(verts):
    fac = {}
    nv = len(verts)
    for i in range(nv):
        for j in range(i+1, nv):
            for k in range(j+1, nv):
                nn = cross(sub(verts[j], verts[i]), sub(verts[k], verts[i]))
                if nn == (0, 0, 0): continue
                g = g3(nn); nn = (nn[0]//g, nn[1]//g, nn[2]//g)
                c = dot(nn, verts[i])
                s = [dot(nn, v)-c for v in verts]
                if all(x <= 0 for x in s): pass
                elif all(x >= 0 for x in s): nn = (-nn[0], -nn[1], -nn[2]); c = -c
                else: continue
                fac[(nn, c)] = True
    return list(fac.keys())

def box_points(Fs, lo, hi):
    xs = np.arange(lo[0], hi[0]+1); ys = np.arange(lo[1], hi[1]+1); zs = np.arange(lo[2], hi[2]+1)
    X, Y, Z = np.meshgrid(xs, ys, zs, indexing="ij")
    pts = np.stack([X.ravel(), Y.ravel(), Z.ravel()], axis=1)
    m = np.ones(len(pts), dtype=bool)
    for (a, b, c), d in Fs:
        m &= (pts[:, 0]*a + pts[:, 1]*b + pts[:, 2]*c) <= d
        if not m.any(): break
    return pts[m]

def Cnk(n, k):
    if n < k or k < 0: return 0
    r = 1
    for j in range(1, k+1): r = r*(n-k+j)//j
    return r

def hstar(L):
    M = [[Cnk(t+3-k, 3) for k in range(4)] for t in range(4)]
    A = [[Fraction(M[i][j]) for j in range(4)] + [Fraction(L[i])] for i in range(4)]
    for col in range(4):
        piv = next(r for r in range(col, 4) if A[r][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        A[col] = [x/A[col][col] for x in A[col]]
        for r in range(4):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [A[r][j]-f*A[col][j] for j in range(5)]
    h = []
    for i in range(4):
        assert A[i][4].denominator == 1, (L, A)
        h.append(int(A[i][4]))
    return h

def tri_vol(verts, facets):
    total = 0
    for (n, c) in facets:
        Fv = [v for v in verts if dot(n, v) == c]
        cx = sum(v[0] for v in Fv)/len(Fv); cy = sum(v[1] for v in Fv)/len(Fv); cz = sum(v[2] for v in Fv)/len(Fv)
        e1 = next((v[0]-Fv[0][0], v[1]-Fv[0][1], v[2]-Fv[0][2]) for v in Fv[1:] if (v[0]-Fv[0][0], v[1]-Fv[0][1], v[2]-Fv[0][2]) != (0, 0, 0))
        n1 = math.sqrt(e1[0]**2+e1[1]**2+e1[2]**2); e1 = (e1[0]/n1, e1[1]/n1, e1[2]/n1)
        nn1 = math.sqrt(n[0]**2+n[1]**2+n[2]**2); nn = (n[0]/nn1, n[1]/nn1, n[2]/nn1)
        e2 = (nn[1]*e1[2]-nn[2]*e1[1], nn[2]*e1[0]-nn[0]*e1[2], nn[0]*e1[1]-nn[1]*e1[0])
        angs = sorted([(math.atan2((v[0]-cx)*e2[0]+(v[1]-cy)*e2[1]+(v[2]-cz)*e2[2],
                                   (v[0]-cx)*e1[0]+(v[1]-cy)*e1[1]+(v[2]-cz)*e1[2]), v) for v in Fv])
        order = [v for _, v in angs]; v0 = order[0]
        for k in range(1, len(order)-1):
            a, b = order[k], order[k+1]
            total += abs(v0[0]*(a[1]*b[2]-a[2]*b[1])-v0[1]*(a[0]*b[2]-a[2]*b[0])+v0[2]*(a[0]*b[1]-a[1]*b[0]))
    return int(total)

def main():
    lim = int(sys.argv[sys.argv.index("--limit")+1]) if "--limit" in sys.argv else None
    print("input:", ART, "sha256:", sha256(ART))
    polys = parse_refpoly(ART)
    assert len(polys) == 4319, len(polys)
    if lim: polys = polys[:lim]
    t0 = time.time(); flags = 0
    from collections import Counter
    hc, vc = Counter(), Counter()
    for P in polys:
        V = np.array(P["verts"]); F = facets_of(P["verts"])
        assert all(c == 1 for _, c in F), (P["id"], F)          # reflexivity
        assert len(F) == P["Nvert"], (P["id"], len(F), P["Nvert"])
        L = [1]; keep = {}
        for t in (1, 2, 3):
            Q = box_points([((n[0], n[1], n[2]), t*c) for (n, c) in F], t*V.min(axis=0), t*V.max(axis=0))
            keep[t] = Q; L.append(int(len(Q)))
        assert L[1] == P["Mpts"], (P["id"], L[1], P["Mpts"])
        h = hstar(L)
        assert h[0] == 1 and h[3] == 1 and h[1] == h[2], (P["id"], L, h)
        Vv = L[3]-3*L[2]+3*L[1]-L[0]
        assert Vv == sum(h), (P["id"], L, h)
        assert tri_vol(P["verts"], F) == Vv, (P["id"], Vv)
        assert any(all(h[i] <= h[i+1] for i in range(m)) and all(h[i] >= h[i+1] for i in range(m, 3)) for m in range(4)), (P["id"], h)
        S1 = set(map(tuple, keep[1].tolist())); S1l = list(S1)
        for q in map(tuple, keep[2].tolist()):
            assert any((q[0]-p[0], q[1]-p[1], q[2]-p[2]) in S1 for p in S1l), (P["id"], "2P fail", q)
        S2 = set(map(tuple, keep[2].tolist()))
        for q in map(tuple, keep[3].tolist()):
            assert any((q[0]-p[0], q[1]-p[1], q[2]-p[2]) in S2 for p in S1l), (P["id"], "3P fail", q)
        hc[tuple(h)] += 1; vc[Vv] += 1
    print(f"REPLAY OK: {len(polys)} polys in {time.time()-t0:.1f}s; distinct h*: {len(hc)}; V range {min(vc)}..{max(vc)}")
    print("h* table:", sorted((list(k), v) for k, v in hc.items()))
    print("V table:", sorted(vc.items()))

if __name__ == "__main__":
    main()
