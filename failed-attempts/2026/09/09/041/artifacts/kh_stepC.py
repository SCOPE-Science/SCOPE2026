"""Step C: orientation tour + crossing signs from PD cyclic order.
Convention (KnotTheory documented): X[a,b,c,d] lists edges counterclockwise;
strand a->c is the LOWER (incoming a, outgoing c), strand b->d is UPPER.
Tour: edges connect crossings; orient knot by walking strands (a<->c),(b<->d).
Sign rule: at crossing, let u = under direction (+1 if a->c else -1),
o = over direction (+1 if b->d else -1). Positions: a=0deg,b=90,c=180,d=270.
Under vector: from center toward outgoing end minus incoming... use tangent = out_pos - in_pos.
sign = sign of cross product (u_tangent x o_tangent)? Calibrate on trefoil to writhe -3.
"""
import json
from collections import defaultdict

def parse_pd(s):
    out = []
    for t in s.split():
        b = t[1:]
        out.append(tuple(int(x) for x in (b.split(',') if ',' in b else list(b))))
    return out

ANG = {}  # filled per crossing as a:0,b:90,c:180,d:270
import math
POS = {'a': 0.0, 'b': 90.0, 'c': 180.0, 'd': 270.0}

def orientation_and_signs(pd):
    n = len(pd)
    # map edge label -> list of (crossing_idx, end_name)
    occ = defaultdict(list)
    for k, (a, b, c, d) in enumerate(pd):
        for nm, e in zip('abcd', (a, b, c, d)):
            occ[e].append((k, nm))
    for e, v in occ.items():
        assert len(v) == 2, (e, v)
    # walk tour: state = (edge, at-crossing-idx). Start edge e0 at crossing k0 end nm0.
    # At crossing, pass through: nm -> pair(nm) (a<->c, b<->d), recording direction.
    # Then travel along new edge to its other crossing.
    pair = {'a': 'c', 'c': 'a', 'b': 'd', 'd': 'b'}
    e0 = pd[0][0]
    k0, nm0 = occ[e0][0]
    tour_edges = []  # sequence of edge labels traversed
    dirs = {}  # (k, end_nm) -> 'in' or 'out' along tour
    # direction of each strand traversal: (k, from_nm -> to_nm)
    traversals = []
    cur_k, cur_nm = k0, nm0
    # we enter crossing cur_k at end cur_nm? Define: we arrive on edge e0 at crossing cur_k.
    for _ in range(2 * n + 5):
        cr = pd[cur_k]
        to_nm = pair[cur_nm]
        traversals.append((cur_k, cur_nm, to_nm))
        new_edge = cr['abcd'.index(to_nm)]
        tour_edges.append(new_edge)
        # travel to other occurrence
        o = occ[new_edge]
        nxt = o[1] if (o[0][0] == cur_k and o[0][1] == to_nm) else o[0]
        # check consistency: if o[0] is current, go to o[1]
        if not (o[0][0] == cur_k and o[0][1] == to_nm) and not (o[1][0] == cur_k and o[1][1] == to_nm):
            raise RuntimeError('edge incidence broken')
        cur_k, cur_nm = nxt
        if cur_k == k0 and cur_nm == nm0:
            break
    return tour_edges, traversals

def signs_from_traversals(pd, traversals):
    # under strand ends a,c ; over ends b,d (hypothesis H1). Also try swapped H2.
    def sgn(H):
        out = []
        tov = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
        for (k, frm, to) in traversals:
            if (frm, to) in H['trajs']:
                pass
        return out
    return None

if __name__ == '__main__':
    for name, s in [('trefoil', 'X1425 X3641 X5263'),
                    ('10_124', 'X4251 X8493 X9,17,10,16 X5,15,6,14 X15,7,16,6 X11,19,12,18 X13,1,14,20 X17,11,18,10 X19,13,20,12 X2837')]:
        pd = parse_pd(s)
        te, tr = orientation_and_signs(pd)
        print(name, 'tour len', len(te), 'n=', len(pd))
        # per-crossing traversal directions
        byk = defaultdict(list)
        for (k, f, t) in tr:
            byk[k].append((f, t))
        for k in sorted(byk):
            print('  X%d' % k, pd[k], byk[k])
