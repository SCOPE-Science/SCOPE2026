#!/usr/bin/env python3
"""Direct tests of scalar and distance-graded one-point metric extension counts."""
from collections import Counter, defaultdict
from itertools import product

def partitions(n, smallest=1):
    if n == 0:
        yield ()
        return
    for a in range(smallest, n + 1):
        for rest in partitions(n-a, a):
            yield (a,) + rest

def scalar_formula(p):
    out=1
    for size in p:
        out *= (1 << (size+1)) - 1
    return out

def grade_formula(p):
    polynomial = {(0,0,0): 1}
    for a in p:
        local=Counter()
        for cnt1 in range(a+1):
            from math import comb
            local[(cnt1,a-cnt1,0)] += comb(a,cnt1)
        for cnt3 in range(a+1):
            from math import comb
            local[(0,a-cnt3,cnt3)] += comb(a,cnt3)
        local[(0,a,0)] -= 1
        tmp=Counter()
        for (x,y,z),w in polynomial.items():
            for (u,v,t),q in local.items():
                tmp[(x+u,y+v,z+t)] += w*q
        polynomial = dict(tmp)
    return Counter({k:v for k,v in polynomial.items() if v})

def direct(p):
    cluster=[]
    for idx,a in enumerate(p): cluster.extend([idx]*a)
    n=len(cluster)
    result=Counter()
    for assign in product((1,2,3),repeat=n):
        admissible=True
        for i in range(n):
            for j in range(i+1,n):
                d=1 if cluster[i]==cluster[j] else 2
                if abs(assign[i]-assign[j])>d or assign[i]+assign[j]<d:
                    admissible=False;break
            if not admissible:break
        if admissible:
            result[(assign.count(1),assign.count(2),assign.count(3))] +=1
    return result

# Full direct diagrams through seven vertices, including their full distance-grade histograms.
checked_direct=0
for n in range(1,8):
    for p in partitions(n):
        x=direct(p); y=grade_formula(p)
        assert x==y, (p,x,y)
        assert sum(x.values())==scalar_formula(p)
        checked_direct += 1

# Full fixed-cardinality injectivity through thirty named parameters.
checked_partitions=0
for n in range(1,31):
    by_count={}
    for p in partitions(n):
        count=scalar_formula(p)
        assert count not in by_count, (n,p,by_count.get(count))
        by_count[count]=p
        checked_partitions+=1

assert scalar_formula((5,)) == scalar_formula((1,1,2)) == 63
assert sum((5,))==5 and sum((1,1,2))==4

# All multiplicative collisions with scalar count <= one million come from the relation.
lim=1_000_000
by_product=defaultdict(list)
for n in range(1,24):
    for p in partitions(n):
        value=scalar_formula(p)
        if value<=lim:
            by_product[value].append(p)
for v, ps in by_product.items():
    if len(ps)<=1: continue
    for a in ps:
        for b in ps:
            delta=Counter(x+1 for x in a)
            delta.subtract(Counter(x+1 for x in b))
            t=delta[6]
            assert all(delta[k]==({2:-2*t,3:-t,6:t}.get(k,0)) for k in delta), (a,b,delta)
print('VERIFY_OK')
print('direct_profiles',checked_direct)
print('unique_partitions_through_n30',checked_partitions)
print('smallest_numerical_collision',63, (5,), (1,1,2))
print('multiplicative_collision_limit',lim)
