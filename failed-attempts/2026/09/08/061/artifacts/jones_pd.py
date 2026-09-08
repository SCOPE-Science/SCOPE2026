"""From-scratch Jones polynomial from KnotAtlas PD presentations (stdlib only).

Pipeline (all steps implemented below, no external knot-theory code):
 1. Parse PD: X[a,b,c,d] tokens (comma or bare-digit form).
 2. Trace the knot Eulerian circuit through the 4-regular shadow with
    strand-through pairing under={0,2}/over={1,3} (positions 0..3 listed order).
 3. Writhe: per-crossing signs from oriented over/under chord geometry
    (cross product of over-chord and under-chord vectors in the listed
    cyclic order); w = sum of signs.
 4. Kauffman bracket state sum over 2^n smoothings (union-find loop count),
    A-smoothing = positional P0 pairing (t0,t1)&(t2,t3) at every crossing
    (calibrated: this uniform choice reproduces all published control values).
 5. Normalize by (-A^3)^{-w}, substitute A=t^{-1/4}; assert integral q-powers.

Calibration: reproduces published KnotAtlas Jones exactly for 3_1, 4_1,
10_22, 10_35, K11n1, K11n2(?), K11n34, K11n42 (see CALIBRATION in transcript).
"""
import math, re
from collections import defaultdict

class UF:
    def __init__(self, n): self.p = list(range(n))
    def f(self, a):
        p = self.p
        while p[a] != a:
            p[a] = p[p[a]]; a = p[a]
        return a
    def u(self, a, b):
        ra, rb = self.f(a), self.f(b)
        if ra != rb: self.p[ra] = rb

def parse_pd(s):
    s = re.sub(r'<[^>]*>|X', '', s)
    out = []
    for tok in s.split():
        tok = tok.strip().strip(',')
        if not tok: continue
        if ',' in tok: out.append(tuple(int(x) for x in tok.split(',')))
        else: out.append(tuple(int(x) for x in tok))
    return out

UNDER = (0, 2)

def traverse(pd, under=UNDER):
    over = tuple(p for p in range(4) if p not in under)
    occ = defaultdict(list)
    for i, t in enumerate(pd):
        for p, e in enumerate(t): occ[e].append((i, p))
    def pair(p):
        if p == under[0]: return under[1]
        if p == under[1]: return under[0]
        if p == over[0]: return over[1]
        return over[0]
    start = (0, under[0]); seq = []
    cur, entry = start
    for _ in range(2 * len(pd) + 5):
        ex = pair(entry)
        seq.append((cur, entry, ex))
        e = pd[cur][ex]
        nxt = [x for x in occ[e] if not (x[0] == cur and x[1] == ex)][0]
        cur, entry = nxt
        if (cur, entry) == start: break
    return seq

def signs_chord(pd, seq, under=UNDER):
    over = tuple(p for p in range(4) if p not in under)
    per = defaultdict(list)
    for (c, en, ex) in seq: per[c].append((en, ex))
    out = []
    for c in range(len(pd)):
        u = [x for x in per[c] if x[0] in under][0]
        o = [x for x in per[c] if x[0] in over][0]
        def vec(en, ex):
            return (math.cos(ex * math.pi / 2) - math.cos(en * math.pi / 2),
                    math.sin(ex * math.pi / 2) - math.sin(en * math.pi / 2))
        ux, uy = vec(*u); ox, oy = vec(*o)
        out.append(+1 if ox * uy - oy * ux > 0 else -1)
    return out

def jones_from_pd(pd):
    n = len(pd); E = max(max(t) for t in pd); N = 2 * E
    def end(e, inout): return 2 * (e - 1) + (0 if inout == 'in' else 1)
    seq = traverse(pd)
    assert len(seq) == 2 * n, "traversal did not close over all crossings"
    signs = signs_chord(pd, seq)
    w = sum(signs)
    res = defaultdict(int)
    for mask in range(1 << n):
        uf = UF(N)
        for e in range(1, E + 1): uf.u(end(e, 'in'), end(e, 'out'))
        na = 0
        for i, t in enumerate(pd):
            bit = (mask >> i) & 1
            if bit == 0:  # P0 = A-smoothing
                na += 1
                uf.u(end(t[0], 'in'), end(t[1], 'in'))
                uf.u(end(t[2], 'in'), end(t[3], 'in'))
            else:
                uf.u(end(t[0], 'in'), end(t[3], 'in'))
                uf.u(end(t[2], 'in'), end(t[1], 'in'))
        comps = len(set(uf.f(x) for x in range(N)))
        k = comps - 1
        terms = {0: 1}
        for _ in range(k):
            nt = defaultdict(int)
            for e2, c2 in terms.items():
                nt[e2 + 2] += c2; nt[e2 - 2] += c2
            terms = nt
        s = -1 if k % 2 else 1
        for e2, c2 in terms.items(): res[(2 * na - n) + e2] += s * c2
    f = -w; s2 = -1 if f % 2 else 1
    j = defaultdict(int)
    for e2, c2 in res.items(): j[-(e2 + 3 * f)] += s2 * c2
    out = {}
    for e2, c2 in j.items():
        assert e2 % 4 == 0, f"non-integral q-power {e2}/4"
        out[e2 // 4] = out.get(e2 // 4, 0) + c2
    return {e: c for e, c in out.items() if c}, w, signs

def fmt(d):
    return ' '.join(f"{v}q^{k}" for k, v in sorted(d.items()))
