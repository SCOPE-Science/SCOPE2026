"""Braid-closure toolkit for exact Jones (Kauffman bracket) + Alexander (Fox/Wirtinger).
Pure Python + sympy only. All polynomials exact (integer arithmetic).
Mirror convention: fixed internally; equalities/inequalities are convention-consistent.
"""
import itertools
from fractions import Fraction

# ---------- polynomial helpers (dict-based, integer exponents) ----------
def poly_clean(d):
    return {e: c for e, c in d.items() if c != 0}

def poly_add(a, b):
    r = dict(a)
    for e, c in b.items():
        r[e] = r.get(e, 0) + c
    return poly_clean(r)

def poly_mul_scalar(a, s):
    if s == 0:
        return {}
    return poly_clean({e: c * s for e, c in a.items()})

def poly_shift(a, k):
    return {e + k: c for e, c in a.items()}

def poly_key(d):
    return tuple(sorted(d.items()))

# ---------- braid combinatorics ----------
def strand_positions(s, word):
    """word = list of (i, e), i in 1..s-1, e=+-1. Returns final position p[j] for strand starting at j."""
    pos_of_strand = list(range(s))
    for (i, e) in word:
        a = i - 1
        # swap strands at positions a, a+1
        s_at_a = [st for st in range(s) if pos_of_strand[st] == a][0]
        s_at_b = [st for st in range(s) if pos_of_strand[st] == a + 1][0]
        pos_of_strand[s_at_a], pos_of_strand[s_at_b] = a + 1, a
    return pos_of_strand  # p[j]

def closure_components(s, word):
    """Components of braid closure: cycles of strand connectivity. Returns list of cycles (lists of strand ids)."""
    p = strand_positions(s, word)
    seen = [False] * s
    comps = []
    for j in range(s):
        if not seen[j]:
            cyc = []
            k = j
            while not seen[k]:
                seen[k] = True
                cyc.append(k)
                k = p[k]
            comps.append(cyc)
    return comps

def n_components(s, word):
    return len(closure_components(s, word))

def writhe(word):
    return sum(e for (_, e) in word)

# ---------- Kauffman bracket state sum ----------
# Level-segment model: nodes (l, j), l=0..m gaps, j=0..s-1 positions. Total S=s*(m+1).
# Unions: continuations (non-involved positions), closure (gap m <-> gap 0),
#         smoothing pairings at each crossing (geometry depends on sign + state bit).
# Convention (standard): A-smoothing (bit 0, coeff A) is vertical (parallel) for +
# crossings and horizontal (cup-cap) for - crossings. Calibrated so a positive
# kink has bracket -A^{+3} (Reidemeister I) and RII/RIII hold.

class UF:
    __slots__ = ("p", "r")
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n
    def find(self, x):
        p = self.p
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x
    def union(self, a, b):
        p, r = self.p, self.r
        a = self.find(a); b = self.find(b)
        if a == b:
            return
        if r[a] < r[b]:
            a, b = b, a
        p[b] = a
        if r[a] == r[b]:
            r[a] += 1
    def count(self):
        return len(set(self.find(i) for i in range(len(self.p))))

def bracket_circles(s, word, state):
    """state: int bitmask, bit l (0=A,1=B) for crossing l. Returns # circles."""
    m = len(word)
    S = s * (m + 1)
    uf = UF(S)
    def node(l, j):
        return l * s + j
    # continuations + smoothings
    for l in range(m):
        i, e = word[l]
        a = i - 1  # positions a, a+1 involved
        b = state[l]  # 0/1
        # geometry: horizontal means (top a <-> top a+1) and (bottom a <-> bottom a+1)
        # vertical means (top a <-> bottom a) and (top a+1 <-> bottom a+1)
        if e == 1:
            horiz = (b == 1)
        else:
            horiz = (b == 0)
        if horiz:
            uf.union(node(l, a), node(l, a + 1))
            uf.union(node(l + 1, a), node(l + 1, a + 1))
        else:
            uf.union(node(l, a), node(l + 1, a))
            uf.union(node(l, a + 1), node(l + 1, a + 1))
        for j in range(s):
            if j != a and j != a + 1:
                uf.union(node(l, j), node(l + 1, j))
    # closure: gap m <-> gap 0
    for j in range(s):
        uf.union(node(m, j), node(0, j))
    return uf.count()

