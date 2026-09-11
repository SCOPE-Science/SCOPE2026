"""Bounded preset-fallback attempt (lane-719): construct dihedral quantum Tanner
Q0 with n0 in [400,600] (D_50, Delta=3 -> n=450), log HX,HZ, and attempt the
exact-distance certificate: exhaustive no-logical scan to weight 4,
randomized probe at weights 5-7, heuristic upper-bound (explicit logical) search.
Pure stdlib. Run: python3 fallback_attempt.py  (cwd = this dir)
"""
import json, math, random, time, itertools, sys

M = 50            # D_M has order 2M = 100
N_G = 2 * M
DELTA = 3

def mul(a, b):
    xa, pa = a % M, a // M
    xb, pb = b % M, b // M
    if pa == 0 and pb == 0:
        return (xa + xb) % M
    if pa == 0:
        return M + ((xb - xa) % M)
    if pb == 0:
        return M + ((xa + xb) % M)
    return (xb - xa) % M

def inv(a):
    x, p = a % M, a // M
    if p == 0:
        return (-x) % M
    return a  # reflections are involutions

R = lambda k: (k % M)          # r^k
S = lambda k: M + (k % M)      # s r^k

A = [R(1), R(-1), S(0)]
B_CANDS = [[R(2), R(-2), S(1)], [R(3), R(-3), S(1)], [R(2), R(-2), S(3)],
           [R(4), R(-4), S(1)], [R(3), R(-3), S(5)]]

def check_tnc(A, B):
    for a in A:
        for b in B:
            for g in range(N_G):
                if mul(a, g) == mul(g, b):
                    return False
    return True

def generates(A, B):
    seen = {0}
    stack = [0]
    gens = A + B
    while stack:
        g = stack.pop()
        for h in gens:
            for gg in (mul(g, h), mul(h, g)):
                if gg not in seen:
                    seen.add(gg)
                    stack.append(gg)
    return len(seen) == N_G

B = None
for cand in B_CANDS:
    if check_tnc(A, cand) and generates(A, cand):
        B = cand
        break
assert B is not None, "no TNC generator pair found"
print("A =", A, "B =", B, "TNC ok, generates ok", flush=True)

AI = {a: i for i, a in enumerate(A)}
BI = {b: i for i, b in enumerate(B)}

def face_key(g, a, b):
    ag = mul(a, g)
    gb = mul(g, b)
    agb = mul(a, gb)
    return frozenset((g, 100 + ag, 100 + gb, agb))

facemap = {}
faces = []
for g in range(N_G):
    for a in A:
        for b in B:
            k = face_key(g, a, b)
            if k not in facemap:
                facemap[k] = len(faces)
                faces.append(k)
n = len(faces)
print("nfaces =", n, flush=True)

inc0 = {g: [] for g in range(N_G)}   # V0 vertex g -> face ids
inc1 = {g: [] for g in range(N_G)}   # V1 vertex g -> face ids
for fi, k in enumerate(faces):
    for v in k:
        if v < 100:
            inc0[v].append(fi)
        else:
            inc1[v - 100].append(fi)
assert all(len(v) == 9 for v in inc0.values()), "V0 degree != 9"
assert all(len(v) == 9 for v in inc1.values()), "V1 degree != 9"

def phi0(g, a, b):
    return facemap[face_key(g, a, b)]

def phi1(g, a, b):
    return facemap[face_key(mul(inv(a), g), a, b)]

# verify phi1 lands on v1=g and is bijective per vertex
for g in range(N_G):
    imgs = [phi1(g, a, b) for a in A for b in B]
    assert len(set(imgs)) == 9, f"phi1 not bijective at {g}"
    assert all(fi in inc1[g] for fi in imgs), f"phi1 incidence fail at {g}"

# local codes: CA=[3,2,2] SPC rows u1=[1,0,1],u2=[0,1,1]; CB=[3,1,3] rep v=[1,1,1]
# C0 = CA x CB basis (A-outer order): r1=[1,1,1,0,0,0,1,1,1], r2=[0,0,0,1,1,1,1,1,1]
# C1 = CA^perp x CB^perp: c=[1,1,1], d1=[1,0,1],d2=[0,1,1] -> s1=[1,0,1]*3, s2=[0,1,1]*3
C0 = [[1,1,1,0,0,0,1,1,1],[0,0,0,1,1,1,1,1,1]]
C1 = [[1,0,1,1,0,1,1,0,1],[0,1,1,0,1,1,0,1,1]]
AB = [(a, b) for a in A for b in B]

