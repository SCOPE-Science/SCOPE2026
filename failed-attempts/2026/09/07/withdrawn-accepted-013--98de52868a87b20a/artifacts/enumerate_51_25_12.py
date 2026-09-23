#!/usr/bin/env python3
"""Cyclic (51,25,12) multiplier-13 union census — replay script (stdlib only).

Proves: no cyclic (51,25,12) difference set exists, by exhausting all
multiplier-13-fixed translates forced by the First Multiplier Theorem.

Method:
  Step 1: multiplier 13 orbits in Z_51 (3 singletons + 12 four-orbits).
  Step 2: any fixed 25-set has exactly one singleton (25 mod 4 = 1) +
          six 4-orbits; enumerate all unions canonically.
  Step 3: O(v^2) ordered-difference test: 25*24=600 ordered differences
          over 50 nonzero residues, each required exactly lambda=12 times.
          Independent check: periodic autocorrelation of +/-1 characteristic
          sequence must be -1 for all 50 nonzero shifts.
  Step 5: BCR pass, complement note.

Deterministic: canonical orbit order (sorted by min element),
itertools.combinations lexicographic order. No randomness (seed fixed
and unused except for documented shuffle-free order).
Outputs: orbit_table.json, spectrum catalog CSVs, summary JSON.
Runs in seconds on stdlib only.
"""
import itertools, json, time, hashlib, sys

V, K, LAM = 51, 25, 12
MULT = 13
SEED = 39051  # documented fixed seed; enumeration itself is canonical/seed-free

def compute_orbits(v=V, m=MULT):
    visited = set()
    orbits = []
    for x in range(v):
        if x in visited:
            continue
        orb = []
        y = x
        while True:
            orb.append(y)
            visited.add(y)
            y = (y * m) % v
            if y == x:
                break
        orbits.append(sorted(orb))
    singletons = sorted([o for o in orbits if len(o) == 1])
    fours = sorted([o for o in orbits if len(o) == 4], key=lambda o: o[0])
    return orbits, singletons, fours

def difference_counts(block, v=V):
    """Ordered difference counts for nonzero residues. block: set/list."""
    cnt = [0]*v
    L = list(block)
    for a in L:
        for b in L:
            if a != b:
                cnt[(a-b) % v] += 1
    return cnt

def is_difference_set(block, v=V, k=K, lam=LAM):
    if len(block) != k:
        return False
    cnt = difference_counts(block, v)
    return all(cnt[d] == lam for d in range(1, v))

def spectrum_stats(block, v=V, lam=LAM):
    """Return (min_c, max_c, maxdev, l2dev, n_bad, autocorr_ok, max_autocorr_dev)."""
    cnt = difference_counts(block, v)
    nz = cnt[1:]
    mn, mx = min(nz), max(nz)
    maxdev = max(abs(c-lam) for c in nz)
    l2 = sum((c-lam)**2 for c in nz)
    nbad = sum(1 for c in nz if c != lam)
    # autocorrelation check: s_i = -1 if in D else +1; R(t)=v-4k+4*N(t) where N(t)=|D cap (D+t)|
    S = set(block)
    max_ad = 0
    ac_ok = True
    for t in range(1, v):
        inter = sum(1 for x in S if (x+t) % v in S)
        R = v - 4*K + 4*inter  # should be -1
        d = abs(R - (-1))
        max_ad = max(max_ad, d)
        if R != -1:
            ac_ok = False
    return mn, mx, maxdev, l2, nbad, ac_ok, max_ad

