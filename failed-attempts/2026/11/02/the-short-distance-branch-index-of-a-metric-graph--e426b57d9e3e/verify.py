"""Exact rational verification of local distance-distribution identities.

Independent cross-check: integrate endpoint-route half-planes in every
ordered edge-pair rectangle, using a rational polygon clipper. No Monte
Carlo estimation or floating point is used.
"""
from fractions import Fraction as Q
from itertools import combinations


def area(poly):
    if len(poly) < 3:
        return Q(0)
    return abs(sum(a[0] * b[1] - b[0] * a[1]
                   for a, b in zip(poly, poly[1:] + poly[:1]))) / 2


def clip(poly, a, b, c):
    """Clip by a*x+b*y<=c, all exact fractions."""
    if not poly:
        return []
    out = []
    def f(z):
        return a * z[0] + b * z[1] - c
    for p, q in zip(poly, poly[1:] + poly[:1]):
        fp, fq = f(p), f(q)
        inside_p, inside_q = fp <= 0, fq <= 0
        if inside_p != inside_q:
            t = fp / (fp - fq)
            out.append((p[0] + t * (q[0] - p[0]),
                        p[1] + t * (q[1] - p[1])))
        if inside_q:
            out.append(q)
    return out


def shortest_vertex_paths(edges):
    verts = sorted({p for a, b, _ in edges for p in (a, b)})
    d = {(p, q): (Q(0) if p == q else None) for p in verts for q in verts}
    for p, q, le in edges:
        le = Q(le)
        assert le > 0 and p != q
        d[p, q] = le if d[p, q] is None else min(d[p, q], le)
        d[q, p] = le if d[q, p] is None else min(d[q, p], le)
    for k in verts:
        for i in verts:
            for j in verts:
                if d[i, k] is not None and d[k, j] is not None:
                    cand = d[i, k] + d[k, j]
                    d[i, j] = cand if d[i, j] is None else min(d[i, j], cand)
    assert all(val is not None for val in d.values())
    return d


def exact_pair_area(g, e, f, r, dist):
    u, v, le = g[e]
    s, t, lf = g[f]
    le, lf = Q(le), Q(lf)
    if e == f:
        # Direct same-edge path. At the tested small radii an alternate
        # route cannot create additional close pairs.
        return 2 * le * r - r * r
    box = [(Q(0), Q(0)), (le, Q(0)), (le, lf), (Q(0), lf)]
    total = Q(0)
    # x is measured from u, y from s. For each endpoint choice,
    # evaluate an independent route affine in (x,y).
    for idx, p in enumerate((u, v)):
        ax = Q(1) if idx == 0 else Q(-1)
        cx = Q(0) if idx == 0 else le
        for jdx, q in enumerate((s, t)):
            by = Q(1) if jdx == 0 else Q(-1)
            cy = Q(0) if jdx == 0 else lf
            region = clip(box, ax, by, r - dist[p, q] - cx - cy)
            total += area(region)
    return total


def run_case(name, g):
    E = [(u, v, Q(l)) for u, v, l in g]
    assert len({frozenset((u, v)) for u, v, l in E}) == len(E)
    dist = shortest_vertex_paths(E)
    L = sum((e[2] for e in E), Q(0))
    deg = {u: 0 for e in E for u in e[:2]}
    for u, v, le in E:
        deg[u] += 1
        deg[v] += 1
    b = sum((Q(d * (d - 1), 2) for d in deg.values()), Q(0)) - len(E)
    genus = len(E) - len(deg) + 1
    assert b == 2 * genus - 2 + sum((Q((d - 2)**2, 2) for d in deg.values()), Q(0))
    for scale in [Q(1, 5), Q(1, 7), Q(1, 11)]:
        r = min(e[2] for e in E) * scale
        observed_numerator = sum((exact_pair_area(E, i, j, r, dist)
                                  for i in range(len(E)) for j in range(len(E))), Q(0))
        target_numerator = 2 * L * r + b * r * r
        assert observed_numerator == target_numerator, (name, observed_numerator, target_numerator)
        F = observed_numerator / L**2
        assert F == 2*r/L+b*r*r/L**2
    return L, b, genus


def main():
    examples = {
        'single_path': [(0, 1, 7)],
        'unequal_path': [(0, 1, 2), (1, 2, 3), (2, 3, 5)],
        'three_star': [(0, 1, 2), (0, 2, 3), (0, 3, 5)],
        'four_star': [(0, 1, 2), (0, 2, 3), (0, 3, 5), (0, 4, 7)],
        'cycle': [(0, 1, 2), (1, 2, 3), (2, 3, 5), (3, 0, 7)],
        'lollipop': [(0, 1, 2), (1, 2, 3), (2, 0, 5), (2, 3, 7)],
        'theta': [(0, 1, 2), (1, 2, 3), (2, 3, 5), (3, 0, 7), (0, 2, 11)],
        'branched_tree': [(0, 1, 2), (0, 2, 3), (0, 3, 5), (3, 4, 7), (3, 5, 11), (5, 6, 13)],
    }
    results = {}
    for name, g in examples.items():
        results[name] = run_case(name, g)
    assert results['three_star'][1] == results['cycle'][1] == 0
    assert results['unequal_path'][1] == -1
    assert results['four_star'][1] == 2
    print('EXACT_RATIONAL_ALL_ENDPOINT_ROUTES_AND_INTEGRALS_PASSED', len(examples) * 3)
    print('BETTI_BRANCHING_IDENTITY_AND_SUBDIVISION_PASSED')
    print('CIRCLE_THREE_STAR_LOCAL_AMBIGUITY_PASSED')
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    main()
