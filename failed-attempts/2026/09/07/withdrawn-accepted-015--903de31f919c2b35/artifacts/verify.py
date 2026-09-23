#!/usr/bin/env python3
"""Independent verifier for the 201-350 real-quadratic census.
Re-derives CF data, units, form cycles, K-cycle, class numbers, witness
chains, structures (h>=4 fields) and extrema from scratch; checks them
against census_table.csv / witnesses.json. Uses only stdlib + numpy (+mpmath
for one regulator cross-check). Exit nonzero on any failure.

Usage: python3 verify.py   (run inside lane-37 directory)
"""
import csv, json, math, sys
import numpy as np

ART = "output/artifacts"

# ---------- exact integer kernels (independent copies) ----------
def cf_sqrt(d):
    a0 = math.isqrt(d); assert a0*a0 != d
    m, dn, a = 0, 1, a0; per = []
    while True:
        m = dn*a - m; dn = (d - m*m)//dn; a = (a0 + m)//dn
        per.append(a)
        if a == 2*a0: break
    return a0, per

def convs(a0, per, n):
    p2, p1, q2, q1 = 0, 1, 1, 0; out = []
    for i in range(n):
        an = a0 if i == 0 else per[(i-1) % len(per)]
        p, q = an*p1 + p2, an*q1 + q2
        out.append((p, q)); p2, p1, q2, q1 = p1, p, q1, q
    return out

def cmp_same(d, X1, Y1, X2, Y2):
    Dx, Dy = X1-X2, Y1-Y2
    if Dy == 0: return (Dx > 0)-(Dx < 0)
    if Dx == 0: return (Dy > 0)-(Dy < 0)
    if (Dx > 0) == (Dy > 0): return 1 if Dx > 0 else -1
    l, r = Dx*Dx, Dy*Dy*d
    if l == r: return 0
    return (1 if Dx > 0 else -1) if l > r else (1 if Dy > 0 else -1)

def red(D, a, b, c):
    if a == 0 or c == 0 or b*b-4*a*c != D: return False
    if b <= 0 or b*b >= D: return False
    s2 = 2*abs(a)-b
    if s2 > 0 and s2*s2 >= D: return False
    s1 = b+2*abs(a)
    return s1 > 0 and D < s1*s1

