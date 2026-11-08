#!/usr/bin/env python3
"""Complete exhaustive binary 2x8 toroidal four-pixel mask census."""
from itertools import combinations

ALL_WINDOWS=(1<<16)-1
positions=tuple((i,j) for i in range(2) for j in range(3))
masks=tuple(combinations(positions,4))

def hit(b,mask):
    seen=0
    for i in range(2):
        for j in range(8):
            z=0
            for k,(di,dj) in enumerate(mask):
                z|=((b>>(8*((i+di)&1)+((j+dj)&7)))&1)<<k
            seen|=1<<z
    return seen==ALL_WINDOWS

samples=[]
for mask in masks:
    good={b for b in range(1<<16) if hit(b,mask)}
    samples.append((mask,good))

spanning=[(m,s) for m,s in samples if len({y for x,y in m})==3]
nonspanning=[(m,s) for m,s in samples if len({y for x,y in m})==2]
assert len(spanning)==12 and len(nonspanning)==3
assert all(len(s)==64 for m,s in spanning)
assert all(s==spanning[0][1] for m,s in spanning)
assert all(len(s)==0 for m,s in nonspanning)

G=spanning[0][1]
def transform(b,dr,dc,flip=False,reflect=False):
    new=0
    for i in range(2):
        for j in range(8):
            ii=(i+dr)&1
            jj=(((-j if reflect else j)+dc)&7)
            new|=(((b>>(8*ii+jj))&1)^int(flip))<<(8*i+j)
    return new

rem=set(G)
translation=[]
while rem:
    seed=min(rem)
    orb={transform(seed,i,j) for i in range(2) for j in range(8)}
    assert orb<=G and len(orb)==16
    translation.append((seed,orb))
    rem-=orb
assert len(translation)==4
assert [x for x,_ in translation]==[0x0b5e,0x0da7,0x0f5a,0x0fa5]

rem=set(G);classes=[]
while rem:
    seed=min(rem)
    orb={transform(seed,i,j,flip,ref) for i in range(2) for j in range(8) for flip in (0,1) for ref in (0,1)}
    assert orb<=G
    classes.append((seed,len(orb)))
    rem-=orb
assert sorted(x[1] for x in classes)==[32,32]

for b in G:
    d=[((b>>j)&1)^((b>>(8+j))&1) for j in range(8)]
    assert all(d[j]!=(d[(j+1)&7]) for j in range(8))

print('DIRECT_OK: 65536 arrays, 15 masks, 12 universal masks x 64 identical arrays; 3 impossible masks')
print('TRANSLATION_REPRESENTATIVES',','.join(f'0x{seed:04x}' for seed,_ in translation))
print('SYM_CLASSES',classes)
