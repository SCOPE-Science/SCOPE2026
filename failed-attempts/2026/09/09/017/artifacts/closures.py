"""Enumerate pretzel-like closures: build columns, close with arbitrary stub pairing."""
import sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-314/output/artifacts')
from pbuilder import bracket_of, det_of_bracket, P0, P1


def columns(ns, internals, signs):
    cr = {}; edges = {}; eid = [0]; cid = [0]

    def new_edge(a=None):
        eid[0] += 1
        edges[eid[0]] = [] if a is None else [a]
        return eid[0]

    def reg(e, c, p):
        edges[e].append((c, p))

    stubs = {}
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
        stubs[(i, 'TL')] = topL; stubs[(i, 'TR')] = topR
        stubs[(i, 'BL')] = s0; stubs[(i, 'BR')] = s1
    return cr, edges, stubs


def close_and_bracket(ns, pairing, internals, signs):
    cr, edges, stubs = columns(ns, internals, signs)

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

    for a, b in pairing:
        merge(stubs[a], stubs[b])
        # union stub ids
        ea = stubs[a]
        for k, v in list(stubs.items()):
            if v == stubs[b]:
                stubs[k] = ea
    # check closed: every edge has 2 ends
    for e, ends in edges.items():
        if len(ends) != 2:
            return None
    return bracket_of(cr, edges, P0, P1)


def matchings(ns):
    if not ns:
        yield []
        return
    a = ns[0]
    for i in range(1, len(ns)):
        b = ns[i]
        rest = [x for j, x in enumerate(ns) if j != 0 and j != i]
        for m in matchings(rest):
            yield [(a, b)] + m


if __name__ == '__main__':
    stubs = [(c, e) for c in range(3) for e in ('TL', 'TR', 'BL', 'BR')]
    ns = (3, 3, -2)
    inter = ['cross', 'cross', 'straight']  # natural parities (odd->cross, even->straight)
    signs = [1, 1, -1]
    n = 0; hits = []
    for pairing in matchings(stubs):
        # pretzel-like: no within-column bridges; each bridge connects neighboring columns (ring)
        ok = True
        for a, b in pairing:
            if a[0] == b[0]:
                ok = False; break
            if abs(a[0] - b[0]) not in (1, 2):
                ok = False; break
        if not ok:
            continue
        n += 1
    print('pretzel-like closures:', n)
