#!/usr/bin/env python3
"""Independent finite exact checks of Lucas-incremented pseudo-Frobenius sets."""
import heapq

def compositions(n):
    if n==0: return [()]
    if n<0: return []
    return [(2,)+x for x in compositions(n-2)]+[(3,)+x for x in compositions(n-3)]

def candidates(a,L):
    sets=[]
    for end in (a-2,a-1):
        for steps in compositions(end-1):
            p=[1]
            for s in steps:p.append(p[-1]+s)
            sets.append(tuple(p))
        for steps in compositions(end-3):
            p=[0,3]
            for s in steps:p.append(p[-1]+s)
            sets.append(tuple(p))
    if a%2:
        sets.extend([tuple(range(2,a,2)),(0,)+tuple(range(4,a,2))])
    return {sum(L[i] for i in b) for b in sets},sets

def apery(m,gs):
    dist=[10**30]*m;dist[0]=0;pq=[(0,0)]
    while pq:
        d,r=heapq.heappop(pq)
        if dist[r]!=d:continue
        for g in gs:
            s=(r+g)%m;v=d+g
            if v<dist[s]:dist[s]=v;heapq.heappush(pq,(v,s))
    return dist

def c(n):
    if n==0:return 1
    if n<0:return 0
    return c(n-2)+c(n-3)

L=[2,1]
for _ in range(20):L.append(L[-1]+L[-2])
for a in range(3,18):
    m=L[a];gs=[m]+[m+L[j] for j in range(a)]
    w=apery(m,gs)
    pf={r for r in range(1,m) if all(w[(r+L[j])%m]<=w[r]+L[j] for j in range(a))}
    xs,B=candidates(a,L)
    assert len(xs)==len(B),('nonunique',a)
    assert xs==pf, ('PF error',a,sorted(xs-pf),sorted(pf-xs))
    for ids in B:
        assert not any(j+1 in ids for j in ids) and not (0 in ids and 2 in ids)
    claimed=c(a-2)+c(a-3)+c(a-4)+c(a-5)+2*(a%2)
    assert len(pf)==claimed,(a,len(pf),claimed)
    print(f'a={a} m={m} type={len(pf)} exact_PF=ok')
print('All checks passed for a=3..17.')
