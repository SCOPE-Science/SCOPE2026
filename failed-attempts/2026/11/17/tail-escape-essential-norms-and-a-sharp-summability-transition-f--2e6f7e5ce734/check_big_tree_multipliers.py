#!/usr/bin/env python3
"""Exact finite-coordinate verification for weighted-tree multiplier formulas.

Mathematical theorem for infinite trees requires the accompanying analytic proof.
This checks exact row coefficients, operator norm, and finite-section tails.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random


def data(parents, c, psi):
    # vertex 0=root, and each numbered vertex has a smaller-numbered parent
    rows = {}
    for v in range(1, len(parents)):
        path = []
        p = parents[v]
        while p:
            path.append(p)
            p = parents[p]
        beta = c[v] * (psi[v] - psi[parents[v]])
        row = {v:psi[v]}
        for w in path:
            row[w] = row.get(w, Q(0)) + beta / c[w]
        rows[v] = (beta, row, path)
    return rows


def matnorm_row(row):
    return sum(map(abs, row.values()), Q(0))


def check_profile(parents, c, psi):
    assert parents[0] is None
    rows = data(parents,c,psi)
    # Operator norm for root-plus-max space: check every vertex row.
    root_norm = abs(psi[0])+max((abs(rows[v][0]) for v in rows),default=Q(0))
    tail_norm=max((matnorm_row(rows[v][1]) for v in rows),default=Q(0))
    predicted=max(root_norm,tail_norm)
    brute=Q(0)
    for x in product((-1,1),repeat=len(parents)-1):
        f=[Q(0)]*len(parents)
        for v in range(1,len(parents)):
            f[v]=f[parents[v]]+Q(x[v-1],1)/c[v]
        m=max((c[v]*abs(psi[v]*f[v]-psi[parents[v]]*f[parents[v]]) for v in rows),default=Q(0))
        brute=max(brute,m)
    brute=max(brute,root_norm)
    assert predicted==brute,(predicted,brute)
    # For each depth cutoff, check exact row-tail identity by signs.
    depths=[0]*len(parents)
    for v in range(1,len(parents)):
        depths[v]=depths[parents[v]]+1
    for N in range(max(depths)):
        vals=[]
        for v,(beta,row,path) in rows.items():
            if depths[v]<=N: continue
            expected=abs(psi[v])+abs(beta)*sum((Q(1)/c[w] for w in path if depths[w]>N),Q(0))
            actual=sum((abs(a) for w,a in row.items() if depths[w]>N),Q(0))
            assert expected==actual,(N,v,expected,actual)
            vals.append(expected)
        assert vals
    return len(rows)


def main():
    rng=Random(30171)
    trees=[ [None,0,1,2,3,4], [None,0,0,1,1,2,2], [None,0,1,1,2,2,4] ]
    count=0
    for parents in trees:
        for alpha in (0,1,2):
            depths=[0]*len(parents)
            for v in range(1,len(parents)): depths[v]=depths[parents[v]]+1
            c=[Q(1)]+[Q(d**alpha) for d in depths[1:]]
            for _ in range(10):
                psi=[Q(rng.randrange(-6,7),rng.randrange(1,6)) for v in parents]
                count+=check_profile(parents,c,psi)
    # critical and supercritical explicit symbol limits, evaluated symbolically
    # beta_n * H_(n-1) = H_(n-1)/H_n + (n/(n-1))**alpha -> 2
    for alpha in (0,1):
        H=[Q(0)]
        for n in range(1,251): H.append(H[-1]+Q(1,n**alpha))
        for n in range(2,251):
            a_n=Q(1,n**alpha)/H[n]
            a_prev=Q(1,(n-1)**alpha)/H[n-1]
            direct=n**alpha*(a_n+a_prev)*H[n-1]
            expression=H[n-1]/H[n]+Q(n**alpha,(n-1)**alpha)
            assert direct==expression
        print('ASYMPTOTIC_CRITICAL_TEST alpha=',alpha,'betaH_n250=',float(direct))
    for N in (8,16,32,64):
        # For alpha=2 compact symbol, tail row bound tends zero.
        remainder=sum((Q(1,k*k) for k in range(N+1,20000)),Q(0))+Q(1,19999)
        assert remainder<Q(1,N)
        print('SUMMABLE_TAIL_BOUND N=',N,'bound=',float(remainder))
    print('EXACT_FINITE_ROW_AND_OPERATOR_NORMS_PASS cases=',90,'rows=',count)
    print('BIG_WEIGHTED_TREE_MULTIPLIER_CHECKS_PASS')

if __name__=='__main__': main()
