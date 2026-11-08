#!/usr/bin/env python3
"""Independent exact arithmetic tests for nested prefix shelf inversions."""
from fractions import Fraction as F
from itertools import product
from math import comb


def exact_formula(k, m, p):
    u = F(m*m-1, 12*m*m)
    v = p*(1-p)/m**2
    theta = F(m-1, 2*m) + p/m
    return theta*comb(k,2), (u*k*(k-1)*(2*k+5) + v*k*(k-1)*(2*k-1))/6


def brute(m, n, p):
    # This intentionally never calls the pair indicator or projection proof.
    # It instead constructs actual top/bottom shelf stacks at each prefix.
    outcomes = [(s, b) for s in range(m) for b in (0,1)]
    masses = [F(1,m)*(p if b else (1-p)) for s,b in outcomes]
    es = [F(0) for _ in range(n+1)]
    eij = [[F(0) for _ in range(n+1)] for _ in range(n+1)]
    total=F(0)
    for seq in product(range(len(outcomes)), repeat=n):
        shelves = [[] for _ in range(m)]
        xs = [0]*(n+1)
        weight=F(1)
        for j,t in enumerate(seq,1):
            s,b = outcomes[t]
            weight *= masses[t]
            if b: shelves[s].insert(0,j)
            else: shelves[s].append(j)
            a=[x for row in shelves for x in row]
            xs[j]=sum(a[i]>a[z] for i in range(len(a)) for z in range(i+1,len(a)))
        total += weight
        for i in range(1,n+1):
            es[i] += weight*xs[i]
            for j in range(i,n+1):
                eij[i][j] += weight*xs[i]*xs[j]
    assert total == 1
    count=0
    for i in range(1,n+1):
        expected, variance=exact_formula(i,m,p)
        assert es[i] == expected, (m,n,p,i,es[i],expected)
        count += 1
        for j in range(i,n+1):
            actual=eij[i][j]-es[i]*es[j]
            assert actual == variance, (m,n,p,i,j,actual,variance)
            count += 1
    return count


def algebra():
    count=0
    for k in range(1,31):
        w=[k-2*j+1 for j in range(1,k+1)]
        assert sum(w)==0
        assert sum(z*z for z in w)==F(k*(k*k-1),3)
        assert sum((j-1)**2 for j in range(1,k+1))==F(k*(k-1)*(2*k-1),6)
        for l in range(k,k+5):
            assert sum((k-2*j+1)*(l-2*j+1) for j in range(1,k+1))==sum(z*z for z in w)
            count += 1
    for m in range(1,11):
        for p in (F(0), F(1,7), F(1,3), F(1,2), F(4,5), F(1)):
            u=F(m*m-1,12*m*m)
            v=p*(1-p)/m**2
            theta=F(m-1,2*m)+p/m
            assert theta*(1-theta)==3*u+v
            count += 1
    return count

if __name__=='__main__':
    checks=algebra()
    for m,n,p in ((1,5,F(1,3)), (2,5,F(1,3)), (2,5,F(4,5)), (3,4,F(2,5)), (3,4,F(1,2))):
        checks += brute(m,n,p)
    print(f'PASS {checks} exact rational/algebra assertions')
