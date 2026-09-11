"""Bounded fallback attempt #2 (lane-719): Delta=5 dihedral Tanner Q0 at n0=400
(G=D_16, n=25*32/2=400), CA=[5,1,5] rep, CB=[5,4,2] SPC -> (dA,dB)=(5,2).
Goal per exact criterion: rate>=1/8, no logical of weight<8, explicit wt-d0 logical.
Fast checks: TNC pair search, CSS build, rank/rate, exhaustive ker-scan to
weight 4 (column grouping), randomized probes at 5-7, greedy upper bound.
Pure stdlib.
"""
import json, math, random, time, itertools

M = 16
N_G = 2 * M
DELTA = 5

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
    return (-x) % M if p == 0 else a

R = lambda k: (k % M)
S = lambda k: M + (k % M)
rots = [R(k) for k in range(M)]
refs = [S(k) for k in range(M)]

def sym5_sets(pool):
    # inverse-closed 5-sets: pairs {r^k,r^-k} + one involution (r^8 or a reflection)
    invs = [R(8)] + refs
    pairs = []
    seen = set()
    for k in range(1, M):
        a, b = R(k), R(-k)
        if a == b or frozenset((a, b)) in seen:
            continue
        seen.add(frozenset((a, b)))
        pairs.append((a, b))
    out = []
    L = len(pairs)
    for i in range(L):
        for j in range(i + 1, L):
            for v in invs:
                s = frozenset((pairs[i][0], pairs[i][1], pairs[j][0], pairs[j][1], v))
                if len(s) == 5:
                    out.append(sorted(s))
    # dedup
    u = []
    seen2 = set()
    for s in out:
        t = tuple(s)
        if t not in seen2:
            seen2.add(t)
            u.append(s)
    return u

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
    gens = list(A) + list(B)
    while stack:
        g = stack.pop()
        for h in gens:
            for gg in (mul(g, h), mul(h, g)):
                if gg not in seen:
                    seen.add(gg)
                    stack.append(gg)
    return len(seen) == N_G

cands = sym5_sets(None)
print("symmetric 5-sets:", len(cands), flush=True)
random.Random(0).shuffle(cands)
A = B = None
tried = 0
for i, Ca in enumerate(cands):
    for Cb in cands[i + 1:]:
        tried += 1
        if check_tnc(Ca, Cb) and generates(Ca, Cb):
            A, B = Ca, Cb
            break
    if A is not None or tried > 4000:
        break
assert A is not None, "no TNC Delta=5 pair found in budget"
print("A =", A, "B =", B, "tried", tried, flush=True)

AI = {a: i for i, a in enumerate(A)}
BI = {b: i for i, b in enumerate(B)}

def face_key(g, a, b):
    ag = mul(a, g)
    gb = mul(g, b)
    agb = mul(a, gb)
    return frozenset((g, 1000 + ag, 1000 + gb, agb))

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
inc0 = {g: [] for g in range(N_G)}
inc1 = {g: [] for g in range(N_G)}
for fi, k in enumerate(faces):
    for v in k:
        (inc0 if v < 1000 else inc1)[v if v < 1000 else v - 1000].append(fi)
assert all(len(v) == 25 for v in inc0.values())
assert all(len(v) == 25 for v in inc1.values())

def phi0(g, a, b):
    return facemap[face_key(g, a, b)]

def phi1(g, a, b):
    return facemap[face_key(mul(inv(a), g), a, b)]

for g in range(N_G):
    imgs = [phi1(g, a, b) for a in A for b in B]
    assert len(set(imgs)) == 25 and all(fi in inc1[g] for fi in imgs)

