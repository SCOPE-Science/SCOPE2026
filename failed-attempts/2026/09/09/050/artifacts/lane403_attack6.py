"""Lane-403 attack v6: pure binary tower corrections + local density (target phase).

Binary tower N = 2^n, mod-projection (coherent). Checks:
 (B1) single cycles + coherence at all levels 1..12.
 (B2) no cyclic quotient of order 3 (or any odd m): quotient order | 2^n.
      Exact: enumerate divisors; odd divisors of 2^n = {1} only.
 (B3) local O(U,V) at level 3: V = perms of 8 atoms preserving mod-4 blocks
      (fibers size 2 -> |V| = 2^4 = 16). U = level-2 nbhd (pattern = +1 mod 4).
      Exact count of U-cyclic lifts + coverage by V-orbit.
 (U1) twisted universal-type (levels 2,6 tower, mod proj): among the 12
      parity-preserving single-cycle twists (recomputed), pick first with
      N24-lift single; local O(U,V) coverage at level 2 (V = 36).
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

def proj_mod(p, N, M):
    q = []
    for b in range(M):
        imgs = {p[a] % M for a in range(N) if a % M == b}
        if len(imgs) != 1:
            return None
        q.append(next(iter(imgs)))
    return q

# ---- B1 ----
sig = {n: odo(2 ** n) for n in range(1, 13)}
res["B1_single"] = {n: single(sig[n]) for n in range(1, 13)}
coh = True
for n in range(1, 12):
    for a in range(2 ** (n + 1)):
        if (sig[n + 1][a] % (2 ** n)) != sig[n][a % (2 ** n)]:
            coh = False
res["B1_coherent_mod"] = coh

# ---- B2: odd-order cyclic quotients impossible ----
import math
res["B2"] = {
    "odd_divisors_of_2n": {n: [d for d in range(1, 2 ** n + 1)
                               if (2 ** n) % d == 0 and d % 2 == 1]
                           for n in range(1, 9)},
    "lemma": "A cyclic quotient of a single 2^n-cycle has order dividing 2^n, "
             "hence no odd-order (>1) cyclic quotient at any binary level. "
             "Dynamical lift: binary odometer has no 3-cyclic clopen partition "
             "(eigenvalue e^{2pi i/3} absent); its H-orbit misses every basic "
             "open requiring a 3-factor. Corrigendum: v5's 24-atom 'U3 witness' "
             "used the 2-6-24 tower (a 3-factor odometer), NOT the binary tower, "
             "so it did not witness a binary-level open; the valid finite shadow "
             "is the divisor fact + 2^n mod 3 table (log4).",
}

# ---- B3: local orbit level 3 binary ----
s2 = sig[2]  # +1 mod 4
s3 = sig[3]  # +1 mod 8
V = []
for mask in range(16):
    g = list(range(8))
    for b in range(4):
        if (mask >> b) & 1:
            # swap fiber {a: a%4==b} = {b, b+4}
            g[b], g[b + 4] = g[b + 4], g[b]
    V.append(g)
assert len({tuple(g) for g in V}) == 16
loc = {}
for g in V:
    c = tuple(conj(g, s3))
    loc[c] = loc.get(c, 0) + 1
lifts = [t for t in itertools.permutations(range(8))
         if single(list(t)) and proj_mod(list(t), 8, 4) == s2]
hit = set(tuple(t) for t in lifts) & set(loc)
res["B3_local"] = {
    "V_size": 16,
    "distinct_conjugates": len(loc),
    "all_conj_single_cycles": all(single(list(c)) for c in loc),
    "all_conj_in_U": all(proj_mod(list(c), 8, 4) == s2 for c in loc),
    "U_cyclic_lifts": len(lifts),
    "covered": len(hit),
    "coverage": len(hit) / len(lifts),
}

# ---- U1: twisted universal-type local coverage ----
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
            h24 = [h[a % 6] + 6 * (a // 6) for a in range(24)]
            if single(compose(h24, odo(24))):
                good.append(h)
res["U1_candidates"] = len(good)
h = good[0]
su = compose(h, odo(6))
qbar = proj_mod(su, 6, 2)
Vu = []
for pe in itertools.permutations(evens):
    for po in itertools.permutations(odds):
        g = [0] * 6
        for i, b in enumerate(evens):
            g[b] = pe[i]
        for i, b in enumerate(odds):
            g[b] = po[i]
        Vu.append(g)
locu = set(tuple(conj(g, su)) for g in Vu)
liftsu = [t for t in itertools.permutations(range(6))
          if single(list(t)) and proj_mod(list(t), 6, 2) == qbar]
hitu = set(tuple(t) for t in liftsu) & locu
res["U1_local"] = {
    "h6": h,
    "V_size": len(Vu),
    "distinct": len(locu),
    "U_cyclic_lifts": len(liftsu),
    "covered": len(hitu),
    "coverage": len(hitu) / len(liftsu),
    "covers_all": set(tuple(t) for t in liftsu) <= locu,
}

with open(os.path.join(ART, "finite_level_log6.json"), "w") as f:
    json.dump(res, f, indent=1)
print(json.dumps(res, indent=1))
