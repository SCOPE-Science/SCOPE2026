#!/usr/bin/env python3
"""Exhaustive forward orbit tracer for synchronous majority on five cubic identity graphs.
All graph data and arithmetic are explicit; Python 3 standard library only.
"""
import collections
import json

LCF = [
 [-5,2,-3,-2,6,4,2,5,-2,-4,6,3],
 [6,3,-4,-4,-3,3,6,2,-3,-2,4,4],
 [4,-2,5,2,-4,-2,3,-5,2,-3,-2,2],
 [6,-5,2,6,-2,6,6,3,5,6,-3,6],
 [2,-5,-2,6,3,6,4,-3,5,6,-4,6],
]

def graph_from_lcf(offsets):
    n=len(offsets)
    edges=set()
    for i,d in enumerate(offsets):
        for j in ((i+1)%n,(i+d)%n):
            edges.add(tuple(sorted((i,j))))
    assert len(edges)==18
    neighbors=[0]*n
    for a,b in edges:
        neighbors[a]|=1<<b;neighbors[b]|=1<<a
    assert all(v.bit_count()==3 for v in neighbors)
    return neighbors

def classify(offsets):
    adj=graph_from_lcf(offsets)
    successor=[sum(1<<i for i,mask in enumerate(adj) if (x&mask).bit_count()>=2)
               for x in range(4096)]
    solved={}
    for x in range(4096):
        if x in solved:continue
        trail=[];visited={};state=x
        while state not in visited and state not in solved:
            visited[state]=len(trail)
            trail.append(state)
            state=successor[state]
        if state in visited:
            a=visited[state]
            cycle=trail[a:]
            key=min(cycle)
            period=len(cycle)
            for z in cycle:solved[z]=(key,0,period)
            for j in range(a-1,-1,-1):
                solved[trail[j]]=(key,a-j,period)
        else:
            key,entry,period=solved[state]
            for z in reversed(trail):
                entry+=1;solved[z]=(key,entry,period)
    assert len(solved)==4096
    basin=collections.Counter(key for key,entry,period in solved.values())
    phist=collections.Counter(period for key,entry,period in solved.values())
    entrance=collections.Counter(entry for key,entry,period in solved.values())
    sizes={p:collections.Counter() for p in [1,2]}
    for key,size in basin.items():sizes[solved[key][2]][size]+=1
    assert sum(basin.values())==4096
    def power(x,k):
        for _ in range(k):x=successor[x]
        return x
    return {
        'fixed_states':sum(sizes[1].values()),
        'two_cycle_orbits':sum(sizes[2].values()),
        'period_one_basin_population':phist[1],
        'period_two_basin_population':phist[2],
        'entry_histogram':[entrance[j] for j in range(max(entrance)+1)],
        'basin_histogram':{str(p):{str(s):sizes[p][s] for s in sorted(sizes[p])} for p in [1,2]},
        'max_entry_time':max(entrance),
        'max_entry_witnesses':[x for x in range(4096) if solved[x][1]==max(entrance)],
        'largest_fixed_basin':max(sizes[1]),
        'largest_two_cycle_basin':max(sizes[2]),
        'map_power_identity':all(power(x,10)==power(x,8) for x in range(4096))
    }

if __name__=='__main__':
    print(json.dumps({f'G{i+1}':classify(o) for i,o in enumerate(LCF)},sort_keys=True,indent=2))
