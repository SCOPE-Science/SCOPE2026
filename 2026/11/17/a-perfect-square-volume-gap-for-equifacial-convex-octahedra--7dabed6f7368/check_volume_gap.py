"""Exact algebraic and finite combinatorial corroboration of the octahedral volume gap.

The cited geometric classification supplies the exhaustion of realizations; this script
independently enumerates cube matching types and checks the algebraic gap identity.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def gap(r2, d, e):
    """All coordinates are rational, and R=r^2 is used to avoid radicals."""
    s2 = 2*r2+(e-d)**2
    p2 = r2+d*d
    q2 = r2+e*e
    alpha = (p2+q2-s2)/2
    beta = (s2+q2-p2)/2
    gamma = (s2+p2-q2)/2
    assert alpha == d*e
    assert beta == r2+e*(e-d)
    assert gamma == r2+d*(d-e)
    # Squared volumes, using determinant formulas for the two six-vertex hulls:
    vt2 = F(4,9)*r2*r2*(d+e)**2
    vc2 = F(16,9)*alpha*beta*gamma
    gap2 = F(4,9)*(d-e)**2*(r2-2*d*e)**2
    assert vt2-vc2 == gap2
    return beta>0 and gamma>0, vt2, vc2, gap2


def enumerate_cube_colorings():
    verts = list(range(8))
    edges = [(i, i ^ (1 << bit)) for i in verts for bit in range(3)
             if i < (i ^ (1 << bit))]
    assert len(edges)==12
    matches = []
    for tup in combinations(range(12), 4):
        endpoints = [v for k in tup for v in edges[k]]
        if len(set(endpoints)) == 8:
            matches.append(frozenset(tup))
    assert len(matches) == 9
    splits = set()
    for m0, m1, m2 in combinations(matches, 3):
        if len(m0|m1|m2)==12 and len(m0&m1)==len(m1&m2)==len(m0&m2)==0:
            splits.add(frozenset([m0,m1,m2]))
    assert len(splits) == 4
    straight = [frozenset(k for k,(i,j) in enumerate(edges) if (i^j)==(1 << bit))
                for bit in range(3)]
    distribution = sorted(sum(m in straight for m in split) for split in splits)
    assert distribution == [1,1,1,3]
    return len(matches),len(splits),distribution


def main():
    n=0
    for id_,ie,iR in [(d,e,R) for d in range(1,8) for e in range(1,8) for R in range(1,21)]:
        feasible,vt2,vc2,gap2=gap(F(iR),F(id_),F(ie))
        if feasible:
            assert vt2>=vc2
            if id_!=ie and iR!=2*id_*ie:assert vt2>vc2
            if id_!=ie and iR==2*id_*ie:
                p2=F(iR)+F(id_)**2; q2=F(iR)+F(ie)**2
                s2=2*F(iR)+(F(ie)-F(id_))**2
                assert s2>max(p2,q2)
                assert vt2==vc2
            n+=1
    assert n>500
    cm,cs,dist=enumerate_cube_colorings()
    print(f'PASS: {n} exact feasible volume comparisons and gap identities; cube matchings {cm}; partitions {cs}; straight-match distribution {dist}.')

if __name__=='__main__':main()
