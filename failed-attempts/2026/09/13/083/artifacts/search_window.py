"""Extended closed-walk search (revisits allowed) + classification + realizability.

Walk encoding: arrays. Precompute for each state: exits (next states + exit side).
DFS iterative with per-branch use cap and length cap; on return to start (len>=3),
record weight vector (branch multiplicities) + install + intersections.
Dedupe by weight vector. Collect slope histogram. Target window: t in (-1, -1/2).
"""
import pickle, math, time
from collections import Counter
import snappy, flipper
import flipper.kernel.triangulation3 as T3m
from flipper.kernel.triangulation3 import MERIDIANS, LONGITUDES, TEMPS

WDIR = "output/artifacts"
D = pickle.load(open(f"{WDIR}/track_data.pkl", "rb"))
branches, switches, NV = D["branches"], D["switches"], D["NV"]
NB = len(branches)
M = snappy.Manifold('10_145')
mono = flipper.monodromy_from_bundle(M)
B = mono.bundle(veering=True)
V = snappy.Manifold(B.snappy_string())
data = V._get_tetrahedra_gluing_data()
NT = len(data)
T3 = B.triangulation3
WSTAR = {0: 2, 1: 3, 2: 0, 3: 1}
bkey = {}
for b, members in enumerate(branches):
    for s in members:
        bkey[s] = b

# states indexed 0..71; trans[i] = list of (next_state, exit_side, tri, entry_side)
slist = []
sindex = {}
for b, members in enumerate(branches):
    ((i1, v1), j1), ((i2, v2), j2) = members
    for (tb, sb) in [((i1, v1), j1), ((i2, v2), j2)]:
        st = (b, tb, sb)
        sindex[st] = len(slist)
        slist.append(st)
NS = len(slist)
trans = [[] for _ in range(NS)]
for si, (b, tb, sb) in enumerate(slist):
    L = WSTAR[tb[1]]
    smalls = [j for j in range(4) if j != tb[1] and j != L]
    exits = smalls if sb == L else [L]
    for se in exits:
        b2 = bkey[(tb, se)]
        m2 = branches[b2]
        nxt = m2[1] if m2[0] == (tb, se) else m2[0]
        ns = sindex[(b2, (nxt[0][0], nxt[0][1]), nxt[1])]
        trans[si].append((ns, se))
TRI = [s[1] for s in slist]
ENT = [s[2] for s in slist]
BR = [s[0] for s in slist]

import cmath
CORN = {0: 1 + 0j, 1: cmath.exp(2j * math.pi / 3), 2: cmath.exp(4j * math.pi / 3)}
def turn_sign(W, s_in, s_out):
    P = [CORN[W.index(w)] for w in W]
    mid = lambda s: sum(P[W.index(w)] for w in W if w != s) / 2
    a, b = mid(s_in), mid(s_out)
    cset = set(w for w in W if w != s_in) & set(w for w in W if w != s_out)
    c = CORN[W.index(next(iter(cset)))]
    d = b - a
    n = c - (a + b) / 2
    cr = d.real * n.imag - d.imag * n.real
    return 1 if cr > 0 else -1

def install_and_classify(path):
    """path: list of state indices (closed walk, path[-1] connects to path[0]).
    Returns (E, iM, iL)."""
    E = {}
    n = len(path)
    for k in range(n):
        si = path[k]
        sj = path[(k + 1) % n]
        # exit side: the se with trans[si] leading to sj
        se = None
        for (ns, see) in trans[si]:
            if ns == sj:
                se = see
                break
        assert se is not None
        tb = TRI[si]; sb = ENT[si]
        i, v = tb
        W = sorted(w for w in range(4) if w != v)
        s = turn_sign(W, sb, se)
        cset = set(w for w in W if w != sb) & set(w for w in W if w != se)
        c = next(iter(cset))
        E[(i, v, c)] = E.get((i, v, c), 0) + s
    for t in T3.tetrahedra:
        for s_ in range(4):
            for o in range(4):
                t.peripheral_curves[TEMPS][s_][o] = 0
    for (i, v, w), e in E.items():
        T3.tetrahedra[i].peripheral_curves[TEMPS][v][w] = e
    return E, T3.intersection_number(TEMPS, MERIDIANS), T3.intersection_number(TEMPS, LONGITUDES)

def zung_t(a, b):
    d = 6 * b - a
    return float('inf') if d == 0 else -b / d

def search(LMAX, CAP, starts='all', tlim=8.0):
    seen = set()
    hits = Counter()
    window = []
    t0 = time.time()
    NST = NS if starts == 'all' else len(starts)
    for s0 in (range(NS) if starts == 'all' else starts):
        # iterative DFS: stack of (state, depth, it_index)
        useb = [0] * NB
        path = [s0]
        useb[BR[s0]] = 1
        stack = [(s0, 0, 0)]
        while stack:
            si, depth, ii = stack[-1]
            if ii < len(trans[si]):
                ns, se = trans[si][ii]
                stack[-1] = (si, depth, ii + 1)
                if ns == s0 and depth + 1 >= 3:
                    wv = tuple(sorted(path_branch_counts(path, useb)))
                    if wv not in seen:
                        seen.add(wv)
                        E, iM, iL = install_and_classify(path)
                        a, b = -iL, iM
                        g = math.gcd(a, b)
                        prim = (a // g, b // g) if g else (a, b)
                        t = zung_t(*prim)
                        hits[(prim, round(t, 6) if abs(t) != float('inf') else 'inf', len(path))] += 1
                        if isinstance(t, float) and -1 < t < -0.5:
                            window.append((prim, t, len(path), list(path)))
                    continue
                if depth + 1 >= LMAX:
                    continue
                if useb[BR[ns]] >= CAP:
                    continue
                useb[BR[ns]] += 1
                path.append(ns)
                stack.append((ns, depth + 1, 0))
            else:
                stack.pop()
                useb[BR[si]] -= 1
                path.pop()
        if time.time() - t0 > tlim * 60:
            print("TIME LIMIT", flush=True)
            break
    return seen, hits, window

def path_branch_counts(path, useb):
    return [(b, c) for b, c in enumerate(useb) if c > 0]

import sys
LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 16
CAP = int(sys.argv[2]) if len(sys.argv) > 2 else 2
seen, hits, window = search(LMAX, CAP)
print(f"LMAX={LMAX} CAP={CAP} distinct weight vectors: {len(seen)}", flush=True)
for k in sorted(hits, key=lambda x: (x[1] if isinstance(x[1], float) else 999, x[2])):
    print(f"  class {k[0]}  t={k[1]}  len {k[2]}  x{hits[k]}", flush=True)
print("WINDOW HITS (t in (-1,-1/2)):", len(window), flush=True)
for w in window[:20]:
    print("  ", w[0], w[1], "len", w[2], flush=True)
