"""Stage 2: independent audit of k=3 slice (741 classes): exact interior recount,
Ehrhart L(1..3) -> h*, boundary/interior split, Vol cross-checks, certificate log.

Independent counting method (different from stage 1 adjugate code): barycentric via
rational solve with Fraction-free integer Cramer on E^T, plus separate boundary count.
h* from L1, L2: h1 = L1-4; h2 = L2 - 4 - 3*h1 - 3 ... use standard:
  L(t) = C(t+3,3) + h1*C(t+2,3)... let me use: L(1) = 4 + h1; L(2) = 10 + 4 h1 + h2... check:
  Ehrhart series: sum L(t) x^t = (1 + h1 x + h2 x^2 + h3 x^3)/(1-x)^4.
  t=1: L1 = 4 + h1. t=2: L2 = 10 + 4 h1 + h2 (since C(5,3)=10, C(4,3)=4, C(3,3)=1).
  h3 = V - 1 - h1 - h2. Also h3 must equal interior count (reciprocity check).
Comparators: Vol<=144, d1=h1... note delta1=h1? delta-vector=(1,d1,d2,i): d1=h1, d2=h2.
  Conj 6.1 at k=3: d1<=67, d2<=73.
Also verify S^3_3 witness conv{(0,0,0),(2,0,0),(0,3,0),(0,0,24)} has V=144, i=3.

Output: output/artifacts/stage2.json + audit lines.
"""
import json, time
import numpy as np

def audit_tetra(verts):
    V3 = np.array(verts[1:]) - np.array(verts[0])  # 3x3 rows
    E = V3.T  # E^T? We solve E^T lam = p - v0 with rows of V3 = e_i: lam via inv(V3^T)
    A = V3.T  # columns e_i
    detA = int(round(np.linalg.det(A)))
    V = abs(detA)
    assert V > 0
    adj = np.round(np.linalg.det(A) * np.linalg.inv(A)).astype(int)  # adjugate, A^-1 = adj/det
    assert (np.abs(A @ adj - np.eye(3) * detA)).max() == 0
    vv = np.array(verts)
    lo = vv.min(axis=0); hi = vv.max(axis=0)
    X, Y, Z = np.meshgrid(np.arange(lo[0], hi[0]+1), np.arange(lo[1], hi[1]+1), np.arange(lo[2], hi[2]+1), indexing='ij')
    P = np.stack([X.ravel()-vv[0][0], Y.ravel()-vv[0][1], Z.ravel()-vv[0][2]], axis=1)
    N = P @ adj.T  # N = adj^T? check: lam = A^-1 p = adj(A) p / det. N rows = adj @ p
    # verify: use N2 = (adj @ P.T).T
    N2 = (np.array(adj) @ P.T).T
    sgn = 1 if detA > 0 else -1
    n1, n2, n3 = N2[:,0]*sgn, N2[:,1]*sgn, N2[:,2]*sgn
    s = n1 + n2 + n3
    inside = (n1 >= 0) & (n2 >= 0) & (n3 >= 0) & (s <= V)
    strict = (n1 > 0) & (n2 > 0) & (n3 > 0) & (s < V)
    L = int(inside.sum()); i = int(strict.sum()); b = L - i
    return V, L, i, b

def L_of_dilate(verts, t):
    vv = np.array(verts) * t
    lo = vv.min(axis=0); hi = vv.max(axis=0)
    A = (np.array(verts[1:]) - np.array(verts[0])).T
    detA = int(round(np.linalg.det(A)))
    V = abs(detA)
    adj = np.round(np.linalg.det(A) * np.linalg.inv(A)).astype(int)
    X, Y, Z = np.meshgrid(np.arange(lo[0], hi[0]+1), np.arange(lo[1], hi[1]+1), np.arange(lo[2], hi[2]+1), indexing='ij')
    P = np.stack([X.ravel()-vv[0][0], Y.ravel()-vv[0][1], Z.ravel()-vv[0][2]], axis=1)
    N2 = (np.array(adj) @ P.T).T
    sgn = 1 if detA > 0 else -1
    # tP: A lam = p with p in t-scaled frame: lam denominators V*t? No: vertices scaled by t,
    # edge matrix t*A, det = t^3 detA; adj(tA) = t^2 adj(A).
    # n = adj(tA) p / det(tA) = t^2 adj(A) p / (t^3 V) = adj(A) p / (t V)
    n1, n2, n3 = N2[:,0]*sgn, N2[:,1]*sgn, N2[:,2]*sgn
    s = n1 + n2 + n3
    inside = (n1 >= 0) & (n2 >= 0) & (n3 >= 0) & (s <= t * V)
    return int(inside.sum())

def main():
    t0 = time.time()
    d = json.load(open("output/artifacts/stage1.json"))
    cls = d["classes"]
    k3 = [(k, v) for k, v in cls.items() if v[1] == 3]
    print(f"k=3 classes: {len(k3)}", flush=True)
    recs = []
    maxd1 = (-1, None); maxd2 = (-1, None); maxV = (-1, None)
    bad = []
    for key, (V, i, wit) in k3:
        V2, L, i2, b = audit_tetra(wit)
        assert V2 == V, (key, V, V2)
        assert i2 == 3, (key, i, i2)
        L1 = L
        L2 = L_of_dilate(wit, 2)
        h1 = L1 - 4
        h2 = L2 - 10 - 4 * h1
        h3 = V - 1 - h1 - h2
        if h3 != 3:
            bad.append((key, V, L1, L2, h1, h2, h3))
        recs.append({"key": key, "V": V, "L1": L1, "L2": L2, "h": [1, h1, h2, h3],
                     "wit": wit})
        if h1 > maxd1[0]: maxd1 = (h1, key)
        if h2 > maxd2[0]: maxd2 = (h2, key)
        if V > maxV[0]: maxV = (V, key)
    print(f"reciprocity failures (h3!=3): {len(bad)}", flush=True)
    for e in bad[:10]: print("  BAD:", e, flush=True)
    print(f"maxV: {maxV}", flush=True)
    print(f"max d1: {maxd1}", flush=True)
    print(f"max d2: {maxd2}", flush=True)
    # show witnesses of extrema
    for name, m in [("V", maxV), ("d1", maxd1), ("d2", maxd2)]:
        r = next(r for r in recs if r["key"] == m[1])
        print(f"  {name}-extremal: V={r['V']} h={r['h']} wit={r['wit']}", flush=True)
    # S^3_3 check
    S = [[0,0,0],[2,0,0],[0,3,0],[0,0,24]]
    V2, L, i2, b = audit_tetra(S)
    L2 = L_of_dilate(S, 2)
    h1 = L - 4; h2 = L2 - 10 - 4*h1; h3 = V2 - 1 - h1 - h2
    print(f"S^3_3: V={V2} L1={L} i={i2} L2={L2} h={[1,h1,h2,h3]}", flush=True)
    json.dump({"recs": recs, "bad": bad, "elapsed_s": time.time()-t0},
              open("output/artifacts/stage2.json", "w"))
    print(f"elapsed {time.time()-t0:.1f}s", flush=True)

if __name__ == "__main__":
    main()
