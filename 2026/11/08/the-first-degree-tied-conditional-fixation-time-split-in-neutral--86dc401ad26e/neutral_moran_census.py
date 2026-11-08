#!/usr/bin/env python3
"""Exact complete census for neutral birth-death Moran fixation-time inequivalence.
Uses only Python standard library; no data or external graph catalog.
Run: python3 neutral_moran_census.py
"""
from fractions import Fraction as F
from itertools import combinations, permutations


def edges(n):
    return list(combinations(range(n),2))

def graph_of(n, mask):
    a=[set() for _ in range(n)]
    for i,(u,v) in enumerate(edges(n)):
        if (mask>>i)&1:
            a[u].add(v); a[v].add(u)
    return a

def connected(a):
    seen={0}; todo=[0]
    while todo:
        for v in a[todo.pop()]:
            if v not in seen:
                seen.add(v); todo.append(v)
    return len(seen)==len(a)

def canonical_maps(n):
    e=edges(n); lookup={pair:i for i,pair in enumerate(e)}
    return [tuple(lookup[tuple(sorted((perm[u],perm[v])))] for u,v in e) for perm in permutations(range(n))]

def representatives(n):
    maps=canonical_maps(n)
    rep={}
    for mask in range(1<<len(edges(n))):
        if not connected(graph_of(n,mask)):
            continue
        canon=min(sum(1<<p[i] for i in range(len(p)) if (mask>>i)&1) for p in maps)
        rep[canon]=canon
    return sorted(rep)

def solve(A,b):
    N=len(b); z=[list(A[i])+[b[i]] for i in range(N)]
    for j in range(N):
        k=next(k for k in range(j,N) if z[k][j]!=0)
        if k!=j: z[j],z[k]=z[k],z[j]
        c=z[j][j]
        for x in range(j,N+1): z[j][x]/=c
        for i in range(N):
            if i==j: continue
            c=z[i][j]
            if not c: continue
            for x in range(j,N+1): z[i][x]-=c*z[j][x]
    return [z[i][N] for i in range(N)]

def fixation_times(n,a):
    degree=[len(x) for x in a]; normal=sum((F(1,d) for d in degree),F(0))
    states=list(range(1,(1<<n)-1)); where={s:i for i,s in enumerate(states)}
    N=len(states); A=[[F(int(i==j)) for j in range(N)] for i in range(N)]
    h=[sum((F(1,degree[v]) for v in range(n) if (s>>v)&1),F(0))/normal for s in states]
    for i,s in enumerate(states):
        for source in range(n):
            for target in a[source]:
                p=F(1,n*degree[source])
                new=(s|(1<<target)) if s&(1<<source) else (s&~(1<<target))
                if new in where:
                    A[i][where[new]]-=p
    u=solve(A,h)
    assert all(sum((A[i][j]*u[j] for j in range(N)),F(0))==h[i] for i in range(N))
    return [(h[where[1<<v]],u[where[1<<v]]/h[where[1<<v]]) for v in range(n)]

def main():
    EXPECTED={2:1,3:2,4:6,5:21}
    winners=[]
    for n in range(2,6):
        reps=representatives(n)
        assert len(reps)==EXPECTED[n], (n,len(reps))
        count=0
        for mask in reps:
            a=graph_of(n,mask); stats=fixation_times(n,a)
            unequal=[(i,j) for i in range(n) for j in range(i+1,n)
                     if stats[i][0]==stats[j][0] and stats[i][1]!=stats[j][1]]
            if unequal:
                count+=1; assert n==5
                winners.append(mask)
                print('n=5 canonical graph',mask,'edges', [e for k,e in enumerate(edges(n)) if mask>>k&1], 'unequal_pairs',unequal)
        if n<=4: assert count==0
        if n==5: assert count==7
        print('n',n,'connected_classes',len(reps),'classes_with_distinction',count)
    # The path representative, chosen independently by a concrete edge list.
    a=[{1},{0,2},{1,3},{2,4},{3}]
    stats=fixation_times(5,a)
    assert stats[1][0]==stats[2][0]==F(1,7)
    assert stats[1][1]==F(14650,329)
    assert stats[2][1]==F(26955,658)
    assert stats[1][1]-stats[2][1]==F(2345,658)
    print('P5 seed1',stats[1], 'seed2',stats[2], 'difference',stats[1][1]-stats[2][1]);print('PASS')
if __name__=='__main__':main()