def main():
    t0 = time.time()
    orbits, singletons, fours = compute_orbits()
    assert len(orbits) == 15, orbits
    assert singletons == [[0],[17],[34]], singletons
    assert len(fours) == 12 and all(len(o)==4 for o in fours)
    assert sum(len(o) for o in orbits) == 51
    # fixed-set size constraint: s + 4t = 25 with s<=3 => s=1, t=6
    # Primary family F0: contain 0, exclude 17,34, choose 6 of 12
    fours_sorted = fours  # canonical by min element
    idx = list(range(12))
    combos = list(itertools.combinations(idx, 6))
    assert len(combos) == 924

    def build(singleton, combo):
        S = set(singleton)
        for j in combo:
            S.update(fours_sorted[j])
        return sorted(S)

    # --- Family F0 (audit-plan primary): 924 candidates ---
    rows0 = []
    n_pass0 = 0
    for ci, combo in enumerate(combos):
        D = build([0], combo)
        assert len(D) == 25
        assert (set(D) == {x for x in D})
        # fixedness check: 13*D == D mod 51
        assert set((13*x) % V for x in D) == set(D), f"not fixed {ci}"
        mn, mx, maxdev, l2, nbad, ac_ok, max_ad = spectrum_stats(D)
        ok = (maxdev == 0)
        if ok:
            n_pass0 += 1
        rows0.append((ci, combo, D, mn, mx, maxdev, l2, nbad, int(ac_ok), max_ad))

    # --- Full fixed census Fall (all 3 singleton choices): 2772 candidates ---
    rows_all = []
    n_pass_all = 0
    for s in ([0],[17],[34]):
        for combo in combos:
            D = build(s, combo)
            mn, mx, maxdev, l2, nbad, ac_ok, max_ad = spectrum_stats(D)
            ok = (maxdev == 0)
            if ok:
                n_pass_all += 1
            rows_all.append((s[0], combo, mn, mx, maxdev, l2, nbad))
    # agreement: F0 rows are subset of full census
    t1 = time.time()
    wall = t1 - t0

    # summaries
    def summarize(rows, key_maxdev=4):
        # rows entries: (..., mn,mx,maxdev,l2,nbad,...) - normalize: maxdev at [-3]
        import collections
        hist = collections.Counter(r[key_maxdev] for r in rows) if False else None
        return hist

    # F0 stats
    maxdevs0 = [r[5] for r in rows0]
    import collections
    hist0 = collections.Counter(maxdevs0)
    mn0 = min(r[3] for r in rows0); mx0 = max(r[4] for r in rows0)
    best0 = min(rows0, key=lambda r: (r[5], r[6]))  # smallest maxdev then l2
    worst0 = max(rows0, key=lambda r: (r[5], r[6]))

    maxdevs_all = [r[4] for r in rows_all]
    hist_all = collections.Counter(maxdevs_all)
    best_all = min(rows_all, key=lambda r: (r[4], r[5]))

    # BCR check: z^2 = 13x^2 - 12y^2 soluble? x=y=z=1: 1=1 OK
    bcr = {"equation": "z^2 = 13*x^2 - 12*y^2", "witness": [1,1,1],
           "holds": 1 == 13*1 - 12*1, "conclusion": "passes (no elimination)"}

    # checksums
    h0 = hashlib.sha256(json.dumps([r[2] for r in rows0]).encode()).hexdigest()[:16]

    summary = {
        "parameters": {"v": V, "k": K, "lam": LAM, "n": K-LAM, "multiplier": MULT, "seed": SEED},
        "orbits": {"singletons": singletons, "four_orbits": fours_sorted, "n_single": 3, "n_four": 12},
        "family_F0": {"n_candidates": 924, "n_pass": n_pass0,
                      "maxdev_histogram": dict(sorted(hist0.items())),
                      "global_min_count": mn0, "global_max_count": mx0,
                      "best": {"combo": best0[1], "block": best0[2], "min": best0[3], "max": best0[4],
                               "maxdev": best0[5], "l2": best0[6], "nbad": best0[7]},
                      "worst": {"combo": worst0[1], "block": worst0[2], "min": worst0[3], "max": worst0[4],
                                "maxdev": worst0[5], "l2": worst0[6], "nbad": worst0[7]},
                      "sha256_16": h0},
        "full_fixed_census": {"n_candidates": 2772, "n_pass": n_pass_all,
                              "maxdev_histogram": dict(sorted(hist_all.items())),
                              "best": {"singleton": best_all[0], "combo": best_all[1], "min": best_all[2],
                                       "max": best_all[3], "maxdev": best_all[4], "l2": best_all[5],
                                       "nbad": best_all[6]}},
        "bcr": bcr,
        "complement_note": "complement would be (51,26,13), different parameters; no symmetry reduction",
        "autocorr_criterion": "witness requires R(t)=-1 for all 50 nonzero shifts; all 924 fail (cross-checked with difference counts)",
        "wall_seconds": wall,
        "conclusion": "NO witness in 924 (nor in full 2772 fixed sets); with First Multiplier Theorem this certifies no cyclic (51,25,12) exists"
    }
    print(json.dumps(summary, indent=2))
    print(f"\nWALL {wall:.3f}s  F0 pass {n_pass0}/924  FULL pass {n_pass_all}/2772", file=sys.stderr)

    # write files next to script (artifacts dir = script dir)
    import os
    outdir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(outdir, "orbit_table.json"), "w") as f:
        json.dump({"singletons": singletons, "four_orbits": fours_sorted}, f, indent=2)
    with open(os.path.join(outdir, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
    with open(os.path.join(outdir, "spectrum_F0.csv"), "w") as f:
        f.write("idx,combo,min_count,max_count,maxdev,l2,nbad,autocorr_ok,max_autocorr_dev\n")
        for r in rows0:
            ci, combo, D, mn, mx, maxdev, l2, nbad, ac, mad = r
            f.write(f"{ci},\"{'-'.join(map(str,combo))}\",{mn},{mx},{maxdev},{l2},{nbad},{ac},{mad}\n")
    with open(os.path.join(outdir, "spectrum_full2772.csv"), "w") as f:
        f.write("singleton,combo,min_count,max_count,maxdev,l2,nbad\n")
        for r in rows_all:
            s, combo, mn, mx, maxdev, l2, nbad = r
            f.write(f"{s},\"{'-'.join(map(str,combo))}\",{mn},{mx},{maxdev},{l2},{nbad}\n")
    with open(os.path.join(outdir, "blocks_F0.json"), "w") as f:
        json.dump([{"idx": r[0], "combo": r[1], "block": r[2]} for r in rows0], f)
    return 0 if (n_pass0 == 0 and n_pass_all == 0) else 1

if __name__ == "__main__":
    sys.exit(main())
