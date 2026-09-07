#!/usr/bin/env python3
"""Deterministic Kunz enumeration for genus g=26, m in {6,7,8,9}.
Method A: exhaustive composition filter (no pruning) -- primary auditable path.
Method B: backtracking with partial pruning -- cross-check.
Also computes invariants and writes CSV + log.
Stdlib only. Deterministic. Single core.
"""
import hashlib, json, time, sys, csv, itertools

G = 26
MS = [6,7,8,9]

def kunz_ok(k, m):
    # k: tuple length m-1, 1-indexed as k[0]=k_1
    # check inequalities
    for i in range(1, m):
        for j in range(1, m):
            s = i + j
            if s < m:
                if k[i-1] + k[j-1] < k[s-1]:
                    return False
            elif s > m:
                t = s - m  # 1..m-1
                if k[i-1] + k[j-1] + 1 < k[t-1]:
                    return False
            # s==m: no constraint
    return True

def compositions_positive(n, parts):
    # deterministic lexicographic generation via recursion
    # yields tuples of length `parts` of positive ints summing to n
    if parts == 1:
        yield (n,)
        return
    for first in range(1, n - parts + 2):
        for rest in compositions_positive(n - first, parts - 1):
            yield (first,) + rest

def enumerate_methodA(m, g):
    res = []
    count_tested = 0
    for k in compositions_positive(g, m-1):
        count_tested += 1
        if kunz_ok(k, m):
            res.append(k)
    res.sort()
    return res, count_tested

def enumerate_methodB(m, g):
    # backtracking assigning k_1..k_{m-1} in order, prune:
    #  - sum bounds: partial sum s, remaining r slots each >=1, so s + r <= g and s + (remaining max?) s<=g-r; and s>=... also final sum==g
    #  - inequality pruning: any inequality whose all three indices assigned is checked immediately
    res = []
    k = [0]*(m-1)
    n = m-1
    def assigned(idx):  # 1-indexed
        return k[idx-1] != 0
    def check_partial():
        # only check fully-assigned triples
        for i in range(1, m):
            if not assigned(i): continue
            for j in range(1, m):
                if not assigned(j): continue
                s = i+j
                if s < m:
                    if not assigned(s): continue
                    if k[i-1]+k[j-1] < k[s-1]: return False
                elif s > m:
                    t = s-m
                    if not assigned(t): continue
                    if k[i-1]+k[j-1]+1 < k[t-1]: return False
        return True
    def rec(pos, remaining):
        # pos: next index to assign (0-based), remaining sum to distribute including pos..n-1
        if pos == n:
            if remaining == 0:
                if kunz_ok(tuple(k), m):
                    res.append(tuple(k))
            return
        slots_left_after = n - pos - 1
        # k_pos in [1, remaining - slots_left_after]
        lo, hi = 1, remaining - slots_left_after
        for v in range(lo, hi+1):
            k[pos] = v
            if check_partial():
                rec(pos+1, remaining - v)
            k[pos] = 0
    rec(0, g)
    res.sort()
    return res

def apery(k, m):
    return [0] + [m*k[i] + (i+1) for i in range(m-1)]

