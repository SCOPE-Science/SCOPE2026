"""Uniform smoothing-rule calibration: 3 candidate rules x known slopes (0,-1/6,-1/3).

Rule R0: large side opposite pi-corner (current). R1/R2: large = side CW/CCW from
pi-corner (uniform handedness). For each rule: build transitions, DFS closed walks
(LMAX=26, CAP=3), classify frozen, report distinct classes. Success = rule
reproducing t in {0, -1/6, -1/3} (tolerance: exact fraction match).
"""
import pickle, math, time, sys
from itertools import product
import snappy
import flipper.kernel.triangulation3 as T3m

WDIR = "output/artifacts"
V = snappy.Manifold(f"{WDIR}/V_flipper_veering.tri")
D = pickle.load(open(f"{WDIR}/track_data.pkl", "rb"))
C = pickle.load(open(f"{WDIR}/corner_data.pkl", "rb"))
branches = D["branches"]; data = D["gluing_data"]
NB = len(branches); NT = len(data)
MC = C["corners"]["M"]; LC = C["corners"]["L"]
WSTAR = {0: 2, 1: 3, 2: 0, 3: 1}
bkey = {}
for b, members in enumerate(branches):
    for s in members:
        bkey[s] = b
VM = T3m.VERTICES_MEETING; EL = T3m.EXIT_CUSP_LEFT; ER = T3m.EXIT_CUSP_RIGHT
flow = lambda A, Bb: 0 if (A < 0) == (Bb < 0) else (A if (A < 0) != (A < -Bb) else -Bb)
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
assert inter(MC, LC) == -1

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

def large_side(v, rule):
    # sides of triangle (.,v): {j != v}. pi-corner w*=WSTAR[v]; opposite side j=w*.
    # rule 0: j = w*. rule 1/2: the other two sides (ordered by sorted W position).
    W = sorted(w for w in range(4) if w != v)
    opp = WSTAR[v]
    others = [j for j in range(4) if j != v and j != opp]
    if rule == 0:
        return opp
    # handedness: order (opp, others...) hmm need canonical: sides sorted; pick by index offset
    sides = sorted(j for j in range(4) if j != v)
    k = sides.index(opp)
    return sides[(k + rule) % 3]

def run_rule(rule, LMAX=26, CAP=3, tlim=600):
    slist, sindex = [], {}
    for b, members in enumerate(branches):
        ((i1, v1), j1), ((i2, v2), j2) = members
        for (tb, sb) in [((i1, v1), j1), ((i2, v2), j2)]:
            sindex[(b, tb, sb)] = len(slist)
            slist.append((b, tb, sb))
    NS = len(slist)
    trans = [[] for _ in range(NS)]
    for si, (b, tb, sb) in enumerate(slist):
        L = large_side(tb[1], rule)
        smalls = [j for j in range(4) if j != tb[1] and j != L]
        for se in (smalls if sb == L else [L]):
            b2 = bkey[(tb, se)]
            m2 = branches[b2]
            nxt = m2[1] if m2[0] == (tb, se) else m2[0]
            trans[si].append((sindex[(b2, (nxt[0][0], nxt[0][1]), nxt[1])], se))
    TRI = [s[1] for s in slist]; ENT = [s[2] for s in slist]; BR = [s[0] for s in slist]
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
        TE = {(i, s_, o): E.get((i, s_, o), 0) for i in range(NT) for s_ in range(4) for o in range(4)}
        return -inter(TE, LC), inter(TE, MC)
    def zung_t(a, b):
        d = 6 * b - a
        return float('inf') if d == 0 else -b / d
    seen, hits = set(), {}
    t0 = time.time()
    for s0 in range(NS):
        useb = [0] * NB; path = [s0]; useb[BR[s0]] = 1
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
                    continue
                if depth + 1 >= LMAX or useb[BR[ns]] >= CAP:
                    continue
                useb[BR[ns]] += 1; path.append(ns); stack.append((ns, depth + 1, 0))
            else:
                stack.pop(); useb[BR[si]] -= 1; path.pop()
        if time.time() - t0 > tlim:
            break
    return seen, hits

rule = int(sys.argv[1])
LMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 26
CAP = int(sys.argv[3]) if len(sys.argv) > 3 else 3
seen, hits = run_rule(rule, LMAX, CAP)
print(f"RULE {rule}: distinct {len(seen)}", flush=True)
for k in sorted(hits, key=lambda x: (x[1] if isinstance(x[1], float) else 999, x[2])):
    print(f"  class {k[0]} t={k[1]} len {k[2]} x{hits[k]}", flush=True)
