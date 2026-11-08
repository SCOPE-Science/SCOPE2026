"""Exact finite-case consistency checks for a half-retention PD threshold theorem.
Run with Python 3 (standard library only): python verify.py
The infinite assertion is established by the proof, not by this finite checker.
"""
from collections import defaultdict
from math import comb

LEAF = None

def graft(t):
    return (t, LEAF)

def masks(tree, start=0):
    """Return descendant-leaf masks for each edge and the next leaf index."""
    if tree is LEAF:
        return [], 1 << start, start + 1
    left, lm, mid = masks(tree[0], start)
    right, rm, finish = masks(tree[1], mid)
    return left + [lm] + right + [rm], lm | rm, finish

def pmf_polynomials(tree):
    """Map PD values to polynomials in q represented by degree->coefficient."""
    edges, mask, n = masks(tree)
    assert len(edges) == 2 * n - 2 and mask == (1 << n) - 1
    polynomials = defaultdict(lambda: defaultdict(int))
    for survivors in range(1 << n):
        k = survivors.bit_count()
        diversity = sum(bool(edge & survivors) for edge in edges)
        # q^(n-k) (1-q)^k, expanded over integers.
        for j in range(k + 1):
            polynomials[diversity][n - k + j] += (-1) ** j * comb(k, j)
    return {pd: dict(coeff) for pd, coeff in polynomials.items()}, n

def diff_polys(pa, pb, min_pd=0, moment=False):
    ans = defaultdict(int)
    for sign, p in ((1, pa), (-1, pb)):
        for pd, coeff in p.items():
            if pd < min_pd:
                continue
            mult = pd if moment else 1
            for power, value in coeff.items():
                ans[power] += sign * mult * value
    return {k: v for k, v in ans.items() if v}

def monomials(items):
    return {power: coeff for power, coeff in items if coeff != 0}

def check():
    cherry = (LEAF, LEAF)
    caterpillar = graft(graft(cherry))
    balanced = (cherry, cherry)
    # Two nonisomorphic rooted four-leaf full-binary shapes.
    p, n = pmf_polynomials(caterpillar)
    r, _ = pmf_polynomials(balanced)
    expected_base = {
        1: {3: 1, 4: -1},
        2: {3: -3, 4: 3},
        3: {2: -1, 3: 4, 4: -3},
        4: {2: 1, 3: -2, 4: 1},
    }
    for pd in range(2 * n - 1):
        actual = diff_polys({pd: p.get(pd, {})}, {pd: r.get(pd, {})})
        assert actual == expected_base.get(pd, {}), (pd, actual)
    print("Four-leaf probability-generating-function identity: verified")
    for n in range(4, 12):
        p, m = pmf_polynomials(caterpillar)
        r, _ = pmf_polynomials(balanced)
        assert m == n
        got_mean = diff_polys(p, r, moment=True)
        expected_mean = {2: 1, 3: -1}
        assert got_mean == expected_mean, (n, got_mean)
        got_tail = diff_polys(p, r, min_pd=n - 1)
        expected_tail = monomials([
            (n - 2, -(n - 4)),
            (n - 1, 2 * n - 6),
            (n, -(n - 2)),
        ])
        assert got_tail == expected_tail, (n, got_tail, expected_tail)
        print(f"{n} leaves: exact mean and half-PD tail polynomial identities verified")
        caterpillar, balanced = graft(caterpillar), graft(balanced)
    # Independent boundary check at n<=3: no distinct tree shapes.
    def shapes(n):
        if n == 1:
            return {"."}
        all_shapes = set()
        for k in range(1, n):
            for a in shapes(k):
                for b in shapes(n - k):
                    all_shapes.add("(" + ",".join(sorted((a, b))) + ")")
        return all_shapes
    assert [len(shapes(n)) for n in (2, 3, 4)] == [1, 1, 2]
    print("Two, three, four leaf shape counts: verified")
    print("All checks passed; numerical enumeration is not the infinite proof")

if __name__ == "__main__":
    check()
