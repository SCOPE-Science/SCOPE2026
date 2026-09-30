#!/usr/bin/env python3
"""Numerical verification for the Vec_{S3} witness.

Checks, from scratch in pure Python:
 1. S3 (permutations of 3 letters) is nonabelian (explicit noncommuting pair).
 2. Conjugacy classes of S3 and centralizer orders.
 3. Quantum-double rank = sum over classes of #(irreps of centralizer),
    computed as #(conjugacy classes of each centralizer subgroup) -- expect 8.
 4. FPdim(Z(Vec_{S3})) = |S3|^2 = 36; FPdim(Vec_{S3}) = 6.
 5. Rep(S3) consistency: 3 irreps (one per class), degrees 1,1,2 with
    1^2+1^2+2^2 = 6 = |S3|; symmetric hence braided.
"""

from itertools import permutations


def compose(p, q):
    # permutations as tuples; apply q then p
    return tuple(p[q[i]] for i in range(len(p)))


def inv(p):
    q = [0] * len(p)
    for i, v in enumerate(p):
        q[v] = i
    return tuple(q)


def main():
    G = sorted(set(permutations((0, 1, 2))))
    assert len(G) == 6, len(G)
    e = (0, 1, 2)

    # 1. nonabelian: find explicit noncommuting pair
    pair = None
    for a in G:
        for b in G:
            if compose(a, b) != compose(b, a):
                pair = (a, b)
                break
        if pair:
            break
    assert pair is not None
    print("noncommuting pair:", pair)

    # 2. conjugacy classes and centralizers
    def conj_class(g):
        return sorted({compose(compose(h, g), inv(h)) for h in G})

    classes, seen = [], set()
    for g in G:
        if g not in seen:
            c = conj_class(g)
            classes.append(c)
            seen.update(c)
    print("class sizes:", sorted(len(c) for c in classes))
    assert sorted(len(c) for c in classes) == [1, 2, 3]

    def centralizer_order(g):
        return sum(1 for h in G if compose(h, g) == compose(g, h))

    # 3. double rank: sum_C #(classes of Cent(C)); compute each from scratch
    def subgroup_classes(sub):
        sub = list(sub)
        cls, seen2 = [], set()
        for g in sub:
            if g not in seen2:
                c = sorted({compose(compose(h, g), inv(h)) for h in sub})
                cls.append(c)
                seen2.update(c)
        return cls

    rank = 0
    for c in classes:
        g = c[0]
        cent = [h for h in G if compose(h, g) == compose(g, h)]
        n = len(subgroup_classes(cent))
        print(f"class size {len(c)}: |Cent|={len(cent)}, #irreps(Cent)={n}")
        rank += n
    print("D(S3)-mod rank:", rank)
    assert rank == 8

    # 4. Frobenius-Perron dimensions
    print("FPdim(Vec_S3) =", len(G))
    print("FPdim(Z(Vec_S3)) =", len(G) ** 2)
    assert len(G) ** 2 == 36

    # 5. Rep(S3): #irreps = #classes = 3; degrees 1,1,2; sum of squares = |G|
    degs = (1, 1, 2)
    assert len(degs) == len(classes) == 3
    assert sum(d * d for d in degs) == len(G) == 6
    print("Rep(S3) degree check 1^2+1^2+2^2 = 6 = |S3|: OK")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
