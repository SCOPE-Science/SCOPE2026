"""Independent integer-bitset verification for the 24-vertex McGee 7-cage.

Reconstructs the LCF chords, simulates parallel zero forcing with bit operations,
and obtains graph metrics from bitset breadth expansions instead of deque BFS.
Python 3 standard library only: python verify_bitsets.py.
"""
from collections import Counter
from itertools import combinations

ALL=(1<<24)-1
neighbors=[0]*24
for v in range(24):
    for w in ((v+1)%24,(v+(12,7,-7)[v%3])%24):
        neighbors[v]|=1<<w
        neighbors[w]|=1<<v
assert all(row.bit_count()==3 for row in neighbors)

def bits(mask):
    while mask:
        b=mask&-mask
        yield b.bit_length()-1
        mask^=b

def pds(mask):
    active=mask
    for i in bits(mask):active |= neighbors[i]
    rounds=0
    while True:
        next_bits=0
        for i in bits(active):
            white=neighbors[i]&~active
            if white and not (white & (white-1)):next_bits|=white
        if not next_bits:return active==ALL,rounds
        active|=next_bits
        rounds+=1

for k in (1,2):
    assert not any(pds(sum(1<<x for x in t))[0] for t in combinations(range(24),k))
accepted=[];waves=Counter()
for t in combinations(range(24),3):
    mask=sum(1<<x for x in t)
    ok,r=pds(mask)
    if ok:accepted.append(mask);waves[r]+=1
assert len(accepted)==576
assert waves==Counter({2:144,3:272,4:160})
length=len(accepted)
jump=[0]*length;slide=[0]*length
for a in range(length):
    for b in range(a+1,length):
        diff=accepted[a]^accepted[b]
        if diff.bit_count()!=2: continue
        jump[a]|=1<<b;jump[b]|=1<<a
        x,y=tuple(bits(diff))
        if neighbors[x]&(1<<y):
            slide[a]|=1<<b;slide[b]|=1<<a
assert sum(x.bit_count() for x in jump)//2==6184
assert sum(x.bit_count() for x in slide)//2==1328

def expansion(graph,source):
    distances=[-1]*length
    seen=1<<source
    frontier=seen
    step=0
    while frontier:
        for i in bits(frontier):distances[i]=step
        successor=0
        for i in bits(frontier):successor|=graph[i]
        frontier=successor&~seen
        seen|=frontier
        step+=1
    return distances

metric=Counter(); penalty=Counter(); exc=Counter(); extreme=set()
for i in range(length):
    a=expansion(jump,i)
    b=expansion(slide,i)
    assert min(a)==min(b)==0
    assert max(a)==4 and max(b) in (8,9)
    exc[max(b)]+=1
    for j in range(i+1,length):
        metric[(a[j],b[j])]+=1
        penalty[b[j]-a[j]]+=1
        if b[j]-a[j]==7:
            assert (a[j],b[j])==(1,8)
            extreme.add(frozenset((accepted[i],accepted[j])))
assert exc==Counter({8:432,9:144})
assert penalty==Counter({0:8856,1:21048,2:41056,3:50216,4:35568,5:8600,6:248,7:8})
assert len(extreme)==8
assert sum(metric.values())==165600
assert metric[(1,8)]==8
assert sum(metric[(a,9)] for a in range(1,5))==136
print('VERIFY_BITSETS_OK')
print('576 three-sensor optima; TJ 6184 edges and diameter 4; TS 1328 edges and diameter 9')
print('TS eccentricity classes 8:432 and 9:144; max excess 7 on eight pairs')
