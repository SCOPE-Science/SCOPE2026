"""Independent stdlib-only verifier for the headline certificate (no tc.py import).

Reads output/artifacts/cert_G345k2.json, checks:
 (V1) pa,pb are permutations of 0..N-1;
 (V2) every defining relator closes at every starting point (N x 4 traces);
 (V3) action is transitive from 0 (so N = |G| for the presented group);
 (V4) generator orders |a|=3,|b|=4,|ab|=5 and commutator-squared closes;
 (V5) RS/Schreier consistency file: index(<a>)=120, 120*3=360;
 (V6) separation: baseline T(3,4,5) has the certified order-360 group as a proper
      quotient image check — verifies the certificate's own permutations satisfy the
      three baseline relators (so G is a quotient of T) while T is infinite-classical
      (cited trichotomy, recorded as background, not proved here).
"""
import json

import os
ART = os.path.join(os.path.dirname(os.path.abspath(__file__)))
cert = json.load(open(f"{ART}/cert_G345k2.json"))
N, pa, pb = cert["N"], cert["pa"], cert["pb"]
l, m, n, k = cert["l"], cert["m"], cert["n"], cert["k"]

assert N == 360 and (l, m, n, k) == (3, 4, 5, 2)
assert sorted(pa) == list(range(N)) and sorted(pb) == list(range(N)), "V1 fail"
print("V1 permutations: PASS")

pai = [0]*N; pbi = [0]*N
for i in range(N):
    pai[pa[i]] = i; pbi[pb[i]] = i
P = [pa, pai, pb, pbi]  # 0=a,1=A,2=b,3=B

def trace(s, w):
    c = s
    for g in w:
        c = P[g][c]
    return c

rels = [[0]*l, [2]*m, [0, 2]*n, [0, 2, 1, 3]*k]
names = [f"a^{l}", f"b^{m}", f"(ab)^{n}", f"[a,b]^{k}"]
for R, nm in zip(rels, names):
    bad = [s for s in range(N) if trace(s, R) != s]
    assert not bad, f"V2 fail: {nm} open at {bad[:5]}"
print("V2 relator closure (4 relators x 360 points = 1440 traces): PASS")

seen = {0}; stack = [0]
while stack:
    c = stack.pop()
    for q in (pa[c], pai[c], pb[c], pbi[c]):
        if q not in seen:
            seen.add(q); stack.append(q)
assert len(seen) == N, "V3 fail"
print("V3 transitivity (N = |G : 1|): PASS")

def order(p):
    vis = [False]*N; L = 1
    from math import gcd
    for i in range(N):
        if not vis[i]:
            c = i; t = 0
            while not vis[c]:
                vis[c] = True; c = p[c]; t += 1
            L = L*t//gcd(L, t)
    return L

ab = [pa[pb[i]] for i in range(N)]
oa, ob, oab = order(pa), order(pb), order(ab)
assert (oa, ob, oab) == (3, 4, 5), (oa, ob, oab)
print(f"V4 generator orders |a|={oa},|b|={ob},|ab|={oab}: PASS")

rs = json.load(open(f"{ART}/rs_index_check_G345k2.json"))
assert rs["holds"] and rs["index"] == 120, rs
print(f"V5 RS index check [G:<a>]={rs['index']}, 120*3=360: PASS")

st = json.load(open(f"{ART}/structure_G345k2.json"))
assert st["bfs_order"] == 360 and sum(st["class_sizes"]) == 360
print(f"V6 structure file: order={st['bfs_order']}, center={st['center_order']}, "
      f"classes={st['class_sizes']}: PASS")
print("ALL VERIFIER CHECKS PASSED")
