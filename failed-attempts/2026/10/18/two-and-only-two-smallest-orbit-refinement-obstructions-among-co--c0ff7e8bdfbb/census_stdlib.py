#!/usr/bin/env python3
"""Exhaustive, dependency-free cactus-refinement orbit census through eight vertices.

All graphs are finite, connected, loopless and undirected.  Graphs are represented
by tuples of neighbour bitmasks.  This file uses no data tables or external programs.
"""
import collections
import itertools
import json


def edges(g):
    return [(i,j) for i in range(len(g)) for j in range(i+1,len(g)) if (g[i]>>j)&1]


def extend(g, mask):
    n=len(g)
    h=list(g)+[0]
    for i in range(n):
        if (mask>>i)&1:
            h[i]|=1<<n
            h[n]|=1<<i
    return tuple(h)


def paths_bounded(g, source, target, deleted_edge):
    """Number of distinct simple paths from source to target avoiding edge, capped at two."""
    n=len(g)
    stack=[(source,1<<source)]
    count=0
    while stack:
        u,seen=stack.pop()
        for v in range(n):
            if not (g[u]>>v)&1 or (seen>>v)&1:continue
            if (u==deleted_edge[0] and v==deleted_edge[1]) or (v==deleted_edge[0] and u==deleted_edge[1]):continue
            if v==target:
                count+=1
                if count>=2:return 2
            else:stack.append((v,seen|(1<<v)))
    return count


def cactus(g):
    # All generated graphs are connected: the added vertex has a nonempty neighbourhood.
    # Each graph edge lies on at most one cycle iff its endpoints are joined by at
    # most one alternative simple path after that edge is removed.
    return all(paths_bounded(g,u,v,(u,v))<=1 for u,v in edges(g))


def profiles(g):
    deg=[x.bit_count() for x in g]
    return [(deg[i],tuple(sorted(deg[j] for j in range(len(g)) if (g[i]>>j)&1))) for i in range(len(g))]


def isomorphism(g,h,forced=None):
    """Exact bijection search. Forced map {u:v} can test pointed automorphisms."""
    n=len(g)
    if n!=len(h):return False
    a,b=profiles(g),profiles(h)
    if sorted(a)!=sorted(b):return False
    forced=forced or {}
    mp=dict(forced)
    if len(set(mp.values()))!=len(mp):return False
    for u,v in mp.items():
        if a[u]!=b[v]:return False
    if any(((g[u]>>w)&1)!=((h[v]>>z)&1) for u,v in mp.items() for w,z in mp.items()):return False
    inv=set(mp.values())
    by_profile=collections.defaultdict(list)
    for v in range(n):by_profile[b[v]].append(v)
    order=sorted((v for v in range(n) if v not in mp),key=lambda v:(len(by_profile[a[v]]),-a[v][0],v))
    def rec(k):
        if k==len(order):return True
        u=order[k]
        for v in by_profile[a[u]]:
            if v in inv:continue
            if any(((g[u]>>x)&1)!=((h[v]>>y)&1) for x,y in mp.items()):continue
            mp[u]=v;inv.add(v)
            if rec(k+1):return True
            del mp[u];inv.remove(v)
        return False
    return rec(0)


def canonkey(g):
    return tuple(sorted(profiles(g)))


def refinement(g):
    n=len(g)
    color=[0]*n
    for _ in range(n):
        signature=[(color[u],tuple(sorted(color[v] for v in range(n) if (g[u]>>v)&1))) for u in range(n)]
        tab={s:i for i,s in enumerate(sorted(set(signature)))}
        new=[tab[s] for s in signature]
        if all((color[u]==color[v])==(new[u]==new[v]) for u in range(n) for v in range(n)):
            return new
        color=new
    raise AssertionError('Unexpected number of refinement rounds')


def orbit_partition(g):
    # An exact orbit relation: u~v iff a permutation preserving all edges maps u to v.
    n=len(g)
    classes=[]
    unseen=set(range(n))
    while unseen:
        u=min(unseen)
        cls=[v for v in sorted(unseen) if isomorphism(g,g,{u:v})]
        classes.append(cls)
        unseen.difference_update(cls)
    return sorted(tuple(sorted(x)) for x in classes)


def partition(c):
    cells=collections.defaultdict(list)
    for i,x in enumerate(c):cells[x].append(i)
    return sorted(tuple(z) for z in cells.values())


def census():
    levels={1:[(0,)]}
    report=[]
    for n in range(1,9):
        if n>1:
            buckets=collections.defaultdict(list)
            for g in levels[n-1]:
                for mask in range(1,1<<(n-1)):
                    h=extend(g,mask)
                    if not cactus(h):continue
                    key=canonkey(h)
                    if not any(isomorphism(h,k) for k in buckets[key]):
                        buckets[key].append(h)
            levels[n]=[h for bucket in buckets.values() for h in bucket]
        exceptions=[]
        for g in levels[n]:
            wl=partition(refinement(g));orbits=orbit_partition(g)
            if wl!=orbits:
                exceptions.append({'edges':edges(g),'wl_cells':wl,'orbits':orbits,'degree_sequence':sorted(x.bit_count() for x in g)})
        exceptions.sort(key=lambda d:(len(d['edges']),d['edges']))
        report.append({'n':n,'number_of_cactus_types':len(levels[n]),'nonrefinable_types':len(exceptions),'exceptions':exceptions})
    return report

if __name__=='__main__':
    report=census()
    assert [row['number_of_cactus_types'] for row in report]==[1,1,2,4,9,23,63,188]
    assert [row['nonrefinable_types'] for row in report]==[0,0,0,0,0,0,0,2]
    assert sorted(len(x['edges']) for x in report[-1]['exceptions'])==[9,10]
    for x in report[-1]['exceptions']:
        assert sorted(map(len,x['wl_cells']))==[2,6]
        assert sorted(map(len,x['orbits']))==[2,2,4]
    print(json.dumps(report,sort_keys=True,separators=(',',':')))
