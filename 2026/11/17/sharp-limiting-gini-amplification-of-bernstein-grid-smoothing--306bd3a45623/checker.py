#!/usr/bin/env python3
"""Exact-rational finite corroboration of a Bernstein-collocation Gini theorem."""
from fractions import Fraction as Q
from math import comb
from itertools import combinations

def bernstein(n):
    return [[Q(comb(n,j)*k**j*(n-k)**(n-j),n**n) for j in range(n+1)]
            for k in range(n+1)]

def gini(v):
    return sum(abs(v[i]-v[j]) for i in range(len(v)) for j in range(i+1,len(v)))

def mass_bound(n):
    B=bernstein(n)
    s=[sum(B[k][j] for k in range(n+1)) for j in range(n+1)]
    return s, max(s)

def exact_cut_norm(n):
    B=bernstein(n); N=n+1
    v=Q(0); winners=[]; verified=0
    for mask in range(1,(1<<N)-1):
        x=[Q((mask>>j)&1) for j in range(N)]
        y=[sum(B[k][j]*x[j] for j in range(N)) for k in range(N)]
        q=gini(y)/gini(x)
        verified+=1
        if q>v: v=q; winners=[mask]
        elif q==v: winners.append(mask)
    return v,winners,verified

def endpoint(n):
    u=[Q((n-k)**n,n**n) for k in range(n+1)]
    S=sum(u)
    R=S-Q(2,n)*sum(k*u[k] for k in range(n+1))
    return R,S

def main():
    vals={2:Q(1),3:Q(88,81),4:Q(37,32),5:Q(3781,3125),6:Q(1217,972)}
    cuts=0
    for n in range(2,9):
        B=bernstein(n)
        assert all(sum(row)==1 for row in B)
        s,mass=mass_bound(n)
        R,S=endpoint(n)
        assert mass==S and s[0]==s[-1]==S
        v,w,c=exact_cut_norm(n)
        cuts+=c
        assert R<=v<=S
        if n in vals: assert v==vals[n],(n,v)
        assert v>1 if n>=3 else v==1
        print(f'EXACT_N={n}_CUTS={c}_NORM={v}_ENDPOINT={R}_COLUMN_MAX={S}')
    print(f'EXACT_ALL_BINARY_CUTS_PASSED {cuts}')
    for n in range(3,101):
        R,S=endpoint(n)
        assert Q(1)<R<S
        assert S<Q(8,5)  # implied by geometric envelope <1.6
    print('EXACT_ENDPOINT_AMPLIFICATION_AND_UPPER_ENVELOPE_PASSED_N3_TO_N100')
    for N in range(2,13):
        # Jensen coarea weight bound: q(S)q(S^c) <= N qmax * s(N-s)/N^2
        # Tested for a sample of rational probability vectors and every cut.
        for a in range(1,5):
            weights=[Q((j+1)**a) for j in range(N)]
            sm=sum(weights); weights=[w/sm for w in weights]
            qm=max(weights)
            for mask in range(1,(1<<N)-1):
                s=mask.bit_count(); p=sum(weights[j] for j in range(N) if mask>>j&1)
                assert N*N*p*(1-p)<=N*qm*s*(N-s)
    print('EXACT_WEIGHTED_GINI_COMPARISON_ALL_TESTED_CUTS_PASSED')
    print('ALL_BERNSTEIN_GINI_CHECKS_PASSED')

if __name__=='__main__':main()
