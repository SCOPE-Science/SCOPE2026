#!/usr/bin/env python3
"""Direct finite checks of super-coalition partition formulas."""
from itertools import combinations
from math import comb
from collections import Counter

def parts(n):
    def rec(i,ls):
        if i==n:
            yield tuple(tuple(x) for x in ls)
            return
        for j in range(len(ls)):
            ls[j].append(i)
            yield from rec(i+1,ls)
            ls[j].pop()
        ls.append([i]);yield from rec(i+1,ls);ls.pop()
    yield from rec(0,[])

def edges(sizes):
    groups=[i for i,n in enumerate(sizes) for _ in range(n)]
    return groups, [(i,j) for i in range(len(groups)) for j in range(i+1,len(groups)) if groups[i]!=groups[j]]

def direct(sizes):
    grp,es=edges(sizes);n=len(grp)
    nei=[set() for _ in range(n)]
    for i,j in es:nei[i].add(j);nei[j].add(i)
    @__import__('functools').lru_cache(None)
    def super_dom(mask):
        outside={i for i in range(n) if not(mask>>i)&1}
        return all(any(i in nei[v] and len(nei[v]&outside)==1 for v in range(n) if (mask>>v)&1) for i in outside)
    counts=Counter()
    for blocks in parts(n):
        if len(blocks)>4:continue
        mask=[sum(1<<u for u in b) for b in blocks]
        if any(super_dom(s) for s in mask):continue
        if all(any(i!=j and super_dom(mask[i]|mask[j]) for j in range(len(blocks))) for i in range(len(blocks))):
            counts[len(blocks)]+=1
    return counts

def formula(sizes):
    n=sum(sizes);grp,es=edges(sizes)
    Q=[(i,j) for i,j in es if sizes[grp[i]]>=2 and sizes[grp[j]]>=2]
    e=len(Q)
    match2=sum(1 for a,b in combinations(Q,2) if len(set(a+b))==4)
    tri=sum(1 for a,b,c in combinations(range(n),3) if all(tuple(sorted(z)) in Q for z in ((a,b),(a,c),(b,c))))
    return {2:2**(n-1)-1-n-e,3:comb(n,2)+(n-3)*e+match2,4:tri}

if __name__=='__main__':
    count=0
    def integer_partitions(n,hi=None):
        if n==0:yield ();return
        for k in range(1,min(hi or n,n)+1):
            for t in integer_partitions(n-k,k):yield tuple(sorted(t+(k,),reverse=True))
    for n in range(7,9):
        all_s=sorted(set(integer_partitions(n)))
        for sizes in all_s:
            if len(sizes)<2: continue
            a=direct(sizes);f=formula(sizes)
            expected=Counter({k:v for k,v in f.items() if v})
            assert a==expected,(sizes,a,expected)
            count+=1
        print('DIRECT_PARTITION_ENUMERATION_OK',n,len(all_s),flush=True)
    for sizes in ((7,2),(5,2,2),(3,3,3)):
        a=direct(sizes);f=formula(sizes)
        assert a==Counter({k:v for k,v in f.items() if v}),(sizes,a,f)
        print('NINE_VERTEX_DIRECT_OK',sizes,dict(a),flush=True)
        count+=1
    assert direct((2,2,2)) == Counter({2:13,3:65,4:8})
    assert formula((2,2,2,2)) == {2:95,3:304,4:32}
    print('SMALL_BOUNDARY_AND_EIGHT_VERTEX_EXAMPLE_OK',flush=True)
    print('VERIFY_OK',count)
