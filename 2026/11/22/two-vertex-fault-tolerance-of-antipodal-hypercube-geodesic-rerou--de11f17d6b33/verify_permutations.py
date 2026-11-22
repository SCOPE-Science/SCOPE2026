#!/usr/bin/env python3
"""Exhaustive rank/intersection orbit verifier for faulted cube geodesics."""
from itertools import permutations
from collections import deque


def orbit_representatives(n):
    for k in range(1,n):
        a=(1<<k)-1
        for ell in range(k,n):
            for t in range(max(0,k+ell-n),min(k,ell)+1):
                b=((1<<t)-1)
                for q in range(k,k+ell-t):
                    b|=1<<q
                if a!=b:
                    yield k,ell,t,a,b


def run():
    for n in range(3,9):
        ps=list(permutations(range(n)))
        index={p:i for i,p in enumerate(ps)}
        forbidden_prefixes=[]
        swaps=[]
        for p in ps:
            v=0
            seen=set()
            for j in p[:-1]:
                v|=(1<<j)
                seen.add(v)
            forbidden_prefixes.append(seen)
            swaps.append(tuple(index[p[:j]+(p[j+1],p[j])+p[j+2:]] for j in range(n-1)))
        bad=[]
        total=0
        single_faults=[]
        for k,ell,t,a,b in orbit_representatives(n):
            total+=1
            good=bytearray((a not in q and b not in q) for q in forbidden_prefixes)
            visited=bytearray(len(ps))
            components=[]
            edges=0
            for i in range(len(ps)):
                if not good[i]:
                    continue
                edges+=sum(good[j] for j in swaps[i])
                if visited[i]:
                    continue
                visited[i]=1
                queue=[i]
                for v in queue:
                    for w in swaps[v]:
                        if good[w] and not visited[w]:
                            visited[w]=1
                            queue.append(w)
                components.append(len(queue))
            edges//=2
            if n==4:
                single_faults.append((k,ell,t,sum(good),edges,len(components)))
            if len(components)!=1:
                bad.append((k,ell,t,components))
        if n==3:
            assert bad==[(1,2,0,[1,1])],bad
        else:
            assert not bad,(n,bad)
        if n==4:
            expected=[(1,1,0,12,14,1),(1,2,0,14,16,1),
                      (1,2,1,16,21,1),(1,3,0,12,12,1),
                      (1,3,1,14,17,1),(2,2,0,16,20,1),
                      (2,2,1,16,21,1),(2,3,1,14,16,1),
                      (2,3,2,16,21,1),(3,3,2,12,14,1)]
            assert single_faults==expected,(single_faults,expected)
        print('n=%d orbit_pairs=%d disconnected=%d %s' % (n,total,len(bad),str(bad) if bad else ''))
    print('PERMUTATION_ORBITS_OK')

if __name__=='__main__':
    run()
