#!/usr/bin/env python3
"""Primary census: <13>-orbits in Z_157, all 325 unions, exact ordered-difference test.
Target: no <13>-invariant (157,13,1) difference set.
Only stdlib. Writes orbits.json, census.json, SURVIVORS.txt, spectra digest."""
import json, hashlib, itertools, os

HERE = os.path.dirname(os.path.abspath(__file__))
V = 157
T = 13

assert pow(T, 6, V) == 1 and pow(T, 3, V) == V - 1  # ord exactly 6

# canonical orbits: least element as representative, orbits sorted by representative
seen = [False] * V
orbits = []
for a in range(V):
    if not seen[a]:
        o = set()
        y = a
        for _ in range(6):
            o.add(y)
            y = (y * T) % V
        o = sorted(o)
        for z in o:
            seen[z] = True
        orbits.append(o)
assert len(orbits) == 27
assert sorted(map(len, orbits)) == [1] + [6] * 26
triv = [o for o in orbits if o == [0]]
sext = sorted([o for o in orbits if len(o) == 6], key=lambda o: o[0])
assert len(sext) == 26
reps = [o[0] for o in sext]

with open(os.path.join(HERE, "orbits.json"), "w") as f:
    json.dump({"v": V, "t": T, "order": 6, "trivial": [0],
               "sextuple_orbits": sext, "representatives": reps}, f, indent=1)


def spectrum(S):
    """Ordered-difference multiplicity histogram for the 156 ordered pairs i!=j.
    PASS (planar DS) iff every nonzero residue occurs exactly once (count==1)."""
    cnt = [0] * V
    L = sorted(S)
    for a in L:
        for b in L:
            if a != b:
                cnt[(a - b) % V] += 1
    return cnt


results = []
survivors = []
for i, j in itertools.combinations(range(26), 2):
    S = [0] + sext[i] + sext[j]
    assert len(set(S)) == 13
    cnt = spectrum(S)
    nz = cnt[1:]  # residues 1..156
    distinct = sum(1 for c in nz if c > 0)
    mx = max(nz)
    n0 = sum(1 for c in nz if c == 0)
    is_ds = all(c == 1 for c in nz)
    results.append({"pair": [i, j], "reps": [reps[i], reps[j]],
                    "S": sorted(S),
                    "distinct_nonzero": distinct, "max_mult": mx,
                    "missing": n0, "is_ds": is_ds,
                    "hist": sorted(nz)})
    if is_ds:
        survivors.append([i, j])

census = {"v": V, "k": 13, "lam": 1, "n_sets": len(results),
          "n_survivors": len(survivors), "survivors": survivors,
          "results": results}
with open(os.path.join(HERE, "census.json"), "w") as f:
    json.dump(census, f, indent=1)

with open(os.path.join(HERE, "SURVIVORS.txt"), "w") as f:
    f.write("survivors=%d\n" % len(survivors))
    for p in survivors:
        f.write("%s\n" % (p,))

# aggregate stats for the report
import collections
agg_distinct = collections.Counter(r["distinct_nonzero"] for r in results)
agg_max = collections.Counter(r["max_mult"] for r in results)
print("sets:", len(results), "survivors:", len(survivors))
print("distinct_nonzero distribution:", dict(sorted(agg_distinct.items())))
print("max_mult distribution:", dict(sorted(agg_max.items())))
h = hashlib.sha256(open(os.path.join(HERE, "census.json"), "rb").read()).hexdigest()
print("census.json sha256:", h)
