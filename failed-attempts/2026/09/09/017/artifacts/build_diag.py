"""Build pretzel P(3,3,-(2+m)) diagrams as fat-graph PD. Self-contained, stdlib only."""
import json

def build_pretzel(ns, xs=(0.0, 10.0, 20.0), bot_shift=1):
    cr = {}      # c -> dict(pos, ports{port:edge}, over:(pin,pout), under:(pin,pout))
    edges = {}   # e -> [(c1,p1),(c2,p2)]
    eid = [0]; cid = [0]
    def new_edge(a=None):
        eid[0] += 1
        edges[eid[0]] = [] if a is None else [a]
        return eid[0]
    def reg(e, c, p):
        edges[e].append((c, p))
    cols = []
    for i, n in enumerate(ns):
        x = xs[i]; s = 1 if n > 0 else -1
        topL = new_edge(); topR = new_edge()
        s0, s1 = topL, topR
        for k in range(1, abs(n) + 1):
            cid[0] += 1; c = cid[0]; y = -float(k)
            eSE = new_edge(); eSW = new_edge()
            # ports: NW=s0, NE=s1, SE=eSE, SW=eSW
            if s > 0:
                over, under = ('NW', 'SE'), ('NE', 'SW')
            else:
                over, under = ('NE', 'SW'), ('NW', 'SE')
            cr[c] = {'pos': (x, y), 'ports': {'NW': s0, 'NE': s1, 'SE': eSE, 'SW': eSW},
                     'over': over, 'under': under, 'colsign': s}
            reg(s0, c, 'NW'); reg(s1, c, 'NE'); reg(eSE, c, 'SE'); reg(eSW, c, 'SW')
            s0, s1 = eSW, eSE
        cols.append({'topL': topL, 'topR': topR, 'botL': s0, 'botR': s1})
    # pretzel closure: identify stubs pairwise (share edge id via merge)
    def merge(e_keep, e_drop):
        for end in edges[e_drop]:
            edges[e_keep].append(end)
        del edges[e_drop]
        for c, d in cr.items():
            for p, e in d['ports'].items():
                if e == e_drop:
                    d['ports'][p] = e_keep
        for col in cols:
            for k in ('topL', 'topR', 'botL', 'botR'):
                if col[k] == e_drop:
                    col[k] = e_keep
    # top cycle: TR1-TL2, TR2-TL3, TR3-TL1 ; bottom: BR1-BL2, BR2-BL3, BR3-BL1
    merge(cols[0]['topR'], cols[1]['topL'])
    merge(cols[1]['topR'], cols[2]['topL'])
    merge(cols[2]['topR'], cols[0]['topL'])
    if bot_shift == 'caps':
        for c in range(3):
            merge(cols[c]['botL'], cols[c]['botR'])
    else:
        merge(cols[0]['botR'], cols[(0 + bot_shift) % 3]['botL'])
        merge(cols[1]['botR'], cols[(1 + bot_shift) % 3]['botL'])
        merge(cols[2]['botR'], cols[(2 + bot_shift) % 3]['botL'])
    return cr, edges, cols

def trace_components(cr, edges):
    # successor: arriving at crossing c via in-port p on edge e -> leave via matching out-port
    nxt = {}
    for c, d in cr.items():
        oi, oo = d['over']; ui, uo = d['under']
        nxt[(c, oi)] = d['ports'][oo]
        nxt[(c, oo)] = d['ports'][oi]
        nxt[(c, ui)] = d['ports'][uo]
        nxt[(c, uo)] = d['ports'][ui]
    # edge endpoints: edge -> [(c,p),(c2,p2)]
    visited = set(); comps = []
    orient = {}  # (c,p) arrival directed: store strand direction sign later
    for e, ends in edges.items():
        for side in (0, 1):
            if (e, side) in visited:
                continue
            # walk
            loop = []; cur = (e, side)
            while cur not in visited:
                visited.add(cur)
                loop.append(cur)
                ce, cs = cur
                ends2 = edges[ce]
                (c_here, p_here) = ends2[cs]
                e2 = nxt[(c_here, p_here)]
                ends3 = edges[e2]
                # arrive at other crossing via e2: find side index of end != (c_here,p_here) if e2==ce loop...
                # find which end of e2 is NOT the current departure; departure end is the one at c_here
                if len(ends3) != 2:
                    raise ValueError('non-closed edge')
                if ends3[0] == (c_here, p_here):
                    ns = 1
                elif ends3[1] == (c_here, p_here):
                    ns = 0
                else:
                    # e2 != ce always here (nxt gives different edge), so arrival end:
                    # arrival crossing = the end of e2 that is not c_here... e2 connects c_here to other
                    ns = 0 if ends3[0][0] != c_here or ends3[0] == (c_here, p_here) else 0
                    ns = 0 if ends3[0] != (c_here, ends3[0][1]) or True else 0
                    # generic: pick end whose crossing != c_here
                    ns = 0 if ends3[1][0] == c_here else 1
                    # careful: both ends could share crossing? not in our diagrams
                    if ends3[0][0] == c_here and ends3[1][0] == c_here:
                        raise ValueError('loop edge')
                    ns = 0 if ends3[1][0] == c_here else 1
                    # wait: arrival end = end NOT at c_here
                    ns = 1 if ends3[0][0] == c_here else 0
                cur = (e2, ns)
            comps.append(loop)
    return comps, nxt

if __name__ == '__main__':
    import sys
    m = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    ns = (3, 3, -(2 + m))
    cr, edges, cols = build_pretzel(ns)
    assert all(len(v) == 2 for v in edges.values()), 'open stubs remain'
    comps, nxt = trace_components(cr, edges)
    print('m=%d ns=%s crossings=%d edges=%d components=%d' % (m, ns, len(cr), len(edges), len(comps)))
    print('top edges: %s bot edges: %s' % ([cols[i]['topL'] for i in range(3)], [cols[i]['botL'] for i in range(3)]))
