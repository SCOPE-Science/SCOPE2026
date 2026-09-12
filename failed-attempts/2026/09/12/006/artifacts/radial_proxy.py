"""Bounded attack + recovery test for lane-1067 (stdlib only, seeded).

Part A: audit-patch arithmetic for the canonical dyadic-RSW arm route
        (Ahlberg-Baldasso Sec.4.2 shape): mesh m, annulus count |J|,
        best-possible bound, required RSW parameter.
Part B: triangular-lattice proxy Monte Carlo (pc=1/2, rigorous 5/48 arm):
  B1: one-arm P[origin red-cluster reaches R] scaling vs n^{-1/3} shape.
  B2: radial-exploration proxy on A(16,32): P[fixed test cell queried]
        vs cap 0.30*16^{-1/3} = 0.119.
"""
import random, math, collections, json

rng = random.Random(20260912)
out = {}

# ---------------- Part A ----------------
n = 16
cap_rev = 0.30 * n ** (-1.0 / 3.0)
cap_win = 0.70 * n ** (-1.0 / 3.0)
m = 1.0 / math.ceil(n ** 0.25)          # Ahlberg-Baldasso mesh at n=16 -> 1/2
s = math.sqrt(m)
J = [j for j in range(0, 30) if (4 ** j) * m <= s + 1e-12]
slack = 3.0 / n
best_q = 1.0 / 32.0                            # max q = c1^4/32 with c1 <= 1
best_bound = 1.0 / n + ((1 - best_q) + slack) ** (len(J) / 2.0)
perf_bound = 1.0 / n + (slack) ** (len(J) / 2.0)  # even with perfect q=1
out['A'] = {'n': n, 'cap_rev': cap_rev, 'cap_win': cap_win, 'mesh_m': m,
            'sqrt_m': s, 'absJ': len(J), 'best_q': best_q,
            'best_bound': best_bound, 'perfect_q_bound': perf_bound}
print('A: cap_rev=%.6f cap_win=%.6f m=%.3f |J|=%d' % (cap_rev, cap_win, m, len(J)))
print('A: best-RSW bound=%.4f perfect-RSW bound=%.4f (both vs cap %.4f)'
      % (best_bound, perf_bound, cap_rev))
# asymptotic exponent ceiling of this route family
import math as _m
gamma_max = best_q / (32 * _m.log(2))
print('A: asymptotic exponent ceiling of route = %.6f vs claimed 1/3' % gamma_max)
out['A']['gamma_max'] = gamma_max
# mesh sweep at n=16: |J| and perfect-RSW floor over all admissible meshes
print('A mesh sweep at n=16 (need bound<=%.4f):' % cap_rev)
sweep = []
for a in (0.25, 1.0 / 3.0, 0.4, 0.49):
    mm = n ** (-a)
    JJ = [j for j in range(0, 30) if (4 ** j) * mm <= math.sqrt(mm) + 1e-12]
    floor = 1.0 / n + (3.0 / n) ** (len(JJ) / 2.0)
    sweep.append({'a': a, 'm': mm, 'absJ': len(JJ), 'perfect_floor': floor})
    print('  m=n^(-%.2f)=%.4f |J|=%d perfect-RSW floor=%.4f' % (a, mm, len(JJ), floor))
out['A']['mesh_sweep'] = sweep

# ---------------- lattice geometry ----------------
NB = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)]
SQ3 = math.sqrt(3.0)

def build(Rkeep):
    sites, idx = [], {}
    R = int(math.ceil(Rkeep)) + 2
    for j in range(-R, R + 1):
        for i in range(-R, R + 1):
            x = i + 0.5 * j
            y = 0.5 * SQ3 * j
            r = math.hypot(x, y)
            if r <= Rkeep:
                idx[(i, j)] = len(sites)
                sites.append((x, y, r, math.atan2(y, x)))
    pairs = [None] * len(sites)
    for (ij, k) in idx.items():
        pairs[k] = ij
    nbrs = []
    for k in range(len(sites)):
        i, j = pairs[k]
        lst = []
        for (di, dj) in NB:
            t = idx.get((i + di, j + dj))
            if t is not None:
                lst.append(t)
        nbrs.append(lst)
    return sites, nbrs

def angdist(a, b):
    return abs((a - b + math.pi) % (2 * math.pi) - math.pi)

