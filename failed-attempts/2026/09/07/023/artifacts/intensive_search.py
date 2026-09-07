#!/usr/bin/env python3
"""Intensive perturbation of a given cap + fresh greedy. Stdlib only."""
import json, random, time, sys, os
BASE = os.path.dirname(os.path.abspath(__file__))

def load():
    with open(os.path.join(BASE, "points.json")) as f: points = json.load(f)
    with open(os.path.join(BASE, "lines.json")) as f: lines = json.load(f)
    n = len(points)
    lop = [[-1]*n for _ in range(n)]
    for li, L in enumerate(lines):
        for a in range(6):
            for b in range(a+1, 6):
                i, j = L[a], L[b]
                lop[i][j] = li; lop[j][i] = li
    return points, lines, lop

def greedy_fill(keep, lines, lop, n, rng):
    allowed = [True]*n
    for p in keep: allowed[p] = False
    for ii in range(len(keep)):
        for jj in range(ii+1, len(keep)):
            li = lop[keep[ii]][keep[jj]]
            for p in lines[li]: allowed[p] = False
    cur = list(keep)
    while True:
        # find allowed list
        al = [i for i in range(n) if allowed[i]]
        if not al: break
        q = al[rng.randrange(len(al))]
        cur.append(q); allowed[q] = False
        for a in cur[:-1]:
            li = lop[a][q]
            for p in lines[li]: allowed[p] = False
    return cur

def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    seconds = int(sys.argv[2]) if len(sys.argv) > 2 else 90
    startfile = sys.argv[3] if len(sys.argv) > 3 else os.path.join(BASE, "cap51.json")
    rng = random.Random(seed)
    import random as R; R.seed(seed+12345)
    points, lines, lop = load()
    n = len(points)
    with open(startfile) as f: d = json.load(f)
    best = sorted(d["indices"])
    print(f"start {len(best)}", flush=True)
    t0 = time.time()
    it = 0
    # also fresh greedy interleaved
    while time.time()-t0 < seconds:
        it += 1
        if it % 5 == 0:
            # fresh greedy
            cur = greedy_fill([], lines, lop, n, rng)
        else:
            # perturb best: drop k
            k = rng.choices([1,2,3,4,5],[0.3,0.3,0.2,0.1,0.1])[0]
            k = min(k, len(best))
            drop = set(rng.sample(best, k))
            keep = [p for p in best if p not in drop]
            cur = greedy_fill(keep, lines, lop, n, rng)
        if len(cur) > len(best):
            best = sorted(cur)
            print(f"iter {it}: NEW BEST {len(best)} ({time.time()-t0:.1f}s)", flush=True)
            coords = [points[i] for i in best]
            with open(os.path.join(BASE, "best_cap.json"), "w") as f:
                json.dump({"size": len(best), "indices": best, "coords": coords, "seed": seed, "iter": it}, f, indent=1)
        if it % 2000 == 0:
            print(f"iter {it} best={len(best)} elapsed={time.time()-t0:.1f}s", flush=True)
    print(f"FINAL BEST {len(best)}")

if __name__ == "__main__":
    main()
