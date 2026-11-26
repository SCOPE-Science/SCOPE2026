#!/usr/bin/env python3
"""Direct exhaustive checker for minimum domination and exchange graphs of K(n,2)."""
from itertools import combinations
from collections import Counter, deque
import json, sys


def analyze(n):
    V=list(combinations(range(n),2)); N=len(V); bit={e:i for i,e in enumerate(V)}
    full=(1<<N)-1
    closed=[]
    for i,u in enumerate(V):
        mask=1<<i
        for j,v in enumerate(V):
            if u[0] not in v and u[1] not in v:
                mask|=1<<j
        closed.append(mask)
    assert all(closed[i]!=full for i in range(N))
    for i,j in combinations(range(N),2):
        assert closed[i]|closed[j]!=full
    opt=[]
    for t in combinations(range(N),3):
        if closed[t[0]]|closed[t[1]]|closed[t[2]]==full:opt.append(t)
    sidx={t:i for i,t in enumerate(opt)}
    typ=[]
    for t in opt:
        endpoints=set(x for i in t for x in V[i]); typ.append('triangle' if len(endpoints)==3 else 'matching' if len(endpoints)==6 else 'OTHER')
    assert 'OTHER' not in typ
    res={'n':n,'minimum':3,'total':len(opt),'triangle':typ.count('triangle'),'matching':typ.count('matching')}
    for mode in ('jump','slide'):
        nbr=[set() for _ in opt]
        for i,t in enumerate(opt):
            for old in t:
                for nw in range(N):
                    if nw in t or (mode=='slide' and (closed[old]>>nw)&1==0):
                        # slide means old/new Kneser adjacent; closed includes old plus its neighbors.
                        continue
                    tt=tuple(sorted((*[x for x in t if x!=old],nw)))
                    j=sidx.get(tt)
                    if j is not None and j!=i:
                        nbr[i].add(j)
        assert all(i in nbr[j] for i,a in enumerate(nbr) for j in a)
        seen=set(); sizes=[]; matching_sizes=[]
        for i in range(len(opt)):
            if i in seen:continue
            seen.add(i);todo=[i]
            for v in todo:
                for w in nbr[v]:
                    if w not in seen:seen.add(w);todo.append(w)
            sizes.append(len(todo))
            if typ[i]=='matching':matching_sizes.append(len(todo))
            assert all(typ[k]==typ[i] for k in todo)
        res[mode]={'edges':sum(map(len,nbr))//2,'components':dict(sorted(Counter(sizes).items())),
                   'matching_components':dict(sorted(Counter(matching_sizes).items())),
                   'triangle_edges':sum(len(nbr[i]) for i,t in enumerate(typ) if t=='triangle'),
                   'matching_degree':sorted({len(nbr[i]) for i,t in enumerate(typ) if t=='matching'})}
    return res

if __name__=='__main__':
    report=[analyze(n) for n in range(5,11)]
    print(json.dumps(report,sort_keys=True,indent=2))
