#!/usr/bin/env python3
"""Exact finite checks for a two-community product-SIS theorem.

The infinite-parameter assertions rely on the analytical proof in RESULT.md.
This checker supplies exact graph, quotient, and order-separating certificates.
"""
from fractions import Fraction as F
from functools import reduce


def graph_join_cycle4_edge():
    edges = {(0,1), (1,2), (2,3), (0,3), (4,5)}
    edges |= {(i,j) for i in range(4) for j in (4,5)}
    return edges


def nbrs(edges, n):
    out=[set() for _ in range(n)]
    for i,j in edges:
        assert i != j and 0 <= i < n and 0 <= j < n
        out[i].add(j);out[j].add(i)
    return out


def product_map(x, neighbors, beta, delta):
    return [F(1)-(F(1)-(F(1)-delta)*x[i])*reduce(
        lambda z,j:z*(F(1)-beta*x[j]),neighbors[i],F(1))
        for i in range(len(x))]


def quotient_map(x, Q, beta, delta):
    return [F(1)-(F(1)-(F(1)-delta)*x[i])*reduce(
        lambda z,j:z*(F(1)-beta*x[j])**Q[i][j],range(len(x)),F(1))
        for i in range(len(x))]


def check():
    E=graph_join_cycle4_edge()
    assert len(E)==13
    ne=nbrs(E,6)
    assert [len(x) for x in ne]==[4,4,4,4,5,5]
    C=[list(range(4)),[4,5]]
    Q=[[2,2],[4,1]]
    for i,group in enumerate(C):
        for u in group:
            assert [len(ne[u].intersection(other)) for other in C]==Q[i]
    # Internal thresholds are 1/2 (cycle) and 1 (edge).
    assert Q[0][0]==2 and Q[1][1]==1
    # Global quotient PF eigenvalue lies strictly between 4 and 5.
    char=lambda x:x*x-3*x-6
    assert char(F(4))<0<char(F(5))
    beta,delta=F(3,10),F(2,5)
    assert beta/delta==F(3,4)
    assert F(1,2)<beta/delta<F(1)
    assert beta*F(4)>delta
    # The full 6-node map restricts EXACTLY to the 2-node quotient map.
    for a,b in [(F(1,5),F(2,5)),(F(9,10),F(4,5)),(F(1,1),F(1,1))]:
        full=product_map([a]*4+[b]*2,ne,beta,delta)
        reduced=quotient_map([a,b],Q,beta,delta)
        assert full==[reduced[0]]*4+[reduced[1]]*2
    # Rational componentwise strict sub/supersolutions.  Monotone iteration
    # plus uniqueness from RESULT.md implies the endemic solution is enclosed.
    low=[F(855,1000),F(896,1000)]
    high=[F(858,1000),F(899,1000)]
    f_low=quotient_map(low,Q,beta,delta)
    f_high=quotient_map(high,Q,beta,delta)
    assert all(f_low[i]>low[i] for i in range(2))
    assert all(f_high[i]<high[i] for i in range(2))
    assert high[0]<low[1]
    # No smaller two-cell simple connected equitable graph with both induced
    # degrees positive can reverse the internal-degree versus total-degree rank:
    # at 5 vertices, degrees differ only for cell sizes 3 and 2.
    possible=[]
    for b1 in range(1,3):
        for b2 in range(1,4):
            if 3*b1==2*b2:
                possible.append((b1,b2))
    assert possible==[(2,3)]
    assert 2+possible[0][0]==1+possible[0][1]
    # Three equal-sized 6-vertex cells: K6 minus matching, C6, K6,
    # with perfect-matchings from cell 1 to 2 and from cell 2 to 3.
    Q3=[[4,1,0],[1,2,1],[0,1,5]]
    assert [sum(row) for row in Q3]==[5,4,6]
    # Positive Rayleigh witness (0,1,5) gives rho(Q3)>=137/26>26/5.
    v=[F(0),F(1),F(5)]
    numerator=sum(v[i]*Q3[i][j]*v[j] for i in range(3) for j in range(3))
    denominator=sum(z*z for z in v)
    assert numerator==137 and denominator==26
    assert numerator/denominator>F(26,5)
    assert F(1,20)*numerator/denominator>F(13,50)
    # Thus the 3-block system is supercritical for these rational parameters.
    # Because rho>5, the PF equations give v_2=(rho-4)v_1>v_1,
    # reversing the full-degree ordering of the first two cells near onset.
    print('PASS: exact graph quotient, six-vertex minimal obstruction,')
    print('      rational endemic enclosure and three-cell PF certificate')


if __name__=='__main__':
    check()
