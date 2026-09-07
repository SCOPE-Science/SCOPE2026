#!/usr/bin/env python3
"""Exhaustive circulant enumeration for RT(30,K4,6) lower-bound optimality.
Covers all circulants C30(J) with J subset of {1..14} plus optional {15}.
For each k with edges > 180 (k>=7 even; k>=6 odd) checks K4-freeness (27405 quads)
and alpha<=5 (heuristic filter + exact 593775 6-sets). Reproduces counts:
 k=6 even: 3003 graphs, 12 feasible (180 edges)
 k=7 even: 3432 graphs, 170 K4-free, 0 feasible
 k=8 even: 3003 graphs, 49 K4-free, 0 feasible
 k=9 even: 2002 graphs, 10 K4-free, 0 feasible (also forced by degree>=18)
 k=10 even: 1001 graphs, 1 K4-free, 0 feasible (degree>=18 forces I6)
 k=6+15 (195e): 3003 graphs, 64 K4-free, 0 feasible
 k=7+15 (225e): 3432 graphs, 8 K4-free, 0 feasible
 k=8+15 (255e): 3003 graphs, 0 K4-free
k>=9 even / k>=8 odd have degree>=18 so Ramsey degree bound alone forces alpha>=6.
Usage: python3 circulant_enum.py [--quick] (quick does k=6,7 only)
"""
import itertools, os, random, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# import helpers from search.py (same dir)
import search

n = 30
rng = random.Random(12345)

def mk(jumps, inc15=False):
    adj = [0]*n
    for i in range(n):
        m = 0
        for d in jumps:
            m |= (1 << ((i+d) % n)) | (1 << ((i-d) % n))
        if inc15:
            m |= (1 << ((i+15) % n))
        adj[i] = m
    return adj

def test_graph(adj):
    ok,_ = search.is_k4_free_exact(adj)
    if not ok:
        return ("k4", False)
    s = search.find_I6_heuristic(adj, rng, trials=120)
    if s is not None:
        return ("k4free-hasI6", False)
    ok2,_ = search.alpha_le5_exact(adj)
    return ("k4free-feasible" if ok2 else "k4free-hasI6exact", ok2)

def run_k(k, inc15=False):
    total = 0; k4free = 0; feas = []
    for jumps in itertools.combinations(range(1,15), k):
        total += 1
        adj = mk(list(jumps), inc15)
        status, ok = test_graph(adj)
        if status.startswith("k4free"):
            k4free += 1
        if ok:
            feas.append(sorted(jumps))
    tag = f"k={k}{'+15' if inc15 else ''}"
    print(f"{tag}: total={total} k4free={k4free} feasible={len(feas)}", flush=True)
    for j in feas:
        print(f"  FEAS {j}", flush=True)
    return k4free, feas

if __name__ == "__main__":
    quick = "--quick" in sys.argv
    t0 = time.time()
    if quick:
        run_k(6, False)
        run_k(7, False)
    else:
        for k in [6,7,8,9,10]:
            run_k(k, False)
        for k in [6,7,8]:
            run_k(k, True)
    print(f"done {time.time()-t0:.1f}s")
