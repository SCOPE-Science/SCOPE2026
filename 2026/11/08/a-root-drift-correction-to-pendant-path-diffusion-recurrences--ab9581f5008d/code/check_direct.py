#!/usr/bin/env python3
"""Independent exhaustive labelled-state iteration for triangle-plus-tail diffusion."""
from itertools import product

def count_direct(k):
    assert 2 <= k <= 5
    n=k+3
    neighbors=[[1,2,3],[0,2],[0,1]]+[[] for _ in range(k)]
    for j in range(k):
        v=3+j
        neighbors[v].append(0 if j==0 else v-1)
        if j<k-1: neighbors[v].append(v+1)
    def update(x):
        return tuple(x[v]+sum((x[w]>x[v])-(x[w]<x[v])
                              for w in neighbors[v]) for v in range(n))
    # Adjacent gap <= deg(u)+deg(v)-1 in every nonflat two-cycle.
    # Core x_0=0, two other triangle coordinates in [-4,4].
    ranges=[range(-4,5),range(-4,5),range(-4,5)]+\
           [range(-3,4)]*(k-2)+[range(-2,3)]
    total=0; count=0
    for a,b,*gaps in product(*ranges):
        vals=[0,a,b]; last=0
        for d in gaps:
            last+=d; vals.append(last)
        x=tuple(vals)
        total+=1
        if update(update(x))==x:
            count+=1
    return total,count

expected={2:123,3:469,4:1675,5:6029}
for k in range(2,6):
    total,n=count_direct(k)
    assert n==expected[k],(k,total,n)
    print('k=',k,'tested=',total,'initially_periodic=',n,'primitive_two=',n-1)
print('DIRECT_PASS')
