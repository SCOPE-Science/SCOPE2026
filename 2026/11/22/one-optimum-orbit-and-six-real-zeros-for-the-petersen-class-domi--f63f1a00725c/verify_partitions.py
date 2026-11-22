#!/usr/bin/env python3
"""Independent direct canonical set-partition enumeration (no matching recurrence)."""
from itertools import combinations
from collections import Counter
V = list(combinations(range(5), 2))
N = 10
# Direct Petersen adjacencies.
adj = [[i != j and set(V[i]).isdisjoint(V[j]) for j in range(N)] for i in range(N)]
counts=Counter(); minsize=11; minimum=[]; partitions=0

def blocks_valid(blocks):
    for B in blocks:
        if not any(all(adj[w][u] for u in B) for w in range(N)):
            return False
    return True

def go(i, blocks):
    global minsize,partitions
    if i==N:
        partitions+=1
        if not blocks_valid(blocks):return
        k=len(blocks)
        counts[k]+=1
        if k<minsize: minsize=k;minimum.clear()
        if k==minsize:minimum.append(tuple(tuple(b) for b in blocks))
        return
    for b in blocks:
        b.append(i);go(i+1,blocks);b.pop()
    blocks.append([i]);go(i+1,blocks);blocks.pop()

go(0,[])
assert partitions == 115975
assert minsize==4
assert dict(counts)=={4:30,5:604,6:1575,7:1130,8:295,9:30,10:1}
assert all(sorted(map(len,B))==[2,2,3,3] for B in minimum)
print('PARTITION_CERTIFICATE_OK')
print('all-set-partitions=',partitions)
print('counts-by-classes=',sorted(counts.items()))
print('optimal-shape-count=',len(minimum))
