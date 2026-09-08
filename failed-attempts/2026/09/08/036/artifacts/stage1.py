"""Stage 1: enumerate HNF superset V<=144, canonicalize, count interior per class.

Per raw tetra: compute key=canon_key (exact class), i_current = fast interior count.
Per class: i_min = min over appearances (true interior count of the class).
Also: class_vol = volume (= same for all appearances); witness = lexicographically
smallest vertex tuple among appearances with i_current == i_min (a true V<=144
representative whenever the class genuinely has volume <=144).

Interior count: vectorized barycentric test over bounding box.
E = edge matrix (rows e1,e2,e3), V=|det|. For p in box: solve E^T lambda = p
  via adjugate: n_i = (adj(E^T) p)_i, interior iff all n_i > 0 and sum < V.
Bpad: iterate box of translated verts (min..max per coord). For V<=144 boxes are small.

Speed: numpy batch over box points. ~2M tetrahedra... too slow in Python if naive
(~2M x HNF(24x e-gcd) + box scan). Estimate: HNF ~50us => 100s; box scan ~200us => 400s.
Total ~10 min single core; 32 cores => <1 min with multiprocessing. Use mp.Pool.

Sharding: iterate (a,c,f) triples? Raw loop 2M items in Python itself is slow (~60s
just to generate). Generate in numpy-vectorized per-(a,c,f, b-config)? Simpler:
generate raw list as compact array of params (a,b,c,d,e,f) via nested loops in Python
(2M tuples ~ fine, ~30s), then mp.Pool over chunks.

Memory: store per-class dict in each worker, merge at end (classes ~ few thousand,
merge cheap).

Output: stage1.json {VMAX, n_raw, classes: {key_str: {V, i_min, wit}}, elapsed_s}
"""
import json, math, sys, time
import numpy as np
import itertools
from multiprocessing import Pool

sys.path.insert(0, "output/artifacts")
from canon import canon_key

VMAX = 144

def gen_params():
    out = []
    for a in range(1, VMAX + 1):
        for c in range(1, VMAX // a + 1):
            for f in range(1, VMAX // (a * c) + 1):
                V = a * c * f
                for b in range(c):
                    for d in range(f):
                        for e in range(f):
                            out.append((a, b, c, d, e, f))
    return out

def worker(chunk):
    import numpy as np, sys
    sys.path.insert(0, "output/artifacts")
    from canon import canon_key
    res = {}  # key -> [V, i_min, wit]
    for (a, b, c, d, e, f) in chunk:
        V = a * c * f
        v0 = (0, 0, 0); v1 = (a, 0, 0); v2 = (b, c, 0); v3 = (d, e, f)
        # interior count via adjugate method
        # E rows: e1=(a,0,0), e2=(b,c,0), e3=(d,e,f). E^T columns... solve E^T lam = p:
        # a*l1 + b*l2 + d*l3 = x
        #        c*l2 + e*l3 = y
        #               f*l3 = z
        # => l3 = z/f; l2 = (y - e l3)/c = (f y - e z)/(c f); l1 = (x - b l2 - d l3)/a
        # numerators over V=a c f: n3 = a c z; n2 = a (f y - e z); n1 = c f x - c b l2num... let me:
        # n3 = V l3 = a c z. n2 = V l2 = a f y - a e z. n1 = V l1 = c f x - b f? ...
        # V l1 = c f x - (b)(V l2)/c... V l1 = cf x - b*(a f y - a e z)/a ... use integer: n1 = c f x - b*(f y - e z)*c/c...
        # Simplest: n1 = V*x... no. Direct: l1 = (x - b*l2 - d*l3)/a, V*l1 = c f x - b f*(V l2)/(a f)*... messy; use Cramer:
        #det E^T = V. n1 = det of E^T with col1 replaced by p:
        # |x b d|      |a x d|      |a b x|
        # |y c e| etc.
        xs = np.arange(0, a + 1)
        # bounding box: x in [0, max(a,b,d)], y in [0, max(c,e)], z in [0, f]
        xmax = max(a, b, d); ymax = max(c, e)
        X, Y, Z = np.meshgrid(np.arange(xmax + 1), np.arange(ymax + 1), np.arange(f + 1), indexing='ij')
        X = X.ravel(); Y = Y.ravel(); Z = Z.ravel()
        n3 = a * c * Z
        n2 = a * (f * Y - e * Z)
        # n1 = det[[x,b,d],[y,c,e],[z,e? ...]] columns of E^T are e1,e2,e3 as column vectors:
        # E^T = [[a,b,d],[0,c,e],[0,0,f]]; replace col 0 by p: [[x,b,d],[y,c,e],[z,0,f]]
        n1 = X * (c * f) - b * (Y * f - e * Z) + d * (Y * 0 - c * Z)
        # = cf x - b f y + b e z - c d z
        m = (n1 > 0) & (n2 > 0) & (n3 > 0) & (n1 + n2 + n3 < V)
        i_cnt = int(m.sum())
        verts = (v0, v1, v2, v3)
        key = canon_key(verts)
        if key in res:
            if i_cnt < res[key][1]:
                res[key][1] = i_cnt
                res[key][2] = [list(v) for v in verts]
        else:
            res[key] = [V, i_cnt, [list(v) for v in verts]]
    return res

def main():
    t0 = time.time()
    params = gen_params()
    n_raw = len(params)
    print(f"raw count: {n_raw}", flush=True)
    import os
    NCPU = 32
    chunk = (n_raw + NCPU - 1) // NCPU
    chunks = [params[i:i + chunk] for i in range(0, n_raw, chunk)]
    with Pool(NCPU) as pool:
        parts = pool.map(worker, chunks)
    merged = {}
    for part in parts:
        for k, v in part.items():
            if k in merged:
                if v[1] < merged[k][1]:
                    merged[k] = v
            else:
                merged[k] = v
    # depth distribution
    from collections import Counter
    dist = Counter(v[1] for v in merged.values())
    print(f"classes: {len(merged)}", flush=True)
    print("depth dist (i_min): " + str(sorted(dist.items())), flush=True)
    out = {"VMAX": VMAX, "n_raw": n_raw, "n_classes": len(merged),
           "depth_dist": {str(k): v for k, v in sorted(dist.items())},
           "classes": {str(k): v for k, v in merged.items()},
           "elapsed_s": time.time() - t0}
    with open("output/artifacts/stage1.json", "w") as fh:
        json.dump(out, fh)
    print(f"elapsed {time.time()-t0:.1f}s", flush=True)

if __name__ == "__main__":
    main()
