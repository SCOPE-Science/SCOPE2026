"""Lane-403 finite-level Baire-coding attack (stdlib only).

Model: X = {0,1}^N, atoms of P_n = ints 0..2^n-1.
phi0 = binary odometer: a -> a+1 mod 2^n.
Twist h = level-m prefix permutation; sigma* = h o phi0 (apply phi0 then h).
Certs: single-cycle (minimality proxy), off-universal discussed in DRAFT;
density proxy: match cyclic targets; obstruction: 3-factor targets unmatched;
local orbit O(U,V) at levels 2-3 with V = P_2-preserving perms (16 elts).
"""
import json, itertools, os

OUT = os.path.join(os.path.dirname(__file__), ".")
os.makedirs(OUT, exist_ok=True)

def compose(p, q):
    """return p o q : apply q then p. perms as lists."""
    return [p[q[i]] for i in range(len(q))]

def odometer(n):
    N = 2 ** n
    return [(a + 1) % N for a in range(N)]

def is_single_cycle(p):
    N = len(p)
    seen = [False] * N
    x, c = 0, 0
    while not seen[x]:
        seen[x] = True
        x = p[x]
        c += 1
    return c == N

def cycle_type(p):
    N = len(p)
    seen = [False] * N
    lens = []
    for i in range(N):
        if not seen[i]:
            x, c = i, 0
            while not seen[x]:
                seen[x] = True
                x = p[x]
                c += 1
            lens.append(c)
    return tuple(sorted(lens))

def perm_parity(p):
    n = len(p)
    seen = [False] * n
    trans = 0
    for i in range(n):
        if not seen[i]:
            x, c = i, 0
            while not seen[x]:
                seen[x] = True
                x = p[x]
                c += 1
            trans += c - 1
    return trans % 2

def h_at_factory(m, swaps):
    def h_at(n):
        N = 2 ** n
        h = list(range(N))
        if n < m:
            return h
        shift = n - m
        mp = {}
        for (u, v) in swaps:
            mp[u] = v
            mp[v] = u
        for a in range(N):
            block = a >> shift
            sub = a & ((1 << shift) - 1) if shift else 0
            nb = mp.get(block, block)
            h[a] = (nb << shift) | sub
        return h
    return h_at

# Candidate: swap level-3 blocks 0<->1 (both under L2 atom 0), keeps L2 4-cycle.
M_LEVEL = 3
SWAPS = [(0, 1)]
h_at = h_at_factory(M_LEVEL, SWAPS)

res = {"candidate": {"m": M_LEVEL, "swaps": SWAPS}, "levels": {}}
for n in range(1, 9):
    N = 2 ** n
    o = odometer(n)
    h = h_at(n)
    s = compose(h, o)
    ct = cycle_type(s)
    res["levels"][n] = {
        "N": N,
        "single_cycle": is_single_cycle(s),
        "cycle_type": list(ct),
        "parity": perm_parity(s),
    }

# coherence: sigma_{n+1} projects to sigma_n
coh = True
for n in range(1, 8):
    o1 = compose(h_at(n + 1), odometer(n + 1))
    o0 = compose(h_at(n), odometer(n))
    for a in range(2 ** (n + 1)):
        if (o1[a] >> 1) != o0[a >> 1]:
            coh = False
res["coherent_projections"] = coh

s2 = compose(h_at(2), odometer(2))
res["sigma_mod_P2"] = s2

n = 3
N = 8
sig3 = compose(h_at(3), odometer(3))
Vs = []
for mask in range(16):
    g = list(range(8))
    for b in range(4):
        if (mask >> b) & 1:
            g[2 * b], g[2 * b + 1] = g[2 * b + 1], g[2 * b]
    Vs.append(g)

def invert(p):
    q = [0] * len(p)
    for i, v in enumerate(p):
        q[v] = i
    return q

def conj(g, s):
    gi = invert(g)
    return compose(compose(g, s), gi)

loc_orbit = {}
for g in Vs:
    c = tuple(conj(g, sig3))
    loc_orbit[c] = loc_orbit.get(c, 0) + 1
res["local_orbit"] = {
    "V_size": len(Vs),
    "distinct_conjugates": len(loc_orbit),
    "all_single_cycles": all(is_single_cycle(list(c)) for c in loc_orbit),
    "in_U_all": all(
        all((list(c)[a] >> 1) == (s2[a >> 1]) for a in range(8))
        for c in loc_orbit
    ),
}

count_lift = 0
for entries in itertools.product(range(8), repeat=8):
    if sorted(entries) != list(range(8)):
        continue
    ok = all((entries[a] >> 1) == s2[a >> 1] for a in range(8))
    if not ok:
        continue
    if is_single_cycle(list(entries)):
        count_lift += 1
res["U_cyclic_lifts"] = {
    "count": count_lift,
    "local_orbit_covers": len(loc_orbit),
    "coverage_fraction": len(loc_orbit) / count_lift if count_lift else None,
}
reached_cyc = [c for c in loc_orbit
               if is_single_cycle(list(c)) and
               all((list(c)[a] >> 1) == s2[a >> 1] for a in range(8))]
res["U_cyclic_lifts"]["unreached"] = count_lift - len(reached_cyc)

tau = [1, 2, 0, 4, 5, 3, 6, 7]
res["obstruction"] = {
    "tau_cycle_type": list(cycle_type(tau)),
    "sigma3_cycle_type": list(cycle_type(sig3)),
    "conjugate_possible": sorted(cycle_type(tau)) == sorted(cycle_type(sig3)),
    "interpretation": "No g in Homeo(X) can send sig3-pattern to tau-pattern: "
    "cycle type is a conjugacy invariant. Hence H.phi* misses the basic open "
    "set of maps with a cyclic 3-partition, so H.phi* is NOT dense in M.",
}

import random
random.seed(403)
def find_conjugator(s, t):
    N = len(s)
    def order(p):
        out, x = [], 0
        for _ in range(N):
            out.append(x)
            x = p[x]
        return out
    os_, ot = order(s), order(t)
    g = [0] * N
    for i in range(N):
        g[os_[i]] = ot[i]
    return g

NN = 16
sig4 = compose(h_at(4), odometer(4))
perm = list(range(NN))
random.shuffle(perm)
t = [0] * NN
for i in range(NN):
    t[perm[i]] = perm[(i + 1) % NN]
g = find_conjugator(sig4, t)
assert tuple(conj(g, sig4)) == tuple(t)
res["cyclic_match_level4"] = {"ok": True, "N": NN}

with open(os.path.join(OUT, "finite_level_log.json"), "w") as f:
    json.dump(res, f, indent=1)
print(json.dumps(res, indent=1))
