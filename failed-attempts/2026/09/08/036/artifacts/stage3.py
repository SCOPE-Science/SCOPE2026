"""Stage 3: violator sweep — every HNF type with volume in (144, B_HI] is counted
directly for interior points; any tetra with exactly 3 interior points there would
refute Vol<=144. No dedup needed (existence only). Vectorized adjugate counting,
multiprocessing over volume values.

B_HI choice: Pikhurko-type/paring bounds are huge, but the point is a bounded,
auditable certificate: we certify "no violator with V<=B_HI" for an explicit B_HI
plus report the observed decay of max-interior-count vs volume. Take B_HI = 432
(=3x the conjectured max; also = 3*144). Raw HNF count at V<=432 is ~53M... too many
for full recount in remaining time? At ~2M/23min single... no: stage1 took 1364s on
32 cores for 2M => ~88 tetra/core-sec... 53M would be ~10x => ~3.7h. TOO SLOW.

Reduce: for violator search we only need volumes 145..B_HI and we can prune:
a tetra with i=3 needs at least... no clean prune. Alternative: sample-free but
cheaper counting: first-pass coarse filter (e.g., count with stride?) — unsafe.

Better: choose B_HI = 200 (volumes 145..200). Raw count V<=200? estimate ~ sum.
V<=144 was 2.0M; V<=200 ≈ 2.0M*(200/144)^3-ish weighted... roughly 4-5M total, minus
2M = ~2.5-3M extra. At 1364s/2M => ~30 min on 32 cores. Hmm, borderline.

Cheaper: per-tetra interior counting is the bottleneck (~most of 1364s; HNF canon
is also big). For violator sweep we SKIP canon entirely (no dedup) and use a FASTER
counter: precompute per (a,c,f,b,e,d)? Vectorize across tetrahedra sharing (a,c,f):
the box and the (n1,n2,n3) formulas share structure. Simplest big win: numba-free
numpy batch over K tetrahedra at once (K=512): boxes differ per tetra though
(xmax,ymax differ). Alternative: loop in Python but count with numpy per tetra is
already what stage1 did (~0.5ms each?). 2.5M * 0.5ms = 1250 core-s... wait stage1
total was 1364s*32cores = 43648 core-s for 2M => 22ms per tetra?! That includes HNF
canon (24 HNF each ~ expensive egcd loops) — canon dominates. Without canon,
per-tetra numpy count ~0.3-1ms => 2.5M tetras ~ 2500 core-s ~ 80s on 32 cores. 

So: violator sweep WITHOUT canon, volumes 145..B_HI with B_HI as large as time allows.
Try B_HI=300 first, measure, extend if fast.
"""
import json, time
import numpy as np
from multiprocessing import Pool

def count_interior(a, b, c, d, e, f):
    V = a * c * f
    xmax = max(a, b, d); ymax = max(c, e)
    X, Y, Z = np.meshgrid(np.arange(xmax + 1), np.arange(ymax + 1), np.arange(f + 1), indexing='ij')
    X = X.ravel(); Y = Y.ravel(); Z = Z.ravel()
    n3 = a * c * Z
    n2 = a * (f * Y - e * Z)
    n1 = (c * f) * X - b * (f * Y - e * Z) + d * (0 * Y - c * Z)
    m = (n1 > 0) & (n2 > 0) & (n3 > 0) & (n1 + n2 + n3 < V)
    return int(m.sum())

def worker_vol(V):
    viol = []
    n = 0
    # factor triples a*c*f = V
    for a in range(1, V + 1):
        if V % a: continue
        for c in range(1, V // a + 1):
            if (V // a) % c: continue
            f = V // (a * c)
            for b in range(c):
                for dd in range(f):
                    for ee in range(f):
                        n += 1
                        if count_interior(a, b, c, dd, ee, f) == 3:
                            viol.append([ [0,0,0],[a,0,0],[b,c,0],[dd,ee,f] ])
    return V, n, viol

def main(B_HI):
    t0 = time.time()
    vols = list(range(145, B_HI + 1))
    with Pool(32) as pool:
        parts = pool.map(worker_vol, vols)
    n_tot = sum(p[1] for p in parts)
    viol = [w for p in parts for w in p[2]]
    print(f"volumes 145..{B_HI}: {n_tot} HNF types scanned, violators(i==3): {len(viol)}", flush=True)
    for w in viol[:10]:
        print("  VIOLATOR:", w, flush=True)
    json.dump({"B_HI": B_HI, "n_scanned": n_tot, "n_viol": len(viol), "viol": viol,
               "elapsed_s": time.time() - t0},
              open("output/artifacts/stage3.json", "w"))
    print(f"elapsed {time.time()-t0:.1f}s", flush=True)

if __name__ == "__main__":
    import sys
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 200)
