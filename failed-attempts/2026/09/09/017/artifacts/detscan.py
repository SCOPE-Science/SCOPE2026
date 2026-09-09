"""Fast det-at-root-of-unity scan over candidate closures (background-safe, chunked)."""
import sys, json, cmath
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-314/output/artifacts')
from closures import columns

A = cmath.exp(-1j * cmath.pi / 4)
D = -A * A - (-A) ** (-2)  # loop value placeholder (computed per state below)


def det_scan(ns, pairing, inter, signs):
    cr, edges, stubs = columns(ns, inter, signs)

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
        merge(stubs[tuple(a)], stubs[tuple(b)])
    for e, ends in edges.items():
        if len(ends) != 2:
            return None
    N = len(cr); cl = sorted(cr)
    # per-crossing port tuples
    overs = {}; unders = {}
    for c, d in cr.items():
        overs[c] = d['over']; unders[c] = d['under']
    total = 0j
    Apow = {}
    for mask in range(1 << N):
        a_ct = 0
        ch = {}
        for i, c in enumerate(cl):
            b = (mask >> i) & 1; ch[c] = b
            if b == 0:
                a_ct += 1
        # union-find circles
        parent = {}
        for c in cr:
            for p in ('NW', 'NE', 'SE', 'SW'):
                parent[(c, p)] = (c, p)

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
        for c in cr:
            oi, oo = overs[c]; ui, uo = unders[c]
            if ch[c] == 0:
                uu((c, oi), (c, ui)); uu((c, oo), (c, uo))
            else:
                uu((c, oi), (c, uo)); uu((c, oo), (c, ui))
        roots = set()
        for s in parent:
            roots.add(ff(s))
        k = len(roots)
        base = a_ct - (N - a_ct)
        # contribution at A: A^base * (-A^2-A^-2)^(k-1)
        total += (A ** base) * ((-A * A - A ** (-2)) ** (k - 1))
    return abs(total)


if __name__ == '__main__':
    both = json.load(open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-314/output/artifacts/both.json'))
    ns = (3, 3, -2); inter = ['cross', 'cross', 'straight']; signs = [1, 1, -1]
    import sys as _s
    chunk = [int(x) for x in _s.argv[1:3]] if len(_s.argv) > 2 else [0, len(both)]
    lo, hi = chunk
    hits = []
    for idx in range(lo, min(hi, len(both))):
        d = det_scan(ns, both[idx], inter, signs)
        if d is not None and abs(d - 3) < 0.05:
            hits.append((idx, d, both[idx]))
            print('HIT', idx, d, both[idx], flush=True)
    print('done %d-%d hits=%d' % (lo, hi, len(hits)), flush=True)
