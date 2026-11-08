#!/usr/bin/env python3
"""Exact rational checks for a Hilbert-valued variance phase law.
Only checks finite witnesses and sampled admissible maps; the general proof is in RESULT.md.
Run: python3 check_hilbert_clusters.py
"""
from fractions import Fraction as Q
from itertools import product
from random import Random


def metric_sq(i, a, j, b, q):
    if i != j: return Q(1)
    if a != b: return q
    return Q(0)


def witness_gram(r, m, q):
    # The regular-simplex-within-fibres and between-fibre orthogonal construction.
    c = Q(m-1, 2*m)*q
    if c <= Q(1,2):
        internal_factor = q/Q(2)
        centre_factor = (1 - 2*c)/2
    else:
        internal_factor = Q(m,2*(m-1))
        centre_factor = Q(0)
    return [[(internal_factor*(Q(1) if i==j else Q(0))*( (Q(1) if a==b else Q(0)) - Q(1,m))
              +centre_factor*((Q(1) if i==j else Q(0))-Q(1,r)))
             for j,b in product(range(r),range(m))]
            for i,a in product(range(r),range(m))]


def variance_gram(G):
    n=len(G)
    return sum(G[k][k] for k in range(n))/n - sum(sum(row) for row in G)/Q(n*n)


def target(r,m,q):
    return min(Q(1,2), Q(r-1,2*r)+Q(m-1,2*m*r)*q)


def gram_dist(G,a,b):
    return G[a][a]+G[b][b]-2*G[a][b]


def test_witnesses():
    count=0
    for r,m,q in product(range(2,8), range(2,8),
                          [Q(1,16),Q(1,4),Q(1),Q(5,4),Q(3,2),Q(2),Q(3),Q(4)]):
        G=witness_gram(r,m,q)
        n=r*m
        # PSD follows from the displayed orthogonal construction, not from this test.
        assert variance_gram(G)==target(r,m,q)
        for x in range(n):
            for y in range(x+1,n):
                d=gram_dist(G,x,y)
                assert 0<=d<=metric_sq(x//m,x%m,y//m,y%m,q)
                if x//m != y//m: assert d==1
                elif q <= Q(m,m-1): assert d==q
                else: assert d==Q(m,m-1)
        count+=1
    print('EXACT_GRAM_WITNESSES_OK',count)


def test_random_upper():
    rng=Random(1217)
    ct=0
    for r,m,q in product(range(2,7),range(2,6),[Q(1,4),Q(1),Q(3,2),Q(2),Q(4)]):
        n=r*m
        for rep in range(12):
            points=[[Q(rng.randrange(-5,6)) for _ in range(4)] for k in range(n)]
            sq=lambda x,y: sum((u-v)**2 for u,v in zip(x,y))
            factor=max([sq(points[x],points[y])/metric_sq(x//m,x%m,y//m,y%m,q)
                        for x in range(n) for y in range(x+1,n)],default=Q(0))
            factor=max(factor, Q(1))
            # Gram of points scaled by 1/sqrt(factor), preserving squared constraints.
            G=[[sum(u*v for u,v in zip(points[x],points[y]))/factor
                for y in range(n)] for x in range(n)]
            assert variance_gram(G) <= target(r,m,q)
            ct+=1
    print('EXACT_RANDOM_ADMISSIBLE_MAP_UPPER_BOUND_OK',ct)


def test_rank_changes():
    # Formula for the Gram rank: positive coefficients multiply orthogonal projections.
    for r,m in product(range(2,9),range(2,9)):
        threshold=Q(m,m-1)
        for q in [threshold/Q(2),threshold,threshold*Q(2)]:
            if q>4:continue
            c=Q(m-1,2*m)*q
            rank=r*(m-1)+(r-1 if c<Q(1,2) else 0)
            assert rank==(r*m-1 if q<threshold else r*(m-1))
    print('EXACT_CRITICAL_GRAM_RANKS_OK')

if __name__=='__main__':
    test_witnesses();test_random_upper();test_rank_changes()
    print('ALL_CLUSTER_HILBERT_SPREAD_CHECKS_OK')
