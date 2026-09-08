"""Planar TL-tangle calculator: exact Kauffman bracket for braid closures and JW turnbacks.
Elements: formal combos {pairing on 2m points (top 0..m-1, bottom m..2m-1): poly}.
Stack (compose), crossing elements, closure trace. Closed under planar composition.
"""
from collections import defaultdict

ONE = {0: 1}
D = {2: -1, -2: -1}

def padd(a, b):
    c = dict(a)
    for e, v in b.items():
        c[e] = c.get(e, 0) + v
        if c[e] == 0: del c[e]
    return c

def pmul(a, b):
    if not a or not b: return {}
    c = defaultdict(int)
    for e1, v1 in a.items():
        for e2, v2 in b.items(): c[e1+e2] += v1*v2
    return {e: v for e, v in c.items() if v != 0}

def dpow(k):
    r = {0: 1}
    for _ in range(k): r = pmul(r, D)
    return r

def ident(m):
    return tuple(sorted([(j, m+j) for j in range(m)]))

def E_tangle(m, i):
    """TL generator E_i as pairing: top pair (i,i+1), bottom pair (m+i,m+i+1), rest straight."""
    pairs = [(i, i+1), (m+i, m+i+1)]
    for j in range(m):
        if j in (i, i+1): continue
        pairs.append((j, m+j))
    return tuple(sorted(pairs))

def stack(m, A, B):
    """Compose tangles A (above) and B (below): glue A.bottom to B.top. Returns (C, loops)."""
    # labels: A.top = T (0..m-1), A.bot/B.top = M (m..2m-1 ~ 0..m-1 positions), B.bot = Bot.
    # UF over T(0..m-1), M(0..m-1 as m..2m-1), Bot(0..m-1 as 2m..3m-1).
    par = list(range(3*m))
    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry: par[rx] = ry
    for (x, y) in A:
        xa = x if x < m else (x-m)+m  # A.top x in 0..m-1 -> T; A.bot in m..2m-1 -> M
        ya = y if y < m else (y-m)+m
        union(xa, ya)
    for (x, y) in B:
        xb = (x+m) if x < m else (x-m)+2*m  # B.top -> M; B.bot -> Bot
        yb = (y+m) if y < m else (y-m)+2*m
        union(xb, yb)
    # read off T-Bot pairing + count middle-only loops
    # partner of each T point among T∪Bot; middle-only components = loops
    seen_mid = set()
    loops = 0
    # components touching M only (not T, not Bot)
    comps = defaultdict(list)
    for x in range(3*m):
        comps[find(x)].append(x)
    pairs = []
    for r, members in comps.items():
        T = [x for x in members if x < m]
        Md = [x for x in members if m <= x < 2*m]
        Bt = [x for x in members if x >= 2*m]
        if not T and not Bt:
            # middle-only: must be a closed loop (even # points, all valence 2? assume loop: +1)
            loops += 1
        else:
            # exactly 2 of T∪Bot expected (planar tangles: pairings compose to pairing + loops)
            tb = T + Bt
            assert len(tb) == 2, f"non-pairing composition: {tb}"
            a, b = tb
            a = a if a < m else a-2*m+m  # Bot label back to m..2m-1
            b = b if b < m else b-2*m+m
            pairs.append((min(a, b), max(a, b)))
    return tuple(sorted(pairs)), loops

class Tangle:
    def __init__(self, m, terms=None):
        self.m = m
        self.terms = terms or {ident(m): dict(ONE)}  # pairing -> poly
    def __mul__(self, other):
        assert self.m == other.m
        out = {}
        for pa, wa in self.terms.items():
            for pb, wb in other.terms.items():
                pc, loops = stack(self.m, pa, pb)
                w = pmul(pmul(wa, wb), dpow(loops))
                out[pc] = padd(out.get(pc, {}), w)
        return Tangle(self.m, {p: w for p, w in out.items() if w})
    def __add__(self, other):
        out = dict(self.terms)
        for p, w in other.terms.items():
            out[p] = padd(out.get(p, {}), w)
        return Tangle(self.m, {p: w for p, w in out.items() if w})
    def scale(self, poly):
        return Tangle(self.m, {p: pmul(w, poly) for p, w in self.terms.items() if pmul(w, poly)})

def crossing_tangle(m, g):
    i = abs(g)-1
    pos = g > 0
    I = Tangle(m)
    E = Tangle(m, {E_tangle(m, i): dict(ONE)})
    if pos:
        return I.scale({1: 1}).__add__(E.scale({-1: 1}))
    else:
        return I.scale({-1: 1}).__add__(E.scale({1: 1}))

def closure_bracket(m, tang):
    """Markov trace: glue top to bottom, count circles. Returns unnormalized bracket poly."""
    tot = {}
    for p, w in tang.terms.items():
        par = list(range(2*m))
        def find(x):
            while par[x] != x:
                par[x] = par[par[x]]; x = par[x]
            return x
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry: par[rx] = ry
        for (x, y) in p: union(x, y)
        for j in range(m): union(j, m+j)
        nb = len(set(find(x) for x in range(2*m)))
        tot = padd(tot, pmul(w, dpow(nb-1)))
    return tot

def braid_bracket(m, word):
    t = Tangle(m)
    for g in word:
        t = t * crossing_tangle(m, g)
    return closure_bracket(m, t)

def e_insert(m, s):
    """TL E_{2s} tangle (for JW turnback on cable pair s)."""
    return Tangle(m, {E_tangle(m, 2*s): dict(ONE)})

def to_jones(br, word):
    from collections import defaultdict as dd
    w = sum(1 if g > 0 else -1 for g in word)
    f = dd(int)
    for e, c in br.items(): f[e-3*w] += c*((-1)**(-w))
    q = dd(int)
    for e, c in f.items():
        if e % 4 != 0: return None
        q[-e//4] += c
    return dict(q)

if __name__ == "__main__":
    import sys; sys.path.insert(0, 'output/artifacts')
    print("trefoil:", to_jones(braid_bracket(2, [-1,-1,-1]), [-1,-1,-1]), "expect {-4:-1,-3:1,-1:1}")
    print("cable tiny plain:", dict(sorted(braid_bracket(4, [2,1,3,2]))), "brute {2:-1,10:-1}")
    from jw_cable import cable_word
    m2, cw = cable_word([1], 2, "braid")
    t = Tangle(m2)
    for g in cw: t = t * crossing_tangle(m2, g)
    t_turn = e_insert(m2, 0) * t  # e at top
    print("cable tiny turnback:", dict(sorted(closure_bracket(m2, t_turn))), "brute {2:-1,6:1,8:1}")
