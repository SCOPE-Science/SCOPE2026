#!/usr/bin/env python3
"""Exact minimax domination-game verification, standard library only.
The graph constructions and recurrence are explicit. Python 3.9+.
"""
from functools import lru_cache
from collections import Counter, defaultdict
from itertools import combinations
import json

def graph(name):
    if name == 'heawood':
        n=14
        edges=[(p,7+line) for p in range(7) for line in range(7)
               if (line-p)%7 in (0,1,3)]
    elif name == 'mobius_kantor':
        n=16
        edges=[(i,(i+1)%8) for i in range(8)]
        edges += [(i,8+i) for i in range(8)]
        edges += [(8+i,8+(i+3)%8) for i in range(8)]
    elif name == 'pappus':
        n=18
        edges=[]
        for x in range(3):
            for y in range(3):
                p=3*x+y
                edges += [(p,9+x),(p,12+y),(p,15+(x+y)%3)]
    elif name == 'desargues':
        from itertools import combinations
        two=list(combinations(range(5),2))
        three=list(combinations(range(5),3))
        n=20
        edges=[(i,10+j) for i,a in enumerate(two) for j,b in enumerate(three)
               if set(a).issubset(b)]
    else:
        raise ValueError(name)
    edges=sorted({tuple(sorted(e)) for e in edges})
    a=[set() for _ in range(n)]
    for x,y in edges: a[x].add(y); a[y].add(x)
    assert len(edges)==3*n//2 and all(len(s)==3 for s in a)
    seen={0}; q=[0]
    for x in q:
        for y in a[x]-seen: seen.add(y);q.append(y)
    assert len(seen)==n
    return a

def evaluate(name):
    a=graph(name);n=len(a);full=(1<<n)-1
    closed=[1<<i | sum(1<<j for j in a[i]) for i in range(n)]
    @lru_cache(None)
    def V(mask,turn):
        if mask==full: return 0
        values=(V(mask|h,1-turn) for h in closed if (h|mask)!=mask)
        return 1+(min(values) if turn==0 else max(values))
    d,s=V(0,0),V(0,1)
    def response(anchor,first):
        dist={anchor:0};q=[anchor]
        for u in q:
            for w in a[u]:
                if w not in dist:dist[w]=dist[u]+1;q.append(w)
        assert len(dist)==n
        bydist=defaultdict(Counter)
        for j,h in enumerate(closed):
            if (closed[anchor]|h)==closed[anchor]:continue
            remaining_turn=0 if first=='dominator' else 1
            cost=2+V(closed[anchor]|h,remaining_turn)
            bydist[dist[j]][cost]+=1
        return {str(k):{str(c):ct for c,ct in sorted(co.items())}
                for k,co in sorted(bydist.items())}
    resp={first: response(0,first) for first in ('dominator','staller')}
    # Verify the reported response geometry at every possible initial vertex.
    for anchor in range(n):
        assert 1+V(closed[anchor],1)==d
        assert 1+V(closed[anchor],0)==s
        for first in ('dominator','staller'):
            assert response(anchor,first)==resp[first]
    return dict(name=name, vertices=n, edges=3*n//2, dominator_start=d, staller_start=s,
                second_ply_outcomes=resp, memoized_states=V.cache_info().currsize)

if __name__=='__main__':
    results=[evaluate(n) for n in ['heawood','mobius_kantor','pappus','desargues']]
    print(json.dumps(results,sort_keys=True,indent=2))
    expect={'heawood':(7,6),'mobius_kantor':(7,6),'pappus':(8,7),'desargues':(9,9)}
    assert all((r['dominator_start'],r['staller_start'])==expect[r['name']] for r in results)
    print('PYTHON_VERIFICATION_OK')