def bracket_poly(s, word):
    """Unnormalized Kauffman bracket <L> as dict {A-exp: coeff} (integers)."""
    m = len(word)
    from collections import defaultdict
    acc = defaultdict(int)
    for mask in range(1 << m):
        n1 = bin(mask).count("1")
        n0 = m - n1
        pw = n0 - n1  # A^(n0-n1)
        state = [(mask >> l) & 1 for l in range(m)]
        c = bracket_circles(s, word, state)
        # contribution: A^pw * d^(c-1), d = -A^2 - A^-2
        # expand d^(c-1)
        if c == 0:
            continue
        # d^k expansion
        dk = {0: 1}
        for _ in range(c - 1):
            nd = defaultdict(int)
            for ex, cf in dk.items():
                nd[ex + 2] += cf * (-1)
                nd[ex - 2] += cf * (-1)
            dk = dict(nd)
        for ex, cf in dk.items():
            acc[pw + ex] += cf
    return poly_clean(dict(acc))

def jones_poly_general(s, word):
    """Normalized Jones V(t) for any braid closure (knots or links).
    Returns dict {t-exp (int for knots, Fraction for links): coeff}."""
    from fractions import Fraction
    m = len(word)
    br = bracket_poly(s, word)
    w = writhe(word)
    sgn = -1 if (w % 2 != 0) else 1
    acc = {}
    for ex, cf in br.items():
        acc[ex - 3 * w] = acc.get(ex - 3 * w, 0) + (cf * sgn if w % 2 else cf)
    acc = poly_clean(acc)
    res = {}
    for ex, cf in acc.items():
        q, r = divmod(ex, 4)
        # divmod: ex = 4*q + r, r in 0..3; t-exp = -ex/4
        te = Fraction(-ex, 4)
        res[te] = res.get(te, 0) + cf
    return poly_clean(res)