# CA=[5,1,5] rep u=[1]*5 ; CB=[5,4,2] SPC checks e_i+e_4. C0=CA x CB: 4 gens u x v_j
u = [1, 1, 1, 1, 1]
V = [[1, 0, 0, 0, 1], [0, 1, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
C0 = [[uu * vv for uu in u for vv in v] for v in V]  # outer A-major? fix order below
AB = [(a, b) for a in A for b in B]
# C0 gen (i,j): bit = u_i * v_j
C0 = [[[u[AI[a]] * v[BI[b]] for (a, b) in AB] for v in V]][0]
# C1 = CA^perp x CB^perp: CA^perp = SPC checks W (4 vectors wt2), CB^perp = rep w=[1]*5
W = [[1, 1, 0, 0, 0], [1, 0, 1, 0, 0], [1, 0, 0, 1, 0], [1, 0, 0, 0, 1]]
w = [1, 1, 1, 1, 1]
C1 = [[W_[AI[a]] * w[BI[b]] for (a, b) in AB] for W_ in W]

def wt(e):
    return bin(e).count("1")

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

ok = all(wt(r & s) % 2 == 0 for r in HX for s in HZ)
print("CSS orthogonal:", ok, "rows:", len(HX), len(HZ),
      "genwt range:", min(map(wt, HZ)), max(map(wt, HZ)), min(map(wt, HX)), max(map(wt, HX)), flush=True)
assert ok

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
    return len(pivs)

def in_rowspace(stab_rows, e):
    pivs = {}
    for r in stab_rows:
        while r:
            p = r.bit_length() - 1
            if p in pivs:
                r ^= pivs[p]
            else:
                pivs[p] = r
                break
    r = e
    while r:
        p = r.bit_length() - 1
        if p in pivs:
            r ^= pivs[p]
        else:
            return False
    return True

rx, rz = gf2_rank(list(HX)), gf2_rank(list(HZ))
k = n - rx - rz
print(f"rankX={rx} rankZ={rz} n={n} k={k} rate={k/n:.4f} (need >=0.125)", flush=True)

def columns(Hrows, n):
    cols = [0] * n
    for i, r in enumerate(Hrows):
        rr = r
        while rr:
            lsb = rr & (-rr)
            j = lsb.bit_length() - 1
            cols[j] |= (1 << i)
            rr ^= lsb
    return cols

def scan_le4(Hker, Hstab, n):
    t0 = time.time()
    cols = columns(Hker, n)
    byval = {}
    for j, c in enumerate(cols):
        byval.setdefault(c, []).append(j)
    found = set()
    for c, js in byval.items():
        if c == 0:
            for j in js:
                found.add((j,))
    for c, js in byval.items():
        if c != 0 and len(js) >= 2:
            for i, j in itertools.combinations(js, 2):
                found.add((i, j))
    for i, j in itertools.combinations(range(n), 2):
        x = cols[i] ^ cols[j]
        if x in byval:
            for t in byval[x]:
                if t != i and t != j:
                    found.add(tuple(sorted((i, j, t))))
    pairxor = {}
    for i, j in itertools.combinations(range(n), 2):
        pairxor.setdefault(cols[i] ^ cols[j], []).append((i, j))
    for x, L in pairxor.items():
        if len(L) >= 2:
            if len(L) > 4000:
                return {"aborted": True}
            for (i, j), (t, uu) in itertools.combinations(L, 2):
                if len({i, j, t, uu}) == 4:
                    found.add(tuple(sorted((i, j, t, uu))))
    logicals = []
    stab = 0
    for tup in found:
        e = 0
        for j in tup:
            e |= (1 << j)
        if not in_rowspace(list(Hstab), e):
            logicals.append([len(tup), sorted(tup)])
        else:
            stab += 1
    logicals.sort()
    return {"aborted": False, "n_ker_le4": len(found), "stabilizer_hits": stab,
            "n_logicals_le4": len(logicals), "first_logicals": logicals[:6],
            "min_logical_w": (logicals[0][0] if logicals else None),
            "seconds": round(time.time() - t0, 1)}

print("--- X side scan (ker HZ / row HX) ---", flush=True)
sx = scan_le4(HZ, HX, n)
print(json.dumps({kk: (vv if kk != "first_logicals" else vv) for kk, vv in sx.items()}), flush=True)
print("--- Z side scan (ker HX / row HZ) ---", flush=True)
sz = scan_le4(HX, HZ, n)
print(json.dumps({kk: (vv if kk != "first_logicals" else vv) for kk, vv in sz.items()}), flush=True)

counts = {w: math.comb(n, w) for w in (5, 6, 7)}
print("comb counts w=5..7:", {w: f"{c:.3e}" for w, c in counts.items()}, flush=True)
s7 = sum(math.comb(n, w) for w in range(8))
print(f"total binary vecs weight<8 at n={n}: {s7:.6e}", flush=True)

with open("fallback_attempt2_summary.json", "w") as f:
    json.dump({"group": "D_16", "A": A, "B": B, "n": n, "Delta": DELTA,
               "rankX": rx, "rankZ": rz, "k": k, "rate": k / n,
               "scanX": sx, "scanZ": sz,
               "weight_lt8_count": s7}, f)
print("saved fallback_attempt2_summary.json", flush=True)
