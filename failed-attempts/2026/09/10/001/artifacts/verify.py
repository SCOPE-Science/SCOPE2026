#!/usr/bin/env python3
"""Lane-486 target-phase verification: C5 substitution sharpness + loss arithmetic.

Checks (stdlib only, deterministic):
 1. G_k = k-fold C5 substitution: n=5^k, m formula.
 2. P5-freeness of G_0,G_1,G_2 by exhaustive 5-subset scan (G_2: C(25,5)=53130).
 3. hom(G_1)=2 (no K3/I3 + witnesses), hom(G_2)=4 (no K5/I5 + K4/I4 witnesses).
    => hom = 2^k = n^{log_5 2}; target c=1/8 strictly below => not refuted.
 4. Explicit 9-vertex P4-free (cograph) induced subgraph of G_2 (I4 compatibility).
 5. Exact one-step loss-factor arithmetic for increment_table.csv.
 6. Concavity spot-check for degenerate-node preservation lemma.
"""
import itertools
import math

LOG = []


def log(s):
    LOG.append(s)
    print(s)


def c5_adj():
    n = 5
    adj = [0] * n
    for i in range(n):
        for j in ((i - 1) % 5, (i + 1) % 5):
            adj[i] |= (1 << j)
    return adj


def substitute(base_adj, block_adj):
    """C5-style substitution: replace each vertex of base by copy of block graph.
    base_adj: list of bitmasks (nb vertices), block_adj: list of bitmasks (mb)."""
    nb = len(base_adj)
    mb = len(block_adj)
    n = nb * mb
    adj = [0] * n
    for i in range(nb):
        for u in range(mb):
            v = i * mb + u
            mask = 0
            # inside block: copy of block graph
            b = block_adj[u]
            uu = 0
            while b:
                if b & 1:
                    mask |= (1 << (i * mb + uu))
                uu += 1
                b >>= 1
            # across blocks: complete iff base-edge
            b2 = base_adj[i]
            j = 0
            while b2:
                if b2 & 1:
                    for w in range(mb):
                        mask |= (1 << (j * mb + w))
                j += 1
                b2 >>= 1
            adj[v] = mask
    return adj


def popcount(x):
    return bin(x).count("1")


def nedges(adj):
    return sum(popcount(a) for a in adj) // 2


def induced_edges(adj, subset):
    mask = 0
    for v in subset:
        mask |= (1 << v)
    t = 0
    for v in subset:
        t += popcount(adj[v] & mask)
    return t // 2


def is_connected(adj, subset):
    s = set(subset)
    seen = {subset[0]}
    stack = [subset[0]]
    while stack:
        v = stack.pop()
        w = adj[v]
        for u in s:
            if u not in seen and (w >> u) & 1:
                seen.add(u)
                stack.append(u)
    return seen == s


def is_P5(adj, subset):
    # 5 vertices, 4 edges, connected, maxdeg<=2  <=> induced P5
    if induced_edges(adj, subset) != 4:
        return False
    if not is_connected(adj, subset):
        return False
    mask = 0
    for v in subset:
        mask |= (1 << v)
    for v in subset:
        if popcount(adj[v] & mask) > 2:
            return False
    return True


def has_P5(adj):
    for sub in itertools.combinations(range(len(adj)), 5):
        if is_P5(adj, sub):
            return True, sub
    return False, None


def has_Kt(adj, t):
    for sub in itertools.combinations(range(len(adj)), t):
        if induced_edges(adj, sub) == t * (t - 1) // 2:
            return True, sub
    return False, None


def has_It(adj, t):
    for sub in itertools.combinations(range(len(adj)), t):
        if induced_edges(adj, sub) == 0:
            return True, sub
    return False, None


def has_P4(adj):
    for sub in itertools.combinations(range(len(adj)), 4):
        e = induced_edges(adj, sub)
        if e == 3 and is_connected(adj, list(sub)):
            mask = 0
            for v in sub:
                mask |= (1 << v)
            if all(popcount(adj[v] & mask) <= 2 for v in sub):
                return True, sub
    return False, None


# ---- Build blow-ups ----
G = [[0]]  # G_0 = K1 ; adjacency bitmasks
C5 = c5_adj()
G.append(C5)  # G_1 = C5
G.append(substitute(C5, C5))  # G_2, n=25

for k in (0, 1, 2):
    n = len(G[k])
    assert n == 5 ** k, (k, n)
    log(f"G_{k}: n={n} m={nedges(G[k])}")
# m formula check: m_{k+1} = 5*m_k + 5*m(C5)*4^k? just report values
assert nedges(G[1]) == 5
assert nedges(G[2]) == 5 * 5 + 5 * 25  # 5 blocks x5 edges + 5 C5-edges x25 cross
log(f"m_2 cross-check OK (25+125=150)")

