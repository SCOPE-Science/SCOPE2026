"""PD-code (KnotTheory X-notation) -> fat-graph + bracket. Bounded step: build + test."""
import sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-314/output/artifacts')
from math import comb


def pd_from_X(chords, nstrand_init=30):
    # X[i,j,k,l]: incoming lower, incoming upper?, standard KnotTheory: X[a,b,c,d] =
    # edges a,b,c,d counterclockwise starting at incoming UNDER strand? Convention:
    # X[i,j,k,l]: strand i enters from below-left going to k (upper?), j to l...
    # KnotTheory doc: X[a,b,c,d] with a = lower incoming, b = lower outgoing?? Use:
    # crossing with incoming under = a, outgoing under = c? Standard: 'Xijkl: incoming
    # under-strand is i, outgoing under is j?? ' We calibrate empirically on 8_19.
    # Model: 4 directed half-edges; over strand: l->j? under: i->k? (KnotTheory: 'the
    # edge coming in from below is i, counterclockwise j,k,l; over-strand is j->l'? )
    # Try option: over: (k)->(i)?? We try all consistent wirings and pick by Jones match.
    raise NotImplementedError


# KnotTheory X[a,b,c,d]: edge a arrives at crossing as the LOWER (under) incoming,
# then counterclockwise: b is the lower OUTGOING (under continues a->c?)...
# Doc (KnotTheory manual): 'X[i,j,k,l] represents a crossing with incoming edge i,
# outgoing edge j, incoming edge k, outgoing edge l where i,k are the lower strand'?
# We implement generic: strands (a->c) and (b->d); over = one of them. Try variants.
def build_from_X(chords, over_choice):
    cr = {}; edges = {}
    def E(x):
        if x not in edges:
            edges[x] = []
        return x
    for ci, (a, b, c, d) in enumerate(chords):
        cn = ci + 1
        E(a); E(b); E(c); E(d)
        edges[a].append((cn, 'in0')); edges[b].append((cn, 'in1'))
        edges[c].append((cn, 'out0')); edges[d].append((cn, 'out1'))
        # strands: in0->out0 (a->c), in1->out1 (b->d)
        if over_choice == 'ac':
            over, under = (('in0', 'out0')), (('in1', 'out1'))
        else:
            over, under = (('in1', 'out1')), (('in0', 'out0'))
        cr[cn] = {'over': over, 'under': under,
                  'ends': {'in0': (a, cn), 'in1': (b, cn), 'out0': (c, cn), 'out1': (d, cn)}}
    return cr, edges


def circles_X(cr, edges, choice, P0, P1):
    parent = {}
    def ff(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    def uu(a, b):
        ra, rb = ff(a), ff(b)
        if ra != rb:
            parent[ra] = rb
    pts = []
    for c, d in cr.items():
        for p in ('in0', 'in1', 'out0', 'out1'):
            parent[(c, p)] = (c, p); pts.append((c, p))
    # edge gluings: edge x connects its occurrence list; each edge has exactly 2 ends
    occ = {}
    for c, d in cr.items():
        for p, (x, _) in d['ends'].items():
            occ.setdefault(x, []).append((c, p))
    for x, L in occ.items():
        assert len(L) == 2, (x, L)
        uu(L[0], L[1])
    for c, d in cr.items():
        oi, oo = d['over']; ui, uo = d['under']
        P = P0(oi, oo, ui, uo) if choice[c] == 0 else P1(oi, oo, ui, uo)
        uu((c, P[0][0]), (c, P[0][1])); uu((c, P[1][0]), (c, P[1][1]))
    return len(set(ff(s) for s in pts))


def bracket_X(cr, edges, P0, P1):
    N = len(cr); cl = sorted(cr); res = {}
    for mask in range(1 << N):
        ch = {}; a = 0
        for i, c in enumerate(cl):
            b = (mask >> i) & 1; ch[c] = b
            if b == 0:
                a += 1
        k = circles_X(cr, edges, ch, P0, P1)
        base = a - (N - a); e = k - 1
        for j in range(e + 1):
            res[base + 2 * j - 2 * (e - j)] = res.get(base + 2 * j - 2 * (e - j), 0) + comb(e, j) * ((-1) ** e)
    return res


def writhe_X(cr, edges):
    # orient: walk; crossing sign from (over,in->out) x (under,in->out) with orientation
    # build adjacency: at crossing, strand mates
    occ = {}
    for c, d in cr.items():
        for p, (x, _) in d['ends'].items():
            occ.setdefault(x, []).append((c, p))
    # directed walk over (edge, end-index)
    # state: (x, k) standing at occurrence k of edge x, travel to other occurrence, through crossing
    pair = {}
    for c, d in cr.items():
        oi, oo = d['over']; ui, uo = d['under']
        pair[(c, oi)] = (c, oo); pair[(c, oo)] = (c, oi)
        pair[(c, ui)] = (c, uo); pair[(c, uo)] = (c, ui)
    other = {}
    for x, L in occ.items():
        other[(x, 0)] = (x, 1); other[(x, 1)] = (x, 0)
    at = {(x, k): occ[x][k] for x in occ for k in (0, 1)}
    seen = set(); cur = None
    for x in occ:
        cur = (x, 0); break
    over_dir = {}; under_dir = {}
    # abstract positions for direction: assign each port a vector; sign only needs relative orientation:
    # use planar embedding unknown -> CANNOT compute writhe from abstract PD without geometry!
    return None


if __name__ == '__main__':
    # 8_19 PD from KnotAtlas
    raw = [(4, 2, 5, 1), (8, 4, 9, 3), (9, 15, 10, 14), (5, 13, 6, 12),
           (13, 7, 14, 6), (11, 1, 12, 16), (15, 11, 16, 10), (2, 8, 3, 7)]
    P0 = lambda a, b, c, d: [(a, c), (b, d)]
    P1 = lambda a, b, c, d: [(a, d), (b, c)]
    for over_choice in ('ac', 'bd'):
        cr, edges = build_from_X(raw, over_choice)
        for name, Q0, Q1 in [('P0=A', P0, P1), ('P1=A', P1, P0)]:
            B = bracket_X(cr, edges, Q0, Q1)
            print(over_choice, name, dict(sorted(B.items())))
