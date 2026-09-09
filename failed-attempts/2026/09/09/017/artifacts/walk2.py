"""Correct directed strand walk for fat-graph diagrams. State (e,side): stand at
end `side` of edge e, travel to other end, pass through crossing, repeat."""
import sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-314/output/artifacts')
from build_diag import build_pretzel


def link_components(cr, edges):
    port_edge = {}
    for c, d in cr.items():
        for p, e in d['ports'].items():
            port_edge[(c, p)] = e
    pair = {}
    for c, d in cr.items():
        oi, oo = d['over']; ui, uo = d['under']
        pair[(c, oi)] = (c, oo); pair[(c, oo)] = (c, oi)
        pair[(c, ui)] = (c, uo); pair[(c, uo)] = (c, ui)
    # edge side index lookup
    side_of = {}
    for e, ends in edges.items():
        for i, end in enumerate(ends):
            side_of[(e, end)] = i
    seen = set(); comps = []
    for e, ends in edges.items():
        for s in (0, 1):
            if (e, s) in seen:
                continue
            L = 0; cur = (e, s)
            while cur not in seen:
                seen.add(cur); L += 1
                ce, cs = cur
                (c_arr, p_arr) = edges[ce][1 - cs]   # travel along edge
                (c2, p2) = pair[(c_arr, p_arr)]       # through crossing
                e2 = port_edge[(c2, p2)]
                cur = (e2, side_of[(e2, (c2, p2))])   # stand at departure end
            comps.append(L)
    return len(comps), sorted(comps)


if __name__ == '__main__':
    for m in range(7):
        cr, edges, cols = build_pretzel((3, 3, -(2 + m)))
        print('m=%d' % m, link_components(cr, edges))
