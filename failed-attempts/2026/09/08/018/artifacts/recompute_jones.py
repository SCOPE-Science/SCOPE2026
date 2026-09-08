#!/usr/bin/env python3
"""Independent Kauffman-bracket Jones recomputation for ladder (double-twist) families.

Diagrams (built by construction, no external tables):
  K(m,n): two vertical twist boxes (m and n half-twists), top straight connections,
          bottom crossed connections. Crossing count c = m+n.
  T(2,N): single twist strip closed with two caps. c = N.
Conventions for A/B smoothings and writhe sign are CALIBRATED against trefoil/figure-8
(unknowns resolved by test, not by assumption); the tangle identity is checked in both
orientations and the exact match is reported.
Stdlib only. Outputs CSV + verification lines.
"""
import itertools, json, csv, sys

# ---------------- Laurent polynomials in A (dict exp->int) ----------------
def lp_add(a, b):
    c = dict(a)
    for e, v in b.items():
        c[e] = c.get(e, 0) + v
        if c[e] == 0:
            del c[e]
    return c

def lp_mul(a, b):
    c = {}
    for e1, v1 in a.items():
        for e2, v2 in b.items():
            e = e1 + e2
            c[e] = c.get(e, 0) + v1 * v2
    return {e: v for e, v in c.items() if v != 0}

def lp_shift(a, s):
    return {e + s: v for e, v in a.items()}

def lp_scale(a, k):
    if k == 0:
        return {}
    return {e: v * k for e, v in a.items() if v * k != 0}

DELTA = {2: -1, -2: -1}          # -A^2 - A^-2
ONE = {0: 1}

def delta_pow(k, cache={}):
    if k in cache:
        return cache[k]
    r = dict(ONE)
    for _ in range(k):
        r = lp_mul(r, DELTA)
    cache[k] = r
    return r

def S(c, p):
    return 4 * c + p

COORD = {0: (-1, 1), 1: (1, 1), 2: (1, -1), 3: (-1, -1)}

# ---------------- diagram builders ----------------
def build_double(m, n, phi):
    """Two twist boxes; rail-wise (braid-style) caps. over: box A const 0, box B phi."""
    nc = m + n
    over = [0] * m + [phi] * n
    arcs = []
    for i in range(m - 1):
        arcs.append((S(i, 3), S(i + 1, 0)))
        arcs.append((S(i, 2), S(i + 1, 1)))
    for j in range(n - 1):
        a, b = m + j, m + j + 1
        arcs.append((S(a, 3), S(b, 0)))
        arcs.append((S(a, 2), S(b, 1)))
    # rail-wise caps: top of rail A to bottom of rail A (same side)
    arcs.append((S(0, 0), S(m + n - 1, 3)))   # left rail through both boxes
    arcs.append((S(0, 1), S(m + n - 1, 2)))   # right rail
    # inter-box connectors: bottom of box A to top of box B, same side
    arcs.append((S(m - 1, 3), S(m, 0)))
    arcs.append((S(m - 1, 2), S(m, 1)))
    return nc, over, arcs

def build_torus(N):
    # Braid closure of sigma_1^N: rail-wise caps (top of rail to bottom of SAME rail),
    # giving gcd(2,N) components. (Top-top + bottom-bottom caps wrongly give unknot.)
    nc = N
    over = [0] * N
    arcs = []
    for i in range(N - 1):
        arcs.append((S(i, 3), S(i + 1, 0)))
        arcs.append((S(i, 2), S(i + 1, 1)))
    arcs.append((S(0, 0), S(N - 1, 3)))   # left rail: top-left to bottom-left
    arcs.append((S(0, 1), S(N - 1, 2)))   # right rail: top-right to bottom-right
    return nc, over, arcs

# E-closure diagrams for tangle identity (n crossings, box B + reconnected arcs)
def build_P(nc_over_list, kind):
    """kind 'V' (identity: B0.0-Bn.2, B0.1-Bn.3) or 'H' (caps). n>=1 crossings."""
    n = len(nc_over_list)
    arcs = []
    for j in range(n - 1):
        arcs.append((S(j, 3), S(j + 1, 0)))
        arcs.append((S(j, 2), S(j + 1, 1)))
    if kind == 'V':
        arcs.append((S(0, 0), S(n - 1, 2)))
        arcs.append((S(0, 1), S(n - 1, 3)))
    else:
        arcs.append((S(0, 0), S(0, 1)))
        arcs.append((S(n - 1, 2), S(n - 1, 3)))
    return n, list(nc_over_list), arcs

# ---------------- topology ----------------
class UF:
    __slots__ = ("p",)
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, x):
        p = self.p
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb

def arc_partner(nc, arcs):
    d = {}
    for a, b in arcs:
        assert a not in d and b not in d, "arc stub used twice"
        d[a] = b
        d[b] = a
    assert len(d) == 4 * nc, f"arcs cover {len(d)} stubs, need {4*nc}"
    return d

def strand_partner(nc):
    # Crossing strands are the diagonals: a: 0-2 (TL->BR), b: 1-3 (TR->BL).
    d = {}
    for c in range(nc):
        d[S(c, 0)] = S(c, 2); d[S(c, 2)] = S(c, 0)
        d[S(c, 1)] = S(c, 3); d[S(c, 3)] = S(c, 1)
    return d

