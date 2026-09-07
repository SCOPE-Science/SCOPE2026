"""Independent verifier for Z_60 Sidon census. Stdlib only.
Checks:
  (V1) witness sums/diffs distinct counts (28/42, no zero diff).
  (V2) every stored dihedral rep has 28 distinct sums + 42 distinct nonzero diffs (sums-primary).
  (V3) every stored dihedral rep is dihedral-canonical (lex-min) and translation reps are canonical; recounts translation/dihedral class sizes (expect 7 per trans class, 2 per dihedral class, 0 self-mirror).
  (V4) checksums match stored tables.
  (V5) cold re-run: independent sums-based DFS (different pruning code from search.py) proving no 8-set and recounting rooted 7-sets; compares to stored exhaustion stats (visited/attempts/depth must match exactly under frozen ordering).
Usage: python3 verify.py [--dir DIR]
Exit 0 PASS, nonzero FAIL.
"""
import os, sys, json, hashlib, time, argparse

N = 60

def sums_set(S):
    return {(a + b) % N for i, a in enumerate(S) for b in list(S)[i:]}

def diffs_set(S):
    return {(a - b) % N for a in S for b in S if a != b}

def trans_canonical(S):
    best = None
    for a in S:
        T = tuple(sorted(((x - a) % N for x in S)))
        if best is None or T < best:
            best = T
    return best

def dihedral_canonical(S):
    c1 = trans_canonical(S)
    neg = tuple(sorted(((-x) % N for x in S)))
    c2 = trans_canonical(neg)
    return c1 if c1 < c2 else c2

