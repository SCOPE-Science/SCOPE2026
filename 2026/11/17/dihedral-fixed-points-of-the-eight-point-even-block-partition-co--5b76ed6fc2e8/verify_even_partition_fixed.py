#!/usr/bin/env python3
"""Independent exhaustive verification of fixed-point collapses for even-block partitions on eight labels.
Run: python3 verify_even_partition_fixed.py
The certificate is stored alongside this program as collapse_certificate.json.
Uses only the Python standard library.
"""
import collections
import itertools
import json
from pathlib import Path

N = 8

def all_partitions_by_rgs(n):
    # Every restricted-growth string encodes one set partition, exactly once.
    def rec(a, maximum):
        if len(a)==n:
            blocks=[[] for _ in range(maximum+1)]
            for i,j in enumerate(a):blocks[j].append(i)
            yield tuple(sorted(tuple(block) for block in blocks))
        else:
            for j in range(maximum+2):
                yield from rec(a+(j,),max(maximum,j))
    yield from rec((0,),0)

def is_refinement(a,b):
    # Compare membership via the canonical map from label to b-block.
    locate={label:j for j,block in enumerate(b) for label in block}
    return all(len({locate[x] for x in block})==1 for block in a)

def permutation(sign,shift):
    return tuple((sign*i+shift)%N for i in range(N))

def image_partition(p,g):
    return tuple(sorted(tuple(sorted(g[i] for i in block)) for block in p))

def edges_of(triangle):
    return tuple(itertools.combinations(triangle,2))

def cycle_type(g):
    unseen=set(range(N)); out=[]
    while unseen:
        i=min(unseen);j=i;length=0
        while j in unseen:
            unseen.remove(j);length+=1;j=g[j]
        assert j==i
        out.append(length)
    return tuple(sorted(out))

def check_graph(nodes,edges):
    adj={v:set() for v in nodes}
    for a,b in edges:
        assert a in adj and b in adj and a!=b
        adj[a].add(b);adj[b].add(a)
    seen=set();components=0;trees=[]
    for root in sorted(nodes):
        if root not in seen:
            components+=1
            queue=[root];seen.add(root);tree=[]
            for a in queue:
                for b in sorted(adj[a]):
                    if b not in seen:
                        seen.add(b);queue.append(b);tree.append((a,b))
            trees.append(tree)
    return components,len(edges)-len(nodes)+components,trees

def main():
    partitions=list(all_partitions_by_rgs(N))
    assert len(partitions)==4140 and len(set(partitions))==4140
    v=sorted((p for p in partitions if len(p)>1 and all(len(block)%2==0 for block in p)),key=lambda p:(-len(p),p))
    assert len(v)==378
    by_blocks=collections.Counter(len(p) for p in v)
    assert by_blocks=={4:105,3:210,2:63},by_blocks
    lookup={p:i for i,p in enumerate(v)}
    edges=set()
    for i,a in enumerate(v):
        for j,b in enumerate(v):
            if len(a)>len(b) and is_refinement(a,b): edges.add((i,j))
    triangles=set()
    succ=collections.defaultdict(set)
    for i,j in edges:succ[i].add(j)
    for i,j in edges:
        for k in succ[j]:
            assert (i,k) in edges
            triangles.add((i,j,k))
    assert len(edges)==1995 and len(triangles)==1890
    certificate=json.loads((Path(__file__).resolve().parent/'collapse_certificate.json').read_text(encoding='utf-8'))
    assert certificate['schema_version']==1
    reps=certificate['representatives']
    assert set(reps)=={'1','2','4','8'}
    expected={
       (8,): (2,1,0,0),
       (4,4): (10,11,2,0),
       (2,2,2,2): (58,163,90,16),
       (1,1,2,2,2): (26,67,42,0),
    }
    seen_types=set()
    for k in [1,2,4,8]:
        g=permutation(-1 if k>=8 else 1,k%8)
        ctype=cycle_type(g)
        seen_types.add(ctype)
        nodes={i for i,p in enumerate(v) if image_partition(p,g)==p}
        e={edge for edge in edges if set(edge).issubset(nodes)}
        t={face for face in triangles if set(face).issubset(nodes)}
        record=reps[str(k)]
        assert [len(nodes),len(e),len(t)]==record['fixed_faces']
        expected_counts=expected[ctype]
        assert (len(nodes),len(e),len(t))==expected_counts[:3]
        for ed,tr in record['collapses']:
            edge=tuple(ed);face=tuple(tr)
            assert edge in e and face in t and edge in edges_of(face)
            containing=[f for f in t if edge in edges_of(f)]
            assert containing==[face],('not free',k,edge,face)
            e.remove(edge);t.remove(face)
        assert not t and sorted(map(list,e))==record['remaining_edges']
        components,rank,tree=check_graph(nodes,e)
        assert components==1 and rank==expected_counts[3]
        assert len(tree)==1 and len(tree[0])==len(nodes)-1
        print('type',ctype,'original_cells',record['fixed_faces'],
              'elementary_collapses',len(record['collapses']),'remaining_edges',len(e),
              'components',components,'circle_rank',rank)
    assert seen_types==set(expected)
    # Every nonidentity dihedral element belongs to one of the four checked S8 cycle types.
    distribution=collections.Counter()
    for sign in (1,-1):
        for k in range(8):
            if sign==1 and k==0:continue
            distribution[cycle_type(permutation(sign,k))]+=1
    assert distribution=={(8,):4,(4,4):2,(2,2,2,2):5,(1,1,2,2,2):4},distribution
    print('dihedral_distribution',sorted(distribution.items()))
    print('ALL CHECKS PASSED')

if __name__=='__main__': main()
