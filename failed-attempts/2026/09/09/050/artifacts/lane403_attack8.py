"""Lane-403 attack v8: level-4 local orbit O(U,V) exact (target phase).

U = level-3 nbhd of binary odometer (pattern s3 = +1 mod 8).
Lifts psi on 16 atoms with psi(a)%8 == s3(a%8): 2^16 candidates; filter
bijective + single-16-cycle. V = perms of 16 atoms preserving mod-8 blocks
(fibers {b,b+8}, |V| = 2^8 = 256). Local orbit = {g s4 g^-1 : g in V},
s4 = +1 mod 16. Coverage of U-cyclic lifts by local orbit: exact Hjorth
local-density shadow at levels 3->4.
"""
import json, os, itertools

ART = os.path.dirname(os.path.abspath(__file__))
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

s3 = odo(8)
s4 = odo(16)

# enumerate lifts: psi(a) = s3(a%8) + 8*e_a, e_a in {0,1}
lifts = []
for mask in range(2 ** 16):
    psi = [(a % 8 + 1) % 8 + 8 * ((mask >> a) & 1) for a in range(16)]
    if sorted(psi) != list(range(16)):
        continue
    if single(psi):
        lifts.append(tuple(psi))
res["U_cyclic_lifts_count"] = len(lifts)

# V-orbit
V = []
for mask in range(2 ** 8):
    g = list(range(16))
    for b in range(8):
        if (mask >> b) & 1:
            g[b], g[b + 8] = g[b + 8], g[b]
    V.append(g)
loc = set(tuple(conj(g, s4)) for g in V)
res["V_size"] = len(V)
res["distinct_conjugates"] = len(loc)
res["all_conj_in_U"] = all(
    all((c[a] % 8) == ((a % 8 + 1) % 8) for a in range(16)) for c in loc)
res["all_conj_single"] = all(single(list(c)) for c in loc)
hit = set(lifts) & loc
res["covered"] = len(hit)
res["coverage"] = len(hit) / len(lifts) if lifts else None
res["covers_all"] = set(lifts) <= loc
res["example_unreached"] = next(iter(set(lifts) - loc), None)

with open(os.path.join(ART, "finite_level_log8.json"), "w") as f:
    json.dump(res, f, indent=1)
print(json.dumps(res, indent=1))
