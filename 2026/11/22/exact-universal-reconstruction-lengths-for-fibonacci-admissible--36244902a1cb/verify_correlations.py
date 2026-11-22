#!/usr/bin/env python3
"""Independent exact prefix-lattice autocorrelation verification."""
from collections import defaultdict
from itertools import product

def words(n):
    for bits in product((0,1),repeat=n):
        if all(bits[j]==0 or bits[j+1]==0 for j in range(n-1)):
            yield bits

def poly(w):
    point=(0,0)
    steps=[point]
    for b in w:
        point=(point[0]+(b==0),point[1]+(b==1))
        steps.append(point)
    diffs=defaultdict(int)
    for x in steps:
        for y in steps:
            diffs[(x[0]-y[0],x[1]-y[1])]+=1
    return tuple(sorted(diffs.items()))

def run(n):
    groups=defaultdict(list)
    for w in words(n):groups[poly(w)].append(w)
    # Independent certificate: every autocorrelation fiber consists of a single reversal orbit.
    for fiber in groups.values():
        m=min(fiber)
        assert set(fiber)=={m,m[::-1]},(n,fiber)
    print('CORRELATION_OK',n,'words',sum(len(f) for f in groups.values()),'fibers',len(groups),'size_hist', {k:sum(len(f)==k for f in groups.values()) for k in (1,2,3,4)})

if __name__=='__main__':
    for n in (8,11,15):run(n)
