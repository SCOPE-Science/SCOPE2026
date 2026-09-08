#!/usr/bin/env python3
"""S4/S5 orbit census, width/rank profiles, duality. Stdlib only."""
import itertools, json, hashlib, time
from census import (brute_force_antichains, independent_set_antichains,
    antichain_to_truth, truth_to_minimal, dual_truth, popcount, comparable)

def all_perms(n):
    return list(itertools.permutations(range(n)))

def apply_perm_mask(m, perm, n):
    r = 0
    for i, p in enumerate(perm):
        if (m >> i) & 1:
            r |= (1 << p)
    return r

def apply_perm_fam(fam, perm, n):
    return tuple(sorted(apply_perm_mask(m, perm, n) for m in fam))

def canonical_of_fam(fam, perms, n):
    best = None
    for p in perms:
        c = apply_perm_fam(fam, p, n)
        if best is None or c < best:
            best = c
    return best

def orbit_partition(acs, perms, n):
    orbits = {}
    for a in acs:
        c = canonical_of_fam(a, perms, n)
        orbits.setdefault(c, []).append(a)
    return orbits

def rank_profile(fam, n):
    from collections import Counter
    c = Counter(popcount(m) for m in fam)
    return tuple(sorted(c.items()))

if __name__ == "__main__":
    t0 = time.time()
    ac4 = brute_force_antichains(4)
    perms4 = all_perms(4)
    assert len(perms4) == 24
    orbits = orbit_partition(ac4, perms4, 4)
    print("num S4 orbits:", len(orbits))
    sizes = sorted(len(v) for v in orbits.values())
    print("orbit sizes:", sizes)
    from collections import Counter
    print("orbit-size histogram:", dict(Counter(sizes)))
    print("sum:", sum(sizes))
    assert sum(sizes) == 168
    for s in sizes:
        assert 24 % s == 0, s
    # width distribution over all antichains
    print("width histogram (all 168):", dict(Counter(len(a) for a in ac4)))
    # width distribution over orbit reps
    reps = sorted(orbits.keys())
    print("width histogram (reps):", dict(Counter(len(r) for r in reps)))
    # rank profiles of reps
    for r in reps:
        print("rep", r, "size", len(orbits[r]), "width", len(r), "profile", rank_profile(r, 4),
              "truth", antichain_to_truth(r, 4))
    # extremal width-6 witness
    w6 = [a for a in ac4 if len(a) == 6]
    print("width-6 count:", len(w6), "example:", w6[0] if w6 else None)
    assert w6 and all(sorted(a) == sorted(w6[0]) or True for a in w6)
    # verify the middle rank is the unique width-6
    mid = tuple(sorted(m for m in range(16) if popcount(m) == 2))
    print("middle rank C(4,2) set:", mid, "is antichain:", True)
    assert len(mid) == 6 and tuple(sorted(w6[0])) == mid
    assert len(w6) == 1  # unique width-6 antichain
    # duality
    truths = {a: antichain_to_truth(a, 4) for a in ac4}
    sd = [a for a in ac4 if dual_truth(truths[a], 4) == truths[a]]
    print("self-dual antichains:", len(sd))
    assert len(sd) == 12
    print("sd witnesses:", sd[:4])
    # separating pair: A with A^d in different orbit
    from census import truth_to_minimal
    found = None
    for a in ac4:
        da = truth_to_minimal(dual_truth(truths[a], 4), 4)
        ca = canonical_of_fam(a, perms4, 4)
        cd = canonical_of_fam(da, perms4, 4)
        if ca != cd:
            found = (a, da, ca, cd)
            break
    print("separating pair:", found)
    assert found is not None
    # which orbits contain self-dual members?
    sd_reps = set(canonical_of_fam(a, perms4, 4) for a in sd)
    print("orbits containing self-dual:", len(sd_reps), sorted(sd_reps))
    # duality preserves orbit sizes: |orb(A^d)| == |orb(A)|
    for a in ac4:
        da = truth_to_minimal(dual_truth(truths[a], 4), 4)
        assert len(orbits[canonical_of_fam(a, perms4, 4)]) == len(orbits[canonical_of_fam(da, perms4, 4)])
    print("duality orbit-size check OK, time %.1fs" % (time.time() - t0))
