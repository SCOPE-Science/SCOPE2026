#!/usr/bin/env python3
"""S1: Pretzel PD assembler + validators (stdlib only).
Diagram data: crossings[i] = {'under':[e1,e2], 'over':[e1,e2], 'box':i}.
"""
from collections import Counter


def build_pretzel(twists, mirror=False):
    E = [0]

    def new():
        E[0] += 1
        return E[0]

    t12, t23, tout = new(), new(), new()
    b12, b23, bout = new(), new(), new()
    tops = [(tout, t12), (t12, t23), (t23, tout)]
    bots = [(bout, b12), (b12, b23), (b23, bout)]
    crossings = []
    for i, n in enumerate(twists):
        TL, TR = tops[i]
        BL, BR = bots[i]
        A = [None] * (n + 1)
        B = [None] * (n + 1)
        A[0] = TL
        B[0] = TR
        for k in range(1, n):
            A[k] = new()
            B[k] = new()
        if n % 2 == 1:
            B[n] = BL
            A[n] = BR
        else:
            A[n] = BL
            B[n] = BR
        for k in range(n):
            if k % 2 == 0:
                over = [A[k], A[k + 1]]
                under = [B[k], B[k + 1]]
            else:
                over = [B[k], B[k + 1]]
                under = [A[k], A[k + 1]]
            if mirror:
                over, under = under, over
            crossings.append({'under': under, 'over': over, 'box': i,
                              'A0': A[0], 'B0': B[0], 'ch': -1 if mirror else 1})
    return crossings, E[0]


def build_ends(crossings):
    ends = {}
    for i, x in enumerate(crossings):
        a, b = x['under']
        ends.setdefault(a, []).append((i, 'U', b))
        ends.setdefault(b, []).append((i, 'U', a))
        a, b = x['over']
        ends.setdefault(a, []).append((i, 'O', b))
        ends.setdefault(b, []).append((i, 'O', a))
    return ends


def validate_incidences(crossings, nedges):
    c = Counter()
    for x in crossings:
        for e in x['under'] + x['over']:
            c[e] += 1
    assert set(c.keys()) == set(range(1, nedges + 1)), \
        'edge ids mismatch: %s' % (set(range(1, nedges + 1)) - set(c.keys()))
    assert all(v == 2 for v in c.values()), 'non-2 incidence present'
    return True


def traverse(crossings, ends):
    """Eulerian traversal. Returns (num_components, alternating, edge_dir, visits)."""
    seen = set()
    ncomp = 0
    alt_ok = True
    edge_dir = {}  # e -> (tail_rec, head_rec)
    for e0 in list(ends.keys()):
        for j0 in (0, 1):
            if (e0, j0) in seen:
                continue
            ncomp += 1
            e, j = e0, j0
            roles = []
            while True:
                if (e, j) in seen:
                    break
                seen.add((e, j))
                xi, role, partner = ends[e][j]
                roles.append(role)
                e2 = partner
                # find index of xi-end on e2
                j2 = 0 if ends[e2][0][0] == xi else 1
                # leave e2 via its OTHER end
                j2 = 1 - j2
                edge_dir[e2] = ((e2, 1 - j2), (e2, j2))
                e, j = e2, j2
                if (e, j) == (e0, j0):
                    break
                if len(roles) > 4 * len(crossings) + 10:
                    raise RuntimeError('traversal runaway')
            for a, b in zip(roles, roles[1:] + roles[:1]):
                if a == b:
                    alt_ok = False
    return ncomp, alt_ok, edge_dir


def box_parallel(crossings, ends, edge_dir, box, n):
    """Check whether box strands flow parallel (same vertical direction)."""
    xs = [x for x in crossings if x['box'] == box]
    top_xi = crossings.index(xs[0])
    A0 = xs[0]['A0']
    B0 = xs[0]['B0']

    def into_box(e):
        # True if traversal of e ends at this box's top crossing
        (t, _), (h, _) = edge_dir[e][0], edge_dir[e][1]
        # head end record:
        rec = ends[e][1] if edge_dir[e][1] == (e, 1) else ends[e][0]
        return rec[0] == top_xi

    return into_box(A0) == into_box(B0)


def writhe(crossings, ends, edge_dir):
    w = 0
    boxes = sorted(set(x['box'] for x in crossings))
    for b in boxes:
        par = box_parallel(crossings, ends, edge_dir, b, None)
        ch = [x['ch'] for x in crossings if x['box'] == b][0]
        s = ch if par else -ch
        w += s * sum(1 for x in crossings if x['box'] == b)
    return w


def report(name, twists, mirror=False):
    crossings, nedges = build_pretzel(twists, mirror=mirror)
    validate_incidences(crossings, nedges)
    ends = build_ends(crossings)
    assert all(len(v) == 2 for v in ends.values()), 'edge must have 2 ends'
    ncomp, alt_ok, edge_dir = traverse(crossings, ends)
    w = writhe(crossings, ends, edge_dir)
    print('%s twists=%s mirror=%s: edges=%d xings=%d directed=%d knots=%d alternating=%s writhe=%+d'
          % (name, twists, mirror, nedges, len(crossings), ncomp, ncomp//2, alt_ok, w))
    return crossings, nedges


if __name__ == '__main__':
    report('K10 ', [3, 3, 4], mirror=False)
    report('K11 ', [3, 3, 5], mirror=False)
    report('K11m', [3, 3, 5], mirror=True)
    print('S1-OK')
