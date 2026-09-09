"""Parametric pretzel builder: per-column internal pairing + signs. Persisted for reuse."""
import sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-314/output/artifacts')
from math import comb
import cmath


def build_param(ns, internals, signs=None):
    """ns: tuple of twist counts (abs = crossings). internals[i] in {'cross','straight'}:
    strand pairing TL-BL/TR-BR (straight) or TL-BR/TR-BL (cross).
    signs[i]: over/under assignment (+1 or -1) per column."""
    if signs is None:
        signs = [1 if n > 0 else -1 for n in ns]
    cr = {}; edges = {}; eid = [0]; cid = [0]

    def new_edge(a=None):
        eid[0] += 1
        edges[eid[0]] = [] if a is None else [a]
        return eid[0]

    def reg(e, c, p):
        edges[e].append((c, p))

    cols = []
    for i, n in enumerate(ns):
        s = signs[i]
        topL = new_edge(); topR = new_edge(); s0, s1 = topL, topR
        cross = (internals[i] == 'cross')
        rest_odd = ((abs(n) - 1) % 2 == 1)
        first = (cross != rest_odd)
        for k in range(abs(n)):
            cid[0] += 1; c = cid[0]
            eSE = new_edge(); eSW = new_edge()
            over = ('NW', 'SE') if s > 0 else ('NE', 'SW')
            under = ('NE', 'SW') if s > 0 else ('NW', 'SE')
            cr[c] = {'pos': (i * 10., -float(k)),
                     'ports': {'NW': s0, 'NE': s1, 'SE': eSE, 'SW': eSW},
                     'over': over, 'under': under, 'colsign': s}
            reg(s0, c, 'NW'); reg(s1, c, 'NE'); reg(eSE, c, 'SE'); reg(eSW, c, 'SW')
            sw = first if k == 0 else True
            if sw:
                s0, s1 = eSW, eSE
            else:
                s0, s1 = eSE, eSW
        cols.append({'topL': topL, 'topR': topR, 'botL': s0, 'botR': s1})

    def merge(ek, ed):
        if ek == ed:
            return
        for end in edges[ed]:
            edges[ek].append(end)
        del edges[ed]
        for c, d in cr.items():
            for p, e in d['ports'].items():
                if e == ed:
                    d['ports'][p] = ek

    merge(cols[0]['topR'], cols[1]['topL'])
    merge(cols[1]['topR'], cols[2]['topL'])
    merge(cols[2]['topR'], cols[0]['topL'])
    merge(cols[0]['botR'], cols[1]['botL'])
    merge(cols[1]['botR'], cols[2]['botL'])
    merge(cols[2]['botR'], cols[0]['botL'])
    return cr, edges


def bracket_of(cr, edges, P0, P1):
    N = len(cr); cl = sorted(cr); res = {}
    for mask in range(1 << N):
        ch = {}; a = 0
        for i, c in enumerate(cl):
            b = (mask >> i) & 1; ch[c] = b
            if b == 0:
                a += 1
        parent = {s: s for c in cr for s in [(c, 'NW'), (c, 'NE'), (c, 'SE'), (c, 'SW')]}
        def ff(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        def uu(x, y):
            rx, ry = ff(x), ff(y)
            if rx != ry:
                parent[rx] = ry
        for e, ends in edges.items():
            uu(ends[0], ends[1])
        for c, d in cr.items():
            oi, oo = d['over']; ui, uo = d['under']
            P = P0(oi, oo, ui, uo) if ch[c] == 0 else P1(oi, oo, ui, uo)
            uu((c, P[0][0]), (c, P[0][1])); uu((c, P[1][0]), (c, P[1][1]))
        k = len(set(ff(s) for s in parent))
        base = a - (N - a); e = k - 1
        for j in range(e + 1):
            res[base + 2 * j - 2 * (e - j)] = res.get(base + 2 * j - 2 * (e - j), 0) + comb(e, j) * ((-1) ** e)
    return res


def det_of_bracket(B):
    A = cmath.exp(-1j * cmath.pi / 4)
    return abs(sum(c * A ** k for k, c in B.items()))


P0 = lambda a, b, c, d: [(a, c), (b, d)]
P1 = lambda a, b, c, d: [(a, d), (b, c)]


if __name__ == '__main__':
    import itertools
    for combo in itertools.product('SC', repeat=3):
        inter = ['cross' if x == 'C' else 'straight' for x in combo]
        cr, edges = build_param((3, 3, -2), inter)
        B = bracket_of(cr, edges, P0, P1)
        nz = dict(sorted((k, v) for k, v in B.items() if v != 0))
        print(combo, 'det=%.3f' % det_of_bracket(B), nz)
