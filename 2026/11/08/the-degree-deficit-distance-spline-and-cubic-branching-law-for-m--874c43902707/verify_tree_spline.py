#!/usr/bin/env python3
"""Exact checks for degree-deficit spline and weighted branching law on metric trees."""
from fractions import Fraction as Q
from itertools import combinations
from random import Random

def tree_data(edges):
    n=len(edges)+1
    g=[[] for _ in range(n)]
    for u,v,ell in edges:
        assert ell>0
        g[u].append((v,ell));g[v].append((u,ell))
    ds=[]
    for st in range(n):
        dis=[None]*n;dis[st]=Q(0);stack=[st]
        for u in stack:
            for v,ll in g[u]:
                if dis[v] is None:
                    dis[v]=dis[u]+ll;stack.append(v)
        assert None not in dis
        ds.append(dis)
    q=[2-len(x) for x in g]
    return g,ds,q,sum((e[2] for e in edges),Q(0))

def pos(x):return max(Q(0),x)

def formcdf(edges,r):
    g,ds,q,L=tree_data(edges)
    qc=sum(len(a)**2 for a in g)-4*len(edges)
    return 2*r/L+qc*r*r/(2*L*L)+sum((q[u]*q[v]*pos(r-ds[u][v])**2 for u in range(len(q)) for v in range(len(q)) if u!=v),Q(0))/(2*L*L)

def directcdf(edges,r):
    g,ds,q,L=tree_data(edges)
    acc=Q(0)
    for u,v,a in edges:
        acc+=a*a-pos(a-r)**2
    for (u,v,a),(w,z,b) in combinations(edges,2):
        p,t=min(((ds[x][y],x,y) for x in (u,v) for y in (w,z))) [1:]
        s=ds[p][t]
        x=r-s
        rect=(pos(x)**2-pos(x-a)**2-pos(x-b)**2+pos(x-a-b)**2)/2
        acc+=2*rect
    return acc/(L*L)

def branching_volume(edges):
    g,ds,q,L=tree_data(edges)
    vol=Q(0)
    for v,arms in enumerate(g):
        arm_lengths=[]
        for u,le in arms:
            seen={v};stack=[u];length=Q(0)
            while stack:
                a=stack.pop();seen.add(a)
                for b,bl in g[a]:
                    if b in seen:continue
                    length+=bl;stack.append(b)
            arm_lengths.append(length+le)
        for a,b,c in combinations(arm_lengths,3):
            vol+=a*b*c
    return vol

def verify_case(edges):
    g,ds,q,L=tree_data(edges)
    n=len(q)
    S=[sum((q[u]*q[v]*ds[u][v]**k for u in range(n) for v in range(n)),Q(0)) for k in (1,2,3)]
    tau=branching_volume(edges)
    assert S[0]==2*L,(S[0],L)
    assert S[1]==2*L*L,(S[1],L)
    assert S[2]==2*L**3-12*tau,(S[2],L,tau)
    assert sum(q)==2
    times={Q(0),L,2*L}
    for row in ds:
        times.update(row)
    for u,v,ll in edges:
        times.add(ll)
    sortedtimes=sorted(times)
    for i,t in enumerate(sortedtimes):
        for x in (t, t+Q(1,7)):
            assert formcdf(edges,x)==directcdf(edges,x),(edges,x,formcdf(edges,x),directcdf(edges,x))
    assert formcdf(edges,2*L)==1
    return len(sortedtimes)*2

def main():
    rng=Random(0x52A225)
    cases=[[(0,1,Q(1))],[(0,1,Q(1)),(1,2,Q(1))],[(0,i,Q(1)) for i in range(1,5)],
        [(0,1,Q(1,2)),(0,2,Q(3,5)),(0,3,Q(7,6)),(3,4,Q(9,7)),(3,5,Q(4,3))]]
    for n in range(3,17):
        for k in range(8):
            ed=[(i,rng.randrange(i),Q(rng.randrange(1,9),rng.randrange(2,11))) for i in range(1,n)]
            cases.append(ed)
    evaluations=0
    for e in cases:evaluations+=verify_case(e)
    print('EXACT_TREE_SPLINE_OK cases=%d exact_cdf_evaluations=%d exact_weighted_moment_orders=3 mean_distance_branching_identities=%d' % (len(cases),evaluations,len(cases)))
if __name__=='__main__':main()
