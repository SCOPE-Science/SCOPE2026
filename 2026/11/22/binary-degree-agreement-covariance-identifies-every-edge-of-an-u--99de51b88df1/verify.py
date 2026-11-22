"""Exact arithmetic checks for degree-agreement covariance tomography.
Run with Python 3 standard library: python3 verify.py
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def pmf_other(edges, v, omit):
    dist={0:F(1)}
    for (i,j,p) in edges:
        if v not in (i,j) or omit in (i,j):
            continue
        a=p*(1-p)
        nxt={}
        for k,w in dist.items():
            for z,prob in [(-1,a),(0,1-2*a),(1,a)]:
                nxt[k+z]=nxt.get(k+z,F(0))+w*prob
        dist=nxt
    return dist


def predicted(n,edges):
    edgeprobs={(i,j):p for (i,j,p) in edges}
    ans={}
    for i in range(n):
        for j in range(i+1,n):
            p=edgeprobs.get((i,j),None)
            if p is None:
                ans[(i,j)]=F(0)
            else:
                a=p*(1-p)
                U=pmf_other(edges,i,j); V=pmf_other(edges,j,i)
                delta_i=U.get(0,F(0))-U.get(1,F(0))
                delta_j=V.get(0,F(0))-V.get(1,F(0))
                assert delta_i>0 and delta_j>0
                ans[(i,j)]=2*a*(1-2*a)*delta_i*delta_j
    return ans


def brute(n,edges):
    # Sum all independent signed edge differences in {-1,0,+1}.
    m=len(edges); p0=[p*(1-p) for i,j,p in edges]
    px=[F(0)]*n
    pxy={(i,j):F(0) for i in range(n) for j in range(i+1,n)}
    for z in product((-1,0,1),repeat=m):
        weight=F(1); d=[0]*n
        for t,zz in enumerate(z):
            weight*= (1-2*p0[t]) if zz==0 else p0[t]
            i,j,_=edges[t]; d[i]+=zz; d[j]+=zz
        good=[i for i in range(n) if d[i]==0]
        for i in good:px[i]+=weight
        for x,i in enumerate(good):
            for j in good[x+1:]:pxy[(i,j)]+=weight
    return {(i,j):pxy[(i,j)]-px[i]*px[j]
        for i in range(n) for j in range(i+1,n)}


def run():
    tests=0; pairs=0
    for n in range(2,5):
        possible=[(i,j) for i in range(n) for j in range(i+1,n)]
        for mask in range(1<<len(possible)):
            edges=[(i,j,[F(1,4),F(1,3),F(1,2),F(2,5),F(3,5)][h%5])
                 for h,(i,j) in enumerate(possible) if mask>>h&1]
            got=brute(n,edges); want=predicted(n,edges)
            assert got==want,(n,mask,got,want)
            for ij,c in want.items():
                assert (c>0)==(any(e[:2]==ij for e in edges))
            tests+=1; pairs+=len(want)
    for n,subset in [(5,[(0,1),(1,2),(2,3),(3,4)]),
                     (5,[(0,1),(0,2),(0,3),(0,4)]),
                     (5,[(0,2),(0,3),(1,2),(1,3),(2,4),(3,4)]),
                     (5,[(i,j) for i in range(5) for j in range(i+1,5)])]:
        edges=[(i,j,[F(1,4),F(1,3),F(2,5),F(1,2),F(3,5)][h%5]) for h,(i,j) in enumerate(subset)]
        got=brute(n,edges); want=predicted(n,edges)
        assert got==want
        tests+=1;pairs+=len(want)
    # Fourier lower bound on the strict unimodality gap checked for
    # all homogeneous noise levels in a rational test grid.
    gaps=0
    for m in range(9):
        bound=F(comb(2*m,m),4**m*(m+1))
        for p in [F(1,10),F(1,4),F(1,3),F(1,2),F(2,3),F(3,4)]:
            e=[(0,k+2,p) for k in range(m)]
            dist=pmf_other(e,0,1)
            delta=dist.get(0,F(0))-dist.get(1,F(0))
            assert delta>=bound
            gaps+=1
    print(f'VERIFY_OK {tests} exact host laws, {pairs} pair covariance identities, {gaps} gap bounds')

if __name__=='__main__':run()
