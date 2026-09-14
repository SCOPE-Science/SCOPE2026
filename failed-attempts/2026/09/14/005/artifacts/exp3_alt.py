#!/usr/bin/env python3
"""Bounded alternative assessment: are any grown triangle-free assemblies
not 3-colorable (i.e., chi=4 triangle-free unit-distance candidates)?
Regrows deterministically with same seeds and runs exact DSATUR k=3."""
import sys, time, json
sys.path.insert(0, "output/artifacts")
from exp1_target import grow_triangle_free, find_triangle, n_edges, dsatur_kcolorable
t0 = time.time()
out = []
for target_n, seed, dp in [(60, 101, 0.7), (100, 103, 0.7), (100, 104, 0.85),
                           (150, 105, 0.8), (200, 106, 0.8),
                           (400, 201, 0.8), (800, 203, 0.85)]:
    pts, adj = grow_triangle_free(target_n, seed, double_prob=dp,
                                  stuck_cap=60000)
    r3, n3 = dsatur_kcolorable(adj, 3, budget=400000, time_limit=45.0)
    s = "UNSAT" if r3 is False else ("SAT" if r3 is True else "TIMEOUT")
    out.append({"seed": seed, "n": len(pts), "m": n_edges(adj),
                "dsatur3": s, "nodes": n3})
    print("[%.0fs] seed=%d n=%d m=%d DSATUR3=%s nodes=%s" %
          (time.time()-t0, seed, len(pts), n_edges(adj), s, n3), flush=True)
with open("output/artifacts/exp3_alt.json", "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