def sums_based_exhaustion():
    sys.setrecursionlimit(10000)
    visited = 0; attempts = 0; n7 = 0; n8 = 0
    from collections import Counter
    bydepth = Counter()
    def dfs(cur, sums):
        nonlocal visited, attempts, n7, n8
        visited += 1
        bydepth[len(cur)] += 1
        if len(cur) == 8:
            n8 += 1
            return
        if len(cur) == 7:
            n7 += 1
        start = cur[-1] + 1
        for v in range(start, N):
            attempts += 1
            news = [(2 * v) % N] + [(v + a) % N for a in cur]
            if len(set(news)) != len(news):
                continue
            if any(s in sums for s in news):
                continue
            for s in news: sums.add(s)
            cur.append(v)
            dfs(cur, sums)
            cur.pop()
            for s in news: sums.remove(s)
    t0 = time.perf_counter()
    dfs([0], {(0 + 0) % N})
    t1 = time.perf_counter()
    return visited, attempts, dict(bydepth), n7, n8, t1 - t0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=os.path.dirname(os.path.abspath(__file__)))
    args = ap.parse_args()
    d = args.dir
    fails = []
    def check(name, cond, detail=""):
        print(("PASS" if cond else "FAIL") + f" {name} {detail}")
        if not cond: fails.append(name)
    # load
    with open(os.path.join(d, "k8_exhaustion.json")) as f: exh = json.load(f)
    with open(os.path.join(d, "sidon7_dihedral_reps.json")) as f: dihj = json.load(f)
    with open(os.path.join(d, "sidon7_translation_reps.json")) as f: traj = json.load(f)
    with open(os.path.join(d, "witness.json")) as f: wit = json.load(f)
    W = tuple(wit["witness"])
    # V1
    check("V1-witness-sums", len(sums_set(W)) == 28 and len(wit["sums"]) == 28,
          f"sums={len(sums_set(W))}")
    D = diffs_set(W)
    check("V1-witness-diffs", len(D) == 42 and 0 not in D, f"diffs={len(D)} has0={0 in D}")
    check("V1-witness-values", sorted(sums_set(W)) == [0,1,2,3,4,6,7,8,10,12,13,14,15,16,19,20,21,23,24,27,32,38,39,40,41,45,50,58],
          "exact sum table match")
    # V2
    bad = 0
    for r in dihj["reps"]:
        S = tuple(r)
        if len(sums_set(S)) != 28: bad += 1; continue
        Dd = diffs_set(S)
        if len(Dd) != 42 or 0 in Dd: bad += 1
    check("V2-all-dihedral-reps-sidon", bad == 0, f"bad={bad}/{len(dihj['reps'])}")
    # V3 canonical + pairing
    badc = 0
    for r in dihj["reps"]:
        S = tuple(r)
        if dihedral_canonical(S) != S: badc += 1
    check("V3-dihedral-minimality", badc == 0, f"nonminimal={badc}")
    badt = 0
    for r in traj["reps"]:
        S = tuple(r)
        if trans_canonical(S) != S: badt += 1
    check("V3-translation-minimality", badt == 0, f"nonminimal={badt}")
    # recount pairing: each trans rep's dihedral canonical must land in dihedral table, 2-to-1, no fixed point
    from collections import Counter
    m = Counter()
    for r in traj["reps"]:
        m[dihedral_canonical(tuple(r))] += 1
    check("V3-dihedral-cover", set(m.keys()) == set(tuple(r) for r in dihj["reps"]),
          f"cover {len(m)} vs {len(dihj['reps'])}")
    dist = Counter(m.values())
    check("V3-pairing-2to1-no-self-mirror", dict(dist) == {2: len(dihj["reps"])}, f"dist={dict(dist)}")
    # trans class sizes: need full rooted enumeration? Instead check each trans rep has 7 distinct rooted shifts and all are Sidon
    # (periodicity would give <7). This proves no periodic 7-set without full re-enumeration.
    badp = 0
    for r in traj["reps"]:
        shifts = set(tuple(sorted(((x - a) % N for x in r))) for a in r)
        if len(shifts) != 7: badp += 1
    check("V3-trans-class-size-7", badp == 0, f"bad={badp}")
    check("V3-counts", traj["count"] == 7156 and dihj["count"] == 3578 and exh["num_translation_classes"] == 7156 and exh["num_dihedral_classes"] == 3578,
          f"trans={traj['count']} dih={dihj['count']}")
    # V4 checksums
    h_dih = hashlib.sha256(json.dumps(sorted([tuple(r) for r in dihj["reps"]])).encode()).hexdigest()
    # careful: search.py checksums json.dumps of list-of-tuples? json converts tuples to lists; recompute same way: json.dumps(reps) where reps are tuples -> same as lists
    # Our dihj["reps"] are lists; search computed on tuples. JSON encoding identical, so compare:
    check("V4-sha-dihedral", h_dih == dihj["sha256"] == exh["sha256_dihedral_reps"], f"{h_dih[:16]}...")
    h_trans = hashlib.sha256(json.dumps(sorted([tuple(r) for r in traj["reps"]])).encode()).hexdigest()
    check("V4-sha-translation", h_trans == traj["sha256"] == exh["sha256_translation_reps"], f"{h_trans[:16]}...")
    # V5 cold re-run sums-based
    visited, attempts, bydepth, n7, n8, el = sums_based_exhaustion()
    print(f"cold sums-DFS: visited={visited} attempts={attempts} depth={sorted(bydepth.items())} n7={n7} n8={n8} time={el:.2f}s")
    check("V5-no-8-set", n8 == 0, f"n8={n8}")
    check("V5-n7-match", n7 == exh["num_rooted_7"] == 50092, f"n7={n7}")
    check("V5-visited-match", visited == exh["visited_nodes"], f"visited={visited} vs {exh['visited_nodes']}")
    check("V5-attempts-match", attempts == exh["candidate_attempts"], f"attempts={attempts} vs {exh['candidate_attempts']}")
    # depth distribution match (keys as str in json)
    bd = {int(k): v for k, v in exh["depth_distribution"].items()}
    # bydepth keys int
    check("V5-depth-match", dict(bydepth) == bd, f"{dict(bydepth)} vs {bd}")
    if fails:
        print(f"VERIFY FAIL: {fails}")
        sys.exit(1)
    print("VERIFY PASS: all checks")
if __name__ == "__main__":
    main()