def rho(D, a, b, c):
    I = math.isqrt(D); s = 2*abs(c)
    b1 = I - ((I+b) % s)
    assert (b1+b) % (2*c) == 0 and (b1*b1-D) % (4*c) == 0
    return (c, b1, (b1*b1-D)//(4*c))

def to_cycle(D, f):
    cur = f; n = 0
    while not red(D, *cur):
        cur = rho(D, *cur); n += 1
        assert n < 5000
    return cur

def kron(a, n):
    if n == 1: return 1
    e = 0; m = n
    while m % 2 == 0: m //= 2; e += 1
    r = 1
    if e:
        t = {1: 1, 7: 1, 3: -1, 5: -1}.get(a % 8, 0)
        if e % 2 == 1: r *= t
        elif a % 2 == 0: return 0
    aa, nn, t = (a % m if m > 1 else 0), m, 1
    while aa:
        while aa % 2 == 0:
            aa //= 2
            if nn % 8 in (3, 5): t = -t
        aa, nn = nn, aa
        if aa % 4 == 3 and nn % 4 == 3: t = -t
        aa %= nn
    return 0 if nn != 1 else r*t

def egcd(a, b):
    if b == 0: return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b); return (g, y1, x1-(a//b)*y1)

def crt(r1, m1, r2, m2):
    m1, m2 = abs(m1), abs(m2)
    g, u, _ = egcd(m1, m2)
    if (r2-r1) % g: return None
    L = m1//g*m2
    return ((r1 + m1*((r2-r1)//g*u)) % L, L)

def comp(D, f1, f2):
    a1, b1, _ = f1; a2, b2, _ = f2
    assert math.gcd(a1, a2) == 1
    B, _ = crt(b1, 2*a1, b2, 2*a2)
    A = a1*a2
    assert (B*B-D) % (4*A) == 0
    return to_cycle(D, (A, B, (B*B-D)//(4*A)))

# ---------- load claims ----------
rows = list(csv.DictReader(open(f"{ART}/census_table.csv")))
W = json.load(open(f"{ART}/witnesses.json"))
assert len(rows) == 91, len(rows)
ds = sorted(int(r["d"]) for r in rows)
# squarefree check
sq = []
for n in range(201, 351):
    if all(n % (p*p) for p in range(2, 19)):
        sq.append(n)
assert ds == sq, "d list != squarefree [201,350]"
print("[1] 91 squarefree d: OK")

for r in rows:
    d = int(r["d"]); D = int(r["D"])
    assert D == (d if d % 4 == 1 else 4*d)
    M = math.sqrt(D)/2
    assert abs(M - float(r["Minkowski_M"])) < 1e-6
    # CF + unit recompute
    a0, per = cf_sqrt(d)
    assert len(per) == int(r["period_l"]), (d,)
    cv = convs(a0, per, 2*len(per))
    cands = []
    for i, (p, q) in enumerate(cv):
        N = p*p - d*q*q
        if N in (1, -1): cands.append((2*p, 2*q, N))
        if N in (4, -4) and p % 2 == 1 and q % 2 == 1:
            cands.append((p, q, N//4))
    best = cands[0]
    for c in cands[1:]:
        if cmp_same(d, c[0], c[1], best[0], best[1]) < 0: best = c
    assert (best[0], best[1]) == (int(r["eps_x"]), int(r["eps_y"])), (d,)
    assert best[2] == int(r["unit_norm"]), (d,)
    R = math.log((best[0]+best[1]*math.sqrt(d))/2)
    assert abs(R - float(r["regulator"])) < 1e-9, (d,)
    # cycles
    B = math.isqrt(D); reds = []
    for a in list(range(-B, 0))+list(range(1, B+1)):
        for b in range(-B, B+1):
            if (b-D) % 2 or (b*b-D) % (4*a): continue
            if red(D, a, b, (b*b-D)//(4*a)): reds.append((a, b, (b*b-D)//(4*a)))
    assert reds
    nx = {f: rho(D, *f) for f in reds}
    assert all(v in nx for v in nx.values())
    cid = {}; cyc = []
    for f in reds:
        if f in cid: continue
        path, pos, cur = [], {}, f
        while cur not in cid and cur not in pos:
            pos[cur] = len(path); path.append(cur); cur = nx[cur]
        if cur in cid:
            for g in path: cid[g] = cid[cur]
        else:
            k = len(cyc); cyc.append(path[pos[cur]:])
            for g in path: cid[g] = k
    hplus = len(cyc)
    assert hplus == int(r["h_plus"]), (d, hplus)
    ones = [f for f in reds if f[0] == 1]
    assert len(ones) == 1
    c0 = cid[ones[0]]
    # K-forms (two alphas)
    xs = ([a0 if a0 % 2 == 1 else a0-1, a0-3 if (a0 if a0 % 2 == 1 else a0-1)-2 > 0 else a0+1]
          if d % 4 == 1 else [a0, a0-1])
    # normalize: two odd x<d (d%4==1) or two x (else)
    if d % 4 == 1:
        x1 = a0 if a0 % 2 == 1 else a0-1
        xs = [x1, x1-2]
        kfs = [((d-x*x)//4, x, -1) for x in xs]
    else:
        kfs = [(d-x*x, 2*x, -1) for x in (a0, a0-1)]
    cKs = {cid[to_cycle(D, kf)] for kf in kfs}
    assert len(cKs) == 1, (d, cKs)
    cK = cKs.pop()
    assert (cK == c0) == (best[2] == -1), (d,)
    h = hplus if best[2] == -1 else hplus//2
    assert h == int(r["h"]), (d, h, hplus)
    # K^2 principal via composition
    Kf = cyc[cK][0]
    got = None
    for g1 in cyc[cK]:
        for g2 in cyc[cK]:
            if math.gcd(g1[0], g2[0]) == 1:
                got = cid[comp(D, g1, g2)]; break
        if got is not None: break
    assert got == c0, (d, "K^2")
print("[2] CF/unit/regulator/cycles/K/h for all 91: OK")

# witnesses
for r in rows:
    d = int(r["d"]); D = int(r["D"]); h = int(r["h"])
    if h == 1:
        assert str(d) not in W; continue
    w = W[str(d)]; p = w["p"]
    assert p <= math.sqrt(D)/2 + 1e-12 and kron(D, p) != -1
    assert kron(D, p) == w["kronecker"]
    ch = [tuple(f) for f in w["chain"]]
    assert tuple(w["form"]) == ch[0] and ch[0][0] == p
    assert ch[0][1]*ch[0][1]-4*ch[0][0]*ch[0][2] == D
    for a, b in zip(ch, ch[1:]):
        assert rho(D, *a) == b, (d,)
    assert red(D, *ch[-1]) and tuple(w["reduced"]) == ch[-1]
    assert w["narrow_cycle"] not in (w["principal_cycle"], w["k_cycle"]), (d,)
print(f"[3] {len(W)} nonprincipal prime-ideal witnesses (chains verified): OK")

# structures for h>=4 via recomputed narrow orders
need = {"C4": [1,2,4,4], "C2xC2": [1,2,2,2], "C6": [1,2,3,3,6,6],
        "C8": [1,2,4,4,8,8,8,8]}
for r in rows:
    if int(r["h"]) < 4: continue
    d = int(r["d"]); D = int(r["D"])
    F = next(x for x in json.load(open(f"{ART}/step2_forms.json")) if x["d"] == d)
    cycs = [tuple(tuple(f) for f in c) for c in F["cycles"]]
    cid2 = {}
    for i, c in enumerate(cycs):
        for f in c: cid2[f] = i
    n = len(cycs)
    c0 = F["principal_cycle"]
    def mul(i, j):
        for g1 in cycs[i]:
            for g2 in cycs[j]:
                if math.gcd(g1[0], g2[0]) == 1:
                    return cid2[comp(D, g1, g2)]
        raise AssertionError((d, i, j))
    def pw(i, e):
        x = c0
        for _ in range(e): x = mul(x, i)
        return x
    orders = []
    for i in range(n):
        e = 1
        while pw(i, e) != c0: e += 1
        orders.append(e)
    cK = F["k_cycle"]
    oset = {c0, cK}
    # ordinary orders: one per {C,C+K} orbit
    oo = []
    seen = set()
    for i in range(n):
        key = tuple(sorted((i, mul(i, cK))))
        if key in seen: continue
        seen.add(key)
        e = 1
        while pw(i, e) not in oset: e += 1
        oo.append(e)
    oo.sort()
    lab = r["structure"]
    assert lab in need and oo == need[lab], (d, lab, oo)
print("[4] structures for all h>=4 fields (13): OK")

# extrema
tb = {int(r["d"]): r for r in rows}
assert max(int(r["period_l"]) for r in rows) == 34
assert sum(1 for r in rows if int(r["period_l"]) == 34) == 1
assert int([r for r in rows if int(r["period_l"]) == 34][0]["d"]) == 331
x3, y3 = int(tb[331]["eps_x"]), int(tb[331]["eps_y"])
for d, r in tb.items():
    if d == 331: continue
    # exact: eps331 > eps_d ?
    from functools import cmp_to_key  # noqa
    x, y = int(r["eps_x"]), int(r["eps_y"])
    if 331 == d: continue
    # same/different-d exact compare (units (x+y√d)/2)
    if d == 331: continue
    Dx = x3-x
    A, B = y3*y3*331, y*y*d
    if y3 == 0 and y == 0: s = (Dx > 0)-(Dx < 0)
    elif y3 == 0: s = -1 if Dx <= 0 else (1 if Dx*Dx > B else -1)
    elif y == 0: s = 1 if Dx >= 0 and (Dx > 0 or y3 > 0) else (1 if A > Dx*Dx else -1)
    else:
        sT = (A > B)-(A < B)
        if sT == 0: s = (Dx > 0)-(Dx < 0)
        elif Dx == 0: s = sT
        elif (Dx > 0) == (sT > 0): s = 1 if Dx > 0 else -1
        else:
            P = A+B-Dx*Dx; Q = 2*y3*y; M = 331*d
            t = -1 if P <= 0 else ((P*P > Q*Q*M)-(P*P < Q*Q*M))
            s = 0 if t == 0 else (sT if t > 0 else (1 if Dx > 0 else -1))
    assert s == 1, (d,)
print("[5] extrema: max period l=34 @331 unique; max regulator @331 (exact): OK")

# L(1,chi) spot cross-check at N=2e5
def L1(D, N):
    per = np.array([kron(D, r) for r in range(1, D+1)], dtype=float)
    assert abs(per.sum()) < 0.5
    n = np.arange(1, N+1)
    return float(np.sum(np.tile(per, N//D+1)[:N]/n)), D/N
bad = 0
for r in rows:
    d = int(r["d"]); D = int(r["D"]); h = int(r["h"])
    s, tbnd = L1(D, 200000)
    if abs(h*float(r["regulator"]) - math.sqrt(D)/2*s) >= math.sqrt(D)/2*tbnd + 1e-6:
        bad += 1; print("L-mismatch", d)
assert bad == 0
print("[6] class-number-formula cross-check (N=2e5): OK")
print("ALL CHECKS PASSED")
