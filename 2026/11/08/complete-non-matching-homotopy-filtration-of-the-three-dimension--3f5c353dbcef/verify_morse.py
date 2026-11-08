#!/usr/bin/env python3
"""Exhaustive exact discrete-Morse certificate for a cube's nonmatching filtration.
Public mathematical input: the graph Q3 has vertices 0..7, edges for one-bit flips.
Only standard Python 3 is used.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations

E=tuple((u,u^(1<<j)) for u in range(8) for j in range(3) if u<u^(1<<j))
assert len(E)==12 and len(set(E))==12
assert all(sum(u in e for e in E)==3 for u in range(8))
N=1<<12

@lru_cache(None)
def matching_number(edge_mask):
    if not edge_mask:return 0
    low=edge_mask&-edge_mask
    i=low.bit_length()-1
    a,b=E[i]
    rest=edge_mask^low
    incident=sum((1<<j) for j,(c,d) in enumerate(E) if a in(c,d) or b in(c,d))
    return max(matching_number(rest),1+matching_number(rest & ~incident))

# Independent calculation: exhaustive disjoint-edge families, not recursion.
matchings=[(0,0)]
for r in range(1,5):
    for choices in combinations(range(len(E)),r):
        used=0
        for i in choices:
            pair=(1<<E[i][0])|(1<<E[i][1])
            if pair&used:break
            used|=pair
        else:
            matchings.append((sum(1<<i for i in choices),r))
for s in range(N):
    assert matching_number(s)==max(r for m,r in matchings if m&s==m),s

ORDERS={
 2:(5,11,1,9,6,8,2,0,4,3,7,10),
 3:(4,6,0,1,2,9,10,5,8,3,7,11),
 4:(1,4,9,6,5,8,10,7,3,0,2,11),
}
EXP_CRIT={2:{1:5},3:{3:9},4:{5:1}}
EXP_F={
 2:{-1:1,0:12,1:24,2:8},
 3:{-1:1,0:12,1:66,2:176,3:222,4:108,5:16},
 4:{-1:1,0:12,1:66,2:220,3:486,4:720,5:684,6:372,7:96,8:8},
}
for k in (2,3,4):
    F={s for s in range(N) if matching_number(s)<k}
    dims=Counter(s.bit_count()-1 for s in F)
    assert dict(dims)==EXP_F[k]
    available=set(F)
    pairing={}
    for i in ORDERS[k]:
        bit=1<<i
        for lower in sorted(available):
            upper=lower|bit
            if not lower&bit and upper in available:
                pairing[lower]=upper
                available.remove(lower)
                available.remove(upper)
    assert len(pairing)*2+len(available)==len(F)
    assert 0 not in available and 0 in pairing
    assert Counter(s.bit_count()-1 for s in available)==EXP_CRIT[k]

    # Undo one empty-face pair. This leaves a critical vertex and gives
    # a genuine matching on the ordinary (nonaugmented) face poset.
    singleton=pairing.pop(0)
    assert singleton.bit_count()==1
    critical=set(available)|{singleton}
    assert Counter(s.bit_count()-1 for s in critical)==({0:1}|EXP_CRIT[k])

    # Every cover in the NONEMPTY face poset is directed downward unless
    # it is a matched cover, in which case it is directed upward.
    adj={s:[] for s in F if s}
    indeg={s:0 for s in F if s}
    covers=0
    for upper in F:
        if not upper:continue
        t=upper
        while t:
            low=t&-t;t-=low
            lower=upper^low
            if lower==0:continue
            assert lower in F
            covers+=1
            if pairing.get(lower)==upper:
                adj[lower].append(upper);indeg[upper]+=1
            else:
                adj[upper].append(lower);indeg[lower]+=1
    todo=deque(s for s in indeg if indeg[s]==0)
    seen=0
    while todo:
        s=todo.popleft();seen+=1
        for t in adj[s]:
            indeg[t]-=1
            if not indeg[t]:todo.append(t)
    assert seen==len(F)-1,(k,seen,len(F)-1)
    print('k=',k,'faces_including_empty=',len(F),'nonempty_Hasse_covers=',covers,
      'pairs=',len(pairing),'critical_vertex=',tuple(E[i] for i in range(12) if singleton&(1<<i)),
      'critical_higher=',dict(EXP_CRIT[k]),'acyclic=TRUE')
    print('critical_edge_masks',','.join(str(s) for s in sorted(available)))
print('ALL_CHECKS_PASS')
