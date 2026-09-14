#!/usr/bin/env python3
"""Lane-1816 batch 2 (runs inside workspace to avoid /tmp shadowing)."""
import math
import random
import json
import sys
import time
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/../..")
sys.path.insert(0, "output/artifacts")
from exp1_target import (grow_triangle_free, find_triangle, n_edges,
                         greedy_best, dsatur_kcolorable, mycielski,
                         sa_embed, verify_embedding)

t0 = time.time()
out = {}
for target_n, seed, dp in [(400, 201, 0.8), (400, 202, 0.9), (800, 203, 0.85)]:
    pts, adj = grow_triangle_free(target_n, seed, double_prob=dp,
                                  stuck_cap=60000)
    g = greedy_best(adj, trials=6, seed=seed)
    d4, d4n = dsatur_kcolorable(adj, 4, budget=500000, time_limit=60.0)
    out["grow%d" % seed] = {"n": len(pts), "m": n_edges(adj),
                            "triangle": find_triangle(adj), "greedy": g,
                            "dsatur4": ("SAT" if d4 is True else
                                        ("UNSAT" if d4 is False else "TIMEOUT")),
                            "nodes": d4n}
    print("[%.0fs] seed=%d n=%d m=%d greedy=%s dsatur4=%s" %
          (time.time() - t0, seed, len(pts), n_edges(adj), g,
           out["grow%d" % seed]["dsatur4"]), flush=True)
K2 = [set([1]), set([0])]
M3 = mycielski(K2)
M4 = mycielski(M3)
s, c = sa_embed(M4, restarts=20, iters=15000, seed=55)
out["SA_M4_deep"] = {"stress": s, "verify": verify_embedding(c, M4)}
print("M4deep", s, out["SA_M4_deep"]["verify"], flush=True)
with open("output/artifacts/exp2_results.json", "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1)[:3000])
