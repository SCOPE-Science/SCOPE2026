#!/usr/bin/env python3
"""Exhaustive checks of fixed-cardinality general-position exchange geometry."""
from itertools import combinations, product
from collections import deque

def gp_states(sizes,s):
    n=sum(sizes)
    parts=tuple(i for i,c in enumerate(sizes) for _ in range(c))
    def d(u,v):return 0 if u==v else (2 if parts[u]==parts[v] else 1)
    states=[]
    for a in combinations(range(n),s):
        good=all(d(a[i],a[k])!=d(a[i],a[j])+d(a[j],a[k])
                 for i in range(s) for j in range(s) for k in range(s) if len({i,j,k})==3)
        if good:states.append(frozenset(a))
    return states

def comp_count(states,k):
    sets=set(states); comps=0
    while sets:
        comps+=1
        start=sets.pop(); todo=[start]
        while todo:
            a=todo.pop()
            new={b for b in sets if len(a-b)<=k}
            sets.difference_update(new);todo.extend(new)
    return comps

def predicted(sizes,s,k):
    if s<=2:return 1
    p=sum(x>=s for x in sizes)
    b=(len(sizes)>=s)
    if k<=s-2:return p+int(b)
    if k==s-1:return 1 if b else p
    return 1

def verify():
    total=0; records=0
    for r in (2,3,4):
        for sizes in product(range(1,5),repeat=r):
            if sum(sizes)>11:continue
            for s in range(1,min(sum(sizes), max(r,max(sizes)))+1):
                states=gp_states(sizes,s)
                if not states:continue
                for k in range(1,s+1):
                    measured=comp_count(states,k)
                    expected=predicted(sizes,s,k)
                    assert measured==expected, (sizes,s,k,measured,expected)
                    records+=1
                total+=1
    print('VERIFIED_PROFILES',total,'COMPONENT_COMPARISONS',records)
    for sizes,s in [((4,4,4),3), ((5,5),4), ((4,4,4,4),4), ((3,3,3),3), ((5,1,1,1),4)]:
        states=gp_states(sizes,s)
        print('EXAMPLE',sizes,'s',s,'states',len(states),'components',[(k,comp_count(states,k)) for k in range(1,s+1)])
    print('VERIFY_OK')
if __name__=='__main__': verify()
