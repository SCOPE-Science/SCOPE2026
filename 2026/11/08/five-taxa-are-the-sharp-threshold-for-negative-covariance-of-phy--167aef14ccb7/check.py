"""Exact checks for fixed-size phylogenetic rarefaction on rooted ultrametric trees.

Run with Python 3: python check.py
Only the standard library is needed.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random


def covariance(pairs):
    n = len(pairs)
    mean_a = sum(a for a, _ in pairs) / n
    mean_b = sum(b for _, b in pairs) / n
    return sum((a - mean_a)*(b - mean_b) for a, b in pairs) / n


def evaluate(edges, n, k):
    """Edges are (descendant-leaf-set, branch-length) pairs."""
    rows = []
    for s in combinations(range(n), k):
        S = set(s)
        pd = sum(w for D, w in edges if S.intersection(D))
        pair_total = F(0)
        for a, b in combinations(s, 2):
            pair_total += sum(w for D, w in edges if (a in D) != (b in D))
        mpd = pair_total / (k*(k-1)//2)
        rows.append((s, pd, mpd))
    return rows


def tree_23(H, x, y, z):
    assert H > 0 and 0 < x < H and 0 < z < y < H
    return [
        ({0,1}, H-x), ({2,3,4}, H-y), ({3,4}, y-z),
        ({0}, x), ({1}, x), ({2}, y), ({3}, z), ({4}, z)
    ]


def formula(H,x,y,z):
    p = 3*H*x-H*y-2*H*z+3*x*x-5*x*y-4*x*z+3*y*y+3*z*z
    return F(2,75)*p


def main():
    H=F(1);x=F(1,10);y=F(3,10);z=F(1,4)
    edges=tree_23(H,x,y,z)
    rows=evaluate(edges,5,4)
    assert [(p,m) for _,p,m in rows] == [
        (F(12,5),F(22,15)),
        (F(12,5),F(22,15)),
        (F(47,20),F(29,20)),
        (F(51,20),F(77,60)),
        (F(51,20),F(77,60))
    ],rows
    c=covariance([(p,m) for _,p,m in rows])
    assert c == F(-7,1000) == formula(H,x,y,z),c
    pp=[p for _,p,m in rows]; mm=[m for _,p,m in rows]
    mean_p=sum(pp)/5; mean_m=sum(mm)/5
    var_p=sum((v-mean_p)**2 for v in pp)/5
    var_m=sum((v-mean_m)**2 for v in mm)/5
    assert var_p == F(7,1000) and var_m == F(343,45000)
    assert c*c/(var_p*var_m) == F(45,49) and c<0
    print('five-leaf witness: exact covariance =',c, '; squared correlation = 45/49 (negative sign)')
    # Verify formula independently for additional rational ultrametric trees.
    rng=Random(2046)
    for _ in range(120):
        H=F(rng.randrange(9,25),8)
        x=H*F(rng.randrange(1,8),9)
        y=H*F(rng.randrange(2,8),9)
        z=y*F(rng.randrange(1,8),9)
        rows=evaluate(tree_23(H,x,y,z),5,4)
        assert covariance([(p,m) for _,p,m in rows]) == formula(H,x,y,z)
    print('formula checks: 120 exact independent tree enumerations passed')
    # Two four-leaf rooted binary topologies.  All ultrametric trees of <=4
    # leaves arise by zero-edge collapse of these two shapes.
    for _ in range(120):
        H=F(rng.randrange(9,25),8)
        u=H*F(rng.randrange(1,8),9)
        v=H*F(rng.randrange(1,8),9)
        balanced=[({0,1},H-u),({2,3},H-v),({0},u),({1},u),({2},v),({3},v)]
        for k in (2,3,4):
            rows=evaluate(balanced,4,k)
            assert covariance([(p,m) for _,p,m in rows])>=0
        u=H*F(rng.randrange(1,7),9)
        v=u+(H-u)*F(rng.randrange(1,8),9)
        caterpillar=[({0,1,2},H-v),({0,1},v-u),({0},u),({1},u),({2},v),({3},H)]
        for k in (2,3,4):
            rows=evaluate(caterpillar,4,k)
            assert covariance([(p,m) for _,p,m in rows])>=0
    print('four-leaf topology checks: 720 exact sample distributions passed')
    print('PASS')

if __name__=='__main__':
    main()
