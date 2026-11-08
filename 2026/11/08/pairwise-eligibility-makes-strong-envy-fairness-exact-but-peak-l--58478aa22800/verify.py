#!/usr/bin/env python3
"""Independent finite checks for pair-eligible unit-job strong EF1 peak-load formula.

Uses exhaustive allocation enumeration (not constructive max flow) and exhaustive
subset enumeration for independent evaluations of the claimed formula.
"""
import itertools
import random


def formula(n, singles, q):
    base = [singles[i] + sum(q.get(tuple(sorted((i,j))),0)//2 for j in range(n) if j!=i) for i in range(n)]
    odd_edges = [p for p,v in q.items() if v%2]
    return max((sum(base[i] for i in range(n) if (mask>>i)&1)+
                sum(1 for i,j in odd_edges if mask>>i&1 and mask>>j&1) + mask.bit_count()-1)//mask.bit_count()
               for mask in range(1,1<<n))


def brute(n,singles,q):
    pairs=list(sorted(q))
    best=None
    for allocation in itertools.product(*(range(q[p]+1) for p in pairs)):
        # Allocation to first endpoint for each pair
        if any(abs(2*x-q[p])>1 for x,p in zip(allocation,pairs)):
            continue
        loads=singles.copy()
        for (i,j),x in zip(pairs,allocation):
            loads[i]+=x
            loads[j]+=q[(i,j)]-x
        t=max(loads)
        if best is None or t<best: best=t
    assert best is not None
    return best


def check_all_n3():
    n=3
    edges=list(itertools.combinations(range(n),2))
    count=0
    for qvalues in itertools.product(range(5), repeat=len(edges)):
        q=dict(zip(edges,qvalues))
        for sg in itertools.product(range(3), repeat=n):
            singles=list(sg)
            assert formula(n,singles,q)==brute(n,singles,q), (q,singles)
            count+=1
    return count


def check_random_n4():
    random.seed(20261105)
    count=0
    for _ in range(3500):
        n=4
        edges=list(itertools.combinations(range(n),2))
        q={p:random.randrange(5) for p in edges}
        singles=[random.randrange(4) for _ in range(n)]
        assert formula(n,singles,q)==brute(n,singles,q), (q,singles)
        count+=1
    return count


def online_check():
    r=random.Random(49152)
    count=0
    for _ in range(1200):
        n=r.randrange(2,10)
        pair_load={}
        allocation=[]
        for step in range(r.randrange(1,80)):
            i,j=sorted(r.sample(range(n),2))
            w=r.randrange(1,11)
            x,y=pair_load.get((i,j),(0,0))
            if x<=y:
                x+=w; allocation.append((i,j,w,i))
            else:
                y+=w; allocation.append((i,j,w,j))
            pair_load[(i,j)]=(x,y)
            # Direct EF1 test after each time point for every pair; for chores, remove
            # some job from the larger side and compare pair-specific remaining sums.
            for u,v in itertools.combinations(range(n),2):
                li=[w for a,b,w,z in allocation if (a,b)==(u,v) and z==u]
                lj=[w for a,b,w,z in allocation if (a,b)==(u,v) and z==v]
                for lhs,rhs in ((li,lj),(lj,li)):
                    assert sum(lhs)<=sum(rhs) or any(sum(lhs)-g<=sum(rhs) for g in lhs)
        count+=1
    return count

if __name__=='__main__':
    print('n3_full=',check_all_n3())
    print('n4_random=',check_random_n4())
    print('online_weighted_sequences=',online_check())
    print('all finite tests passed')