def jones_poly(s, word):
    """Normalized Jones V(t) for knot closures as dict {t-exp(int): coeff}.
    V = (-A^3)^(-w) <L>, t = A^-4. Asserts exponents divisible by 4 (knots)."""
    m = len(word)
    br = bracket_poly(s, word)
    w = writhe(word)
    # multiply by (-A^3)^(-w) = (-1)^(-w) A^(-3w) = (-1)^w A^{-3w} (since (-1)^{-w}=(-1)^w)
    sgn = -1 if (w % 2 != 0) else 1
    # (-1)^w factor: if w odd, multiply by -1
    acc = {}
    for ex, cf in br.items():
        acc[ex - 3 * w] = acc.get(ex - 3 * w, 0) + (cf * sgn if w % 2 else cf)
    acc = poly_clean(acc)
    # substitute A = t^{-1/4}: t-exp = -Aexp/4
    res = {}
    for ex, cf in acc.items():
        if ex % 4 != 0:
            raise ValueError(f"non-divisible A exponent {ex} (link? non-knot?)")
        res[-ex // 4] = res.get(-ex // 4, 0) + cf
    return poly_clean(res)

def jones_span(jp):
    if not jp:
        return None
    return max(jp) - min(jp)

# ---------- alternation traversal ----------
def traversal_over_under(s, word):
    """Walk each closure component; return list per component of 'O'/'U' at successive crossing visits.
    Convention: sigma_i^{+1}: strand from position i (left) OVER strand from i+1 (right)."""
    m = len(word)
    # current position per strand-start? Walk components: state = (gap l, position j, direction down/up).
    # Simplify: walk with (level l, pos j) moving downward through braid, wrapping via closure.
    # Track visited (l, j, dir) to decompose into components; record crossing visits in order per component.
    # Crossing l sits between gap l and gap l+1, involving positions a=i-1,a+1.
    # Moving down from (l, j): if crossing l involves j, pass through it to (l+1, j') where j' = mirror (a<->a+1),
    #   recording O/U (over iff (j==a and e==+1) or (j==a+1 and e==-1)).
    #   else move to (l+1, j) silently.
    # Moving down from gap m wraps to gap 0 (closure, silent). (Orientation: all braid strands down, closures up;
    #   our walk goes down through braid then wraps; full component loop alternates down-runs and wraps.)
    # Since walk only moves down+wrap, each component is a cycle; visits recorded in traversal order.
    visited = [[False] * s for _ in range(m + 1)]
    comp_seqs = []
    for l0 in range(m + 1):
        for j0 in range(s):
            if visited[l0][j0]:
                continue
            # walk cycle starting at (l0, j0) moving down
            seq = []
            l, j = l0, j0
            while not visited[l][j]:
                visited[l][j] = True
                if l == m:
                    l, j = 0, j  # closure wrap (silent)
                    continue
                i, e = word[l]
                a = i - 1
                if j == a or j == a + 1:
                    over = ((j == a and e == 1) or (j == a + 1 and e == -1))
                    seq.append('O' if over else 'U')
                    j = a + 1 if j == a else a
                    l = l + 1
                else:
                    l, j = l + 1, j
            if seq:
                comp_seqs.append(seq)
    return comp_seqs

def is_alternating_diagram(s, word):
    seqs = traversal_over_under(s, word)
    for seq in seqs:
        n = len(seq)
        if n == 0:
            continue
        for k in range(n):
            if seq[k] == seq[(k + 1) % n]:
                return False
    return True

# ---------- PD edges + diagram primality (no 2-edge cut) ----------
def pd_edges(s, word):
    """Maximal arcs between crossings (merge continuations + closure). Returns:
    edges: list of dicts {members:[(l,j)], ends:[(crossing, slot)]}; edge_endpoints for graph.
    Each edge has exactly 2 ends (possibly same crossing)."""
    m = len(word)
    S = s * (m + 1)
    uf = UF(S)
    def node(l, j):
        return l * s + j
    for l in range(m):
        i, e = word[l]
        a = i - 1
        for j in range(s):
            if j != a and j != a + 1:
                uf.union(node(l, j), node(l + 1, j))
    for j in range(s):
        uf.union(node(m, j), node(0, j))
    # group
    from collections import defaultdict
    groups = defaultdict(list)
    for l in range(m + 1):
        for j in range(s):
            groups[uf.find(node(l, j))].append((l, j))
    # find ends of each group: member (l,j) is incident to crossing above (l-1, if l>=1 and crossing l-1 involves j)
    # and/or crossing below (l, if l<m and crossing l involves j). Each incidence is an end.
    edges = []
    for root, members in groups.items():
        ends = []
        for (l, j) in members:
            if l >= 1:
                ii, ee = word[l - 1]
                aa = ii - 1
                if j == aa or j == aa + 1:
                    ends.append((l - 1, j))
            if l <= m - 1:
                ii, ee = word[l]
                aa = ii - 1
                if j == aa or j == aa + 1:
                    ends.append((l, j))
        edges.append({"members": members, "ends": ends})
    return edges

def is_diagram_prime(s, word):
    """Brute-force: no pair of PD edges whose removal disconnects crossings into two nonempty sets.
    (Conservative diagram-primeness for knots; returns True if prime.)"""
    m = len(word)
    if m <= 1:
        return True
    edges = pd_edges(s, word)
    # sanity: each edge 2 ends
    for ed in edges:
        if len(ed["ends"]) != 2:
            return False  # malformed (shouldn't happen); treat as non-prime/fail
    E = len(edges)
    # adjacency per edge: pair of crossings (c1, c2)
    adj = []
    for ed in edges:
        c1 = ed["ends"][0][0]; c2 = ed["ends"][1][0]
        adj.append((c1, c2))
    # for each pair of edges, remove and BFS from crossing 0 over remaining adjacency
    import collections
    for a in range(E):
        for b in range(a + 1, E):
            parent = list(range(m))
            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x
            def union(x, y):
                rx, ry = find(x), find(y)
                if rx != ry:
                    parent[ry] = rx
            for k in range(E):
                if k == a or k == b:
                    continue
                union(adj[k][0], adj[k][1])
            r0 = find(0)
            if any(find(c) != r0 for c in range(m)):
                # removal disconnects -> composite signal.
                return False
    return True

def linking_number(s, word):
    """Linking data: returns (ncomp, comp_of_strand, lk) with lk = half signed
    inter-component crossing sum for 2-component closures (else None).
    All braid strands oriented downward (each component oriented accordingly)."""
    from fractions import Fraction
    comps = closure_components(s, word)
    comp_of = {}
    for ci, cyc in enumerate(comps):
        for st in cyc:
            comp_of[st] = ci
    pos_strand = list(range(s))
    inter = 0
    for (i, e) in word:
        a = i - 1
        sA, sB = pos_strand[a], pos_strand[a + 1]
        if comp_of[sA] != comp_of[sB]:
            inter += e
        pos_strand[a], pos_strand[a + 1] = sB, sA
    lk = Fraction(inter, 2) if len(comps) == 2 else None
    return len(comps), comp_of, lk

def is_split_diagram(s, word):
    """True if the PD shadow graph is disconnected (split diagram)."""
    m = len(word)
    if m == 0:
        return n_components(s, word) > 1
    edges = pd_edges(s, word)
    for ed in edges:
        if len(ed["ends"]) != 2:
            return True
    parent = list(range(m))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx
    for ed in edges:
        union(ed["ends"][0][0], ed["ends"][1][0])
    return any(find(c) != find(0) for c in range(m))

# ---------- Alexander via Fox/Wirtinger (abelianized Jacobian minor) ----------
def alexander_poly(s, word):
    """Single-variable Alexander for knot braid closures via Wirtinger+Fox.
    Returns normalized symmetric dict {t-exp: coeff} with Δ(1)=1, Δ(t)=Δ(t^-1).
    Uses sympy for determinant."""
    import sympy as sp
    m = len(word)
    if m == 0:
        return {0: 1}
    t = sp.Symbol("t")
    edges = pd_edges(s, word)
    E = len(edges)
    # Map each PD-edge index -> its two ends. Build over/under info per crossing:
    # At crossing l involving positions a,a+1: the 4 incident PD edges: top-a, top-a+1, bottom-a, bottom-a+1.
    # Identify which edge index corresponds to each. Then over-pair = (top-j, bottom-j') per over strand.
    # Over strand: e=+1 -> left strand (top-a to bottom-(a+1)); e=-1 -> right strand (top-(a+1) to bottom-a).
    # Under strand: the other diagonal.
    # Wirtinger arcs: merge over-pairs (union PD edges through over-pass).
    parent = list(range(E))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx
    # For each crossing, find edge idx at each of 4 slots. Slot of edge end: match (crossing, position).
    from collections import defaultdict
    slot_to_edge = {}
    for idx, ed in enumerate(edges):
        for (c, j) in ed["ends"]:
            slot_to_edge[(c, j)] = idx
    cross_info = []
    for l in range(m):
        i, e = word[l]
        a = i - 1
        try:
            eTA = slot_to_edge[(l, a)]
            eTB = slot_to_edge[(l, a + 1)]
        except KeyError:
            raise ValueError("slot map incomplete (top)")
        # bottom slots: ends listed as (l, j) for bottom too (same crossing index). Distinguish top vs bottom:
        # Our ends list doesn't distinguish top/bottom! Both top-a and bottom-a map to (l, a). AMBIGUOUS.
        # => Need refined ends with side info. Rebuild below.
        cross_info.append(None)
    # Rebuild edges with side info (top/bottom). Redo grouping but record side per end.
    S = s * (m + 1)
    uf = UF(S)
    def node(l, j):
        return l * s + j
    for l in range(m):
        i, e = word[l]
        a = i - 1
        for j in range(s):
            if j != a and j != a + 1:
                uf.union(node(l, j), node(l + 1, j))
    for j in range(s):
        uf.union(node(m, j), node(0, j))
    groups = defaultdict(list)
    for l in range(m + 1):
        for j in range(s):
            groups[uf.find(node(l, j))].append((l, j))
    # assign edge indices
    roots = list(groups.keys())
    r2i = {r: k for k, r in enumerate(roots)}
    E2 = len(roots)
    # end incidence with side: for member (l,j): top-incidence if l>=1 and crossing l-1 involves j (side='bottom' of crossing l-1);
    # bottom-incidence if l<=m-1 and crossing l involves j (side='top' of crossing l).
    # Represent end as (crossing c, side, position j).
    edge_ends = [[] for _ in range(E2)]
    for r, members in groups.items():
        k = r2i[r]
        for (l, j) in members:
            if l >= 1:
                ii, ee = word[l - 1]
                aa = ii - 1
                if j == aa or j == aa + 1:
                    edge_ends[k].append((l - 1, "B", j))
            if l <= m - 1:
                ii, ee = word[l]
                aa = ii - 1
                if j == aa or j == aa + 1:
                    edge_ends[k].append((l, "T", j))
    for k in range(E2):
        if len(edge_ends[k]) != 2:
            raise ValueError(f"edge {k} has {len(edge_ends[k])} ends")
    # slot map with side
    slot = {}
    for k in range(E2):
        for end in edge_ends[k]:
            slot[end] = k
    # Wirtinger merge through over-pass + collect relation data
    parent = list(range(E2))
    def f2(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def u2(x, y):
        rx, ry = f2(x), f2(y)
        if rx != ry:
            parent[ry] = rx
    rels = []  # per crossing: (over_arc_root, under_in_root, under_out_root, hand)
    for l in range(m):
        i, e = word[l]
        a = i - 1
        eTA = slot[(l, "T", a)]; eTB = slot[(l, "T", a + 1)]
        eBA = slot[(l, "B", a)]; eBB = slot[(l, "B", a + 1)]
        if e == 1:
            over_pair = (eTA, eBB)   # left strand over: top-a to bottom-(a+1)
            under_in, under_out = eTB, eBA  # right strand under: top-(a+1) in (from top), bottom-a out
        else:
            over_pair = (eTB, eBA)   # right strand over
            under_in, under_out = eTA, eBB
        u2(*over_pair)
        rels.append((over_pair, under_in, under_out, e))
    # arc labels
    arc_of = {}
    arcs = {}
    for k in range(E2):
        r = f2(k)
        if r not in arcs:
            arcs[r] = len(arcs)
        arc_of[k] = arcs[r]
    A = len(arcs)
    # Build Fox matrix (m relations x A arcs). Relation at crossing: outgoing = over^{hand} * incoming * over^{-hand}?
    # Use r = o*u_in*o^{-1}*u_out^{-1} for e=+1; r = o^{-1}*u_in*o*u_out^{-1} for e=-1.
    # Abelianized Fox derivatives (all generators -> t):
    # For r = o u o^{-1} v^{-1} (v=u_out): dr/do = 1 - o u o^{-1} -> 1-t; dr/du = o -> t; dr/dv = -o u o^{-1} v^{-1} -> -1.
    #   (since abelianized values: o,u,v -> t; o u o^{-1} -> t.)
    # For r = o^{-1} u o v^{-1}: dr/do = -o^{-1} + o^{-1} u -> -t^{-1} + 1 = 1 - t^{-1}; dr/du = o^{-1} -> t^{-1}; dr/dv = -1.
    M = sp.zeros(m, A)
    for l in range(m):
        (o1, o2), uin, uout, e = rels[l]
        ao = arc_of[f2(o1)]
        au = arc_of[f2(uin)]
        av = arc_of[f2(uout)]
        if e == 1:
            M[l, ao] = M[l, ao] + (1 - t)
            M[l, au] = M[l, au] + t
            M[l, av] = M[l, av] + (-1)
        else:
            M[l, ao] = M[l, ao] + (1 - t**(-1))
            M[l, au] = M[l, au] + t**(-1)
            M[l, av] = M[l, av] + (-1)
    # delete last row+column -> (m-1)x(m-1) minor... but A should equal m for knots; assert.
    if A != m:
        raise ValueError(f"arc count {A} != crossings {m} (non-knot or bad diagram?)")
    Mm = M.extract(list(range(m - 1)), list(range(A - 1)))
    det = sp.simplify(Mm.det())
    # Crowell--Fox: for a Wirtinger presentation with one (redundant) relation
    # removed, an (m-1)x(m-1) minor determinant equals +/-t^k * Delta(t)
    # directly (no further division). Verified on trefoil: minor det = 1-t+t^2.
    q = det
    # normalize q to symmetric Alexander with q(1)=1... q = u*Delta, u=±t^k.
    # Clear to Laurent poly dict
    q = sp.expand(q)
    # get coeffs: use Poly after multiplying by t^N
    for N in range(0, 40):
        try:
            p = sp.Poly(sp.expand(q * t**N), t)
            coeffs = {k[0] - N: int(c) for k, c in p.as_dict().items()}
            coeffs = {e: c for e, c in coeffs.items() if c != 0}
            break
        except Exception:
            continue
    else:
        raise ValueError("cannot convert Alexander to poly")
    # fix sign so that coeffs at... evaluate at 1 > 0
    s1 = sum(coeffs.values())
    if s1 < 0:
        coeffs = {e: -c for e, c in coeffs.items()}
        s1 = -s1
    # symmetrize: find shift k so poly symmetric: exponents e+k with min+max symmetric about 0
    if not coeffs:
        raise ValueError("empty Alexander")
    emin, emax = min(coeffs), max(coeffs)
    shift = -(emin + emax) / 2
    # shift must be half-integer or integer; apply by shifting keys (allow Fraction, then require integers)
    from fractions import Fraction as Fr
    newc = {}
    for e, c in coeffs.items():
        ne = Fr(e) + Fr(shift).limit_denominator(2)
        if ne.denominator != 1:
            raise ValueError("cannot symmetrize Alexander to integer exponents")
        newc[int(ne)] = c
    coeffs = newc
    # verify symmetry; if not symmetric, try harder (shouldn't happen for knots)
    if tuple(sorted(coeffs.items())) != tuple(sorted({-e: c for e, c in coeffs.items()}.items())):
        # try negating shift parity? raise
        raise ValueError(f"Alexander not symmetric after normalization: {coeffs}")
    # scale so value at 1 is 1 (should already be ±1; fix)
    s1 = sum(coeffs.values())
    if s1 == -1:
        coeffs = {e: -c for e, c in coeffs.items()}
    elif s1 != 1:
        raise ValueError(f"Alexander(1)={s1}, expected ±1")
    return poly_clean(coeffs)