HZ, HX = [], []
for g in range(N_G):
    for beta in C0:
        e = 0
        for (a, b), bit in zip(AB, beta):
            if bit:
                e |= (1 << phi0(g, a, b))
        HZ.append(e)
for g in range(N_G):
    for beta in C1:
        e = 0
        for (a, b), bit in zip(AB, beta):
            if bit:
                e |= (1 << phi1(g, a, b))
        HX.append(e)

def wt(e):
    return bin(e).count("1")

def css_ok(HX, HZ):
    for r in HX:
        for s in HZ:
            if wt(r & s) % 2:
                return False
    return True

print("CSS orthogonal:", css_ok(HX, HZ), "rows:", len(HX), len(HZ),
      "maxwt:", max(map(wt, HX)), max(map(wt, HZ)), flush=True)
assert css_ok(HX, HZ), "CSS construction invalid"

def gf2_rank(rows):
    pivs = {}
    for r in rows:
        while r:
            p = r.bit_length() - 1
            if p in pivs:
                r ^= pivs[p]
            else:
                pivs[p] = r
                break
    return len(pivs), pivs

def in_rowspace(stab_rows, stab_rank, e):
    pivs = {}
    for r in stab_rows:
        while r:
            p = r.bit_length() - 1
            if p in pivs:
                r ^= pivs[p]
            else:
                pivs[p] = r
                break
    # rank with e appended exceeds rank iff e not in span
    r = e
    while r:
        p = r.bit_length() - 1
        if p in pivs:
            r ^= pivs[p]
        else:
            return False
    return True

rx, _ = gf2_rank(list(HX))
rz, _ = gf2_rank(list(HZ))
k = n - rx - rz
print(f"rankX={rx} rankZ={rz} n={n} k={k} rate={k/n:.4f} (need >=0.125)", flush=True)

def columns(Hrows, m, n):
    cols = [0] * n
    for i, r in enumerate(Hrows):
        rr = r
        while rr:
            lsb = rr & (-rr)
            j = lsb.bit_length() - 1
            cols[j] |= (1 << i)
            rr ^= lsb
    return cols

def low_weight_ker(cols, n, wmax=4, cap=2000000):
    """Exhaustive ker(H) vectors of weight<=wmax via column grouping (w<=4)."""
    found = set()
    byval = {}
    for j, c in enumerate(cols):
        byval.setdefault(c, []).append(j)
    for c, js in byval.items():
        if c == 0:
            for j in js:
                found.add((j,))
    # weight 2: equal nonzero columns
    for c, js in byval.items():
        if c != 0 and len(js) >= 2:
            for i, j in itertools.combinations(js, 2):
                found.add((i, j))
    if wmax >= 3:
        pairs = list(itertools.combinations(range(n), 2))
        for i, j in pairs:
            x = cols[i] ^ cols[j]
            if x in byval:
                for t in byval[x]:
                    if t != i and t != j:
                        found.add(tuple(sorted((i, j, t))))
    if wmax >= 4:
        pairxor = {}
        for i, j in pairs:
            pairxor.setdefault(cols[i] ^ cols[j], []).append((i, j))
        for x, L in pairxor.items():
            if len(L) >= 2:
                if len(L) > 4000:
                    return found, True  # aborted: group explosion
                for (i, j), (t, u) in itertools.combinations(L, 2):
                    if len({i, j, t, u}) == 4:
                        found.add(tuple(sorted((i, j, t, u))))
    return found, False

def scan_side(name, Hker, Hstab, n):
    t0 = time.time()
    rk, _ = gf2_rank(list(Hstab))
    cols = columns(Hker, len(Hker), n)
    found, aborted = low_weight_ker(cols, n, 4)
    logicals = []
    stab_hits = 0
    for tup in found:
        e = 0
        for j in tup:
            e |= (1 << j)
        if not in_rowspace(list(Hstab), rk, e):
            logicals.append([len(tup), sorted(tup)])
        else:
            stab_hits += 1
    dt = time.time() - t0
    logicals.sort()
    return {"n_ker_le4": len(found), "aborted": aborted,
            "stabilizer_hits": stab_hits, "logicals_le4": logicals,
            "scan_seconds": round(dt, 1)}

