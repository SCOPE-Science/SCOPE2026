"""Frozen deterministic search: track from artifact gluing + frozen corner data.

- Triangulation: artifact V file (assert isosig).
- m/l corner tables: frozen corner_data.pkl.
- Intersection: own implementation of flipper's algorithm (verified byte-identical:
  manual i(M,L) = -1 above) on (tet label, side, corner) tables. Tet labels 0..5
  coincide with SnapPy tet indices (verified by construction run).
- DFS closed walks with revisits (cap), classify, window t in (-1,-1/2).
"""
import pickle, math, time, sys
from itertools import product
import snappy
import flipper.kernel.triangulation3 as T3m

WDIR = "output/artifacts"
V = snappy.Manifold(f"{WDIR}/V_flipper_veering.tri")
FROZEN = "gLLMQaedfdffjxaxjkn_aBbB"
assert V.triangulation_isosig() == FROZEN, V.triangulation_isosig()
D = pickle.load(open(f"{WDIR}/track_data.pkl", "rb"))
C = pickle.load(open(f"{WDIR}/corner_data.pkl", "rb"))
assert C["isosig"] == FROZEN
branches, switches = D["branches"], D["switches"]
data = D["gluing_data"]
assert data == V._get_tetrahedra_gluing_data()
NB = len(branches)
NT = len(data)
MC = C["corners"]["M"]; LC = C["corners"]["L"]
WSTAR = {0: 2, 1: 3, 2: 0, 3: 1}
bkey = {}
for b, members in enumerate(branches):
    for s in members:
        bkey[s] = b

# states
slist, sindex = [], {}
for b, members in enumerate(branches):
    ((i1, v1), j1), ((i2, v2), j2) = members
    for (tb, sb) in [((i1, v1), j1), ((i2, v2), j2)]:
        sindex[(b, tb, sb)] = len(slist)
        slist.append((b, tb, sb))
NS = len(slist)
trans = [[] for _ in range(NS)]
for si, (b, tb, sb) in enumerate(slist):
    L = WSTAR[tb[1]]
    smalls = [j for j in range(4) if j != tb[1] and j != L]
    for se in (smalls if sb == L else [L]):
        b2 = bkey[(tb, se)]
        m2 = branches[b2]
        nxt = m2[1] if m2[0] == (tb, se) else m2[0]
        trans[si].append((sindex[(b2, (nxt[0][0], nxt[0][1]), nxt[1])], se))
TRI = [s[1] for s in slist]; ENT = [s[2] for s in slist]; BR = [s[0] for s in slist]

import cmath
CORN = {0: 1 + 0j, 1: cmath.exp(2j * math.pi / 3), 2: cmath.exp(4j * math.pi / 3)}
def turn_sign(W, s_in, s_out):
    P = [CORN[W.index(w)] for w in W]
    mid = lambda s: sum(P[W.index(w)] for w in W if w != s) / 2
    a, b = mid(s_in), mid(s_out)
    cset = set(w for w in W if w != s_in) & set(w for w in W if w != s_out)
    c = CORN[W.index(next(iter(cset)))]
    d = b - a; n = c - (a + b) / 2
    cr = d.real * n.imag - d.imag * n.real
    return 1 if cr > 0 else -1

# flipper intersection algorithm on plain tables: tet indexed by label 0..5
VM = T3m.VERTICES_MEETING; EL = T3m.EXIT_CUSP_LEFT; ER = T3m.EXIT_CUSP_RIGHT
flow = lambda A, Bb: 0 if (A < 0) == (Bb < 0) else (A if (A < 0) != (A < -Bb) else -Bb)
def mktab(E):
    tab = {}
    for i in range(NT):
        for s_ in range(4):
            for o in range(4):
                tab[(i, s_, o)] = E.get((i, s_, o), 0)
    return tab
def inter(TA, TB):
    tot = 0
    for i in range(NT):
        for side in range(4):
            for other in VM[side]:
                if TA[(i, side, other)] > 0:
                    tot -= TA[(i, side, other)] * TB[(i, side, other)]
            for other in VM[side]:
                l = EL[(side, other)]; r = ER[(side, other)]
                tot += flow(TA[(i, side, other)], TA[(i, side, l)]) * flow(TB[(i, side, other)], TB[(i, side, l)])
                tot += flow(TA[(i, side, other)], TA[(i, side, r)]) * flow(TB[(i, side, other)], TB[(i, side, l)])
    return tot
print("sanity i(M,L) =", inter(MC, LC), flush=True)
MT = mktab({}); LT = mktab({})
assert inter(MC, LC) == -1

def classify(path):
    E = {}
    n = len(path)
    for k in range(n):
        si = path[k]; sj = path[(k + 1) % n]
        se = next(see for (ns, see) in trans[si] if ns == sj)
        tb = TRI[si]; sb = ENT[si]
        i, v = tb
        W = sorted(w for w in range(4) if w != v)
        s = turn_sign(W, sb, se)
        c = next(iter(set(w for w in W if w != sb) & set(w for w in W if w != se)))
        E[(i, v, c)] = E.get((i, v, c), 0) + s
    TE = mktab(E)
    return -inter(TE, LC), inter(TE, MC)  # (a, b)

def zung_t(a, b):
    d = 6 * b - a
    return float('inf') if d == 0 else -b / d

def search(LMAX, CAP, tlim_min=8.0):
    seen, hits, window = set(), {}, []
    t0 = time.time()
    for s0 in range(NS):
        useb = [0] * NB
        path = [s0]; useb[BR[s0]] = 1
        stack = [(s0, 0, 0)]
        while stack:
            si, depth, ii = stack[-1]
            if ii < len(trans[si]):
                ns, se = trans[si][ii]
                stack[-1] = (si, depth, ii + 1)
                if ns == s0 and depth + 1 >= 3:
                    wv = tuple(sorted((b, c) for b, c in enumerate(useb) if c))
                    if wv not in seen:
                        seen.add(wv)
                        a, b = classify(path)
                        g = math.gcd(a, b)
                        prim = (a // g, b // g) if g else (a, b)
                        t = zung_t(*prim)
                        key = (prim, round(t, 6) if abs(t) != float('inf') else 'inf', len(path))
                        hits[key] = hits.get(key, 0) + 1
                        if isinstance(t, float) and -1 < t < -0.5:
                            window.append((prim, t, len(path), list(path), dict(useb)))
                    continue
                if depth + 1 >= LMAX or useb[BR[ns]] >= CAP:
                    continue
                useb[BR[ns]] += 1; path.append(ns); stack.append((ns, depth + 1, 0))
            else:
                stack.pop(); useb[BR[si]] -= 1; path.pop()
        if time.time() - t0 > tlim_min * 60:
            print("TIME LIMIT", flush=True)
            break
    return seen, hits, window

LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 16
CAP = int(sys.argv[2]) if len(sys.argv) > 2 else 2
seen, hits, window = search(LMAX, CAP)
print(f"FROZEN LMAX={LMAX} CAP={CAP} distinct: {len(seen)}", flush=True)
for k in sorted(hits, key=lambda x: (x[1] if isinstance(x[1], float) else 999, x[2])):
    print(f"  class {k[0]} t={k[1]} len {k[2]} x{hits[k]}", flush=True)
print("WINDOW:", len(window), flush=True)
for w in window[:20]:
    print("  ", w[0], w[1], "len", w[2], flush=True)
