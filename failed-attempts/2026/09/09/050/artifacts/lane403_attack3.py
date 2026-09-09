"""Lane-403 attack v3: pure/universal-type odometers + exact density sampling.

Fixes v2 bugs: (i) search parity-preserving twists for single-cycle;
(ii) sample random BIJECTIONS lifting tau (fiber-wise perms), not maps.
Tower: N = 2, 6, 24 with mod-projection; odo = +1 mod N.
"""
import json, os, random, itertools

ART = os.path.dirname(os.path.abspath(__file__))
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
    q = []
    for b in range(M):
        imgs = {p[a] % M for a in range(N) if a % M == b}
        if len(imgs) != 1:
            return None
        q.append(next(iter(imgs)))
    return q

res = {}

# ---- (1) twist search: parity-preserving h in S6, s = h o odo(6) ----
evens = [0, 2, 4]
odds = [1, 3, 5]
good = []
for pe in itertools.permutations(evens):
    for po in itertools.permutations(odds):
        h = [0] * 6
        for i, b in enumerate(evens):
            h[b] = pe[i]
        for i, b in enumerate(odds):
            h[b] = po[i]
        s = compose(h, odo(6))
        if single(s):
            # lift to 24
            h24 = [h[a % 6] + 6 * (a // 6) for a in range(24)]
            s24 = compose(h24, odo(24))
            good.append({"h6": h, "N24_single": single(s24),
                         "N24_ctype": list(ctype(s24))})
res["twist_search"] = {"n_h": 36, "n_single_at_6": len(good),
                       "examples": good[:6]}

# ---- (2) pure odometer candidate: h = id ----
h6 = list(range(6))
h24 = list(range(24))
s1, s2, s3 = odo(2), compose(h6, odo(6)), compose(h24, odo(24))
res["pure"] = {
    "single": [single(s1), single(s2), single(s3)],
    "coherence": [proj_mod(s3, 24, 6) == s2, proj_mod(s2, 6, 2) == s1],
}
qbar = proj_mod(s2, 6, 2)

# ---- (3) local orbit O(U,V): V = 36 block-preserving perms ----
V = []
for pe in itertools.permutations(evens):
    for po in itertools.permutations(odds):
        g = [0] * 6
        for i, b in enumerate(evens):
            g[b] = pe[i]
        for i, b in enumerate(odds):
            g[b] = po[i]
        V.append(g)
loc = set(tuple(conj(g, s2)) for g in V)
lifts = [t for t in itertools.permutations(range(6))
         if single(list(t)) and proj_mod(list(t), 6, 2) == qbar]
res["local_orbit_pure"] = {
    "V_size": len(V),
    "distinct": len(loc),
    "U_cyclic_lifts": len(lifts),
    "covers_all": set(tuple(t) for t in lifts) <= loc,
    "coverage": len(set(tuple(t) for t in lifts) & loc) / len(lifts),
}

# ---- (4) exact density sampling: random bijections lifting tau ----
def random_bijection_lift(tau, N=24, M=6):
    tau = list(tau)
    # for each block b, bijection fiber(b) -> fiber(tau(b))
    psi = [0] * N
    for b in range(M):
        src = [a for a in range(N) if a % M == b]
        dst = [c for c in range(N) if c % M == tau[b]]
        random.shuffle(dst)
        for a, c in zip(src, dst):
            psi[a] = c
    return psi

def tau_hit(tau, tries=300):
    for _ in range(tries):
        if single(random_bijection_lift(tau)):
            return True
    return False

six_cycles = [t for t in itertools.permutations(range(6)) if len(
    [c for c in [0] if False]) == 0 and __import__('math').gcd(0, 1) == 1]
# proper 6-cycle test:
def is_6cycle(t):
    x, seen = 0, set()
    for _ in range(6):
        if x in seen:
            return False
        seen.add(x)
        x = t[x]
    return x == 0
six_cycles = [t for t in itertools.permutations(range(6)) if is_6cycle(t)]
res["n_6cycles"] = len(six_cycles)
hits = sum(1 for t in six_cycles if tau_hit(t, tries=200))
res["density_proxy_6cycles"] = {"targets": len(six_cycles), "hits": hits,
                                "hit_rate": hits / len(six_cycles)}
# non-6-cycle tau can NEVER be hit (projection lemma) — verify count
res["projection_lemma"] = ("If psi on 24 atoms is a single cycle lifting tau "
                           "on 6 blocks, tau is a single 6-cycle.")

# ---- (5) rigidity check: odo(24)^{12}, ^{8} distances from id ----
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
def dist_id(p):
    n = len(p)
    return sum(1 for i in range(n) if p[i] != i) / n
res["rigidity"] = {
    "d(s3^12,id)": dist_id(power(s3, 12)),
    "d(s3^8,id)": dist_id(power(s3, 8)),
    "d(s3^6,id)": dist_id(power(s3, 6)),
}

with open(os.path.join(ART, "finite_level_log3.json"), "w") as f:
    json.dump(res, f, indent=1)
print(json.dumps(res, indent=1))
