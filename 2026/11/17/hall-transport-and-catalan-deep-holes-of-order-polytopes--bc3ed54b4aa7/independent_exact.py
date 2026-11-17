#!/usr/bin/env python3
"""Exact small-poset verification via all equality-block partitions."""
from fractions import Fraction as F
from itertools import product, combinations
from random import Random


def partitions(n):
    # restricted growth words encode all set partitions
    def rec(a,m):
        if len(a)==n:
            b=[[] for _ in range(m+1)]
            for i,j in enumerate(a):b[j].append(i)
            yield b
            return
        for j in range(m+2):
            yield from rec(a+[j],max(j,m))
    return list(rec([0],0))


def optimal_squared_error(bits,rel,allparts):
    n=len(bits); best=None
    for blocks in allparts:
        y=[F(0) for _ in range(n)]
        for block in blocks:
            av=F(sum(bits[i] for i in block),len(block))
            for i in block:y[i]=av
        if any(y[i]>y[j] for i in range(n) for j in range(n) if rel[i][j]):continue
        cost=sum((F(b)-y[i])**2 for i,b in enumerate(bits))
        if best is None or cost<best:best=cost
    assert best is not None
    return best


def hall(bits,rel):
    n=len(bits);k=sum(bits)
    if not 0<k<n:return False
    poss=[i for i,v in enumerate(bits) if v]
    zero=[i for i,v in enumerate(bits) if not v]
    return all((n-k)*len(S)<=k*len({j for i in S for j in zero if rel[i][j]})
               for a in range(1,len(poss)+1) for S in combinations(poss,a))


def main():
    rng=Random(88412); tests=0
    for n in range(2,8):
        ps=partitions(n)
        for rep in range(4):
            rel=[[False]*n for _ in range(n)]
            for i in range(n):
                for j in range(i+1,n):rel[i][j]=(rep==0 or rng.random()<0.36)
            for k in range(n):
                for i in range(n):
                    for j in range(n):rel[i][j] |= rel[i][k] and rel[k][j]
            bound=F((n*n)//4,n)
            for bits in product((0,1),repeat=n):
                cost=optimal_squared_error(bits,rel,ps)
                reached=cost==bound
                feasible=(sum(bits) in {n//2,(n+1)//2} and hall(bits,rel))
                assert reached==feasible,(n,rep,bits,cost,bound,feasible)
                tests+=1
    print('ORDER_POLYTOPE_GENERIC_PARTITION_PASS exact_projections=%d n=2..7'%tests)

if __name__=='__main__':main()
