#!/usr/bin/env python3
"""Independent small-case exhaustive checks for two-phase fair/efficient allocation."""
from itertools import product

def utilities(p,q,top,low,assignment):
    goods=[(low,top)]*p+[(top,low)]*q
    return tuple(sum(v[i] for v,who in zip(goods,assignment) if who==i) for i in (0,1))

def ef1_all_prefixes(p,q,top,low,assignment):
    goods=[(low,top)]*p+[(top,low)]*q
    for t in range(1,p+q+1):
        for i in (0,1):
            own=sum(v[i] for v,who in zip(goods[:t],assignment[:t]) if who==i)
            others=[v[i] for v,who in zip(goods[:t],assignment[:t]) if who!=i]
            if others and own<sum(others)-max(others):return False
    return True

def brute_counts(p,q,top,low):
    allocations=list(product((0,1),repeat=p+q))
    utilities_by_alloc=[utilities(p,q,top,low,a) for a in allocations]
    po=set()
    for idx,(u,v) in enumerate(utilities_by_alloc):
        if not any(x>=u and y>=v and (x>u or y>v) for x,y in utilities_by_alloc):
            po.add(idx)
    good=[]
    for idx,a in enumerate(allocations):
        if idx in po and ef1_all_prefixes(p,q,top,low,a):good.append(a)
    return good

def theorem_set(p,q,top,low):
    if q*low>top*(1+p%2):return set()
    ans=set()
    for flips in product((0,1),repeat=p//2):
        a=[]
        for f in flips:a.extend((f,1-f))
        if p%2:a.append(1)
        a.extend([0]*q)
        ans.add(tuple(a))
    return ans

def check():
    cases=0; checked_allocations=0; passed_nonzero=0
    for p in range(2,7):
        for q in range(1,6):
            if p+q>10:continue
            for top,low in ((2,1),(3,1),(3,2),(4,3),(5,2),(5,4),(7,2),(6,3)):
                actual=set(brute_counts(p,q,top,low)); expected=theorem_set(p,q,top,low)
                assert actual==expected,(p,q,top,low,actual,expected)
                cases+=1;checked_allocations+=2**(p+q)
                passed_nonzero+=bool(actual)
    # An independent count-level test at larger lengths, using the structural
    # noncrossing condition for Pareto efficiency, not pairwise scanning.
    more=0
    for p in range(2,11):
        for q in range(1,8):
            for top,low in ((2,1),(3,2),(5,4)):
                goods=[(low,top)]*p+[(top,low)]*q
                observed=0
                for a in product((0,1),repeat=p+q):
                    if 0 in a[:p] and 1 in a[p:]:continue
                    if ef1_all_prefixes(p,q,top,low,a):observed+=1
                assert observed==len(theorem_set(p,q,top,low)),(p,q,top,low,observed)
                more+=1
    print('PASS direct exhaustive Pareto/temporal-EF1 cases:',cases)
    print('PASS total directly evaluated assignments:',checked_allocations)
    print('PASS positive feasible cases:',passed_nonzero)
    print('PASS additional noncrossing-structure cases:',more)
if __name__=='__main__':check()
