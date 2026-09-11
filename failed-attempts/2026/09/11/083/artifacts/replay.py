"""Countable replay: rho1 walk coherence + oscillation census (stdlib only), v2.

Richer C-sequence so walks genuinely diverge:
 - C_0 = {}
 - odd beta (successor-like): C_beta = {beta-1}
 - even beta > 0 (limit-like): C_beta = {beta-1} U {xi < beta : xi % M == r_beta},
   r_beta = ((beta//2) % M), M = 5.
Walk/rho1 (Todorcevic finite form):
 - step(a,b) = min{c in C_b : c >= a}
 - rho1(a,b) = 0 if a>=b else max(|C_b cap a|, rho1(a, step(a,b)))
Branch f_b(xi) = rho1(xi, b). osc = strict sign crossings of difference.
"""
import json
import os
import sys

sys.setrecursionlimit(100000)
N = 200
M = 5

def build_C(N):
    C = {}
    C[0] = set()
    for b in range(1, N):
        if b % 2 == 1:
            C[b] = {b - 1}
        else:
            r = (b // 2) % M
            C[b] = {b - 1} | {x for x in range(b) if x % M == r}
    return C

C = build_C(N)

def step(a, b):
    best = None
    for c in C[b]:
        if c >= a and (best is None or c < best):
            best = c
    assert best is not None and best < b, (a, b)
    return best

memo = {}
def rho1(a, b):
    if a >= b:
        return 0
    key = (a, b)
    if key in memo:
        return memo[key]
    # iterative walk to avoid recursion depth
    stack = []
    cur = b
    while cur > a:
        stack.append(cur)
        cur = step(a, cur)
    # unwind: rho1(a,cur0=a)=0; rho1(a,k)=max(|C_k cap a|, rho1(a, next))
    vals = {a: 0}
    for k in reversed(stack):
        s = step(a, k)
        v = sum(1 for c in C[k] if c < a)
        w = vals[s]
        vals[k] = v if v > w else w
    r = vals[b]
    memo[key] = r
    return r

F = {}
for b in range(N):
    F[b] = [rho1(x, b) for x in range(b)]

def osc_pair(b, g, lo=0):
    th = min(b, g)
    if th - lo < 2:
        return 0
    d = [F[b][x] - F[g][x] for x in range(lo, th)]
    n = 0
    for i in range(len(d) - 1):
        if d[i] * d[i + 1] < 0:
            n += 1
    return n

maxdiff = 0
maxpair = None
for b in range(N):
    Fb = F[b]
    for g in range(b + 1, N):
        Fg = F[g]
        diff = 0
        for x in range(b):
            if Fb[x] != Fg[x]:
                diff += 1
        if diff > maxdiff:
            maxdiff = diff
            maxpair = (b, g)

tails = [0, 50, 100, 140, 170]
tail_stats = {}
for t0 in tails:
    mx = 0
    cnt_le1 = 0
    cnt_ge2 = 0
    tot = 0
    ex = None
    for b in range(t0 + 2, N):
        for g in range(b + 1, N):
            o = osc_pair(b, g, lo=t0)
            tot += 1
            if o <= 1:
                cnt_le1 += 1
            else:
                cnt_ge2 += 1
            if o > mx:
                mx = o
                ex = (b, g)
    tail_stats[str(t0)] = {"max_osc": mx, "n_le1": cnt_le1, "n_ge2": cnt_ge2,
                           "total": tot, "example_max": ex}

triple = None
bases = list(range(20, N, 9))
for i in range(len(bases)):
    for j in range(i + 1, len(bases)):
        for k in range(j + 1, len(bases)):
            b1, b2, b3 = bases[i], bases[j], bases[k]
            o12 = osc_pair(b1, b2)
            o23 = osc_pair(b2, b3)
            o13 = osc_pair(b1, b3)
            if o12 <= 1 and o23 <= 1 and o13 >= 3:
                triple = {"b": [b1, b2, b3], "osc": [o12, o23, o13]}
                break
        if triple:
            break
    if triple:
        break

sample_walks = []
for (a, b) in [(0, 60), (7, 120), (33, 150), (100, 199), (150, 199)]:
    w = []
    cur = b
    while cur > a:
        w.append(cur)
        cur = step(a, cur)
    w.append(a)
    sample_walks.append({"alpha": a, "beta": b, "walk": w,
                         "rho1": rho1(a, b),
                         "C_beta_cap_alpha_size": sum(1 for c in C[b] if c < a)})

log = {
    "N": N, "M": M,
    "C_def": "C_0={}; odd: {b-1}; even b>0: {b-1} U {x<b: x%M==((b//2)%M)}, M=5",
    "rho1_def": "rho1(a,b)=max(|C_b cap a|, rho1(a, min(C_b\\a))), rho1(a,a)=0",
    "osc_def": "strict sign crossings of (f-g) on common domain",
    "coherence": {"max_diff_size": maxdiff, "max_diff_pair": maxpair,
                  "note": "diff sets finite by finite-segment construction; "
                          "question is uniform boundedness pattern"},
    "tail_osc_stats": tail_stats,
    "nontransitivity_triple_full_range": triple,
    "sample_walks": sample_walks,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "replay_log.json")
with open(out, "w") as f:
    json.dump(log, f, indent=1)
print("VERIFY_OK")
print(json.dumps({"max_diff": maxdiff, "maxpair": maxpair,
                  "tails": {k: {"max": v["max_osc"], "le1": v["n_le1"],
                                "ge2": v["n_ge2"]} for k, v in tail_stats.items()},
                  "triple": triple}, indent=1))
