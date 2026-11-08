#!/usr/bin/env python3
"""Finite exact tests for the adjacent-pair statistics and deletion inequality.
No external dependencies.  The analytic asymptotics require separate proof.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial

def edges(w, undirected=False, excluded=None):
    if excluded is None: excluded = -1
    if undirected:
        return {tuple(sorted((w[k],w[k+1]))) for k in range(len(w)-1) if k!=excluded and k+1!=excluded}
    return {(w[k],w[k+1]) for k in range(len(w)-1) if k!=excluded and k+1!=excluded}

def trial(weights, max_n):
    labels=range(len(weights)); assert sum(weights)==1
    assertions=0
    for n in range(2,max_n+1):
        for undirected in (False,True):
            e=e2=Q(0)
            for w in product(labels,repeat=n):
                prob=Q(1)
                for x in w:prob*=weights[x]
                T=len(edges(w,undirected))
                a=[T-len(edges(w,undirected,j)) for j in range(n)]
                assert all(0<=x<=2 for x in a); assertions+=n
                assert sum(a)<=2*T;assertions+=1
                e+=prob*T;e2+=prob*T*T
            assert e2-e*e <=8*e;assertions+=1
            # Direct transition-edge count moment identity.
            edge_labels=list(product(labels,repeat=2)) if not undirected else [(i,j) for i in labels for j in labels if i<=j]
            expected=Q(0)
            for i,j in edge_labels:
                absent=Q(0)
                for w in product(labels,repeat=n):
                    p=Q(1)
                    for x in w:p*=weights[x]
                    if (i,j) not in edges(w,undirected):absent+=p
                expected+=1-absent
                assertions+=1
            assert expected==e;(assertions:=assertions+1)
            print('n',n,'undirected',undirected,'mean',round(float(e),7),'variance',round(float(e2-e*e),7))
    return assertions
if __name__=='__main__':
    total=trial([Q(1,2),Q(1,3),Q(1,6)],6)
    total+=trial([Q(3,4),Q(1,4)],7)
    print('Exact finite assertions:',total)