# ---------------- B1: one-arm ----------------
sites, nbrs = build(34.0)
N = len(sites)
origin = None
for k, (x, y, r, a) in enumerate(sites):
    if abs(x) < 1e-9 and abs(y) < 1e-9:
        origin = k
        break
assert origin is not None
Rs = [8.0, 16.0, 32.0]
hits = [0] * len(Rs)
T1 = 600
for _ in range(T1):
    red = [rng.random() < 0.5 for _ in range(N)]
    if not red[origin]:
        continue
    seen = bytearray(N)
    dq = collections.deque([origin])
    seen[origin] = 1
    maxr = 0.0
    while dq:
        u = dq.popleft()
        ru = sites[u][2]
        if ru > maxr:
            maxr = ru
        for v in nbrs[u]:
            if not seen[v] and red[v]:
                seen[v] = 1
                dq.append(v)
    for t, R in enumerate(Rs):
        if maxr >= R:
            hits[t] += 1
probs = [h / T1 for h in hits]
out['B1'] = {'trials': T1, 'R': Rs, 'hits': hits, 'probs': probs}
print('B1 one-arm probs:', ['R=%g: %.4f' % (R, p) for R, p in zip(Rs, probs)])
slope = (math.log(probs[2]) - math.log(probs[0])) / (math.log(32.0) - math.log(8.0))
out['B1']['loglog_slope_8_32'] = slope
print('B1 log-log slope(8->32)=%.4f [universal -5/48=-0.1042 vs claimed -1/3=-0.3333]' % slope)
shape_32 = 0.30 * 32.0 ** (-1.0 / 3.0)
print('B1: P[arm to 32]=%.4f vs 0.30*32^-1/3 shape=%.4f' % (probs[2], shape_32))
out['B1']['shape_32'] = shape_32

# ---------------- B2: radial query proxy on A(16,32) ----------------
sites2, nbrs2 = build(33.0)
keep = [k for k, (x, y, r, a) in enumerate(sites2) if 15.0 <= r <= 33.0]
keepS = set(keep)
pos = {k: t for t, k in enumerate(keep)}
nbrsA = [[pos[v] for v in nbrs2[k] if v in keepS] for k in keep]
test = min(keep, key=lambda k: (sites2[k][0] - 24.0) ** 2 + sites2[k][1] ** 2)
tx, ty, tr, ta = sites2[test]
M = len(keep)
T2 = 1200
q = 0
q_band = 0
for _ in range(T2):
    th0 = rng.random() * 2 * math.pi
    red = [rng.random() < 0.5 for _ in range(M)]
    seeds = [t for t in range(M)
             if red[t] and sites2[keep[t]][2] >= 30.0
             and angdist(sites2[keep[t]][3], th0) < 0.09]
    tp = pos[test]
    if angdist(ta, th0) < 0.11:
        q += 1
        q_band += 1
        continue
    if not red[tp]:
        continue
    seedS = set(seeds)
    if tp in seedS:
        q += 1
        continue
    seen = bytearray(M)
    dq = collections.deque()
    for t in seeds:
        seen[t] = 1
        dq.append(t)
    found = False
    while dq and not found:
        u = dq.popleft()
        for vp in nbrsA[u]:
            if vp == tp:
                found = True
                break
            if not seen[vp] and red[vp]:
                seen[vp] = 1
                dq.append(vp)
    if found:
        q += 1
phat = q / T2
se = math.sqrt(phat * (1 - phat) / T2)
out['B2'] = {'trials': T2, 'test_xy': [tx, ty], 'test_r': tr, 'queries': q,
             'band_queries': q_band, 'phat': phat, 'se': se,
             'ci95': [phat - 1.96 * se, phat + 1.96 * se],
             'cap': 0.30 * 16.0 ** (-1.0 / 3.0)}
print('B2: test site (%.2f,%.2f) r=%.2f queries=%d/%d phat=%.4f se=%.4f CI95=[%.4f,%.4f] cap=%.4f'
      % (tx, ty, tr, q, T2, phat, se, phat - 1.96 * se, phat + 1.96 * se, out['B2']['cap']))

with open('output/artifacts/proxy_results.json', 'w') as f:
    json.dump(out, f, indent=1)
print('wrote output/artifacts/proxy_results.json')
