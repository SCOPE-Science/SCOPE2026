"""Verifier: uniform lattice width 2 over centrally symmetric reflexive 3-polytopes.
Reads RefPoly.d3 (Kreuzer-Skarke list, 4319 entries) from same directory, filters to
centrally symmetric classes, certifies width exactly 2 for each via explicit attaining
direction (upper bound) plus general symmetric lower bound, with facet-distance-1
reflexivity check. Cross-checks normalized volumes by two independent triangulations
(origin-fan vs vertex-fan, centroid-ordered facet cycles). Stdlib + numpy only.
"""
import math, os
import numpy as np
from math import gcd
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'RefPoly.d3')

def parse(path):
    lines = [l for l in open(path).read().splitlines() if l.strip() != '']
    entries, i, n = [], 0, len(lines)
    while i < n:
        parts = lines[i].split()
        assert parts[0] == '3', parts
        nv = int(parts[1]); i += 1
        rows = []
        for k in range(3):
            rows.append(list(map(int, lines[i].split()))); i += 1
            assert len(rows[-1]) == nv
        entries.append([(rows[0][j], rows[1][j], rows[2][j]) for j in range(nv)])
    return entries

def hull_facets(pts):
    P = list(set(pts)); m = len(P); planes = []
    for a in range(m):
        for b in range(a+1, m):
            for c in range(b+1, m):
                A, B, C = P[a], P[b], P[c]
                ab = (B[0]-A[0], B[1]-A[1], B[2]-A[2]); ac = (C[0]-A[0], C[1]-A[1], C[2]-A[2])
                n = (ab[1]*ac[2]-ab[2]*ac[1], ab[2]*ac[0]-ab[0]*ac[2], ab[0]*ac[1]-ab[1]*ac[0])
                if n == (0,0,0): continue
                dots = [n[0]*(Q[0]-A[0])+n[1]*(Q[1]-A[1])+n[2]*(Q[2]-A[2]) for Q in P]
                if min(dots) < 0 and max(dots) > 0: continue
                nn = n if max(dots) == 0 else (-n[0], -n[1], -n[2])
                g = gcd(gcd(abs(nn[0]), abs(nn[1])), abs(nn[2]))
                nn = (nn[0]//g, nn[1]//g, nn[2]//g)
                c0 = nn[0]*A[0]+nn[1]*A[1]+nn[2]*A[2]
                planes.append((nn, c0))
    out = []
    for (nn, c0) in sorted(set(planes)):
        S = [Q for Q in P if nn[0]*Q[0]+nn[1]*Q[1]+nn[2]*Q[2] == c0]
        if len(S) >= 3:
            A = S[0]
            M = np.array([[Q[0]-A[0], Q[1]-A[1], Q[2]-A[2]] for Q in S])
            if np.linalg.matrix_rank(M) == 2:
                out.append((nn, c0, S))
    return out

def _ordered(S):
    C = np.mean(np.array(S, float), axis=0)
    M = np.array([np.array(Q, float)-C for Q in S])
    u, sv, vt = np.linalg.svd(M)
    nrm = vt[2]
    e1 = np.array(S[0], float)-C
    e1 = e1-(e1@nrm)*nrm; e1 = e1/np.linalg.norm(e1)
    e3 = np.cross(nrm, e1)
    angs = sorted((math.atan2((np.array(Q, float)-C)@e3, (np.array(Q, float)-C)@e1), Q) for Q in S)
    return [Q for _, Q in angs]

def width(V, u):
    vals = [u[0]*v[0]+u[1]*v[1]+u[2]*v[2] for v in V]
    return max(vals)-min(vals)

def vol_origin(F):
    t = 0
    for (nn, c0, S) in F:
        cyc = _ordered(S)
        for k in range(1, len(cyc)-1):
            t += abs(round(float(np.linalg.det(np.array([cyc[0], cyc[k], cyc[k+1]], float)))))
    return t

def vol_apex(V, F):
    A0 = np.array(V[0], float); t = 0
    for (nn, c0, S) in F:
        cyc = _ordered(S)
        for k in range(1, len(cyc)-1):
            M = np.array([np.array(cyc[0])-A0, np.array(cyc[k])-A0, np.array(cyc[k+1])-A0], float)
            t += abs(round(float(np.linalg.det(M))))
    return t



def prim3(p):
    import math
    return math.gcd(math.gcd(abs(p[0]), abs(p[1])), abs(p[2])) == 1

def width2_pairs(V, F):
    D = list(set(nn for (nn, c0, S) in F))
    FD = hull_facets(D)
    xs = [p[0] for p in D]; ys = [p[1] for p in D]; zs = [p[2] for p in D]
    pts = [(x, y, z) for x in range(min(xs), max(xs)+1) for y in range(min(ys), max(ys)+1)
           for z in range(min(zs), max(zs)+1)
           if all(nn[0]*x+nn[1]*y+nn[2]*z <= c0 for (nn, c0, S) in FD)]
    bnd = [p for p in pts if any(nn[0]*p[0]+nn[1]*p[1]+nn[2]*p[2] == c0 for (nn, c0, S) in FD)]
    assert all(prim3(p) for p in bnd)
    reps = []
    seen = set()
    for p in bnd:
        q = (-p[0], -p[1], -p[2])
        if p in seen or q in seen: continue
        seen.add(p); reps.append(p)
    assert all(width(V, p) == 2 for p in reps)
    return len(reps)

def main():
    entries = parse(SRC)
    assert len(entries) == 4319, len(entries)
    sym = [i for i, V in enumerate(entries) if all((-x,-y,-z) in set(V) for (x,y,z) in V)]
    print("total=%d symmetric=%d" % (len(entries), len(sym)))
    assert len(sym) == 13, sym
    for idx in sym:
        V = entries[idx]
        F = hull_facets(V)
        assert all(c0 == 1 for (_, c0, _) in F), idx
        v1 = vol_origin(F); v2 = vol_apex(V, F)
        assert v1 == v2, (idx, v1, v2)
        u = F[0][0]
        w = width(V, u)
        assert w == 2, (idx, u, w)
        xs = [v[0] for v in V]; ys = [v[1] for v in V]; zs = [v[2] for v in V]
        LP = [(x,y,z) for x in range(min(xs),max(xs)+1) for y in range(min(ys),max(ys)+1)
              for z in range(min(zs),max(zs)+1)
              if all(nn[0]*x+nn[1]*y+nn[2]*z <= c0 for (nn,c0,S) in F)]
        INT = [p for p in LP if all(nn[0]*p[0]+nn[1]*p[1]+nn[2]*p[2] < c0 for (nn,c0,S) in F)]
        assert INT == [(0,0,0)], (idx, INT)
        DMAP = {418: 13, 419: 3, 924: 7, 925: 5, 974: 4, 975: 9, 2310: 10, 2311: 4, 3056: 6, 3998: 8, 3999: 5, 4309: 7, 4310: 6}
        np2 = width2_pairs(V, F)
        assert np2 == DMAP[idx+1], (idx, np2)
        print("KS#%d: nv=%d nfac=%d attain=%s width=%d normvol=%d npts=%d w2pairs=%d" % (idx+1, len(V), len(F), u, w, v1, len(LP), np2))
    print("VERIFY_OK")

if __name__ == '__main__':
    main()
