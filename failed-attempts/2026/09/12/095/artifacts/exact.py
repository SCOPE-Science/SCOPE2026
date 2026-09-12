"""Exact-cover backtracking constructor: build the 36x36 design row by row with
fixed 9x9 tile margins R, enforcing pairwise inner product 6 with all previous rows.
Row order: whole point class at a time. Column candidates per row: all 0/1 vectors
with tile sums r_i (the class's row of R). Pruning: pairwise inner products with
previous rows == 6; forward check on remaining inner-product budgets.
Usage: python3 exact.py RJSON SEED OUT [MAXROWS]"""
import numpy as np
import sys
import json
import itertools
import time

def gen_row_candidates(r, rng, cap=4000):
    """Sample 0/1 vectors length 36 with tile sums r (list of 4)."""
    out = set()
    tries = 0
    while len(out) < cap and tries < cap * 30:
        tries += 1
        v = np.zeros(36, dtype=np.int64)
        for j in range(4):
            cols = list(range(j * 9, (j + 1) * 9))
            rng.shuffle(cols)
            for c in cols[:r[j]]:
                v[c] = 1
        out.add(bytes(v.tolist()))
    return [np.array(list(bytes(v)), dtype=np.int64) for v in out]

def main():
    R = [list(map(int, row)) for row in json.loads(sys.argv[1])]
    seed = int(sys.argv[2])
    out = sys.argv[3]
    MAXR = int(sys.argv[4]) if len(sys.argv) > 4 else 36
    rng = np.random.default_rng(seed)
    t0 = time.time()
    # candidate pools per class
    pools = [gen_row_candidates(R[i], rng, cap=6000) for i in range(4)]
    for i in range(4):
        print(f"[exact {seed}] class {i} pool={len(pools[i])}", flush=True)
    rows = []
    sys.setrecursionlimit(10000)
    calls = [0]

    def bt(r):
        calls[0] += 1
        if r == MAXR:
            return True
        i = r // 9
        # order candidates: prefer ones with inner products closest to feasible for future
        for v in pools[i]:
            ok = True
            for s, u in enumerate(rows):
                if int(v @ u) != 6:
                    ok = False
                    break
            if not ok:
                continue
            rows.append(v)
            if bt(r + 1):
                return True
            rows.pop()
            if time.time() - t0 > 240:
                return False
        return False

    # shuffle pools for randomness
    for p in pools:
        rng.shuffle(p)
    done = bt(0)
    print(f"[exact {seed}] done={done} rows={len(rows)} calls={calls[0]} t={time.time()-t0:.0f}s",
          flush=True)
    if rows:
        A = np.array(rows)
        with open(out, "w") as f:
            json.dump({"R": R, "seed": seed, "A": A.tolist()}, f)

if __name__ == "__main__":
    main()
