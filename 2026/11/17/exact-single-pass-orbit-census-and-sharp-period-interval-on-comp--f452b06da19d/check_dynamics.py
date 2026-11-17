"""Direct finite-state check for chip-firing single-pass periodic counts."""
from itertools import combinations, product
from collections import Counter
from math import comb


def weak_compositions(total,n):
    for cuts in combinations(range(total+n-1),n-1):
        positions=(-1,)+cuts+(total+n-1,)
        yield tuple(positions[i+1]-positions[i]-1 for i in range(n))


def graph(parts):
    labels=[]
    for i,k in enumerate(parts): labels += [i]*k
    adj=[tuple(j for j in range(len(labels)) if labels[j]!=labels[v]) for v in range(len(labels))]
    return adj


def step(x, adj):
    firing=[int(x[i]>=len(adj[i])) for i in range(len(x))]
    return tuple(x[i]-firing[i]*len(adj[i])+sum(firing[j] for j in adj[i]) for i in range(len(x))),firing


def direct(parts):
    adj=graph(parts)
    vertices=len(adj); edge_count=sum(map(len,adj))//2
    cnt=Counter()
    for x in weak_compositions(edge_count,vertices):
        nxt,fire=step(x,adj)
        times=[]
        if x==nxt:
            continue
        curr=x
        # Find only orbits initially periodic and with each vertex firing exactly once.
        counts=[0]*vertices
        seen={x:0}
        ok=False
        for t in range(vertices+2):
            nxt,fire=step(curr,adj)
            for i,b in enumerate(fire): counts[i]+=b
            if nxt==x:
                ok=all(v==1 for v in counts)
                if ok:cnt[t+1]+=1
                break
            if nxt in seen: break
            seen[nxt]=t+1
            curr=nxt
    return cnt,comb(edge_count+vertices-1,vertices-1)

if __name__=='__main__':
    cases=[(1,1,1),(2,1,1),(2,2,1),(2,2,2),(3,1,1),(3,2,1),(1,1,1,1),(2,1,1,1),(2,2,1,1)]
    for parts in cases:
        got,states=direct(parts)
        print('parts=',parts,'critical_mass_states=',states,'single_pass_period_counts=',dict(sorted(got.items())))