# ---- P5-freeness ----
for k in (0, 1, 2):
    if len(G[k]) < 5:
        log(f"G_{k}: n<5, P5-free vacuously")
        continue
    found, wit = has_P5(G[k])
    assert not found, (k, wit)
    log(f"G_{k}: P5-free OK (exhaustive over C({len(G[k])},5) 5-sets)")

# ---- hom values ----
f, _ = has_Kt(G[1], 3)
assert not f
f, _ = has_It(G[1], 3)
assert not f
_, k2 = has_Kt(G[1], 2)
_, i2 = has_It(G[1], 2)
log(f"G_1=C5: no K3/I3; K2 witness {k2}, I2 witness {i2} => hom=2=2^1 OK")

f5, _ = has_Kt(G[2], 5)
assert not f5
f5i, _ = has_It(G[2], 5)
assert not f5i
ok4, k4 = has_Kt(G[2], 4)
assert ok4
ok4i, i4 = has_It(G[2], 4)
assert ok4i
log(f"G_2: no K5/I5 (exhaustive C(25,5)=53130); K4 witness {k4}, I4 witness {i4}")
log("=> hom(G_2)=4=2^2; formula hom(G_k)=2^k=n^{log_5 2} holds k<=2")

# ---- exponent comparison ----
cstar = math.log(2) / math.log(5)
log(f"log_5 2 = {cstar:.6f} (upper bound for any P5 EH exponent on this family)")
assert cstar > 1 / 8
log(f"target c=1/8=0.125 < {cstar:.6f}: canonical family does NOT refute target")

# ---- I4 compatibility: explicit P4-free 9-set in G_2 ----
# quotient pattern: blocks {0,1,2} induce P3 in C5? C5[0,1,2] = path 0-1-2 = P3 (cograph).
# inside each block take 3 vertices inducing P3 (C5 minus 2 nonadjacent... take {0,1,2} of block C5 = P3).
nine = []
for blk in (0, 1, 2):
    for u in (0, 1, 2):
        nine.append(blk * 5 + u)
# verify P4-free on induced subgraph
sub = G[2]
found4, _ = has_P4([0] * 0) if False else (False, None)
# direct check on the 9-set
bad = False
for q in itertools.combinations(nine, 4):
    e = induced_edges(sub, list(q))
    if e == 3 and is_connected(sub, list(q)):
        mask = 0
        for v in q:
            mask |= (1 << v)
        if all(popcount(sub[v] & mask) <= 2 for v in q):
            bad = True
            break
assert not bad
log(f"explicit 9-set {nine} induces P4-free subgraph of G_2 (C(9,4)=126 checked)")
log(f"9 >= 25^(1/4)={25 ** 0.25:.3f}: I4 cograph-extraction route not obstructed on G_2")

# ---- loss-factor arithmetic (increment table) ----
c = 1 / 8
vals = {
    "(1/50)^c": (1 / 50) ** c,
    "(1/4)^c": (1 / 4) ** c,
    "(3/4)^c": (3 / 4) ** c,
    "(1/7)^c": (1 / 7) ** c,
    "(3n/4)^c/n^c": (3 / 4) ** c,
}
for k, v in vals.items():
    log(f"{k} = {v:.6f} ({'LOSS <1: one-step stall' if v < 1 else 'ok'})")
log(f"Bacso-Tuza iterated exponent c(1-c) at c=1/8: {c*(1-c):.6f} = 7/64 < 1/8: near-miss quantified")
# additive compensation thresholds
# I5: 1+((n-2)/2)^c >= n^c  <=>  n^c - ((n-2)/2)^c <= 1
lo, hi = 1, 10 ** 13
def holds(n):
    return 1 + ((n - 2) / 2) ** c >= n ** c
powers = [10 ** e for e in range(1, 13)]
ok_powers = [p for p in powers if holds(p)]
mx = max(ok_powers)
log(f"I5 additive compensation 1+((n-2)/2)^(1/8)>=n^(1/8) holds up to n~{mx}")
# high-degree omega-side deficit: n^c-(n-1-s)^c with s=n^c at n=1e12
n = 10 ** 12
s = n ** c
deficit = n ** c - (n - 1 - s) ** c
log(f"high-degree omega deficit n^c-(n-1-s)^c, s=n^c, n=1e12: {deficit:.6f} (<=1 => +1 wins)")

# ---- concavity spot check (degenerate preservation) ----
import random
random.seed(486)
for _ in range(200):
    n = random.randint(2, 500)
    k = random.randint(2, min(n, 6))
    parts = [1] * k
    for _ in range(n - k):
        parts[random.randrange(k)] += 1
    assert sum(p ** c for p in parts) + 1e-9 >= n ** c
log("concavity sum n_i^c>=n^c spot-checked on 200 random partitions (c=1/8)")

log("VERIFY_OK")
with open("output/artifacts/verify.log", "w") as f:
    f.write("\n".join(LOG) + "\n")
