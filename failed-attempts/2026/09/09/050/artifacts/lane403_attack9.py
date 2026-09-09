"""Lane-403 attack v9: universal-factor tower (2,6,30) pure + twisted search.

(a) Pure odo tower 2|6|30: single cycles + mod-coherence (exact).
(b) Twisted search: h30 = single within-fiber swap (fibers a%6, size 5);
    s30 = h30 o odo(30); count how many of the C(30,2)-restricted swaps
    (same-fiber swaps: 6*C(5,2)=60) keep single-30-cycle. Report examples.
(c) Sampled local orbit for one twisted + pure: random V (fiber-preserving
    perms, fibers size 5) of size S=6000; distinct conjugates, fraction that
    are single-30-cycle lifts of the level-2 pattern s6p.
(d) Rigidity probes (corrected convention): quotients fixed by s30^k.
(e) Eigenvalue-group shadow: odd-order quotient orders available at each
    level = divisors (2:{1}, 6:{1,3}, 30:{1,3,5,15}).
"""
import json, os, random, math

ART = os.path.dirname(os.path.abspath(__file__))
random.seed(309)
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

def proj_mod(p, N, M):
    q = []
    for b in range(M):
        imgs = {p[a] % M for a in range(N) if a % M == b}
        if len(imgs) != 1:
            return None
        q.append(next(iter(imgs)))
    return q

s2, s6, s30 = odo(2), odo(6), odo(30)
res["pure"] = {
    "single": [single(s2), single(s6), single(s30)],
    "coherence": [proj_mod(s30, 30, 6) == s6, proj_mod(s6, 6, 2) == s2],
}
res["quotient_orders"] = {
    N: [d for d in range(1, N + 1) if N % d == 0]
    for N in (2, 6, 30)
}

# (b) same-fiber swaps
swaps = []
for b in range(6):
    fib = [a for a in range(30) if a % 6 == b]
    for i in range(5):
        for j in range(i + 1, 5):
            swaps.append((fib[i], fib[j]))
res["n_same_fiber_swaps"] = len(swaps)
good = []
for (u, v) in swaps:
    h = list(range(30))
    h[u], h[v] = h[v], h[u]
    s = compose(h, s30)
    if single(s):
        good.append([u, v])
res["n_single_preserving"] = len(good)
res["examples"] = good[:8]

# (c) sampled local orbits
def random_fiber_perm():
    g = [0] * 30
    for b in range(6):
        fib = [a for a in range(30) if a % 6 == b]
        dst = fib[:]
        random.shuffle(dst)
        for a, c in zip(fib, dst):
            g[a] = c
    return g

for tag, base in (("pure", s30), ("twisted", None)):
    if tag == "twisted":
        if not good:
            res["sampled_twisted"] = {"note": "no good twists"}
            continue
        u, v = good[0]
        h = list(range(30))
        h[u], h[v] = h[v], h[u]
        base = compose(h, s30)
    loc = set()
    n_single_lift = 0
    tgt = proj_mod(base, 30, 6)
    for _ in range(6000):
        g = random_fiber_perm()
        c = tuple(conj(g, base))
        loc.add(c)
        if single(list(c)) and proj_mod(list(c), 30, 6) == tgt:
            n_single_lift += 1
    res[f"sampled_{tag}"] = {
        "V_samples": 6000,
        "distinct": len(loc),
        "single_lift_samples": n_single_lift,
        "base_projects": tgt,
    }

# (d) rigidity probes
def power(p, k):
    n = len(p)
    r = list(range(n))
    base = list(p)
    while k:
        if k & 1:
            r = compose(base, r)
        base = compose(base, base)
        k >>= 1
    return r

def fixes(pk, N, M):
    return all(pk[a] % M == a % M for a in range(N))

res["rigidity"] = {}
for k in [1, 2, 3, 5, 6, 10, 15, 30]:
    pk = power(s30, k)
    res["rigidity"][k] = [M for M in (2, 6, 30) if fixes(pk, 30, M)]

with open(os.path.join(ART, "finite_level_log9.json"), "w") as f:
    json.dump(res, f, indent=1)
print(json.dumps(res, indent=1))
