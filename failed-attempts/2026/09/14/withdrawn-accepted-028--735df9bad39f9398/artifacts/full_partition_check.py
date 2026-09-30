"""Full check: DP over ALL multisets of row lengths with total <= 36,
not just reachable states. Confirms singles outcomes identical."""
from functools import lru_cache
import json

def sm(n):
    return [(max(k-1,0), max(n-k-3,0)) for k in range(n-1)]
def canon(ps):
    return tuple(sorted(p for p in ps if p > 0))

# enumerate all partitions with sum<=36 via recursive generation
MAXT = 36
states = []
def gen(remaining, min_part, cur):
    states.append(tuple(cur))
    for p in range(min_part, remaining+1):
        cur.append(p)
        gen(remaining-p, p, cur)
        cur.pop()
gen(MAXT, 1, [])
# states currently ascending parts; convert to canonical sorted (already sorted asc)
states = [tuple(s) for s in states]
print("total partition-states with sum<=36:", len(states))
assert () in states
# bottom-up by total
states_sorted = sorted(states, key=sum)
memo = {}
for s in states_sorted:
    moves_exist = False
    w = False
    for i, n in enumerate(s):
        r = s[:i]+s[i+1:]
        for L, R in sm(n):
            moves_exist = True
            ns = canon(r + ((L,) if L>0 else ()) + ((R,) if R>0 else ()))
            assert ns in memo or sum(ns) < sum(s), (s, ns)
            # ns must already be computed since sum smaller and canonical sorted?
            # ns sorted? canon sorts, and gen produces all sorted tuples, so present
            if memo[ns] is False:
                w = True
                break
        if w:
            break
    memo[s] = True if not moves_exist else w
P = [n for n in range(37) if memo[(n,) if n>0 else ()] is False]
print("P(full) =", P)
out = json.load(open("output/artifacts/outcomes.json"))
print("P(reach) =", out["P"])
assert P == out["P"]
print("FULL-PARTITION AGREEMENT CONFIRMED over", len(states), "states")
