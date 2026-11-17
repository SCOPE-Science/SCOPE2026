"""Exact finite certificates for independently signed Volterra edge interactions.

Run with: python check_variance_graph.py
Uses only Python standard-library rational arithmetic.  Finite identities
illustrate, but do not replace, the analytic martingale convergence proof.
"""
from fractions import Fraction as Q
from itertools import combinations, product


def step(x, edges, signs):
    m = len(x)
    flux = [Q(0) for _ in range(m)]
    for (i, j, amp), sgn in zip(edges, signs):
        value = Q(sgn) * amp
        flux[i] += value * x[j]
        flux[j] -= value * x[i]
    return tuple(x[i] * (1 + flux[i]) for i in range(m))


def verify(m, edges, x):
    cases = list(product((-1, 1), repeat=len(edges)))
    outcomes = [step(x, edges, s) for s in cases]
    for y in outcomes:
        assert sum(y) == 1 and all(y[i] >= 0 for i in range(m))
    for i in range(m):
        assert sum(y[i] for y in outcomes) == len(cases) * x[i]
    h0 = sum(v * v for v in x)
    eh = sum(sum(v * v for v in y) for y in outcomes) / len(cases)
    delta = 2 * sum(amp * amp * x[i] * x[i] * x[j] * x[j]
                    for i, j, amp in edges)
    assert eh == h0 + delta
    if all(not (x[i] > 0 and x[j] > 0) for i, j, _ in edges):
        assert all(y == x for y in outcomes)
    return len(cases)


def main():
    tested = 0
    amps = (Q(1, 2), Q(1, 3), Q(1, 4), Q(2, 5), Q(1, 5), Q(3, 7))
    for m in (2, 3, 4):
        all_pairs = list(combinations(range(m), 2))
        candidates = [(), tuple(all_pairs), tuple(all_pairs[::2]),
                      tuple(all_pairs[1::2])]
        vectors = [tuple(Q(1, m) for _ in range(m)),
                   tuple([Q(1)] + [Q(0)] * (m-1)),
                   tuple([Q(1, 2),Q(1,2)] + [Q(0)] * (m-2)),
                   tuple(Q(i+1, m*(m+1)//2) for i in range(m))]
        for candidate in candidates:
            edges = [(i, j, amps[k]) for k, (i, j) in enumerate(candidate)]
            for x in vectors:
                tested += verify(m, edges, x)
    # Exact interior coexistence under perfectly correlated global flipping:
    # a=(1/2), b=(1/3), c=(1/4), r=(b,c,a)/(a+b+c).
    a, b, c = Q(1, 2), Q(1, 3), Q(1, 4)
    r = (b / (a+b+c), c / (a+b+c), a / (a+b+c))
    cyclic_edges = [(0,1,a), (0,2,-c), (1,2,b)]
    assert step(r, cyclic_edges, (1,1,1)) == r
    assert step(r, cyclic_edges, (-1,-1,-1)) == r
    # The independent-edge case has the same mean operator but strictly
    # positive conditional quadratic variation at this interior point.
    assert verify(3, cyclic_edges, r) == 8
    vdrift = 2 * sum(e[2]**2*r[e[0]]**2*r[e[1]]**2 for e in cyclic_edges)
    assert vdrift > 0
    print('VARIANCE_GRAPH_EXACT_OK finite_sign_cases=%d correlated_interior_stationarity=1' % (tested+8))


if __name__ == '__main__':
    main()
