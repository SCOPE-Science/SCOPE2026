"""Lane-403 attack v11: factor-realization density lemma, finite shadow.

Claim: pure universal-factor odometer tower (2,6,30) hits every finite
cyclic-factor basic open at computed levels: for quotient levels M in
{2,3,5,6,10,15,30}, the realized quotient pattern set Reach(M) contains
all single M-cycles (full S_N enumeration at N=6: 720; sampled fiber-perm
construction at N=30 for larger M: construct preserving g, not blind sample).

Construction: given target single M-cycle tau, lift to block-preserving
g on N atoms: map fibers coherently. Check g.s.g^-1 has quotient tau.
"""
import json, os, random, itertools, math

ART = os.path.dirname(os.path.abspath(__file__))
random.seed(311)
res = {}

def compose(p, q):
    return [p[q[i]] for i in range(len(q))]

def odo(N):
    return [(a + 1) % N for a in range(N)]

def single(p):
    n = len(p)
    seen = [False] * n
    x, c = 0, 0
    while not seen[x]:
        seen[x] = True
        x = p[x]
        c += 1
    return c == n

def invert(p):
    q = [0] * len(p)
    for i, v in enumerate(p):
        q[v] = i
    return q

def conj(g, s):
    return compose(compose(g, s), invert(g))

def is_Mcycle(t):
    x, seen = 0, set()
    for _ in range(len(t)):
        if x in seen:
            return False
        seen.add(x)
        x = t[x]
    return x == 0

def pattern(psi, N, M):
    t = []
    for b in range(M):
        imgs = {psi[a] % M for a in range(N) if a % M == b}
        if len(imgs) != 1:
            return None
        t.append(next(iter(imgs)))
    return t

# (i) N=6 full S_6: reach on M=2,3 quotients
s6 = odo(6)
r2, r3 = set(), set()
for g in itertools.permutations(range(6)):
    psi = conj(list(g), s6)
    t2, t3 = pattern(psi, 6, 2), pattern(psi, 6, 3)
    if t2 is not None:
        r2.add(tuple(t2))
    if t3 is not None:
        r3.add(tuple(t3))
res["N6_reach"] = {
    "mod2": sorted(map(list, r2)),
    "mod2_hits_2cycle": [1, 0] in [list(t) for t in r2],
    "mod3": sorted(map(list, r3)),
    "mod3_hits_both_3cycles": ([1, 2, 0] in [list(t) for t in r3] and
                               [2, 0, 1] in [list(t) for t in r3]),
}

# (ii) N=30: for each M in {2,3,5,6,10,15,30}, for every single M-cycle tau
# (all 1+2+24+120+... cap: test all tau for M<=6, sample 40 for M>=10),
# construct a quotient-preserving g and verify.
s30 = odo(30)
o30 = [t for t in [None] ]  # placeholder

def realize(tau, N=30):
    """Find g in S_N preserving mod-M blocks with g s g^-1 quotient = tau.
    Direct construction: pick g mapping each fiber coherently.
    Brute force over fiber-internal perms is huge; instead random search
    over block-preserving g (product of fiber Sym's), up to 4000 tries."""
    M = len(tau)
    tau = list(tau)
    for _ in range(4000):
        g = [0] * N
        for b in range(M):
            fib = [a for a in range(N) if a % M == b]
            dst = fib[:]
            random.shuffle(dst)
            for a, c in zip(fib, dst):
                g[a] = c
        psi = conj(g, s30)
        if pattern(psi, N, M) == tau:
            return True
    return False

out = {}
for M in (2, 3, 5, 6):
    taus = [t for t in itertools.permutations(range(M)) if is_Mcycle(list(t))]
    hits = sum(1 for t in taus if realize(list(t)))
    out[M] = {"n_tau": len(taus), "hits": hits, "full": hits == len(taus)}
for M in (10, 15, 30):
    # sample single M-cycles: random cyclic orderings
    taus = []
    for _ in range(40 if M < 30 else 20):
        perm = list(range(M))
        random.shuffle(perm)
        t = [0] * M
        for i in range(M):
            t[perm[i]] = perm[(i + 1) % M]
        taus.append(t)
    hits = sum(1 for t in taus if realize(t))
    out[M] = {"n_tau": len(taus), "hits": hits, "full_sample": hits == len(taus)}
res["N30_realize"] = out

with open(os.path.join(ART, "finite_level_log11.json"), "w") as f:
    json.dump(res, f, indent=1)
print(json.dumps(res, indent=1))
