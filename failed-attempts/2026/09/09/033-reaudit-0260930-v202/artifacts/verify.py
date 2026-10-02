"""Independent verifier: replays the census from committed posets.json + ehrhart.json.
Checks (all exact, stdlib only):
  V1 counts match OEIS A000112 {1,1,2,5,16,63,318};
  V2 every stored relation is a partial order (reflexive/antisym/transitive);
  V3 pairwise non-isomorphism within each n (brute-force S_n match of full relation);
  V4 every record: Lvals are consistent with stored Ehrhart coeffs, Lvals[1]=#ideals,
      lead*n! == e, h* agrees with Lvals and sums to e with all entries >= 0;
  V5 lin-ext e recomputed by independent backtracking equals stored e;
  V6 reciprocity L(-m)=(-1)^n S(P,m-1) with strict maps by antichain-fiber recursion;
  V7 maxima replay: stored arg attains stored max and no type exceeds it.
Writes verify.log. Exits nonzero on any failure.
"""
import itertools, json, math
from fractions import Fraction
from functools import lru_cache

log = open("verify.log", "w")
def say(s):
    log.write(s + "\n"); print(s)

data = json.load(open("posets.json"))
ehr = json.load(open("ehrhart.json"))
rec = {(r["n"], r["idx"]): r for r in ehr["records"]}

# V1
counts = {}
for t in data["types"]:
    counts[t["n"]] = counts.get(t["n"], 0) + 1
assert counts == {0: 1, 1: 1, 2: 2, 3: 5, 4: 16, 5: 63, 6: 318}, counts
say("V1 counts OK " + str(counts))

# V2
for t in data["types"]:
    n, le = t["n"], t["le"]
    for x in range(n):
        assert (le[x] >> x) & 1
        for y in range(n):
            if x != y and ((le[x] >> y) & 1):
                assert not ((le[y] >> x) & 1), ("antisym", t)
            if (le[x] >> y) & 1:
                assert le[y] & ~le[x] == 0, ("trans", t)
say("V2 poset axioms OK (406 types)")

# V3 non-isomorphism via full-relation canonical signature (independent code path)
def sig(le, n):
    F = {(a, b) for a in range(n) for b in range(n) if (le[a] >> b) & 1}
    best = None
    for s in itertools.permutations(range(n)):
        G = frozenset((s[a], s[b]) for (a, b) in F)
        if best is None or sorted(G) < sorted(best):
            best = G
    return best
for n in range(7):
    ts = [t for t in data["types"] if t["n"] == n]
    S = [sig(t["le"], n) for t in ts]
    assert len(set(S)) == len(ts), n
say("V3 pairwise non-isomorphism OK (all n)")

# V4+V5+V6
below_cache = {}
def below(le, n):
    b = []
    for x in range(n):
        m = 0
        for y in range(n):
            if (le[y] >> x) & 1:
                m |= (1 << y)
        b.append(m)
    return b

def lin_ext(le, n, bel):
    @lru_cache(maxsize=None)
    def c(S):
        if S == 0:
            return 1
        t = 0
        m = S
        while m:
            x = (m & -m).bit_length() - 1
            if bel[x] & S == (1 << x):
                t += c(S ^ (1 << x))
            m &= m - 1
        return t
    return c((1 << n) - 1)

def strict(le_full_mask_free_bel, n, bel, S_, k, memo):
    key = (S_, k)
    if key in memo:
        return memo[key]
    if S_ == 0:
        memo[key] = 1
        return 1
    if k == 0:
        memo[key] = 0
        return 0
    mins = [x for x in range(n) if (S_ >> x) & 1 and bel[x] & S_ == (1 << x)]
    # nonempty-subset fiber: value-1 set must be a nonempty antichain of... actually
    # any subset of mins (antichain automatically); empty allowed only if... value 1
    # can be skipped? strict maps: fiber of min value may be empty; allow all subsets
    tot = 0
    for r in range(1 << len(mins)):
        A_ = 0
        for i, x in enumerate(mins):
            if (r >> i) & 1:
                A_ |= (1 << x)
        tot += strict(None, n, bel, S_ & ~A_, k - 1, memo)
    memo[key] = tot
    return tot

for t in data["types"]:
    n, idx, le = t["n"], t["idx"], t["le"]
    r = rec[(n, idx)]
    Nn = n + 1
    coef = [Fraction(r["coef"][p]) for p in range(Nn)]
    for m in range(Nn):
        assert sum(coef[p] * Fraction(m) ** p for p in range(Nn)) == r["Lvals"][m], (n, idx, m)
    bel = below(le, n)
    # Lvals[1] = # ideals (for n>=1; n=0 has single Lvals entry)
    if n >= 1:
        N = 1 << n
        nidl = sum(1 for I in range(N)
                   if all(not (bel[x] & ~I) for x in range(n) if (I >> x) & 1))
        assert r["Lvals"][1] == nidl, (n, idx)
    assert coef[n] * math.factorial(n) == r["e"], (n, idx)
    h = r["hstar"]
    assert len(h) == Nn and all(isinstance(v, int) and v >= 0 for v in h)
    for j in range(Nn):
        assert r["Lvals"][j] == sum(h[i] * math.comb(j + n - i, n) for i in range(j + 1)), (n, idx, j)
    assert sum(h) == r["e"], (n, idx)
    assert lin_ext(le, n, bel) == r["e"], (n, idx)
    full = (1 << n) - 1
    memo = {}
    for m in range(1, n + 2):
        Lm = sum(coef[p] * Fraction(-m) ** p for p in range(Nn))
        assert Lm == ((-1) ** n) * strict(None, n, bel, full, m - 1, memo), (n, idx, m)
say("V4 Ehrhart/h*/volume-equality OK (406 types)")
say("V5 independent linear-extension replay OK (406 types)")
say("V6 Ehrhart-Macdonald reciprocity OK (406 types, m=1..n+1)")

# V7 maxima replay
for n in range(7):
    rs = [r for r in ehr["records"] if r["n"] == n]
    mx = max(r["e"] for r in rs)
    st = ehr["maxima"][str(n)]
    assert st["max"] == mx
    assert all(rec[(n, i)]["e"] == mx for i in st["arg"])
    assert all(r["e"] <= mx for r in rs)
say("V7 per-n maximality replay OK: " + str({n: ehr['maxima'][str(n)] for n in range(7)}))
say("ALL VERIFY_OK")
log.close()
