#!/usr/bin/env python3
"""Exact census of three-player binary generic best-response orientations.

Use: python3 verify.py
All arithmetic is integral; it visits all 2**12 independent orientations.
"""
from collections import Counter, defaultdict
from itertools import permutations
from math import comb

N=8
EDGES=tuple((u, u^(1<<i)) for u in range(N) for i in range(3) if (u^(1<<i))>u)
assert len(EDGES)==12
EINDEX={e:j for j,e in enumerate(EDGES)}


def successors(code):
    adj=[set() for _ in range(N)]
    for j,(a,b) in enumerate(EDGES):
        if (code>>j)&1:a,b=b,a
        adj[a].add(b)
    return adj


def independent_properties(adj):
    """DFS reachability and recursive directed-cycle detection."""
    incoming=[set() for _ in range(N)]
    for a in range(N):
        for b in adj[a]:incoming[b].add(a)
    sinks={a for a in range(N) if not adj[a]}
    sources={a for a in range(N) if not incoming[a]}
    R=[]
    for u in range(N):
        seen={u}; queue=[u]
        while queue:
            for v in adj[queue.pop()]:
                if v not in seen:seen.add(v);queue.append(v)
        R.append(seen)
    weak=bool(sinks) and all(R[u] & sinks for u in range(N))
    connected=bool(sinks) and all(sinks <= R[u] for u in range(N) if u not in sinks)
    superconnected=bool(sinks) and all((set(range(N))-sources)<=R[u] for u in range(N) if u not in sinks)
    colors=[0]*N
    def walk(u):
        colors[u]=1
        for v in adj[u]:
            if colors[v]==1:return True
            if colors[v]==0 and walk(v):return True
        colors[u]=2
        return False
    acyclic=not any(walk(i) for i in range(N) if colors[i]==0)
    return len(sinks),weak,connected,superconnected,acyclic


def reverse_target_connected(adj, targets, origins):
    """Independent reverse-traversal test of target reachability."""
    incoming=[set() for _ in range(N)]
    for u,row in enumerate(adj):
        for v in row:incoming[v].add(u)
    for target in targets:
        seen={target};stack=[target]
        while stack:
            for pred in incoming[stack.pop()]:
                if pred not in seen:seen.add(pred);stack.append(pred)
        if not all(u in seen for u in origins):return False
    return True


def topological_acyclic(adj):
    """Independent Kahn algorithm to check the recursive cycle test."""
    indeg=[0]*N
    for row in adj:
        for b in row:indeg[b]+=1
    queue=[i for i,d in enumerate(indeg) if d==0]
    removed=0
    while queue:
        a=queue.pop();removed+=1
        for b in adj[a]:
            indeg[b]-=1
            if indeg[b]==0:queue.append(b)
    return removed==N


def maps():
    for perm in permutations(range(3)):
        for t in range(8):
            yield tuple(t ^ sum(((v>>i)&1)<<perm[i] for i in range(3)) for v in range(8))
MAPS=tuple(maps())
assert len(set(MAPS))==48


def transformed(code,mp):
    result=0
    for j,(a,b) in enumerate(EDGES):
        if (code>>j)&1:a,b=b,a
        a,b=mp[a],mp[b]
        e=tuple(sorted((a,b)))
        i=EINDEX[e]
        if a>b:result|=1<<i
    return result


if __name__=='__main__':
    counts=Counter(); binsinks=Counter(); orbits=defaultdict(list)
    for code in range(1<<12):
        adj=successors(code)
        p=independent_properties(adj)
        assert p[-1]==topological_acyclic(adj),('cycle mismatch',code)
        sinks=[u for u in range(N) if not adj[u]]
        origins=[u for u in range(N) if adj[u]]
        inbound=set(v for row in adj for v in row)
        assert p[2] == (bool(sinks) and reverse_target_connected(adj,sinks,origins)),('connected',code)
        assert p[3] == (bool(sinks) and reverse_target_connected(adj,inbound,origins)),('super',code)
        binsinks[p[0]]+=1
        counts[p[1:]]+=1
        canonical=min(transformed(code,mp) for mp in MAPS)
        orbits[canonical].append((code,p))
    assert sum(counts.values())==4096
    expected_sinks={0:962,1:2232,2:844,3:56,4:2}
    assert binsinks==expected_sinks,(binsinks,expected_sinks)
    assert counts==Counter({(False,False,False,False):962,
                           (True,False,False,True):642,
                           (True,True,False,False):888,
                           (True,True,False,True):1220,
                           (True,True,True,False):384})
    assert len(orbits)==sum(1 for _ in orbits)
    for canon,rows in orbits.items():
        assert len({p for _,p in rows})==1,(canon,rows)
        assert len(rows) in (2,4,6,8,12,16,24,48),(canon,len(rows))
    oc=Counter(next(iter(rows))[1][1:] for rows in orbits.values())
    print('TOTAL',sum(counts.values()),'ORBITS',len(orbits))
    print('SINK DISTRIBUTION',dict(sorted(binsinks.items())))
    print('CONDITION VECTOR (weak, connected, superconnected, acyclic)')
    for key,value in sorted(counts.items()):print(key,value,'orbits',oc[key])
    print('TOTAL CONNECTION ORBITS',sum(v for k,v in oc.items() if k[1]))
    # Independent Burnside count: each group element fixes an exact subset.
    sumfixed=0
    for mp in MAPS:
        sumfixed+=sum(transformed(code,mp)==code for code in range(1<<12))
    assert sumfixed == 48*len(orbits),(sumfixed,len(orbits))
    print('BURNSIDE FIXED SUM',sumfixed)
    # Independently count factorial moments of sink number by independent sets.
    indep=Counter()
    for subset in range(1<<8):
        size=subset.bit_count()
        if size==0:continue
        if all(not ((subset>>a)&1 and (subset>>b)&1) for a,b in EDGES):
            indep[size]+=1
    assert indep==Counter({1:8,2:16,3:8,4:2})
    for k in range(1,5):
        lhs=sum(comb(j,k)*count for j,count in binsinks.items() if j>=k)
        rhs=indep[k] * (1<<(12-3*k))
        assert lhs==rhs,(k,lhs,rhs)
    print('ALL EXACT CHECKS PASSED')
