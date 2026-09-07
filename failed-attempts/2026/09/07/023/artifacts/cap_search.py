#!/usr/bin/env python3
"""Greedy + iterated perturbation search for large caps in PG(4,5). Stdlib only."""
import json, random, time, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))

def load():
    with open(os.path.join(BASE, "points.json")) as f:
        points = json.load(f)
    with open(os.path.join(BASE, "lines.json")) as f:
        lines = json.load(f)
    n = len(points)
    # line_of_pair as list of lists (n x n, -1 default), use list of array
    lop = [[-1]*n for _ in range(n)]
    for li, L in enumerate(lines):
        for a in range(6):
            for b in range(a+1, 6):
                i, j = L[a], L[b]
                lop[i][j] = li
                lop[j][i] = li
    return points, lines, lop

def greedy_once(order, lines, lop, n):
    # order: permutation for tie-breaking; greedy: iterate picking first allowed in random order?
    # Instead: maintain allowed boolean, repeatedly pick random allowed point
    import random as R
    allowed = bytearray(b'\x01')*n if isinstance(bytearray(b'\x01'), bytes) else None
    allowed = [True]*n
    cap = []
    # for speed, keep list of allowed indices
    # pick using order shuffled each time? simpler: random choice among allowed
    while True:
        # collect allowed
        # find any allowed
        cand = -1
        # random sampling: try random indices until allowed found, but to get maximal need full scan at end
        # do full scan to list
        al = [i for i in range(n) if allowed[i]]
        if not al:
            break
        q = al[R.randrange(len(al))]
        cap.append(q)
        allowed[q] = False
        # forbid rest of lines (a,q) for a in cap[:-1]
        for a in cap[:-1]:
            li = lop[a][q]
            for p in lines[li]:
                allowed[p] = False
        # also cap points themselves already False
    return cap

def improve_cap(cap, lines, lop, n, rng, iters=200):
    """Try 1-for-2 swaps: remove one point, re-greedy fill from remaining + random."""
    best = list(cap)
    bestset = set(best)
    # precompute secant forbidden for best? just try perturbations
    for _ in range(iters):
        # pick a random point to drop (or 1-2 points)
        kdrop = 1 if rng.random() < 0.7 else 2
        drop = rng.sample(best, min(kdrop, len(best)))
        keep = [p for p in best if p not in set(drop)]
        # rebuild allowed from keep
        allowed = [True]*n
        for p in keep:
            allowed[p] = False
        # forbid secants among keep
        for ii in range(len(keep)):
            for jj in range(ii+1, len(keep)):
                li = lop[keep[ii]][keep[jj]]
                for p in lines[li]:
                    allowed[p] = False
        # greedy fill with random order
        cur = list(keep)
        while True:
            al = [i for i in range(n) if allowed[i]]
            if not al:
                break
            q = al[rng.randrange(len(al))]
            cur.append(q)
            allowed[q] = False
            for a in cur[:-1]:
                li = lop[a][q]
                for p in lines[li]:
                    allowed[p] = False
        if len(cur) > len(best):
            best = cur
    return best

def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    trials = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
    rng = random.Random(seed)
    # need separate global random for greedy_once; seed it
    import random as R
    R.seed(seed+999)
    points, lines, lop = load()
    n = len(points)
    print(f"loaded n={n} lines={len(lines)}", flush=True)
    best = []
    t0 = time.time()
    for t in range(trials):
        cap = greedy_once(None, lines, lop, n)
        if len(cap) > len(best):
            best = cap
            print(f"trial {t}: new best {len(best)}  ({time.time()-t0:.1f}s)", flush=True)
            # try to improve immediately with local search
            imp = improve_cap(best, lines, lop, n, rng, iters=100)
            if len(imp) > len(best):
                best = imp
                print(f"  improved to {len(best)}", flush=True)
        # periodically try improvement on best
        if (t+1) % 500 == 0:
            imp = improve_cap(best, lines, lop, n, rng, iters=100)
            if len(imp) > len(best):
                best = imp
                print(f"  periodic improved to {len(best)}", flush=True)
            print(f"trial {t+1}/{trials} best={len(best)} elapsed={time.time()-t0:.1f}s", flush=True)
    print(f"BEST {len(best)}: {sorted(best)}")
    # save best coords
    coords = [points[i] for i in sorted(best)]
    with open(os.path.join(BASE, "best_cap.json"), "w") as f:
        json.dump({"size": len(best), "indices": sorted(best), "coords": coords, "seed": seed, "trials": trials}, f, indent=1)
    print("saved best_cap.json")

if __name__ == "__main__":
    main()
