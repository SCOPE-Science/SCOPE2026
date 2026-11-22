#!/usr/bin/env python3
"""Exact verification of opposite-extremum covariance on small graphs.
Uses exact fractions and exhaustive vertex rank permutations, without sampling.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def integral(a,b,c):
    return sum((Fraction((-1)**j * comb(b,j)*factorial(j)*factorial(c),
                          factorial(j+c+1)*(a+j+c+2))
                for j in range(b+1)), Fraction(0))


def run():
    assertions=0
    graph_count=0
    for n in range(2,6):
        edges=list(combinations(range(n),2))
        perms=list(permutations(range(n)))
        for mask in range(1<<len(edges)):
            graph_count+=1
            neighbor=[set() for _ in range(n)]
            for k,(u,v) in enumerate(edges):
                if mask>>k&1:
                    neighbor[u].add(v);neighbor[v].add(u)
            degree=[len(neighbor[u]) for u in range(n)]
            mx=[0]*n;mn=[0]*n;both=[[0]*n for _ in range(n)]
            for labels in perms:
                peaks=[all(labels[u]>labels[z] for z in neighbor[u]) for u in range(n)]
                valleys=[all(labels[v]<labels[z] for z in neighbor[v]) for v in range(n)]
                for u in range(n):
                    mx[u]+=peaks[u];mn[u]+=valleys[u]
                    if peaks[u]:
                        for v in range(n):
                            if u!=v and valleys[v]: both[u][v]+=1
            total=len(perms)
            for u in range(n):
                assert Fraction(mx[u],total)==Fraction(1,degree[u]+1)
                assert Fraction(mn[u],total)==Fraction(1,degree[u]+1)
                assertions+=2
                for v in range(n):
                    if u==v:continue
                    adjacent = v in neighbor[u]
                    common=len(neighbor[u]&neighbor[v])
                    a=degree[u]-common-int(adjacent)
                    b=degree[v]-common-int(adjacent)
                    joint=Fraction(both[u][v],total)
                    expected=(integral(a,b,common) if adjacent or common else
                              Fraction(1,(a+1)*(b+1)))
                    assert joint==expected,(n,mask,u,v,joint,expected)
                    cov=joint-Fraction(1,(degree[u]+1)*(degree[v]+1))
                    if adjacent:
                        assert cov>=Fraction(1,(degree[u]+1)*degree[v]*(degree[v]+1))
                        assert cov>0
                    elif common:
                        assert cov<0
                    else:
                        assert cov==0
                    assertions+=3
    print(f'PASS: {graph_count} labeled graphs, {assertions} exact assertions; all rank orders n<=5')
if __name__=='__main__':run()
