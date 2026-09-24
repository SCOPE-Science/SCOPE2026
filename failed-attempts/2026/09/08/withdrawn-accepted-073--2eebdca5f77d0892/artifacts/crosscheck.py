#!/usr/bin/env python3
"""crosscheck.py — independent verification of C census (Script B).
Modes:
  brute PAT N      : full itertools enumeration of S_N, classify Av_N(PAT)
  backtrack PAT N  : backtracking enumeration with pruning, full census
  samples PAT N    : re-verify every saved sample line + witness line
Compares against output/artifacts/results_<PAT>.json
Usage: python3 crosscheck.py MODE PAT N
"""
import itertools, json, sys, os

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".")

def relrk(vals):
    s = sorted(vals)
    r = {v: i + 1 for i, v in enumerate(s)}
    return tuple(r[v] for v in vals)

def avoids(perm, pat):
    for q in itertools.combinations(range(len(perm)), 4):
        if relrk([perm[i] for i in q]) == pat:
            return False
    return True

def prefix_ok(prefix, pat):
    # avoidance among placed prefix only (pruning test)
    m = len(prefix)
    if m < 4:
        return True
    last = prefix[-1]
    for i in range(m):
        for j in range(i + 1, m):
            for k in range(j + 1, m - 1):
                if relrk([prefix[i], prefix[j], prefix[k], last]) == pat:
                    return False
    return True

def is_simple(perm):
    n = len(perm)
    for i in range(n):
        lo = hi = perm[i]
        for j in range(i + 1, n):
            lo = min(lo, perm[j]); hi = max(hi, perm[j])
            if hi - lo == j - i and not (i == 0 and j == n - 1):
                return False
    return True

def classify(perm):
    n = len(perm)
    if is_simple(perm):
        return ("simple", 0)
    for k in range(1, n):
        if set(perm[:k]) == set(range(1, k + 1)):
            return ("sum", 0)
    for k in range(1, n):
        if set(perm[:k]) == set(range(n - k + 1, n + 1)):
            return ("skew", 0)
    best = n
    for mask in range(1, 1 << (n - 1)):
        a = 0; ok = True; nb = 0
        for k in range(n - 1):
            if mask & (1 << k):
                blk = perm[a:k + 1]
                if max(blk) - min(blk) != k - a:
                    ok = False; break
                nb += 1; a = k + 1
        if not ok:
            continue
        blk = perm[a:]
        if max(blk) - min(blk) != n - 1 - a:
            continue
        nb += 1
        if nb < best:
            best = nb
    # verify quotient simple, length>=4
    assert best >= 4, f"non-simple quotient length {best} in {perm}"
    return ("inflation", best)

def full_census_brute(pat, n):
    patt = tuple(int(c) for c in pat)
    tot = s = su = sk = infl = 0
    qh = {}
    for perm in itertools.permutations(range(1, n + 1)):
        if not avoids(perm, patt):
            continue
        tot += 1
        t, q = classify(list(perm))
        if t == "simple": s += 1
        elif t == "sum": su += 1
        elif t == "skew": sk += 1
        else: infl += 1; qh[q] = qh.get(q, 0) + 1
    return {"total": tot, "simple": s, "sum": su, "skew": sk,
            "inflation": infl, "qhist": qh}

def full_census_backtrack(pat, n):
    patt = tuple(int(c) for c in pat)
    tot = s = su = sk = infl = 0
    qh = {}
    perm = [0] * n
    used = [False] * (n + 1)
    def dfs(pos):
        nonlocal tot, s, su, sk, infl
        if pos == n:
            t, q = classify(perm)
            tot += 1
            if t == "simple": s += 1
            elif t == "sum": su += 1
            elif t == "skew": sk += 1
            else: infl += 1; qh[q] = qh.get(q, 0) + 1
            return
        for v in range(1, n + 1):
            if used[v]:
                continue
            perm[pos] = v; used[v] = True
            if prefix_ok(perm[:pos + 1], patt):
                dfs(pos + 1)
            used[v] = False
    dfs(0)
    return {"total": tot, "simple": s, "sum": su, "skew": sk,
            "inflation": infl, "qh": qh, "qhist": qh}

def load_c(pat, n):
    d = json.load(open(os.path.join(ART, f"results_{pat}.json")))
    for c in d["cells"]:
        if c["n"] == n:
            return c
    raise KeyError(n)

def main():
    mode, pat, n = sys.argv[1], sys.argv[2], int(sys.argv[3])
    patt = tuple(int(c) for c in pat)
    if mode == "brute":
        got = full_census_brute(pat, n)
        exp = load_c(pat, n)
        expqh = {int(k): v for k, v in exp["qhist"].items()}
        ok = (got["total"] == exp["total"] and got["simple"] == exp["simple"]
              and got["sum"] == exp["sum"] and got["skew"] == exp["skew"]
              and got["inflation"] == exp["inflation"] and got["qhist"] == expqh)
        print(("AGREE " if ok else "DIFF "), pat, n, got)
        if not ok:
            print("EXP ", exp)
            sys.exit(1)
    elif mode == "backtrack":
        got = full_census_backtrack(pat, n)
        exp = load_c(pat, n)
        expqh = {int(k): v for k, v in exp["qhist"].items()}
        ok = (got["total"] == exp["total"] and got["simple"] == exp["simple"]
              and got["sum"] == exp["sum"] and got["skew"] == exp["skew"]
              and got["inflation"] == exp["inflation"] and got["qhist"] == expqh)
        print(("AGREE " if ok else "DIFF "), pat, n, {k: got[k] for k in
              ("total", "simple", "sum", "skew", "inflation")}, got["qhist"])
        if not ok:
            print("EXP ", exp)
            sys.exit(1)
    elif mode == "samples":
        nfail = ntot = 0
        for line in open(os.path.join(ART, f"samples_{pat}_{n}.txt")):
            body, _, tag = line.partition("|")
            perm = [int(x) for x in body.split()]
            t, q = tag.split()
            q = int(q)
            assert len(perm) == n and sorted(perm) == list(range(1, n + 1)), line
            if not avoids(perm, patt):
                print("AVOID-FAIL", pat, n, line.strip()); nfail += 1; continue
            gt, gq = classify(perm)
            ntot += 1
            if gt != t or (gt == "inflation" and gq != q):
                print("TYPE-FAIL", pat, n, line.strip(), "got", gt, gq); nfail += 1
        for line in open(os.path.join(ART, f"witnesses_{pat}.txt")):
            p, rest = line.split(":", 1)
            pp, nn, _w, vals = rest.split(None, 3)
            if int(nn) != n or pp.strip() != f"pi={pat}":
                continue
            perm = [int(x) for x in vals.split()]
            if not avoids(perm, patt):
                print("WIT-AVOID-FAIL", pat, n); nfail += 1; continue
            if not is_simple(perm):
                print("WIT-SIMPLE-FAIL", pat, n); nfail += 1; continue
            ntot += 1
        print(f"SAMPLES-OK pat={pat} n={n} checked={ntot}" if nfail == 0
              else f"SAMPLES-FAIL pat={pat} n={n} fails={nfail}")
        sys.exit(1 if nfail else 0)

main()
