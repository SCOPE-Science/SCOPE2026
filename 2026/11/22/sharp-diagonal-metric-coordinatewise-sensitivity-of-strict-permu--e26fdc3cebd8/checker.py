"""Exact arithmetic checks for diagonal-metric permutahedral projection stability.

Requires Python 3.10+ standard library only. These finite checks supplement the proof.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from random import Random


def formula(a):
    n = len(a)
    assert n >= 3 and all(t > 0 for t in a)
    pivot = max(a)
    others = list(a)
    others.remove(pivot)
    others.sort()
    best = F(1)
    running = F(0)
    for r, val in enumerate(others, 1):
        running += val
        if r >= 2:
            candidate = 1 + F((r-1)*pivot, pivot+running)
            best = max(best, candidate)
    return best


def brute(a):
    n = len(a)
    best = F(0)
    for size in range(2, n+1):
        for subset in combinations(range(n), size):
            total = sum(a[j] for j in subset)
            for i in subset:
                # Row i of the diagonal-metric affine projector on a sum constraint.
                row = sum(abs((F(int(j == i)) - a[i]/total)) for j in subset)
                best = max(best, row)
    return best


def main():
    rng = Random(1729)
    count = 0
    for n in range(3, 8):
        for _ in range(120):
            a = [F(rng.randrange(1, 18)) for _ in range(n)]
            assert formula(a) == brute(a), (n, a, formula(a), brute(a))
            count += 1
    # Explicit proper face: index 1 is the top singleton, remaining four tied
    # in a lower facial block of the standard order-5 permutahedron.
    a = [F(100), F(100), F(1), F(1), F(1)]
    w = [1/t for t in a]
    q = [F(5,2), F(5), F(5,2), F(5,2), F(5,2)]
    y = list(q)
    y[1] += a[1]
    h = [F(1), F(0), F(-1), F(-1), F(-1)]
    block = [0, 2, 3, 4]
    total = sum(a[i] for i in block)
    hsum = sum(h[i] for i in block)
    dh = [F(0) for _ in range(5)]
    for i in block:
        dh[i] = h[i] - a[i]*hsum/total
    eps = F(1, 100)
    yp = [y[i]+eps*h[i] for i in range(5)]
    qp = [q[i]+eps*dh[i] for i in range(5)]
    assert formula(a) == F(303,103)
    assert max(abs(t) for t in dh) == F(303,103)
    vertices = set(permutations([F(5),F(4),F(3),F(2),F(1)]))
    for cand, input_ in ((q,y),(qp,yp)):
        assert sum(cand) == F(15)
        for v in vertices:
            # Membership in convex hull, checked via all 2^5-2 subset facets.
            for mask in range(1,31):
                subset = [i for i in range(5) if mask >> i & 1]
                assert sum(cand[i] for i in subset) <= sum(sorted(v,reverse=True)[:len(subset)])
            # First-order projection inequality for every extreme point.
            assert sum(w[i]*(cand[i]-input_[i])*(v[i]-cand[i]) for i in range(5)) >= 0
    assert max(abs(yp[i]-y[i]) for i in range(5)) == eps
    assert max(abs(qp[i]-q[i]) for i in range(5)) == eps*F(303,103)
    print(f"PASS: {count} exhaustive-subset/formula comparisons; two exact 120-vertex optimality witnesses; finite sharp ratio 303/103.")


if __name__ == '__main__':
    main()
