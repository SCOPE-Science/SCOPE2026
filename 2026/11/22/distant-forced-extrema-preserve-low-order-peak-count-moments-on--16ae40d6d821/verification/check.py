#!/usr/bin/env python3
"""Finite exact checks for a theorem on local maxima under forced extremal rankings."""
import itertools
from fractions import Fraction
from math import factorial, comb

def graph_cycle(n):
    return [tuple({(i-1)%n,(i+1)%n}) for i in range(n)]

def graph_cube(d):
    return [tuple(v^(1<<j) for j in range(d)) for v in range(1<<d)]

def moments_from_ranks(adj, low=None, high=None, order=2):
    n=len(adj)
    total=[0]*(order+1)
    for perm in itertools.permutations(range(n)):
        if low is not None and perm[low] != 0: continue
        if high is not None and perm[high] != n-1: continue
        k=sum(all(perm[v]>perm[u] for u in adj[v]) for v in range(n))
        for i in range(order+1): total[i]+=k**i
    return [Fraction(x,total[0]) for x in total]

def pair_probability(neighbors, v,w, bottom=None,top=None):
    if v==bottom or w==bottom or v in (set(neighbors[top]) if top is not None else set()) or w in (set(neighbors[top]) if top is not None else set()):
        return Fraction(0)
    if v==top or w==top:
        if v==top and w==top:return Fraction(1)
        other=w if v==top else v
        alln=set(neighbors[other]); alln.discard(bottom);alln.discard(top)
        return Fraction(1,len(alln)+1)
    if w in neighbors[v]: return Fraction(0)
    A=set(neighbors[v]); A.discard(bottom);A.discard(top)
    B=set(neighbors[w]); B.discard(bottom);B.discard(top)
    a,b,k=len(A),len(B),len(A&B)
    return (Fraction(1,a+1)+Fraction(1,b+1))/Fraction(a+b-k+2)

def forced_variance(adj,bottom,top):
    n=len(adj); probs=[]
    for v in range(n):
        if v==top:p=Fraction(1)
        elif v==bottom or top in adj[v]:p=Fraction(0)
        else:
            a=sum(int(u not in (bottom,top)) for u in adj[v]);p=Fraction(1,a+1)
        probs.append(p)
    m=sum(probs,Fraction(0))
    second=m
    for v in range(n):
        for w in range(v+1,n):second+=2*pair_probability(adj,v,w,bottom,top)
    return m,second-m*m

def test():
    num=0
    for name,adj,low,high,r in [
        ('C6-opposites',graph_cycle(6),0,3,1),
        ('C7-opposites',graph_cycle(7),0,3,1),
        ('Q2-opposites',graph_cube(2),0,3,2),
        ('Q3-opposites',graph_cube(3),0,7,2),
    ]:
        base=moments_from_ranks(adj,order=max(2,r))
        con=moments_from_ranks(adj,low,high,order=max(2,r))
        lowonly=moments_from_ranks(adj,low,None,order=max(2,r))
        highonly=moments_from_ranks(adj,None,high,order=max(2,r))
        assert base==lowonly==highonly, (name,'one-endpoint invariance')
        dist=3 if name.startswith('C') else len(adj).bit_length()-1
        if dist>2*r: assert base[:r+1]==con[:r+1], (name,base,con)
        exact_m,exact_v=forced_variance(adj,low,high)
        assert exact_m==con[1],(name,exact_m,con[1])
        assert exact_v==con[2]-con[1]**2,(name,exact_v,con)
        num += 3 + (dist>2*r)
        print(name,'distance',dist,'mean',con[1],'variance',exact_v,'moment_match_range',max(0,(dist-1)//2))
    for d in range(2,10):
        n=1<<d
        m,v=forced_variance(graph_cube(d),0,n-1)
        baseline_m=Fraction(n,d+1)
        baseline_v=Fraction(n*(d-1),2*(d+1)**2)
        assert m==baseline_m if d>=3 else m!=baseline_m
        if d>=5: assert v==baseline_v,(d,v,baseline_v)
        num += 1 + (d>=5)
    assert forced_variance(graph_cube(4),0,15)==(Fraction(16,5),Fraction(6,7))
    assert forced_variance(graph_cube(3),0,7)==(Fraction(2),Fraction(4,5))
    print('verified',num+2,'independent exact assertions')
if __name__=='__main__':test()
