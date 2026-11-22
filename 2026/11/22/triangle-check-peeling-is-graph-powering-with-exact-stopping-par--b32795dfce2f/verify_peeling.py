#!/usr/bin/env python3
"""Exhaustive independent test of the triangle-check peeling theorem for n<=6.
The algorithm only uses triangle row cardinalities, not graph distances or union-find
for its actual peeling transitions. Graph distances independently predict the result.
"""
from itertools import combinations
from collections import Counter, deque
from math import comb


def check(n):
    pairs=list(combinations(range(n),2))
    idx={pair:i for i,pair in enumerate(pairs)}
    tris=[sum(1<<idx[x] for x in combinations(t,2)) for t in combinations(range(n),3)]
    m=len(pairs); full=(1<<m)-1
    stop=Counter(); stopper_masks=[]; nfull=0; nfail=0; layer_counts=Counter()
    for erased in range(1<<m):
        remaining=erased; rounds=0
        while True:
            peel=0
            for tri in tris:
                sub=remaining&tri
                if sub and not (sub&(sub-1)):
                    peel |= sub
            if not peel:break
            remaining &=~peel
            rounds+=1
        # Independently calculate connected components and distances in original known-edge graph.
        G=[[] for _ in range(n)]
        for i,(a,b) in enumerate(pairs):
            if not (erased>>i)&1:
                G[a].append(b);G[b].append(a)
        comps=[]; distances=[[-1]*n for _ in range(n)]
        for a in range(n):
            d=distances[a];d[a]=0;q=deque([a])
            while q:
                v=q.popleft()
                for w in G[v]:
                    if d[w]==-1:
                        d[w]=d[v]+1;q.append(w)
        unseen=set(range(n))
        while unseen:
            root=min(unseen)
            comp={i for i in unseen if distances[root][i]>=0}
            unseen-=comp;comps.append(comp)
        predicted=sum(1<<i for i,(a,b) in enumerate(pairs)
                      if distances[a][b]==-1)
        diameter=max([d for row in distances for d in row if d>=0],default=0)
        predicted_rounds=(diameter-1).bit_length() if diameter else 0
        assert remaining==predicted,(n,erased,remaining,predicted)
        assert rounds==predicted_rounds,(n,erased,rounds,predicted_rounds)
        if not remaining:nfull+=1
        else:nfail+=1
        layer_counts[rounds]+=1
        if remaining==erased:
            stop[erased.bit_count()]+=1
            stopper_masks.append(erased)
    minimally=Counter()
    for s in stopper_masks:
        if not s:continue
        if not any(t and t != s and (t&s)==t for t in stopper_masks):
            minimally[s.bit_count()]+=1
    return dict(n=n,patterns=1<<m,stopping_by_size=dict(sorted(stop.items())),
                minimal_by_size=dict(sorted(minimally.items())),
                stopping_total=sum(stop.values()),minimum_nonempty=min((k for k in stop if k>0),default=0),
                success_count=nfull,failure_count=nfail,rounds_all_erasure_patterns=dict(sorted(layer_counts.items())))

if __name__=='__main__':
    for n in range(3,7):print(check(n))
