#!/usr/bin/env python3
"""Reverse indegree peeling on five explicit edge-labelled cubic identity graphs.
Graph edges are embedded independently of the LCF-construction verifier.
Only Python 3 standard library is needed.
"""
import collections
import json

EDGES = [[[0, 1], [0, 7], [0, 11], [1, 2], [1, 3], [2, 3], [2, 11], [3, 4], [4, 5], [4, 10], [5, 6], [5, 9], [6, 7], [6, 8], [7, 8], [8, 9], [9, 10], [10, 11]], [[0, 1], [0, 6], [0, 11], [1, 2], [1, 4], [2, 3], [2, 10], [3, 4], [3, 11], [4, 5], [5, 6], [5, 8], [6, 7], [7, 8], [7, 9], [8, 9], [9, 10], [10, 11]], [[0, 1], [0, 4], [0, 11], [1, 2], [1, 11], [2, 3], [2, 7], [3, 4], [3, 5], [4, 5], [5, 6], [6, 7], [6, 9], [7, 8], [8, 9], [8, 10], [9, 10], [10, 11]], [[0, 1], [0, 6], [0, 11], [1, 2], [1, 8], [2, 3], [2, 4], [3, 4], [3, 9], [4, 5], [5, 6], [5, 11], [6, 7], [7, 8], [7, 10], [8, 9], [9, 10], [10, 11]], [[0, 1], [0, 2], [0, 11], [1, 2], [1, 8], [2, 3], [3, 4], [3, 9], [4, 5], [4, 7], [5, 6], [5, 11], [6, 7], [6, 10], [7, 8], [8, 9], [9, 10], [10, 11]]]

def classify(edges):
    n=12
    adj=[set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b)
        adj[b].add(a)
    assert len(edges)==18 and all(len(s)==3 for s in adj)
    # A distinct tuple-state update, converted back to integer IDs.
    successors=[]
    for x in range(1<<n):
        bits=[(x//(1<<k))%2 for k in range(n)]
        new_bits=[int(sum(bits[j] for j in adj[i])>=2) for i in range(n)]
        successors.append(sum(bit*(1<<i) for i,bit in enumerate(new_bits)))
    inverse=[[] for _ in successors]
    for x,y in enumerate(successors):inverse[y].append(x)
    indegree=[len(p) for p in inverse]
    q=collections.deque(v for v,degree in enumerate(indegree) if degree==0)
    peeled=[]
    while q:
        x=q.popleft()
        peeled.append(x)
        y=successors[x]
        indegree[y]-=1
        if indegree[y]==0:q.append(y)
    cycle_vertices=set(range(1<<n))-set(peeled)
    orbit={}
    depth={}
    cycles={}
    for start in sorted(cycle_vertices):
        if start in orbit:continue
        seq=[]
        x=start
        while x not in orbit and x not in seq:
            seq.append(x)
            x=successors[x]
        assert x==start
        name=min(seq)
        cycles[name]=len(seq)
        for y in seq:orbit[y]=name;depth[y]=0
    for x in reversed(peeled):
        assert successors[x] in orbit
        orbit[x]=orbit[successors[x]]
        depth[x]=depth[successors[x]]+1
    assert len(orbit)==1<<n
    basin_sizes=collections.Counter(orbit.values())
    by_period=collections.Counter(cycles.values())
    eventual=collections.Counter(cycles[orbit[x]] for x in range(1<<n))
    entry=collections.Counter(depth.values())
    size_hist={1:collections.Counter(),2:collections.Counter()}
    for orbit_name,size in basin_sizes.items():size_hist[cycles[orbit_name]][size]+=1
    assert sum(by_period.values())==len(basin_sizes)
    return {
        'fixed_states':by_period[1],
        'two_cycle_orbits':by_period[2],
        'period_one_basin_population':eventual[1],
        'period_two_basin_population':eventual[2],
        'entry_histogram':[entry[i] for i in range(max(entry)+1)],
        'basin_histogram':{str(p):{str(s):size_hist[p][s] for s in sorted(size_hist[p])} for p in [1,2]},
        'max_entry_time':max(entry),
        'max_entry_witnesses':[x for x in range(4096) if depth[x]==max(entry)],
        'largest_fixed_basin':max(size_hist[1]),
        'largest_two_cycle_basin':max(size_hist[2]),
        'map_power_identity':all(step8(x,successors)==successors[successors[step8(x,successors)]] for x in range(4096))
    }

def step8(x,successors):
    for _ in range(8):x=successors[x]
    return x

if __name__=='__main__':
    print(json.dumps({f'G{i+1}':classify(edges) for i,edges in enumerate(EDGES)},sort_keys=True,indent=2))
