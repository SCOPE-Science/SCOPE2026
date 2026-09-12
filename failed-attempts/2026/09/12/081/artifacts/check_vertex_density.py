"""Small-scale Euclidean check: vertex density 2*lambda via Delaunay triangulation.

Sanity illustration that mean vertex count per area converges to 2*lambda
(in the flat limit), supporting mu* = 2*vol(B_1). Falls back to a vendored
Bowyer-Watson Delaunay implementation when scipy is unavailable.
"""
import math, random, json
random.seed(20260912)

# ---------- Delaunay via Bowyer-Watson (small point sets only) ----------
def circumcircle(ax, ay, bx, by, cx, cy):
    d = 2 * (ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))
    if abs(d) < 1e-14:
        return None
    ux = ((ax*ax+ay*ay)*(by-cy) + (bx*bx+by*by)*(cy-ay) + (cx*cx+cy*cy)*(ay-by)) / d
    uy = ((ax*ax+ay*ay)*(cx-bx) + (bx*bx+by*by)*(ax-cx) + (cx*cx+cy*cy)*(bx-ax)) / d
    return (ux, uy, (ax-ux)**2 + (ay-uy)**2)

def delaunay_count_vertices(pts, window):
    # pts: list of (x,y) incl. guard ring; count circumcenters inside window square
    n = len(pts)
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    mx, my = sum(xs)/n, sum(ys)/n
    M = max(max(abs(x-mx) for x in xs), max(abs(y-my) for y in ys)) * 10 + 10
    sup = [(mx-M, my-M), (mx+M, my-M), (mx+M, my+M), (mx-M, my+M)]
    V = list(pts) + sup
    tris = [(n, n+1, n+2), (n, n+2, n+3)]
    for pi in range(n):
        px, py = V[pi]
        bad = []
        for t in tris:
            cc = circumcircle(V[t[0]][0], V[t[0]][1], V[t[1]][0], V[t[1]][1],
                              V[t[2]][0], V[t[2]][1])
            if cc is None:
                continue
            ux, uy, r2 = cc
            if (px-ux)**2 + (py-uy)**2 < r2 - 1e-9:
                bad.append(t)
        bedges = {}
        for t in bad:
            for e in [(t[0],t[1]), (t[1],t[2]), (t[2],t[0])]:
                key = (min(e), max(e))
                bedges[key] = bedges.get(key, 0) + 1
        tris = [t for t in tris if t not in bad]
        for (a, b), c in bedges.items():
            if c == 1:
                tris.append((a, b, pi))
    cnt = 0
    x0, x1, y0, y1 = window
    for t in tris:
        if any(v >= n for v in t):
            continue
        cc = circumcircle(V[t[0]][0], V[t[0]][1], V[t[1]][0], V[t[1]][1],
                          V[t[2]][0], V[t[2]][1])
        if cc is None:
            continue
        ux, uy, _ = cc
        if x0 <= ux <= x1 and y0 <= uy <= y1:
            cnt += 1
    return cnt

def trial(lam, half=1.0, guard=0.6, reps=25):
    area = (2*half)**2
    tot = 0
    for _ in range(reps):
        m = 0
        pts = []
        # homogeneous Poisson via Poisson(total mean) number, uniform positions on extended box
        L = half + guard
        mean = lam * (2*L)**2
        k = random.poisson if hasattr(random, 'poisson') else None
        import numpy as np
        k = int(np.random.poisson(mean))
        pts = [(random.uniform(-L, L), random.uniform(-L, L)) for _ in range(k)]
        tot += delaunay_count_vertices(pts, (-half, half, -half, half))
    est = tot / reps / area / lam   # should be near 2
    return est

import numpy as np
np.random.seed(7)
for lam in [15, 30, 60]:
    est = trial(lam)
    print(f"lambda={lam}: estimated vertex density/lambda = {est:.3f} (flat limit 2.000)")
    assert abs(est - 2.0) < 0.35, est
print("OK: Euclidean vertex density consistent with 2*lambda (supports mu* = 2*vol(B1)).")