def invariants(k, m):
    w = apery(k, m)
    F = max(w) - m
    c = F + 1
    # membership test
    wmod = w  # w[r] is min elem congruent r
    def in_S(x):
        if x < 0: return False
        return x >= w[x % m]
    gaps = [x for x in range(F+1) if not in_S(x)]
    g = len(gaps)
    # embedding dimension: candidates {m} U {w_i}
    # m always minimal generator
    gens = [m]
    for wi in w[1:]:
        indecomp = True
        for a in range(1, wi//2 + 1):
            if in_S(a) and in_S(wi - a):
                indecomp = False
                break
        if indecomp:
            gens.append(wi)
    gens.sort()
    e = len(gens)
    n = c - g
    # Wilf ratio as exact fraction
    from fractions import Fraction
    W = Fraction(e*n, c)
    return {"w": w, "F": F, "c": c, "gaps": gaps, "g": g, "gens": gens, "e": e, "n": n, "W": W}

def main():
    t0 = time.time()
    out = {}
    all_rows = []
    log_lines = []
    log_lines.append(f"genus={G} m_list={MS}")
    log_lines.append("python=" + sys.version.replace("\n"," "))
    for m in MS:
        tA = time.time()
        resA, tested = enumerate_methodA(m, G)
        dA = time.time() - tA
        tB = time.time()
        resB = enumerate_methodB(m, G)
        dB = time.time() - tB
        assert resA == resB, f"method mismatch m={m}: {len(resA)} vs {len(resB)}"
        # hash
        h = hashlib.sha256()
        for k in resA:
            h.update((",".join(map(str,k))+";").encode())
        digest = h.hexdigest()
        log_lines.append(f"m={m} tested_compositions={tested} count={len(resA)} sha256={digest} timeA={dA:.2f}s timeB={dB:.2f}s")
        print(f"m={m}: tested={tested} count={len(resA)} sha={digest[:16]}... A={dA:.2f}s B={dB:.2f}s", flush=True)
        # invariants + verification
        from fractions import Fraction
        fdist = {}
        minW = None; minWk = None
        maxF = -1; maxFk = []
        wilf_fail = []
        for k in resA:
            inv = invariants(k, m)
            assert inv["g"] == G, f"genus mismatch {k} -> {inv['g']}"
            assert sum(k) == G
            assert kunz_ok(k, m)
            # gap count cross-check via w formula
            fdist[inv["F"]] = fdist.get(inv["F"], 0) + 1
            if inv["F"] > maxF:
                maxF = inv["F"]; maxFk = [k]
            elif inv["F"] == maxF:
                maxFk.append(k)
            if (minW is None) or (inv["W"] < minW):
                minW = inv["W"]; minWk = [k]
            elif inv["W"] == minW:
                minWk.append(k)
            if inv["W"] < 1:
                wilf_fail.append(k)
            # embedding dim bound
            assert 1 <= inv["e"] <= m, f"e out of range {k}: {inv['e']}"
            all_rows.append((m, k, inv))
        assert not wilf_fail, f"Wilf failures m={m}: {wilf_fail[:5]}"
        # Frobenius range analysis
        fmin, fmax = min(fdist), max(fdist)
        missing = [F for F in range(fmin, fmax+1) if F not in fdist]
        log_lines.append(f"  F-range=[{fmin},{fmax}] maxF={maxF} #maxWit={len(maxFk)} minWilf={minW}={float(minW):.6f} #minWit={len(minWk)} missingF={missing}")
        log_lines.append(f"  F-dist={sorted(fdist.items())}")
        log_lines.append(f"  minWilf_example_k={minWk[0]} maxF_example_k={maxFk[0]}")
        out[m] = {"count": len(resA), "sha": digest, "fdist": fdist, "missing": missing,
                  "maxF": maxF, "maxFk": maxFk, "minW": str(minW), "minWk": minWk,
                  "vectors": resA}
    total = sum(out[m]["count"] for m in MS)
    dt = time.time() - t0
    log_lines.append(f"total={total} elapsed={dt:.2f}s")
    print(f"TOTAL={total} elapsed={dt:.2f}s", flush=True)
    # write CSV
    with open("output/artifacts/census_26_m6-9.csv", "w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["m","kunz","apery","F","c","e","n","W_frac","W_float","generators"])
        for (m, k, inv) in sorted(all_rows):
            wr.writerow([m, ";".join(map(str,k)), ";".join(map(str,inv["w"])),
                         inv["F"], inv["c"], inv["e"], inv["n"],
                         f"{inv['W'].numerator}/{inv['W'].denominator}",
                         f"{float(inv['W']):.10f}",
                         ";".join(map(str,inv["gens"]))])
    with open("output/artifacts/enumeration.log", "w") as f:
        f.write("\n".join(log_lines) + "\n")
    # summary json for report building
    summ = {str(m): {"count": out[m]["count"], "sha": out[m]["sha"],
                     "fdist": {str(k): v for k, v in sorted(out[m]["fdist"].items())},
                     "missing": out[m]["missing"], "maxF": out[m]["maxF"],
                     "maxF_examples": [list(k) for k in out[m]["maxFk"][:5]],
                     "n_maxF": len(out[m]["maxFk"]),
                     "minW": out[m]["minW"],
                     "minW_examples": [list(k) for k in out[m]["minWk"][:5]],
                     "n_minW": len(out[m]["minWk"])} for m in MS}
    summ["_total"] = total
    summ["_elapsed"] = dt
    with open("output/artifacts/summary.json", "w") as f:
        json.dump(summ, f, indent=2)
    print(json.dumps(summ, indent=2))

if __name__ == "__main__":
    main()
