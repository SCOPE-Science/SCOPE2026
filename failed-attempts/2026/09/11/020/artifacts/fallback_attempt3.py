"""Bounded fallback attempt #3 (lane-719): D_20 Delta=5 n0=500 with balanced
generators (rotations+reflections each side) and stronger random local codes
(CA=[5,2], CB=[5,3], rho=0.4) per Radebold recipe. Checks: TNC, CSS, rate,
exhaustive ker-scan to weight 4, MITM weight-5/6 feasibility probe, weight-7
wall quantification. Pure stdlib.
"""
import json, math, random, time, itertools

M = 20
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

rng = random.Random(42)
# balanced: 2 rotations (inverse pair) + r^10 involution? need 5 sym: {r^k,r^-k} + {r^j,r^-j} + involution(reflection or r^10)
A = [R(1), R(-1), R(3), R(-3), S(0)]
cands_B = [[R(2), R(-2), R(4), R(-4), S(1)],
           [R(2), R(-2), R(5), R(-5), S(3)],
           [R(4), R(-4), R(6), R(-6), S(1)],
           [R(1), R(-1), R(4), R(-4), S(5)]]
B = None
for c in cands_B:
    if check_tnc(A, c) and generates(A, c):
        B = c
        break
assert B is not None, "no balanced TNC pair"
print("A =", A, "B =", B, flush=True)

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

AI = {a: i for i, a in enumerate(A)}
BI = {b: i for i, b in enumerate(B)}
AB = [(a, b) for a in A for b in B]

def mat_mul_vec(Mm, v):
    return [sum(r[j] * v[j] for j in range(len(v))) % 2 for r in Mm]

def code_dist(Grows, ncols):
    # brute-force nonzero codeword min weight (dim<=3 so <=7 codewords... actually 2^k-1)
    k = len(Grows)
    best = ncols + 1
    for mask in range(1, 1 << k):
        w = 0
        for j in range(ncols):
            s = 0
            for i in range(k):
                if (mask >> i) & 1:
                    s ^= Grows[i][j]
            w += s
        if w < best:
            best = w
    return best

def rand_code(ncols, dim, seed):
    r = random.Random(seed)
    # systematic G=[I|P]
    P = [[r.getrandbits(1) for _ in range(ncols - dim)] for _ in range(dim)]
    G = []
    for i in range(dim):
        row = [1 if j == i else 0 for j in range(dim)] + P[i]
        G.append(row)
    return G

def parity_of(G, ncols, dim):
    # H=[P^T|I]
    P = [row[dim:] for row in G]
    H = []
    for j in range(ncols - dim):
        H.append([P[i][j] for i in range(dim)] + [1 if t == j else 0 for t in range(ncols - dim)])
    return H

# search a few random (CA=[5,2],CB=[5,3]) pairs for best min(dA,dB,dApr,dBpr)
best = None
for seed in range(30):
    CA = rand_code(5, 2, 100 + seed)
    CB = rand_code(5, 3, 200 + seed)
    HA = parity_of(CA, 5, 2)
    HB = parity_of(CB, 5, 3)
    dA = code_dist(CA, 5)
    dB = code_dist(CB, 5)
    dApr = code_dist(HA, 5)
    dBpr = code_dist(HB, 5)
    m = min(dA, dB, dApr, dBpr)
    key = (m, dA + dB)
    if best is None or key > best[0]:
        best = (key, seed, CA, CB, HA, HB, (dA, dB, dApr, dBpr))
print("best local distances (dA,dB,dApr,dBpr):", best[6], "seed", best[1], flush=True)
_, _, CA, CB, HA, HB, _ = best

# C0 = CA tensor CB rows: u_i (x) v_j, bit(i,j)=u_i*v_j ; C1 = HA rows tensor HB rows
C0 = []
for u in CA:
    for v in CB:
        C0.append([u[AI[a]] * v[BI[b]] for (a, b) in AB])
C1 = []
for u in HA:
    for v in HB:
        C1.append([u[AI[a]] * v[BI[b]] for (a, b) in AB])
print(f"dimC0={len(C0)} dimC1={len(C1)}", flush=True)

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
      "wt range X:", min(map(wt, HX)), max(map(wt, HX)),
      "Z:", min(map(wt, HZ)), max(map(wt, HZ)), flush=True)
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
            if len(L) > 6000:
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
            "n_logicals_le4": len(logicals),
            "first_logicals": logicals[:4],
            "min_logical_w": (logicals[0][0] if logicals else None),
            "seconds": round(time.time() - t0, 1)}

print("--- X side scan ---", flush=True)
sx = scan_le4(HZ, HX, n)
print(json.dumps(sx), flush=True)
print("--- Z side scan ---", flush=True)
sz = scan_le4(HX, HZ, n)
print(json.dumps(sz), flush=True)

# MITM feasibility probe for weight 5/6/7 certification at this n
counts = {w: math.comb(n, w) for w in (5, 6, 7)}
s7 = sum(math.comb(n, w) for w in range(8))
print("C(n,w):", {w: f"{c:.3e}" for w, c in counts.items()}, flush=True)
print(f"total weight<8: {s7:.6e}", flush=True)
# time one syndrome evaluation throughput
t0 = time.time()
cols = columns(HZ, n)
N = 200000
acc = 0
for t in range(N):
    acc ^= cols[(t * 7919) % n] ^ cols[(t * 104729 + 13) % n] ^ cols[(t * 1299709 + 7) % n]
dt = time.time() - t0
rate = N / dt
print(f"syndrome throughput: {rate:.2e} evals/s -> weight-5 full scan {counts[5]/rate/3600:.2e} h, weight-7 {counts[7]/rate/3600:.2e} h", flush=True)

with open("fallback_attempt3_summary.json", "w") as f:
    json.dump({"group": "D_20", "A": A, "B": B, "n": n, "Delta": DELTA,
               "local_dists": best[6], "rankX": rx, "rankZ": rz, "k": k,
               "rate": k / n, "scanX": sx, "scanZ": sz,
               "weight_lt8_count": s7,
               "syndrome_evals_per_s": rate}, f)
print("saved fallback_attempt3_summary.json", flush=True)
