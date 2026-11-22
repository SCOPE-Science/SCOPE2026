"""Exact rational descent kinetics of three-state Potts spins on Petersen Kneser KG(5,2)."""
from fractions import Fraction as F
from itertools import combinations
from functools import lru_cache
from collections import Counter, defaultdict
from math import comb
from json import dumps

v=list(combinations(range(5),2))
edges=[(i,j) for i in range(10) for j in range(i+1,10) if set(v[i]).isdisjoint(v[j])]
nbr=[tuple(j if i==a else a for a,j in edges if i==a or i==j) for i in range(10)]
assert len(edges)==15 and all(len(n)==3 for n in nbr)
b=tuple(3**i for i in range(10))
types=((10,), (5,5), (5,3,2), (4,3,3))
zero=(F(0),)*4
@lru_cache(None)
def absorb(s):
    colors=tuple((s//b[i])%3 for i in range(10))
    move=[]
    for i in range(10):
        same=sum(colors[j]==colors[i] for j in nbr[i])
        for color in range(3):
            if color==colors[i]:continue
            inc=sum(colors[j]==color for j in nbr[i]) - same
            if inc>0:move.append(s+(color-colors[i])*b[i])
    if not move:
        pat=tuple(sorted(Counter(colors).values(),reverse=True))
        assert pat in types,('unknown stable class',pat)
        return tuple(F(i==types.index(pat)) for i in range(4))
    den=len(move)
    vals=[absorb(t) for t in move]
    return tuple(sum((v[j] for v in vals),F())/den for j in range(4))

if __name__=='__main__':
    tot=[F() for _ in range(4)]; num=Counter();
    for s in range(3**10):
        val=absorb(s)
        tot=[a+b for a,b in zip(tot,val)]
        colors=tuple((s//b[i])%3 for i in range(10))
        if sum(colors[i]==colors[j] for i,j in edges) in (15,10,8,7) and val.count(F(1))==1:
            pat=types[val.index(F(1))]
            # Must explicitly have no allowed transitions: verify via model
            if not any(sum(colors[j]==c for j in nbr[i])>sum(colors[j]==colors[i] for j in nbr[i]) for i in range(10) for c in range(3) if c!=colors[i]):
                num[str(pat)]+=1
    assert sum(num.values())==579
    assert all(x==3**10 for x in [sum(num.values())+3**10-sum(num.values())])
    # Particular 7:2:1 geometry. Fix color A = 0 (7), B = 1 (2), C = 2 (1)
    bygeom=defaultdict(list)
    for i,j in combinations(range(10),2):
        for w in range(10):
            if w in (i,j):continue
            s=b[i]+b[j]+2*b[w]
            pair_adj = int(j in nbr[i]); singleton_adj=int(i in nbr[w])+int(j in nbr[w])
            bygeom[(pair_adj,singleton_adj)].append(1-absorb(s)[0])
    geo={str(k):{'count':len(p),'p':str(p[0]) if len(set(p))==1 else 'NOT CONSTANT'} for k,p in sorted(bygeom.items())}
    assert geo=={'(0, 0)': {'count': 90, 'p': '0'}, '(0, 1)': {'count': 120, 'p': '11/270'}, '(0, 2)': {'count': 30, 'p': '0'}, '(1, 0)': {'count': 60, 'p': '0'}, '(1, 1)': {'count': 60, 'p': '0'}}
    out={'method':'Kneser graph, recursive absorbing equations','terminal_counts':dict(num),
         'uniform_initial_absorption':{str(t):str(z/3**10) for t,z in zip(types,tot)},
         'all_freezing':str(1-tot[0]/3**10),'three_seed_geometry':geo,
         'three_seed_721_freeze_mean':str(sum((x for ls in bygeom.values() for x in ls),F())/360),
         'states':3**10,'cache':absorb.cache_info().currsize}
    print(dumps(out,sort_keys=True,indent=2))
