#!/usr/bin/env python3
"""Exact majority orbit and basin enumeration for all five graph classes.
Uses bit masks and also independently classifies trajectories using direct vertex-neighbor lists.
"""
from collections import Counter
import json
from pathlib import Path
DATA=json.loads(Path(__file__).with_name('GRAPH_DATA.json').read_text(encoding='utf-8'))

def bit_neighbors(rows):
    out=[0]*12
    for i,m in enumerate(rows):
        out[i]=m<<6
        for j in range(6):
            if m>>j&1:out[6+j]|=1<<i
    assert all(m.bit_count()==3 for m in out)
    return out

def direct_neighbors(rows):
    out=[[] for _ in range(12)]
    for i in range(6):
        for j in range(6):
            if rows[i]&(1<<j):out[i].append(6+j);out[6+j].append(i)
    assert all(len(v)==3 for v in out)
    return out

def fast_next(x, neighbor_mask):
    return sum(1<<i for i,mask in enumerate(neighbor_mask) if (x&mask).bit_count()>=2)

def slow_next(x, adjacency):
    bits=[(x>>j)&1 for j in range(12)]
    result=[1 if sum(bits[j] for j in adjacency[i])>1 else 0 for i in range(12)]
    return sum(v<<i for i,v in enumerate(result))

def proof_by_four_iterates(g):
    N=bit_neighbors(g['row_masks'])
    trans=[fast_next(x,N) for x in range(4096)]
    cells=[[0,0] for _ in range(3)]
    basins=Counter()
    for x in range(4096):
        y=trans[x];z=trans[y];w=trans[z];v=trans[w]
        assert trans[v]==w # F^5=F^3 follows from F^4=F^2
        assert v==z,(g['id'],x)
        if z==x:t=0;a=x
        elif w==y:t=1;a=y
        else:t=2;a=z
        p=1 if trans[a]==a else 2
        cells[t][p-1]+=1
        orbit=(a,) if p==1 else tuple(sorted((a,trans[a])))
        basins[orbit]+=1
    assert cells==g['first_entry_period']
    assert cells[0][0]==g['fixed']
    assert cells[0][1]==2*g['two_orbits']
    assert sum(row[1] for row in cells)==g['two_basin']
    assert sum(map(sum,cells))==4096
    assert len(basins)==g['fixed']+g['two_orbits']
    spectrum=Counter(basins.values())
    assert sorted(spectrum.items())==[tuple(t) for t in g['attractor_basin_size_multiplicities']]
    assert max(spectrum)==g['largest_attractor_basin']
    return cells,spectrum

def proof_by_independent_trajectories(g):
    # Separately construct an explicit list-valued transition function, then
    # find the repeat point of each orbit without referring to F^4=F^2.
    adjacency=direct_neighbors(g['row_masks'])
    trans=[slow_next(x,adjacency) for x in range(4096)]
    counters=Counter()
    basins=Counter()
    for x in range(4096):
        path=[];seen={};a=x
        while a not in seen:
            seen[a]=len(path);path.append(a);a=trans[a]
            assert len(path)<=4096
        t=seen[a];p=len(path)-t
        assert p in (1,2)
        counters[t,p]+=1
        orbit=tuple(sorted(path[t:]))
        basins[orbit]+=1
    assert max(t for t,p in counters)==2
    assert [[counters[t,1],counters[t,2]] for t in range(3)]==g['first_entry_period']
    assert len(basins)==g['fixed']+g['two_orbits']
    return Counter(basins.values())

def main():
    for g in DATA['graphs']:
        cells,first=proof_by_four_iterates(g)
        second=proof_by_independent_trajectories(g)
        assert first==second,(g['id'],first,second)
        print(g['id'],'ENTRY_BY_PERIOD=',cells,'BASIN_MULTIPLICITIES=',sorted(first.items()))
    print('DYNAMICS_PASS two_implementations graph_classes=5 initial_states=20480 every_configuration_F4_equals_F2 true')
if __name__=='__main__':main()
