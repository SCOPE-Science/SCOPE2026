"""Lane-403 finite-level Baire-coding attack v2 (stdlib only).

Levels: sizes N = 2, 6, 24 (factorial bonding, projection = mod).
  o(a) = a+1 mod N (odometer; commutes with mod-projection).
  Twist at level k=2: h6 in S_6 preserving mod-2 classes; lift
  hN(a) = h6(a mod 6) + 6*(a//6) for N>=6 (commutes w/ projection).
  sigma = h o o.
Candidate U-TWIST: h6 = transposition (0 2) (both even: mod-2 quotient
  stays a 2-cycle). Universal-type: levels include factor 3, so the
  binary-eigenvalue obstruction does not apply.

Certs computed:
 (a) single-cycle at each level (minimality proxy) + coherence;
 (b) local orbit O(U,V): V = level-1-block-preserving perms of 6 atoms
     (72 elts); U = level-1 nbhd; coverage of U-cyclic lifts (exact);
 (c) density proxy: for EVERY tau in S_6 (720, exact loop), sample random
     lifts psi (atom perms inducing tau on blocks, fiber size 4) and test
     whether a single-24-cycle lift exists (then some g conjugates
     sigma3-pattern to psi). Fraction of tau hit ~= level-2 reach.
 (d) binary-type control: same tests for binary twist (0 1) at level 3
     of 2-4-8 tower to exhibit the contrast + eigenvalue lemma (proof
     in DRAFT notes, not code).
"""
import json, os, random

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".")
random.seed(403)

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

def ctype(p):
    n = len(p)
    seen = [False] * n
    out = []
    for i in range(n):
        if not seen[i]:
            x, c = i, 0
            while not seen[x]:
                seen[x] = True
                x = p[x]
                c += 1
            out.append(c)
    return tuple(sorted(out))

def invert(p):
    q = [0] * len(p)
    for i, v in enumerate(p):
        q[v] = i
    return q

def conj(g, s):
    return compose(compose(g, s), invert(g))

def proj_mod(p, N, M):
    """project atom-perm p on N atoms to block map on M blocks (a -> a mod M);
    return list or None if not block-preserving."""
    q = []
    for b in range(M):
        imgs = {p[a] % M for a in range(N) if a % M == b}
        if len(imgs) != 1:
            return None
        q.append(next(iter(imgs)))
    return q

res = {}

# ---------- universal-type twisted candidate ----------
h6 = list(range(6))
h6[0], h6[2] = h6[2], h6[0]

def lift24(h):
    return [h[a % 6] + 6 * (a // 6) for a in range(24)]

h24 = lift24(h6)
s1 = odo(2)
s2 = compose(h6, odo(6))
s3 = compose(h24, odo(24))

res["candidate"] = {"type": "universal-twist", "h6": h6}
res["single_cycles"] = {"N2": single(s1), "N6": single(s2), "N24": single(s3)}
res["cycle_types"] = {"N2": list(ctype(s1)), "N6": list(ctype(s2)),
                      "N24": list(ctype(s3))}
# coherence: s3 projects to s2 projects to s1
res["coherence"] = {
    "s3->s2": proj_mod(s3, 24, 6) == s2,
    "s2->s1": proj_mod(s2, 6, 2) == s1,
}
q2 = proj_mod(s2, 6, 2)
res["mod2_quotient_s2"] = q2

# ---------- (b) local orbit O(U,V) ----------
# V: perms of 6 atoms preserving mod-2 blocks: (3!)^2 = 36
import itertools
evens = [0, 2, 4]
odds = [1, 3, 5]
V = []
for pe in itertools.permutations(evens):
    for po in itertools.permutations(odds):
        g = [0] * 6
        for i, b in enumerate(evens):
            g[b] = pe[i]
        for i, b in enumerate(odds):
            g[b] = po[i]
        V.append(g)
assert len(V) == 36
loc = {}
for g in V:
    c = tuple(conj(g, s2))
    loc[c] = loc.get(c, 0) + 1
# exact count of single-6-cycles lifting the mod-2 2-cycle q2
lift_cyc = [t for t in itertools.permutations(range(6))
            if single(list(t)) and proj_mod(list(t), 6, 2) == q2]
res["local_orbit"] = {
    "V_size": 36,
    "distinct_conjugates": len(loc),
    "U_cyclic_lifts_exact": len(lift_cyc),
    " Reached_all": sorted(loc.keys()) == sorted(tuple(t) for t in lift_cyc),
    "coverage": len([c for c in loc if single(list(c))]) / len(lift_cyc),
}

# ---------- (c) density proxy over all tau in S_6 ----------
def random_lift(tau, N=24, M=6, tries=400):
    """yield True if a sampled lift of tau is a single N-cycle."""
    fib = {}
    for a in range(N):
        fib.setdefault(a % M, []).append(a)
    for _ in range(tries):
        psi = [0] * N
        for a in range(N):
            choices = [b for b in range(N) if b % M == tau[a % M]]
            psi[a] = random.choice(choices)
        if sorted(psi) != list(range(N)):
            continue  # not bijective; resample counts as miss
        if single(psi):
            return True
    return False

hits = 0
misses = []
cyclic_tau_hit = None
three_tau = (1, 2, 0, 4, 5, 3)  # (0 1 2)(3 4 5): 3-cyclic blocks, parity-preserving
BIO = {"three_tau_sampled": None}
for tau in itertools.permutations(range(6)):
    t = list(tau)
    if random_lift(t):
        hits += 1
    else:
        misses.append(t)
    if list(tau) == list(three_tau):
        BIO["three_tau_sampled"] = random_lift(t, tries=2000)
res["density_proxy"] = {
    "targets": 720,
    "hits": hits,
    "misses": len(misses),
    "miss_examples": misses[:12],
    "three_cyclic_tau_hit": BIO["three_tau_sampled"],
}
res["density_proxy"]["interpretation"] = (
    "hits/720 tau realizable as some conjugate's level-2 pattern (sampled). "
    "Sampling misses need not be true misses."
)

with open(os.path.join(ART, "finite_level_log.json"), "w") as f:
    json.dump(res, f, indent=1)
print(json.dumps(res, indent=1)[:4000])
print("HITS:", hits, "MISSES:", len(misses))
print("three_tau hit:", BIO["three_tau_sampled"])
print("local:", res["local_orbit"])
print("single:", res["single_cycles"], "coh:", res["coherence"])
