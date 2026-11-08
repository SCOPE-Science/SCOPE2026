"""Exact check for the six-vertex, size-three outbreak interdiction result.

Runs on Python 3.9+ with standard library only. Counts independent bond
percolation configurations exactly and certifies all smaller trees via
Pruefer sequences and coefficientwise Bernstein inequalities.
"""
from fractions import Fraction
from itertools import product
from math import comb


def prufer_tree(seq):
    n = len(seq) + 2
    degrees = [1] * n
    for v in seq:
        degrees[v] += 1
    edges = []
    for v in seq:
        u = next(i for i, d in enumerate(degrees) if d == 1)
        edges.append((u, v))
        degrees[u] -= 1
        degrees[v] -= 1
    u, v = [i for i, d in enumerate(degrees) if d == 1]
    edges.append((u, v))
    return edges


def component_risk_counts(n, edges, deleted, threshold):
    """Coefficients of n Q_e(p) in degree-(n-2) Bernstein basis.

    Return c[k] where Q_e(p) = (1/n)*sum_k c[k]*p**k*(1-p)**(n-2-k).
    Each c[k] is the number of seed vertices across open-edge masks
    of cardinality k whose component has size at least threshold.
    """
    rem = [e for e in edges if e != deleted]
    assert len(rem) == n - 2
    c = [0] * (n - 1)
    for mask in range(1 << len(rem)):
        parent = list(range(n))
        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x
        for j, (u, v) in enumerate(rem):
            if mask & (1 << j):
                parent[root(u)] = root(v)
        sizes = {}
        for u in range(n):
            r = root(u)
            sizes[r] = sizes.get(r, 0) + 1
        c[mask.bit_count()] += sum(s for s in sizes.values() if s >= threshold)
    return c


def power_coeffs(n, c):
    """Expand c into exact rational power coefficients of Q(p)."""
    d = n - 2
    out = [Fraction(0) for _ in range(d + 1)]
    for k in range(d + 1):
        for j in range(d - k + 1):
            out[k + j] += Fraction(c[k] * comb(d - k, j) * (-1)**j, n)
    return out


def smaller_trees_certificate():
    counts = {}
    for n in range(2, 6):
        cases = 0
        for seq in product(range(n), repeat=n - 2):
            edges = prufer_tree(seq)
            for h in range(2, n + 1):
                all_c = [component_risk_counts(n, edges, e, h) for e in edges]
                # A single edge has coefficientwise-minimal risk in the
                # nonnegative Bernstein basis over all p in [0,1].
                good = [i for i, ci in enumerate(all_c)
                        if all(all(a <= b for a, b in zip(ci, cj))
                               for cj in all_c)]
                assert good, (n, seq, h, all_c)
                cases += 1
        counts[n] = cases
    assert counts == {2: 1, 3: 6, 4: 48, 5: 500}
    return counts


def witness_certificate():
    # The six-vertex tree has hub 0, leaves 1,2, and handle 0-3-4-5.
    edges = [(0,1), (0,2), (0,3), (3,4), (4,5)]
    risk = {e: power_coeffs(6, component_risk_counts(6, edges, e, 3))
            for e in edges}
    F = Fraction
    expect = {
        (0,1): [F(0),F(0),F(3,2),F(-2,3),F(0)],
        (0,2): [F(0),F(0),F(3,2),F(-2,3),F(0)],
        (0,3): [F(0),F(0),F(1),F(0),F(0)],
        (3,4): [F(0),F(0),F(3,2),F(-5,6),F(0)],
        (4,5): [F(0),F(0),F(2),F(-3,2),F(1,3)],
    }
    assert risk == expect, (risk, expect)
    # Q_hubleaf - Q_3,4 = p^3/6 >0 for 0<p<1.
    assert [a-b for a,b in zip(risk[(0,1)],risk[(3,4)])] == [F(0),F(0),F(0),F(1,6),F(0)]
    # Q_endleaf - Q_3,4 = p^2 (3-4p+2p^2)/6 >0.
    assert [a-b for a,b in zip(risk[(4,5)],risk[(3,4)])] == [F(0),F(0),F(1,2),F(-2,3),F(1,3)]
    # Q_3,4 - Q_0,3 = p^2(3-5p)/6, unique switch 3/5.
    assert [a-b for a,b in zip(risk[(3,4)],risk[(0,3)])] == [F(0),F(0),F(1,2),F(-5,6),F(0)]
    # Independent check via direct probability of a large component at three rates.
    for p in [F(1,10),F(3,5),F(9,10)]:
        vals = {e:sum(ck * p**k for k,ck in enumerate(poly)) for e,poly in risk.items()}
        winners = {e for e,v in vals.items() if v == min(vals.values())}
        expected = {(0,3)} if p<F(3,5) else ({(0,3),(3,4)} if p==F(3,5) else {(3,4)})
        assert winners == expected, (p,winners)
    return risk


def main():
    smaller = smaller_trees_certificate()
    witness = witness_certificate()
    print("PASS: lower-order tree and threshold cases:", smaller)
    print("PASS: exact witness power coefficients:")
    for e, poly in witness.items():
        print(e, [str(x) for x in poly])
    print("PASS: unique 3/5 threshold and all noncompeting edges")


if __name__ == '__main__':
    main()
