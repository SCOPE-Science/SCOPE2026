"""Clean walk for pretzel fat-graph. Appends component census to WORKLOG."""
import sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-314/output/artifacts')
from build_diag import build_pretzel

def components(cr, edges):
    # half-edge walk: state (c,p); edge e=d['ports'][p] leads to other end (c2,p2); then pair through crossing
    end_of = {}
    for e, ends in edges.items():
        assert len(ends) == 2, (e, ends)
        (c1, p1), (c2, p2) = ends
        end_of[(c1, p1)] = (e, (c2, p2))
        end_of[(c2, p2)] = (e, (c1, p1))
    pair = {}
    for c, d in cr.items():
        oi, oo = d['over']; ui, uo = d['under']
        pair[(c, oi)] = (c, oo); pair[(c, oo)] = (c, oi)
        pair[(c, ui)] = (c, uo); pair[(c, uo)] = (c, ui)
    seen = set(); comps = 0; comp_len = []
    for c, d in cr.items():
        for p in ('NW', 'NE', 'SE', 'SW'):
            if (c, p) in seen:
                continue
            comps += 1; L = 0
            cur = (c, p)
            while cur not in seen:
                seen.add(cur); L += 1
                e, (c2, p2) = end_of[cur]
                cur = pair[(c2, p2)]
            comp_len.append(L)
    return comps, comp_len

if __name__ == '__main__':
    for m in range(7):
        cr, edges, cols = build_pretzel((3, 3, -(2 + m)))
        nc, lens = components(cr, edges)
        print('m=%d crossings=%d edges=%d components=%d lens=%s' % (m, len(cr), len(edges), nc, lens))
    # calibrations
    for ns in [(1,1,1),(2,0,0),(2,2,-2),(3,3,-2),(5,1,-2)]:
        cr, edges, cols = build_pretzel(ns)
        nc, lens = components(cr, edges)
        print('ns=%s components=%d lens=%s' % (ns, nc, lens))
