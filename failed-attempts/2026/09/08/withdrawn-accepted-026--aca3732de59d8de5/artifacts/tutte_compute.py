#!/usr/bin/env python3
"""Step 2: per-type Tutte polynomial by deletion-contraction; T(2,0) table; minor certs."""
import json, time
from itertools import combinations

N = 8
FULL = (1 << N) - 1

def rank_of_masks(lines):
    r = [0] * (1 << N)
    for s in range(1, 1 << N):
        pc = bin(s).count("1")
        if pc <= 2:
            r[s] = pc
        else:
            r[s] = 2 if any((s & ~ln) == 0 for ln in lines) else 3
    return r

def tutte_poly(r):
    """Full Tutte dict via memoized deletion-contraction.
    State: (rem tuple, cset mask). rank_minor(A) = r[A|cset]-r[cset]."""
    from functools import lru_cache
    rc = {}
    def rk(cset, sub):
        key = (cset, sub)
        v = rc.get(key)
        if v is None:
            v = r[sub | cset] - r[cset]
            rc[key] = v
        return v
    memo = {}
    calls = [0]
    def T(rem, cset):
        key = (rem, cset)
        v = memo.get(key)
        if v is not None:
            return v
        calls[0] += 1
        if not rem:
            memo[key] = {(0, 0): 1}
            return memo[key]
        remset = 0
        for e in rem:
            remset |= 1 << e
        e = rem[0]
        rest = rem[1:]
        restset = remset ^ (1 << e)
        re_ = rk(cset, 1 << e)
        r_all = rk(cset, remset)
        r_rest = rk(cset, restset)
        if re_ == 0:  # loop
            sub = T(rest, cset)
            out = {}
            for (i, j), c in sub.items():
                out[(i, j + 1)] = out.get((i, j + 1), 0) + c
        elif r_rest < r_all:  # coloop
            sub = T(rest, cset | (1 << e))
            out = {}
            for (i, j), c in sub.items():
                out[(i + 1, j)] = out.get((i + 1, j), 0) + c
        else:
            d = T(rest, cset)
            c = T(rest, cset | (1 << e))
            out = dict(d)
            for k, cc in c.items():
                out[k] = out.get(k, 0) + cc
        memo[key] = out
        return out
    poly = T(tuple(range(N)), 0)
    return poly, calls[0], len(memo)

def eval20(poly):
    return sum(c * (2 ** i) * (0 ** j) if j == 0 else 0 for (i, j), c in poly.items())

t0 = time.time()
data = json.load(open("output/artifacts/reps.json"))
reps = data["reps"]
print("ntypes =", len(reps), "labeled =", data["total_labeled"], flush=True)

rows = []
for t, rep in enumerate(reps):
    lines = rep["lines"]
    # divisibility sanity: count must divide 40320
    assert 40320 % rep["count"] == 0, (t, rep["count"])
    r = rank_of_masks(lines)
    # simplicity sanity: all singletons rank1, pairs rank2
    for e in range(N):
        assert r[1 << e] == 1
    for a, b in combinations(range(N), 2):
        assert r[(1 << a) | (1 << b)] == 2
    poly, calls, nstates = tutte_poly(r)
    # Tutte sanity: T(1,1) = #bases; T(2,2)=2^8
    nbb = sum(poly.values())
    nbases = sum(1 for b in combinations(range(N), 3)
                 if not any(((1 << b[0]) | (1 << b[1]) | (1 << b[2])) & ~ln == 0 or
                            (((1 << b[0]) | (1 << b[1]) | (1 << b[2])) & ~ln) == 0 for ln in lines))
    nb2 = sum(c * (2 ** i) * (2 ** j) for (i, j), c in poly.items())
    assert nbb == nbases, (t, nbb, nbases)
    assert nb2 == 2 ** N, (t, nb2)
    v = eval20(poly)
    rows.append({"type": t, "lines": lines, "count": rep["count"],
                 "nbases": nbases, "t20": v,
                 "poly": sorted([[i, j, c] for (i, j), c in poly.items()]),
                 "nstates": nstates})
    print(f"type {t:2d} nlines={len(lines):2d} count={rep['count']:6d} nbases={nbases:3d} T(2,0)={v} states={nstates}", flush=True)

rows.sort(key=lambda d: -d["t20"])
print("\nTop 8:", flush=True)
for d in rows[:8]:
    print(f"  type {d['type']} T(2,0)={d['t20']} nbases={d['nbases']} lines={d['lines']}", flush=True)
vals = sorted(set(d["t20"] for d in rows), reverse=True)
print("distinct T(2,0) values:", vals, flush=True)
W, R = rows[0], rows[1]
G = W["t20"] - R["t20"]
print(f"maximizer type={W['type']} T={W['t20']}; runner-up type={R['type']} T={R['t20']}; gap G={G}", flush=True)
json.dump(rows, open("output/artifacts/tutte_table.json", "w"))
print(f"tutte time={time.time()-t0:.1f}s", flush=True)
