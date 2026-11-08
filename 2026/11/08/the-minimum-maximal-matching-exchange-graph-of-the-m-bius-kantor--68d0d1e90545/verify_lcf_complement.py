"""Independent complement-first certificate using the [5,-5]^8 LCF representation.
Standalone standard Python 3; enumerates independent unmatched sets, then perfect matchings.
"""
from itertools import combinations
from collections import Counter,deque

def graph():
    V=range(16)
    E=set()
    for i in V:
        for v in ((i+1)%16,(i+(5 if i%2==0 else -5))%16):
            E.add(tuple(sorted((i,v))))
    return sorted(E)

def compute():
    E=graph()
    assert len(E)==24
    # Explicit fixed graph isomorphism to the GP(8,3) construction.
    f=(0,5,6,7,8,13,14,15,1,4,11,2,9,12,3,10)
    assert len(set(f))==16
    GP=set()
    for i in range(8):
        for a,b in ((i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8)):
            GP.add(tuple(sorted((f[a],f[b]))))
    assert GP==set(E)
    adj=[set() for _ in range(16)]
    for a,b in E:adj[a].add(b);adj[b].add(a)
    assert all(len(x)==3 for x in adj)
    allv=set(range(16));opt=[];count_by_size=Counter()
    def perfect(complement):
        if not complement:
            yield ()
            return
        x=min(complement)
        for y in sorted(adj[x]&complement):
            for tail in perfect(complement-{x,y}):
                yield ((x,y),)+tail
    for q in range(0,17,2):
        for un in combinations(range(16),q):
            U=set(un)
            if any(y in U for x in U for y in adj[x] if y>x):continue
            k=(16-q)//2
            for match in perfect(allv-U):
                count_by_size[k]+=1
                if k==6:opt.append(frozenset(tuple(sorted(e)) for e in match))
    assert count_by_size=={6:176,7:336,8:33},count_by_size
    S=set(opt); assert len(S)==176
    neighbors={x:set() for x in S}
    # Generate by common five-edge subsets, a logically different pair construction.
    buckets={}
    for x in S:
        for e in x:
            buckets.setdefault(x-{e},[]).append(x)
    for group in buckets.values():
        for p,q in combinations(group,2):
            neighbors[p].add(q);neighbors[q].add(p)
    assert Counter(map(len,neighbors.values()))=={0:80,2:96}
    assert sum(map(len,neighbors.values()))//2==96
    comps=[];remain=set(S)
    while remain:
        s=next(iter(remain));q={s}; todo=[s]
        for p in todo:
            for nxt in neighbors[p]:
                if nxt not in q:q.add(nxt);todo.append(nxt)
        remain-=q;comps.append(q)
    assert Counter(map(len,comps))=={1:80,16:6}
    # Each nontrivial finite connected 2-regular simple graph is a cycle.
    assert all(all(len(neighbors[s])==2 for s in comp) for comp in comps if len(comp)>1)
    print('LCF_REPRESENTATION=[5,-5]^8')
    print('MAXIMAL_MATCHINGS_BY_SIZE='+str(sorted(count_by_size.items())))
    print('MINIMUM_MAXIMAL_SIZE=6 MINIMUM_MATCHINGS=176')
    print('EXCHANGES_BY_SHARED_FIVE_EDGE_CORE=96')
    print('COMPONENTS='+str(sorted(Counter(map(len,comps)).items())))
    print('SIX_C16_COMPONENTS=True')
    print('VERIFY_OK')
if __name__=='__main__':compute()
