#!/usr/bin/env python3
"""Lane-486 TARGET: Theorem R (conditional reduction) machine certificates.
Stdlib only, exact integer arithmetic where possible.

Theorem R: IF every prime P5-free G has a pure pair A,B with |A|,|B|>=|G|/16,
THEN every P5-free G on n has a P4-free induced H, |H|>=n^{1/4}, hence
hom(G)>=|H|^{1/2}>=n^{1/8} (N0=1).

Certifies:
 R1: exact rate correspondence 16^{1/4}=2; 2*(n/16)^{1/4}=n^{1/4} (exact).
 R2: small-n base automatic: singleton pair gives |H|>=2>=n^{1/4} iff n<=16,
     and singleton rate 1>=n/16 iff n<=16 (same threshold; no gap).
 R3: concavity size-addition for d=1/4 (random partitions).
 R4: Lemma U core by COMPLETE finite check: no labeled P4 on {0,1,2,3} has
     uniform (all/none) cross edges across any 3-1 or 2-2 split
     => complete-join / disjoint-union of P4-free graphs is P4-free.
 R5: degree-sequence separation (K1,3 and K3+I1 are not P4) underpinning R4.
 R6: exact gamma<->d<->c correspondence table (2g^d=1, c=d/2).
"""
import itertools
LOG=[]
def log(s): LOG.append(s); print(s, flush=True)

# R1 exact
assert 16 ** 0.25 == 2.0
import math
for n in [16, 25, 256, 10**6, 10**12]:
    assert abs(2 * (n / 16) ** 0.25 - n ** 0.25) < 1e-9 * n ** 0.25
log("R1: 2*(n/16)^{1/4}==n^{1/4} exact (16^{1/4}=2); prime-step recurrence closes with equality")

# R2 small-n
for n in range(1, 17):
    assert 2 >= n ** 0.25, n
assert abs(2 - 16 ** 0.25) < 1e-12
assert 2 < 17 ** 0.25
log("R2: singleton-pair base |H|>=2>=n^{1/4} holds iff n<=16; rate condition 1>=n/16 iff n<=16. Thresholds coincide: base automatic, N0=1")

# R3 concavity d=1/4
import random
random.seed(1608)
d = 0.25
for _ in range(300):
    n = random.randint(2, 2000)
    k = random.randint(2, min(n, 8))
    parts = [1] * k
    for _ in range(n - k):
        parts[random.randrange(k)] += 1
    assert sum(p ** d for p in parts) + 1e-9 >= n ** d
log("R3: sum n_i^{1/4}>=n^{1/4} spot-checked (300 random partitions)")

# R4: complete check that uniform-cross unions never create P4
def edgeset(n, bits):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    return {pairs[k] for k in range(len(pairs)) if (bits >> k) & 1}
def is_P4(E):
    # 4 vertices {0,1,2,3}: P4 <=> 3 edges, connected, maxdeg<=2
    if len(E) != 3: return False
    deg = [0]*4
    for a, b in E: deg[a]+=1; deg[b]+=1
    if max(deg) > 2: return False
    # connected?
    adj = {i: set() for i in range(4)}
    for a, b in E: adj[a].add(b); adj[b].add(a)
    seen={0}; stack=[0]
    while stack:
        v=stack.pop()
        for u in adj[v]:
            if u not in seen: seen.add(u); stack.append(u)
    return len(seen)==4
def cross(E, S, T):
    return {(min(a,b),max(a,b)) for a in S for b in T if (min(a,b),max(a,b)) in E}
nP4 = 0
checked = 0
for bits in range(1 << 6):
    E = edgeset(4, bits)
    if not is_P4(E): continue
    nP4 += 1
    # every nontrivial split must have NON-uniform cross (else Lemma U false)
    for S in [frozenset([0]), frozenset([0,1]), frozenset([0,2]), frozenset([0,3]),
              frozenset([0,1,2]), frozenset([0,1,3]), frozenset([0,2,3]),
              frozenset([1,2]), frozenset([1,3]), frozenset([1,2,3])]:
        T = frozenset([v for v in range(4) if v not in S])
        if not T: continue
        C = cross(E, S, T)
        full = len(S)*len(T)
        assert 0 < len(C) < full, (E, S, T)
        checked += 1
log(f"R4: all {nP4} labeled P4s x splits checked ({checked}): every split has mixed cross => Lemma U holds (joins/unions of P4-free stay P4-free)")

# R5 degree sequences
def degseq(E):
    deg=[0]*4
    for a,b in E: deg[a]+=1; deg[b]+=1
    return tuple(sorted(deg))
star = {(0,1),(0,2),(0,3)}
k3i = {(0,1),(1,2),(0,2)}
assert degseq(star)==(1,1,1,3) and degseq(k3i)==(0,2,2,2)
# a P4 has degseq (1,1,2,2)
for bits in range(1<<6):
    E=edgeset(4,bits)
    if is_P4(E): assert degseq(E)==(1,1,2,2)
log("R5: K1,3 degseq (1,1,1,3), K3+I1 (0,2,2,2), P4 always (1,1,2,2): case analysis sound")

# R6 correspondence
for g_den in [4, 16, 50, 256]:
    g = 1/g_den
    dd = math.log(2)/math.log(1/g)
    cc = dd/2
    log(f"R6: gamma=1/{g_den}: cograph-d={dd:.6f} -> EH-c={cc:.6f} {'== TARGET 1/8 EXACT' if abs(cc-1/8)<1e-12 else ('BELOW target' if cc<1/8 else 'ABOVE target')}")
log("REDUCE_OK")
with open("output/artifacts/reduce.log","w") as f: f.write("\n".join(LOG)+"\n")