t0 = time.time()
print("--- exhaustive no-logical scan to weight 4 (X side: ker HZ / row HX) ---", flush=True)
sx = scan_side("X", HZ, HX, n)
print(json.dumps(sx), flush=True)
print("--- exhaustive no-logical scan to weight 4 (Z side: ker HX / row HZ) ---", flush=True)
sz = scan_side("Z", HX, HZ, n)
print(json.dumps(sz), flush=True)

# counts: certification cost to weights 5,6,7
costs = {w: math.comb(n, w) for w in (5, 6, 7)}
print("comb counts w=5..7:", {w: f"{c:.3e}" for w, c in costs.items()}, flush=True)

# bounded randomized probe at weights 5,6,7: random support -> syndrome test -> membership
def rand_probe(Hker, Hstab, n, w, trials, seed):
    rng = random.Random(seed)
    cols = columns(Hker, len(Hker), n)
    rk, _ = gf2_rank(list(Hstab))
    ker_hits = 0
    logical_hit = None
    for _ in range(trials):
        sup = rng.sample(range(n), w)
        s = 0
        for j in sup:
            s ^= cols[j]
        if s == 0:
            ker_hits += 1
            e = 0
            for j in sup:
                e |= (1 << j)
            if not in_rowspace(list(Hstab), rk, e):
                logical_hit = sorted(sup)
                break
    return {"w": w, "trials": trials, "ker_hits": ker_hits, "logical_hit": logical_hit}

for w in (5, 6, 7):
    px = rand_probe(HZ, HX, n, w, 200000, 1000 + w)
    pz = rand_probe(HX, HZ, n, w, 200000, 2000 + w)
    print(f"probe X w={w}:", json.dumps(px), flush=True)
    print(f"probe Z w={w}:", json.dumps(pz), flush=True)

# heuristic upper bound: random nullspace codeword + greedy stabilizer reduction
def nullbasis(Hrows, n):
    _, pivs = gf2_rank(list(Hrows))
    pivset = set(pivs)
    free = [c for c in range(n) if c not in pivset]
    basis = []
    order = sorted(pivs, reverse=True)
    for f in free:
        v = 1 << f
        for p in order:
            if (v >> p) & 1:
                v ^= pivs[p]
        basis.append(v)
    return basis

def greedy_reduce(e, stab_rows, rounds=6, seed=0):
    rng = random.Random(seed)
    rows = list(stab_rows)
    for _ in range(rounds):
        rng.shuffle(rows)
        improved = False
        for r in rows:
            if wt(e ^ r) < wt(e):
                e ^= r
                improved = True
        if not improved:
            break
    return e

def heuristic(Hker, Hstab, n, trials, seed):
    rng = random.Random(seed)
    nb = nullbasis(Hker, n)
    rk, _ = gf2_rank(list(Hstab))
    best = None
    for t in range(trials):
        e = 0
        for v in nb:
            if rng.random() < 0.5:
                e ^= v
        if e == 0:
            continue
        e = greedy_reduce(e, Hstab, seed=seed + t)
        w = wt(e)
        if best is None or w < best[0]:
            if not in_rowspace(list(Hstab), rk, e):
                best = (w, e)
    if best is None:
        return {"best_w": None, "support": None}
    w, e = best
    sup = [j for j in range(n) if (e >> j) & 1]
    return {"best_w": w, "support": sup}

hx_up = heuristic(HZ, HX, n, 120, 7)
hz_up = heuristic(HX, HZ, n, 120, 8)
print("heuristic X-logical:", json.dumps({k: (v if k != "support" else v) for k, v in hx_up.items()}), flush=True)
print("heuristic Z-logical:", json.dumps({k: (v if k != "support" else v) for k, v in hz_up.items()}), flush=True)
print("total_seconds:", round(time.time() - t0, 1), flush=True)

out = {"group": "D_50", "A": A, "B": B, "n": n, "Delta": DELTA,
       "rankX": rx, "rankZ": rz, "k": k, "rate": k / n,
       "scanX": sx, "scanZ": sz,
       "comb_counts": {str(w): c for w, c in costs.items()},
       "heuristic_X": hx_up, "heuristic_Z": hz_up}
with open("fallback_attempt_summary.json", "w") as f:
    json.dump(out, f)
def tohex(rows):
    return [hex(r) for r in rows]
with open("Q0_matrices.json", "w") as f:
    json.dump({"n": n, "HX": tohex(HX), "HZ": tohex(HZ)}, f)
print("saved fallback_attempt_summary.json + Q0_matrices.json", flush=True)
