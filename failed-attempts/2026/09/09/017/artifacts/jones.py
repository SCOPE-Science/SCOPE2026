"""Kauffman-bracket state sum -> Jones polynomial, from fat-graph diagrams.
Conventions (KnotAtlas): <L> bracket with <unknot>=1, <L u O> = (-A^2-A^-2)<L>;
A-smoothing (0) joins the regions swept by rotating over-strand CCW (standard);
writhe w; V(t) = ((-A)^(-3w) <L>)(t^{-1/4}), A = t^{1/4}.
Smoothing rule in fat-graph terms: at crossing with over strand (oi->oo) and
under (ui->ui... uo): A-smoothing connects oi-uo? We fix: A-smoothing pairs
(oi,ui)|(oo,uo) vs B-smoothing (oi,uo)|(oo,ui) — orientation of choice only
affects overall mirror; we CALIBRATE against known 8_19 Jones from topic.
State circles counted by union-find over 4N half-edge stubs.
"""
import sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-314/output/artifacts')
from build_diag import build_pretzel
from fractions import Fraction


def stubs(cr):
    for c, d in cr.items():
        for p in ('NW', 'NE', 'SE', 'SW'):
            yield (c, p)


def count_circles(cr, edges, choice, modeA):
    # choice[c] in (0,1): 0 -> pair modeA, 1 -> pair modeB
    # modeA pairs P0=[(oi,ui),(oo,uo)]; modeB pairs [(oi,uo),(oo,ui)]
    parent = {}
    def ff(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    def uu(a, b):
        ra, rb = ff(a), ff(b)
        if ra != rb:
            parent[ra] = rb
    for s in stubs(cr):
        parent[s] = s
    # edge gluings
    for e, ends in edges.items():
        (c1, p1), (c2, p2) = ends
        uu((c1, p1), (c2, p2))
    # smoothings
    for c, d in cr.items():
        oi, oo = d['over']; ui, uo = d['under']
        if choice[c] == 0:
            uu((c, modeA[0][0]), (c, modeA[0][1])); uu((c, modeA[1][0]), (c, modeA[1][1]))
        else:
            uu((c, P1[0][0]), (c, P1[0][1])); uu((c, P1[1][0]), (c, P1[1][1]))
    return len(set(ff(s) for s in stubs(cr)))


def bracket(cr, edges, modeA, P1):
    # returns dict exp(A) -> coeff of <L>
    N = len(cr)
    clist = sorted(cr)
    res = {}
    # iterate 2^N states; N<=14 so <=16384
    for mask in range(1 << N):
        a_ct = 0
        choice = {}
        for i, c in enumerate(clist):
            b = (mask >> i) & 1
            choice[c] = b
            if b == 0:
                a_ct += 1
        k = count_circles(cr, edges, choice, modeA, P1)
        # <L> contribution: A^(a-b) * (-A^2-A^-2)^(k-1)
        b_ct = N - a_ct
        base = a_ct - b_ct
        # expand (-A^2-A^-2)^(k-1)
        from math import comb
        e = k - 1
        for j in range(e + 1):
            c = comb(e, j) * ((-1) ** e)
            # term: (-1)^e A^{2j} A^{2(e-j)}? (-A^2)^j (-A^-2)^{e-j} = (-1)^e A^{2j-2(e-j)}
            exp = base + 2 * j - 2 * (e - j)
            res[exp] = res.get(exp, 0) + c
    return res


def count_circles2(cr, edges, choice, P0, P1):
    parent = {}
    def ff(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    def uu(a, b):
        ra, rb = ff(a), ff(b)
        if ra != rb:
            parent[ra] = rb
    for s in stubs(cr):
        parent[s] = s
    for e, ends in edges.items():
        (c1, p1), (c2, p2) = ends
        uu((c1, p1), (c2, p2))
    for c, d in cr.items():
        oi, oo = d['over']; ui, uo = d['under']
        P = P0(oi, oo, ui, uo) if choice[c] == 0 else P1(oi, oo, ui, uo)
        uu((c, P[0][0]), (c, P[0][1])); uu((c, P[1][0]), (c, P[1][1]))
    return len(set(ff(s) for s in stubs(cr)))


def bracket2(cr, edges, P0, P1):
    from math import comb
    N = len(cr)
    clist = sorted(cr)
    res = {}
    for mask in range(1 << N):
        a_ct = 0
        choice = {}
        for i, c in enumerate(clist):
            b = (mask >> i) & 1
            choice[c] = b
            if b == 0:
                a_ct += 1
        k = count_circles2(cr, edges, choice, P0, P1)
        b_ct = N - a_ct
        base = a_ct - b_ct
        e = k - 1
        for j in range(e + 1):
            c = comb(e, j) * ((-1) ** e)
            exp = base + 2 * j - 2 * (e - j)
            res[exp] = res.get(exp, 0) + c
    return res


def writhe(cr):
    # local crossing sign from geometry: over strand direction vs under.
    # Our crossings: strands run vertically (N-S). Column sign s=+1: over NW->SE, under NE->SW.
    # Orient: knot orientation unknown; but for a twist column both strands run same direction
    # (both down or both up)? In a 2-braid column, strands run ANTI-parallel (one down, one up)? No:
    # twist region of 2 parallel strands: oriented same direction gives writhe sum; standard twist knot clasp...
    # Instead compute writhe GLOBALLY after orienting the knot: walk the knot, assign directions.
    w, _ = oriented_writhe(cr, edges_global)
    return w


edges_global = None


def orient_and_writhe(cr, edges):
    # directed walk (from walk2 logic) gives orientation; crossing sign via right-hand rule
    port_edge = {}
    for c, d in cr.items():
        for p, e in d['ports'].items():
            port_edge[(c, p)] = e
    pair = {}
    for c, d in cr.items():
        oi, oo = d['over']; ui, uo = d['under']
        pair[(c, oi)] = (c, oo); pair[(c, oo)] = (c, oi)
        pair[(c, ui)] = (c, uo); pair[(c, uo)] = (c, ui)
    side_of = {}
    for e, ends in edges.items():
        for i, end in enumerate(ends):
            side_of[(e, end)] = i
    # walk one loop; record arrival direction at each crossing port
    start = None
    for e, ends in edges.items():
        start = (e, 0); break
    # direction vectors: port positions N=(0,1),S=(0,-1),E,W; strand travel dir through crossing:
    D = {'NW': (0, 1), 'NE': (0, 1), 'SW': (0, -1), 'SE': (0, -1)}
    # Actually travel direction along strand at crossing: from in-port to out-port.
    # over strand: oi->oo; under: ui->uo. With orientation, one of the two parallel traversals matches.
    # Simpler robust: oriented crossing sign = sign of (over_dir x under_dir) with over first:
    # need actual oriented dirs: determine orientation by walking.
    seen = set(); cur = start
    over_dir = {}; under_dir = {}
    while cur not in seen:
        seen.add(cur)
        ce, cs = cur
        (c_arr, p_arr) = edges[ce][1 - cs]
        (c2, p2) = pair[(c_arr, p_arr)]
        # strand segment: entered crossing c_arr at p_arr, exits at p2. Direction ~ (pos(p2)-pos(p_arr))
        PV = {'NW': (-1, 1), 'NE': (1, 1), 'SW': (-1, -1), 'SE': (1, -1)}
        v = (PV[p2][0] - PV[p_arr][0], PV[p2][1] - PV[p_arr][1])
        if (c_arr, p_arr) in (('x', 'x'),):
            pass
        oi, oo = cr[c_arr]['over']; ui, uo = cr[c_arr]['under']
        if (p_arr, p2) == (oi, oo) or (p_arr, p2) == (oo, oi):
            over_dir[c_arr] = v if (p_arr, p2) == (oi, oo) else (-v[0], -v[1])
        else:
            under_dir[c_arr] = v if (p_arr, p2) == (ui, uo) else (-v[0], -v[1])
        e2 = port_edge[(c2, p2)]
        cur = (e2, side_of[(e2, (c2, p2))])
    w = 0
    for c in cr:
        ox, oy = over_dir[c]; ux, uy = under_dir[c]
        det = ox * uy - oy * ux
        # crossing sign: +1 if (over x under) > 0? Standard: sign = +1 for RHC (over points E, under points N gives +1?)
        # Calibrate: positive twist column should give +1 per crossing for standard orientation.
        w += 1 if det > 0 else -1
    return w


def jones(cr, edges, P0, P1):
    from math import comb
    N = len(cr)
    clist = sorted(cr)
    res = {}
    for mask in range(1 << N):
        a_ct = 0
        choice = {}
        for i, c in enumerate(clist):
            b = (mask >> i) & 1
            choice[c] = b
            if b == 0:
                a_ct += 1
        k = count_circles2(cr, edges, choice, P0, P1)
        b_ct = N - a_ct
        base = a_ct - b_ct
        e = k - 1
        for j in range(e + 1):
            c = comb(e, j) * ((-1) ** e)
            exp = base + 2 * j - 2 * (e - j)
            res[exp] = res.get(exp, 0) + c
    # normalize: X = (-A)^(-3w) <L>; V(t): A = t^{1/4}
    w = orient_and_writhe(cr, edges)
    # multiply by (-A)^{-3w} = (-1)^{-3w} A^{-3w}
    sgn = (-1) ** (-3 * w)
    X = {}
    for exp, c in res.items():
        X[exp - 3 * w] = X.get(exp - 3 * w, 0) + sgn * c
    # convert A-exponents (multiples of... ) to t-exponents x = exp/4; drop zeros
    V = {}
    for exp, c in X.items():
        if c != 0:
            assert exp % 4 == 0, exp
            V[exp // 4] = c
    return V, w
