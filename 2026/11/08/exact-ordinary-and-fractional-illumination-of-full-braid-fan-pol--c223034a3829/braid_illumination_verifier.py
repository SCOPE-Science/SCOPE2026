#!/usr/bin/env python3
"""Finite exact checks for braid-fan illumination incidence (not a proof)."""
from itertools import permutations
from math import factorial
from random import Random


def lit(perm, u):
    s = 0
    for i in perm[:-1]:
        s += u[i]
        if s <= 0:
            return False
    return True


def generic(u):
    n=len(u)
    return all(sum(u[i] for i in range(n) if mask & (1 << i)) != 0
               for mask in range(1, (1 << n) - 1))


def check():
    checked = 0
    for n in range(2, 9):
        ps=list(permutations(range(n)))
        special=[]
        for j in range(n):
            u=[-1]*n
            u[j]=n-1
            assert sum(u)==0 and generic(u)
            covered={p for p in ps if lit(p,u)}
            assert len(covered)==factorial(n-1)
            assert all(p[0]==j for p in covered)
            special.append(covered)
            checked += len(ps)
        assert set.union(*special)==set(ps)
        assert sum(map(len, special))==len(ps)
        for p in ps:
            assert sum(p in ss for ss in special)==1
        checked += len(ps)
        # Generic zero-sum directions with one negative entry of variable magnitude.
        # Distinct powers ensure strict nonzero proper subset sums.
        for j in range(n):
            positive=[3**k for k in range(n-1)]
            u=positive.copy()
            u.insert(j, -sum(positive))
            assert generic(u)
            assert sum(lit(p,u) for p in ps)==factorial(n-1)
            checked += len(ps)
        # Nongeneric directions can illuminate no more than the sharp count.
        rng=Random(20261102+n)
        for k in range(10):
            u=[rng.randint(-5,5) for _ in range(n-1)]
            u.append(-sum(u))
            if all(x==0 for x in u):
                continue
            assert sum(lit(p,u) for p in ps)<=factorial(n-1)
            checked += len(ps)
    # Independent weighted-zonotope facet/vertex checks, not assuming vertex incidence.
    for n in range(2, 7):
        ps=list(permutations(range(n)))
        weights={(i,j):1+((7*i+11*j)%17) for i in range(n) for j in range(i+1,n)}
        for p in ps:
            rank={v:i for i,v in enumerate(p)}
            x=[0]*n
            for (i,j),w in weights.items():
                x[max((i,j),key=lambda z:rank[z])]+=w
            active=[]
            for mask in range(1,(1<<n)-1):
                lhs=sum(x[i] for i in range(n) if (mask>>i)&1)
                rhs=sum(w for (i,j),w in weights.items() if (mask>>i)&1 or (mask>>j)&1)
                assert lhs<=rhs
                if lhs==rhs: active.append(mask)
            assert len(active)==n-1
            assert set(active)=={sum(1<<p[z] for z in range(k,n)) for k in range(1,n)}
            for pivot in range(n):
                u=[-1]*n
                u[pivot]=n-1
                facet_criterion=all(sum(u[i] for i in range(n) if mask>>i&1)<0 for mask in active)
                assert facet_criterion==lit(p,u)
                checked+=len(active)
    print('BRAID_FAN_ILLUMINATION_EXACT_OK', checked)

if __name__=='__main__':
    check()