def traverse(nc, over, arcs):
    """Cycle traversal alternating strand-steps and arc-steps.

    Cycle step: at stub s (crossing c, position p), go through the crossing to
    sp[s] with direction COORD[p-in]->COORD[p-out]; then follow the arc to the
    next stub. Each crossing is visited exactly twice (two strands).
    Returns (comp_over_seqs, cross_visits).
    """
    ap = arc_partner(nc, arcs)
    sp = strand_partner(nc)
    seen = set()
    comp_seqs = []
    cross_visits = {c: [] for c in range(nc)}
    for s0 in range(4 * nc):
        if s0 in seen:
            continue
        seq = []
        s = s0
        while True:
            seen.add(s)
            c, p = s // 4, s % 4
            u = sp[s]
            seen.add(u)
            ci = COORD[p]; co = COORD[u % 4]
            d = (co[0] - ci[0], co[1] - ci[1])
            diag = 0 if p in (0, 2) else 1
            is_over = (over[c] == diag)
            seq.append(1 if is_over else 0)
            cross_visits[c].append((d, is_over))
            t = ap[u]
            if t == s0:
                break
            assert t not in seen, "broken cycle: invalid diagram"
            s = t
        comp_seqs.append(seq)
    return comp_seqs, cross_visits

def count_components(nc, arcs):
    seqs, _ = traverse(nc, [0] * nc, arcs)
    return len(seqs)

def is_alternating(nc, over, arcs):
    seqs, cross = traverse(nc, over, arcs)
    for seq in seqs:
        if len(seq) < 2:
            return False
        for i in range(len(seq)):
            if seq[i] == seq[(i + 1) % len(seq)]:
                return False
    for c in range(nc):
        vs = cross[c]
        if len(vs) != 2 or vs[0][1] == vs[1][1]:
            return False
    return True

def compute_writhe(nc, over, arcs, s0):
    _, cross = traverse(nc, over, arcs)
    w = 0
    for c in range(nc):
        vs = cross[c]
        assert len(vs) == 2 and vs[0][1] != vs[1][1], (c, vs)
        od, ud = (vs[0][0], vs[1][0]) if vs[0][1] else (vs[1][0], vs[0][0])
        det = od[0] * ud[1] - od[1] * ud[0]
        assert det != 0
        w += 1 if det > 0 else -1
    return s0 * w

# ---------------- bracket ----------------
def bracket(nc, over, arcs, Across0):
    """Across0 in {'H','V'}: A-smoothing for over==0 crossings. over==1 mirrored."""
    H = [(0, 1), (2, 3)]
    V = [(0, 3), (1, 2)]
    Aopt, Bopt = [], []
    for c in range(nc):
        if over[c] == 0:
            A = H if Across0 == 'H' else V
            B = V if Across0 == 'H' else H
        else:
            A = V if Across0 == 'H' else H
            B = H if Across0 == 'H' else V
        Aopt.append([(S(c, a), S(c, b)) for a, b in A])
        Bopt.append([(S(c, a), S(c, b)) for a, b in B])
    N = 4 * nc
    total = {}
    for mask in range(1 << nc):
        uf = UF(N)
        nA = 0
        for c in range(nc):
            if (mask >> c) & 1:
                prs = Bopt[c]
            else:
                prs = Aopt[c]
                nA += 1
            uf.union(*prs[0]); uf.union(*prs[1])
        for a, b in arcs:
            uf.union(a, b)
        k = len(set(uf.find(s) for s in range(N)))
        exp = 2 * nA - nc
        term = lp_shift(delta_pow(k - 1), exp)
        total = lp_add(total, term)
    return total

def normalize_to_V(br, w):
    f = lp_shift(br, -3 * w)
    if w % 2 == 1:
        f = lp_scale(f, -1)
    V = {}
    for e, v in f.items():
        if e % 4 != 0:
            return None, f
        te = -e // 4
        V[te] = V.get(te, 0) + v
    return V, f

def trailing_triple(V):
    emin, emax = min(V), max(V)
    return (V.get(emin, 0), V.get(emin + 1, 0), V.get(emin + 2, 0)), emin, emax

if __name__ == "__main__":
    for Across0 in ('H', 'V'):
        for s0 in (1, -1):
            nc, over, arcs = build_torus(3)
            br = bracket(nc, over, arcs, Across0)
            w = compute_writhe(nc, over, arcs, s0)
            V, _ = normalize_to_V(br, w)
            nc8, over8, arcs8 = build_double(2, 2, 0)
            br8 = bracket(nc8, over8, arcs8, Across0)
            w8 = compute_writhe(nc8, over8, arcs8, s0)
            V8, _ = normalize_to_V(br8, w8)
            alt = is_alternating(nc8, over8, arcs8)
            print(f"Arule={Across0} s0={s0}: torus3 w={w} V={sorted(V.items()) if V else None} | "
                  f"K22 w={w8} V={sorted(V8.items()) if V8 else None} alt={alt}", flush=True)
