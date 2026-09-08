#!/usr/bin/env python3
"""S2a: rotation system + face traversal + Euler check (stdlib only)."""
from pretzel import build_pretzel, build_ends


def rotation(crossings, ends):
    """Cyclic order of incident edge-ends at each crossing.
    Geometry: vertical twist boxes; cyclic order (A_k, B_k, B_{k+1}, A_{k+1}).
    Returns rot[xi] = list of 4 edge ids in cyclic order."""
    rot = []
    for xi, x in enumerate(crossings):
        # Determine A_k, B_k, A_{k+1}, B_{k+1} edge ids from construction:
        # even k: over=[A_k,A_{k+1}], under=[B_k,B_{k+1}]
        # odd k: over=[B_k,B_{k+1}], under=[A_k,A_{k+1}]
        # In both cases the POSITION order is (A_k,B_k,B_{k+1},A_{k+1}).
        k = xi - sum(1 for y in crossings[:xi] if y['box'] == x['box'])
        # recompute: find index within box
        boxxs = [y for y in crossings if y['box'] == x['box']]
        k = boxxs.index(x)
        if k % 2 == 0:
            Ak, Ak1 = x['over']
            Bk, Bk1 = x['under']
        else:
            Bk, Bk1 = x['over']
            Ak, Ak1 = x['under']
        cyc = [Ak, Bk, Ak1, Bk1]
        if k % 2 == 1:
            cyc = [Bk, Ak, Bk1, Ak1]
        rot.append(cyc)
    return rot


def faces(crossings, ends, rot):
    # half-edge id: (xi, slot); slot s corresponds to edge rot[xi][s].
    # partner: the other occurrence of the same edge.
    occ = {}
    for xi, cyc in enumerate(rot):
        for s, e in enumerate(cyc):
            occ.setdefault(e, []).append((xi, s))
    assert all(len(v) == 2 for v in occ.values())
    partner = {}
    for e, (h1, h2) in occ.items():
        partner[h1] = h2
        partner[h2] = h1
    unvisited = set(partner.keys())
    facelist = []
    while unvisited:
        h0 = next(iter(unvisited))
        f = []
        h = h0
        while True:
            unvisited.discard(h)
            f.append(h)
            xi, s = h
            # arrive at vertex xi via half-edge h; depart via next slot clockwise:
            # face rule: depart = predecessor of partner arrival? Use next-slot rule:
            # standard: next = (s + 1) % 4 after arriving through partner edge.
            # Here h is the half-edge AT xi; arrival came from partner(h).
            # Departure half-edge at same vertex: next cyclically, then follow partner.
            hdep = (xi, (s + 1) % 4)
            h = partner[hdep]
            if h == h0:
                break
            if len(f) > 4 * len(crossings) + 10:
                raise RuntimeError('face runaway')
        facelist.append(f)
    return facelist, partner


def check(name, twists, mirror=False):
    crossings, nedges = build_pretzel(twists, mirror=mirror)
    ends = build_ends(crossings)
    rot = rotation(crossings, ends)
    facelist, _ = faces(crossings, ends, rot)
    V, E, F = len(crossings), nedges, len(facelist)
    euler = V - E + F
    incid = sum(len(f) for f in facelist)
    print('%s twists=%s mirror=%s: V=%d E=%d F=%d euler=%d (want 2) incid=%d (want %d)'
          % (name, twists, mirror, V, E, F, euler, incid, 4 * V))
    return euler == 2 and incid == 4 * V


if __name__ == '__main__':
    ok1 = check('K10 ', [3, 3, 4])
    ok2 = check('K11 ', [3, 3, 5])
    ok3 = check('K11m', [3, 3, 5], mirror=True)
    ok4 = check('trefoil-test', [1, 1, 1])
    print('S2a-OK' if all([ok1, ok2, ok3, ok4]) else 'S2a-FAIL')
