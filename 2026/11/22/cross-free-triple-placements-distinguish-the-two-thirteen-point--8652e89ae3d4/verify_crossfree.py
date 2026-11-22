"""Exact finite enumeration of cross-free three-class systems on two STS(13)s.
Run with Python >=3.9: python verify_crossfree.py
All work is from the explicit 13-point block definitions below.
"""
from itertools import combinations
from collections import Counter

N=13
MASK=(1<<N)-1

def triple(t): return tuple(sorted(t))

def designs():
    cyc={triple(((a+t)%13 for a in base)) for t in range(13)
         for base in ((1,3,9),(2,5,6))}
    old={triple(t) for t in ((2,4,10),(2,5,6),(4,6,12),(5,10,12))}
    new={triple(t) for t in ((2,4,6),(2,5,10),(4,10,12),(5,6,12))}
    assert old <= cyc
    return {"cyclic":cyc,"noncyclic":(cyc-old)|new}

def steiner_valid(blocks):
    assert len(blocks)==26
    pairs=Counter(pair for block in blocks for pair in combinations(block,2))
    assert len(pairs)==78 and set(pairs.values())=={1}

def states(blocks):
    # Each vertex is an unordered triple of disjoint 3-subsets (bit masks).
    group=[sum(1<<x for x in c) for c in combinations(range(N),3)]
    lines=[sum(1<<x for x in b) for b in blocks]
    good=set();tested=0
    for i,a in enumerate(group):
        for j in range(i+1,len(group)):
            b=group[j]
            if a&b:continue
            for k in range(j+1,len(group)):
                c=group[k]
                if c&(a|b):continue
                tested+=1
                if not any((line&a) and (line&b) and (line&c) for line in lines):
                    good.add(tuple(sorted((a,b,c))))
    assert tested==200200
    return good

def adjacency(p,valid):
    free=MASK^(p[0]|p[1]|p[2]);near=set()
    for i,a in enumerate(p):
        for x in range(N):
            if not (a>>x)&1:continue
            for y in range(N):
                if not(free>>y)&1:continue
                candidate=list(p);candidate[i]=a^(1<<x)^(1<<y)
                candidate=tuple(sorted(candidate))
                if candidate in valid:near.add(candidate)
    return near

def census(blocks):
    steiner_valid(blocks)
    valid=states(blocks)
    nbr={p:adjacency(p,valid) for p in valid}
    for p,ns in nbr.items():
        assert len(ns)%3==0
        assert all(p in nbr[q] for q in ns)
    edges=sum(map(len,nbr.values()))//2
    seen=set();parts=Counter();motifs=Counter()
    for p in valid:
        if p in seen: continue
        stack=[p];seen.add(p);comp=set()
        while stack:
            x=stack.pop();comp.add(x)
            for y in nbr[x]:
                if y not in seen: seen.add(y);stack.append(y)
        size=len(comp);parts[size]+=1
        if size<=7:
            if size==1:assert not nbr[p];motifs['K1']+=1
            elif size==4:
                assert all(len(nbr[x])==3 for x in comp)
                motifs['K4']+=1
            elif size==7:
                hub=[x for x in comp if len(nbr[x])==6]
                assert len(hub)==1
                leaves=comp-set(hub)
                assert all(len(nbr[x])==3 for x in leaves)
                tri=sum(1 for a,b,c in combinations(leaves,3)
                        if b in nbr[a] and c in nbr[a] and c in nbr[b])
                assert tri==2
                motifs['K4 glued at one vertex K4']+=1
            else:raise AssertionError('unexpected small component')
    assert sum(k*v for k,v in parts.items())==len(valid)
    return valid,edges,parts,motifs

def run():
    data={}
    for name,blocks in designs().items():
        valid,edges,parts,motifs=census(blocks)
        sample = ((0,1,2),(3,4,7),(6,8,11)) if name=="cyclic" else ((0,1,2),(3,4,7),(8,10,11))
        assert tuple(sorted(sum(1<<x for x in t) for t in sample)) in valid
        data[name]=valid
        print(name,'crossfree',len(valid),'edges',edges,
              'component_sizes',dict(sorted(parts.items())),
              'small_shapes',dict(sorted(motifs.items())))
    print('both',len(data['cyclic']&data['noncyclic']),
          'cyclic_only',len(data['cyclic']-data['noncyclic']),
          'noncyclic_only',len(data['noncyclic']-data['cyclic']))
    assert len(data['cyclic'])==6214 and len(data['noncyclic'])==6148

if __name__=='__main__':run()
