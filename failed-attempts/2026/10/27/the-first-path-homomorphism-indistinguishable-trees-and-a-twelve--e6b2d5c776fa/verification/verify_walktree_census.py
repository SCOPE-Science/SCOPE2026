"""Standard-library-only exhaustive generation and walk fingerprints for unlabelled trees."""
from collections import defaultdict
from itertools import permutations

def canon(edges, n):
    adj=[[] for _ in range(n)]
    for a,b in edges: adj[a].append(b);adj[b].append(a)
    def root(v,p): return '('+''.join(sorted(root(w,v) for w in adj[v] if w!=p))+')'
    deg=[len(a) for a in adj]; le=[i for i,d in enumerate(deg) if d<=1]; remaining=n
    while remaining>2:
        remaining-=len(le); nxt=[]
        for v in le:
            deg[v]=0
            for w in adj[v]:
                if deg[w]>0:
                    deg[w]-=1
                    if deg[w]==1: nxt.append(w)
        le=nxt
    return min(root(v,-1) for v in le)

def walk(edges,n,kmax=None):
    adj=[[] for _ in range(n)]
    for a,b in edges: adj[a].append(b);adj[b].append(a)
    v=[1]*n; result=[n]
    for _ in range(kmax or 2*n):
        v=[sum(v[j] for j in adj[i]) for i in range(n)]
        result.append(sum(v))
    return tuple(result)

def all_trees(N):
    trees={1:[tuple()]}
    for n in range(2,N+1):
        seen={}
        for E in trees[n-1]:
            for parent in range(n-1):
                F=tuple(sorted(E+((parent,n-1),)))
                code=canon(F,n)
                if code not in seen:seen[code]=F
        trees[n]=list(seen.values())
    return trees


def matching_numbers(edges):
    hist=[0]*7
    for mask in range(1<<len(edges)):
        used=set();k=0;ok=True
        for i,(u,v) in enumerate(edges):
            if mask>>i&1:
                if u in used or v in used:ok=False;break
                used.update((u,v));k+=1
        if ok:hist[k]+=1
    return hist

def verify():
    expected=[0,1,1,1,2,3,6,11,23,47,106,235,551]
    trees=all_trees(12)
    found=None
    for n in range(1,13):
        allE=trees[n]
        assert len(allE)==expected[n],(n,'enumeration count')
        assert len({canon(E,n) for E in allE})==len(allE),(n,'duplicate')
        buckets={}
        for E in allE:
            buckets.setdefault(walk(E,n),[]).append(E)
        collisions=[v for v in buckets.values() if len(v)>1]
        assert len(buckets)==len(allE)-(1 if n==12 else 0),(n,'path class count')
        assert len(collisions)==(1 if n==12 else 0),(n,'collision groups')
        print(f'ORDER {n}: TREES {len(allE)}, PATH_CLASSES {len(buckets)}')
        if n==12:
            assert len(collisions[0])==2
            A,B=collisions[0]
            assert canon(A,n)!=canon(B,n)
            assert walk(A,n)==walk(B,n)
            assert matching_numbers(A)==matching_numbers(B)==[1,11,42,66,39,6,0]
            assert walk(A,n)[:12]==(12,22,48,98,212,444,958,2028,4372,9302,20046,42760)
            found=[list(map(list,A)),list(map(list,B))]
    print('WITNESS_A',found[0]);print('WITNESS_B',found[1])
    print('PATH_COUNT_THRESHOLD_AND_UNIQUE_CLASS_PASS')

if __name__=='__main__':
    verify()
