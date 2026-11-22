#!/usr/bin/env python3
"""Exact labelled functional-graph and automorphism-orbit census of two 12-vertex graphs.
Use Python 3.9+; no third-party dependencies. Results are exact integers.
"""
import collections
import itertools
import json

def truncated_tetrahedron():
    vertices = [(a,b) for a in range(4) for b in range(4) if a != b]
    where = {v:i for i,v in enumerate(vertices)}
    adjacency = [tuple(sorted([where[(b,a)]]+[where[(a,c)] for c in range(4) if c!=a and c!=b])) for a,b in vertices]
    automorphisms = [tuple(where[(p[a],p[b])] for a,b in vertices) for p in itertools.permutations(range(4))]
    return adjacency,automorphisms

def cuboctahedron():
    edges=sorted((u,u^(1<<j)) for u in range(8) for j in range(3) if u<(u^(1<<j)))
    loc={e:i for i,e in enumerate(edges)}
    adj=[tuple(j for j,f in enumerate(edges) if i!=j and (e[0] in f or e[1] in f)) for i,e in enumerate(edges)]
    automorphisms=[]
    for p in itertools.permutations(range(3)):
        for t in range(8):
            transform=lambda u: t^sum(((u>>j)&1)<<p[j] for j in range(3))
            automorphisms.append(tuple(loc[tuple(sorted((transform(u),transform(v))))] for u,v in edges))
    return adj,automorphisms

def next_states(adjacency):
    assert len(adjacency)==12
    masks=[sum(1<<j for j in v) for v in adjacency]
    ans=[]
    for state in range(4096):
        y=0
        for i,mask in enumerate(masks):
            ones=(state&mask).bit_count();deg=mask.bit_count()
            if 2*ones>deg or (2*ones==deg and state>>i&1):y |=1<<i
        ans.append(y)
    return ans

def census(adj,group):
    n=12;M=1<<n; f=next_states(adj)
    assert all(len(a)==len(set(a)) for a in adj)
    assert all(i not in a for i,a in enumerate(adj))
    assert all(i in adj[j] for i,a in enumerate(adj) for j in a)
    assert len(set(group))==len(group)
    assert all(sorted(g)==list(range(n)) for g in group)
    assert all(sorted(g[j] for j in adj[i])==sorted(adj[g[i]]) for g in group for i in range(n))
    assert all((~f[x])&4095==f[(~x)&4095] for x in range(M))
    entry=[-1]*M;period=[0]*M;cycle_root=[-1]*M
    for origin in range(M):
        if entry[origin]>=0:continue
        path=[];position={};s=origin
        while entry[s]<0 and s not in position:
            position[s]=len(path);path.append(s);s=f[s]
        if s in position:
            cycle=path[position[s]:]
            anchor=min(cycle)
            for v in cycle: entry[v]=0;period[v]=len(cycle);cycle_root[v]=anchor
            path=path[:position[s]]
        for v in reversed(path):
            entry[v]=entry[f[v]]+1
            period[v]=period[f[v]]
            cycle_root[v]=cycle_root[f[v]]
    assert all(e>=0 for e in entry)
    assert set(period)<={1,2}
    fixed={x for x in range(M) if f[x]==x}
    two={tuple(sorted((x,f[x]))) for x in range(M) if f[f[x]]==x and f[x]!=x}
    assert len(fixed)+2*len(two)==sum(e==0 for e in entry)
    assert all((f[f[s]]==s)==(entry[s]==0) for s in range(M))
    def transform(x,g):return sum(((x>>i)&1)<<j for i,j in enumerate(g))
    def orbit_hist(things,move):
        unknown=set(things);by_size=collections.Counter()
        while unknown:
            item=min(unknown)
            orbit={move(item,g) for g in group}
            assert orbit<=unknown
            unknown-=orbit
            by_size[len(orbit)]+=1
        return dict(sorted(by_size.items()))
    fixed_spatial=orbit_hist(fixed,lambda x,g:transform(x,g))
    two_spatial=orbit_hist(two,lambda x,g:tuple(sorted((transform(x[0],g),transform(x[1],g)))))
    # independent Burnside/orbit-stabilizer aggregate identity
    sum_fix=sum(sum(transform(x,g)==x for x in fixed) for g in group)
    sum_two=sum(sum(tuple(sorted((transform(x,g),transform(y,g))))==(x,y) for x,y in two) for g in group)
    assert sum_fix==len(group)*sum(fixed_spatial.values())
    assert sum_two==len(group)*sum(two_spatial.values())
    pop=collections.Counter(period)
    basin=collections.Counter(cycle_root)
    result={
       'vertices':12, 'degree':len(adj[0]), 'automorphism_order':len(group),
       'fixed':len(fixed), 'primitive_two_orbits':len(two),
       'fixed_spatial_classes':sum(fixed_spatial.values()),
       'primitive_two_spatial_classes':sum(two_spatial.values()),
       'fixed_spatial_size_histogram':fixed_spatial,
       'primitive_two_spatial_size_histogram':two_spatial,
       'entry_time_histogram':dict(sorted(collections.Counter(entry).items())),
       'first_entry_period_histogram':{str(p):dict(sorted(collections.Counter(entry[x] for x in range(M) if period[x]==p).items())) for p in sorted(pop)},
       'basin_population':{str(p):pop[p] for p in sorted(pop)},
       'consensus_basin_per_color':[basin[0],basin[M-1]],
       'fixed_support_histogram':dict(sorted(collections.Counter(x.bit_count() for x in fixed).items())),
       'primitive_two_flip_histogram':dict(sorted(collections.Counter((x^y).bit_count() for x,y in two).items())),
       'sharp_first_entry_time':max(entry),
       'sharp_time_witness':next(x for x in range(M) if entry[x]==max(entry)),
       'checksum_states':sum(x^(f[x]<<12) for x in range(M))
    }
    return result

def main():
    out={}
    for name,ctor in (('truncated_tetrahedron',truncated_tetrahedron),('cuboctahedron',cuboctahedron)):
        a,g=ctor();out[name]=census(a,g)
    assert (out['truncated_tetrahedron']['fixed'],out['truncated_tetrahedron']['primitive_two_orbits'],out['truncated_tetrahedron']['primitive_two_spatial_classes'],out['truncated_tetrahedron']['sharp_first_entry_time'])==(16,239,26,5)
    assert (out['cuboctahedron']['fixed'],out['cuboctahedron']['primitive_two_orbits'],out['cuboctahedron']['primitive_two_spatial_classes'],out['cuboctahedron']['sharp_first_entry_time'])==(146,20,3,4)
    print(json.dumps(out,indent=2,sort_keys=True))
    with open('archimedean_census.json','w') as stream:
        json.dump(out,stream,indent=2,sort_keys=True)
        stream.write('\n')
if __name__=='__main__':main()
