#!/usr/bin/env python3
"""Exact independent induced-cycle certificate for finite chordal Walsh claims."""
from itertools import combinations, permutations
from collections import Counter
from pathlib import Path
import csv


def edges(n):
    return list(combinations(range(n), 2))


def forbidden_patterns(n):
    ee = edges(n)
    loc = {e: i for i, e in enumerate(ee)}
    patterns = set()
    for length in range(4, n + 1):
        for sub in combinations(range(n), length):
            # Fix least vertex as first and quotient rotations by reversal.
            a = sub[0]
            for tail in permutations(sub[1:]):
                if tail[0] > tail[-1]:
                    continue
                cyc = (a,) + tail
                ce = {tuple(sorted((cyc[j], cyc[(j+1)%length]))) for j in range(length)}
                cm = sum(1 << loc[e] for e in ce)
                missing = sum(1 << loc[e] for e in combinations(sub, 2) if e not in ce)
                patterns.add((cm, missing))
    return sorted(patterns)


def chordal_set(n):
    pattern = forbidden_patterns(n)
    result=[]
    for m in range(1 << len(edges(n))):
        if all((m & cm) != cm or (m & diag) != 0 for cm, diag in pattern):
            result.append(m)
    return result


def signed_sum(graphs, freq):
    return sum(1 - 2*((g & freq).bit_count() & 1) for g in graphs)


def orbit_reps(n):
    ee=edges(n)
    loc={e:i for i,e in enumerate(ee)}
    emaps=[]
    for p in permutations(range(n)):
        emaps.append(tuple(loc[tuple(sorted((p[a],p[b])))] for a,b in ee))
    unassigned=set(range(1 << len(ee)))
    orbits=[]
    while unassigned:
        m=min(unassigned)
        orbit={sum(1 << a[i] for i in range(len(ee)) if m>>i & 1) for a in emaps}
        assert orbit <= unassigned
        unassigned -= orbit
        orbits.append((m,len(orbit)))
    return orbits


def desc(n, mask):
    ee=edges(n);adj=[set() for _ in range(n)];degs=[0]*n
    for i,(a,b) in enumerate(ee):
        if mask>>i & 1:
            adj[a].add(b);adj[b].add(a);degs[a]+=1;degs[b]+=1
    remaining=set(range(n));sizes=[]
    while remaining:
        start=min(remaining); todo=[start]; seen=set()
        while todo:
            v=todo.pop()
            if v in seen:continue
            seen.add(v);todo.extend(adj[v]-seen)
        sizes.append(len(seen));remaining-=seen
    triangles=sum(int(b in adj[a] and c in adj[a] and c in adj[b]) for a,b,c in combinations(range(n),3))
    return (tuple(sorted(degs,reverse=True)),tuple(sorted(sizes,reverse=True)),triangles)


def main():
    five=chordal_set(5)
    assert len(five)==822
    all_orbits=orbit_reps(5)
    assert sum(k for m,k in all_orbits)==1024
    z=[]
    for rep,size in all_orbits:
        if signed_sum(five,rep)==0:
            z.append((rep,size,desc(5,rep)))
    assert z==[
       (28,30,((2,1,1,1,1),(3,2),0)),
       (31,30,((4,2,2,1,1),(5,),1)),
       (185,60,((3,2,2,2,1),(5,),1))]
    print('n5 chordal=822; zero S5-orbits:',z,'; sum=120')
    path = Path(__file__).with_name('five_vertex_orbits.csv')
    with path.open(newline='', encoding='utf-8') as h:
        rows = list(csv.DictReader(h))
    assert len(rows) == len(all_orbits)
    for (rep,sz),row in zip(all_orbits,rows):
        assert int(row['frequency_mask'])==rep and int(row['orbit_size'])==sz
        assert int(row['walsh_coefficient'])==signed_sum(five,rep)
        assert row['support_edges']==' '.join(str(i) for i in range(10) if rep>>i&1)
    six=chordal_set(6)
    edge0=sum(g&1 for g in six)
    assert len(six)==18154 and edge0==8524
    assert signed_sum(six,639) in (2,-2)
    print('n6 chordal=',len(six),'edge0=',edge0,'witness W(639)=',signed_sum(six,639))
    with Path(__file__).with_name('six_vertex_edge_census.csv').open(newline='', encoding='utf-8') as h:
        rows = list(csv.DictReader(h))
    assert len(rows)==16
    for k,row in enumerate(rows):
        v=[g for g in six if g.bit_count()==k]
        assert int(row['number_of_edges'])==k
        assert int(row['chordal_graphs'])==len(v)
        assert int(row['chordal_graphs_with_edge_01'])==sum(g&1 for g in v)
    print('every n6 W(S) == 2 mod 4 by vertex symmetry and parity of edge inclusion counts')

if __name__ == '__main__':main()
