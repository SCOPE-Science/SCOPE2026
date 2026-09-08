"""From-scratch Jones polynomial via Kauffman bracket from PD codes (stdlib only).

PD convention (KnotAtlas/KnotTheory): X[i,j,k,l], edges CCW from incoming under-edge.
Under strand: i -> k (requires k == i+1 mod 2n). Over strand: j <-> l.
Two binary conventions calibrated jointly against KnotAtlas 3_1/4_1/5_2 (see CALIBRATION):
  SIGN: +1 iff over runs j -> l (i.e. l == j+1 mod 2n), else -1.
  A-smoothing at every crossing = pairing P:(i,j)+(k,l) [option 0]; B = Q:(i,l)+(j,k).
Bracket <D> = sum_states A^{a-b} (-A^2-A^-2)^{c-1}; f = (-A^3)^{-w}<D>; V(q) = f|_{A=q^{-1/4}}.
Two independent evaluations: (A) direct 2^n state sum with union-find circles;
(B) memoized skein recursion with walk-based circle counter. Must agree exactly.
"""
import itertools, re
from collections import defaultdict

def parse_pd(s):
    s = s.replace(',', ' ').replace('{',' ').replace('}',' ').replace('_',' ')
    return [tuple(map(int,t)) for t in re.findall(r'X\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)', s)]

def signs_of(pd):
    n = len(pd); m = 2*n; s = []
    for (i,j,k,l) in pd:
        assert k == (i % m) + 1, f"under-strand order violated at {(i,j,k,l)}"
        if j == (l % m) + 1: s.append(+1)
        elif l == (j % m) + 1: s.append(-1)
        else: raise ValueError(f"over-strand order violated at {(i,j,k,l)}")
    return s

class LP(dict):
    def add(self, o):
        r = LP(self)
        for e, c in o.items():
            r[e] = r.get(e, 0) + c
            if r[e] == 0: del r[e]
        return r
    def mul(self, o):
        r = LP()
        for e1, c1 in self.items():
            for e2, c2 in o.items():
                r[e1+e2] = r.get(e1+e2, 0) + c1*c2
        return LP({e: c for e, c in r.items() if c})

def circles_uf(pd, smooth):
    """Method-A counter: union-find over 4n half-edges."""
    parent = {}
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb: parent[ra] = rb
    for c, (i, j, k, l) in enumerate(pd):
        for e in (i, j, k, l): parent[(c, e)] = (c, e)
    for c, (i, j, k, l) in enumerate(pd):
        if smooth[c] == 0: union((c,i),(c,j)); union((c,k),(c,l))
        else: union((c,i),(c,l)); union((c,j),(c,k))
    edgepos = defaultdict(list)
    for c, (i, j, k, l) in enumerate(pd):
        for e in (i, j, k, l): edgepos[e].append((c, e))
    for e, locs in edgepos.items():
        assert len(locs) == 2, (e, locs)
        union(locs[0], locs[1])
    return len(set(find(a) for a in parent))

def circles_walk(pd, smooth):
    """Method-B counter: trace each loop explicitly (independent implementation)."""
    n = len(pd)
    hid = {}; k = 0
    for c, (i, j, k2, l) in enumerate(pd):
        for e in (i, j, k2, l): hid[(c, e)] = k; k += 1
    N = k; mate = [0]*N; across = [0]*N
    edgepos = defaultdict(list)
    for c, (i, j, k2, l) in enumerate(pd):
        for e in (i, j, k2, l): edgepos[e].append(hid[(c, e)])
        h = {e: hid[(c, e)] for e in (i, j, k2, l)}
        pairs = [(i,j),(k2,l)] if smooth[c] == 0 else [(i,l),(j,k2)]
        for a, b in pairs: mate[h[a]] = h[b]; mate[h[b]] = h[a]
    for e, (a, b) in edgepos.items(): across[a] = b; across[b] = a
    seen = [False]*N; circ = 0
    for s in range(N):
        if seen[s]: continue
        circ += 1; v = s
        while not seen[v]:
            seen[v] = True; v = mate[v]
            if not seen[v]: seen[v] = True; v = across[v]
    return circ

DLOOP = LP({2: -1, -2: -1})

def bracket_sum(pd):
    n = len(pd); res = LP({0: 1}); res = LP()
    for bits in itertools.product((0, 1), repeat=n):
        a = n - sum(bits); b = sum(bits)
        p = LP({0: 1})
        for _ in range(circles_uf(pd, bits) - 1): p = p.mul(DLOOP)
        q = LP({e + (a - b): c for e, c in p.items()})
        res = res.add(q)
    return res

def bracket_rec(pd):
    n = len(pd); memo = {}
    def rec(bits):
        if bits in memo: return memo[bits]
        if -1 not in bits:
            p = LP({0: 1})
            for _ in range(circles_walk(pd, bits) - 1): p = p.mul(DLOOP)
            memo[bits] = p; return p
        c = bits.index(-1)
        b0 = list(bits); b0[c] = 0; p0 = rec(tuple(b0))
        b1 = list(bits); b1[c] = 1; p1 = rec(tuple(b1))
        r = LP()
        for e, cf in p0.items(): r[e+1] = r.get(e+1, 0) + cf
        for e, cf in p1.items(): r[e-1] = r.get(e-1, 0) + cf
        r = LP({e: c_ for e, c_ in r.items() if c_})
        memo[bits] = r; return r
    return rec(tuple([-1]*n))

def to_jones(br, w):
    sgn = 1 if w % 2 == 0 else -1
    V = {}
    for e, c in br.items():
        assert (e - 3*w) % 1 == 0
        f = e - 3*w
        assert f % 4 == 0, f"bracket/normalization mismatch: exp {e}, w {w}"
        V[-f//4] = V.get(-f//4, 0) + sgn*c
    return {e: c for e, c in V.items() if c}

def jones_both(pd):
    s = signs_of(pd); w = sum(s)
    b1 = bracket_sum(pd); b2 = bracket_rec(pd)
    assert dict(b1) == dict(b2), f"method disagreement: {dict(b1)} vs {dict(b2)}"
    return w, to_jones(b1, w), dict(b1)

def fmt(V):
    parts = []
    for e in sorted(V):
        c = V[e]
        t = "1" if e == 0 else ("q" if e == 1 else ("q^{-1}" if e == -1 else f"q^{{{e}}}"))
        parts.append(f"{c:+d} {t}")
    return " ".join(parts).lstrip("+").replace("+ -", "- ")

if __name__ == "__main__":
    pd = [(1,4,2,5),(3,6,4,1),(5,2,6,3)]
    w, V, br = jones_both(pd)
    print("w =", w, "V =", fmt(V), " bracket=", br)
    print("atlas 3_1: -q^{-4} + q^{-3} + q^{-1}")
