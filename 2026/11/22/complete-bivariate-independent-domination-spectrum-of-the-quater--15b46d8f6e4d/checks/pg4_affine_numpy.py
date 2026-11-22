#!/usr/bin/env python3
"""Independently enumerate maximal independent sets in the projective plane over GF(4)."""
import numpy as np

def gfprod(a,b):
    value=0
    for i in range(2):
        for j in range(2):
            if a&(1<<i) and b&(1<<j):value^=1<<(i+j)
    if value&4:value^=7
    return value

# Different model: 16 affine points, 5 points at infinity, 20 affine lines, and one line at infinity.
points=[('aff',x,y) for x in range(4) for y in range(4)]+[('inf',s) for s in range(5)]
lines=[('slope',s,b) for s in range(4) for b in range(4)]+[('vertical',b) for b in range(4)]+[('infty',)]
assert len(points)==len(lines)==21
line_masks=[]
for line in lines:
    mask=0
    for i,p in enumerate(points):
        if line[0]=='slope':
            ok=p[0]=='aff' and (p[2] ^ gfprod(line[1],p[1]))==line[2] or p==('inf',line[1])
        elif line[0]=='vertical':
            ok=p[0]=='aff' and p[1]==line[1] or p==('inf',4)
        else:ok=p[0]=='inf'
        if ok:mask|=1<<i
    assert mask.bit_count()==5
    line_masks.append(mask)
assert len(set(line_masks))==21
assert all(sum((m>>i)&1 for m in line_masks)==5 for i in range(21))
assert all((line_masks[i]&line_masks[j]).bit_count()==1 for i in range(21) for j in range(i+1,21))

# Every maximal independent set is S plus precisely the lines disjoint from S.
masks=np.arange(1<<21,dtype=np.uint32)
coverage=masks.copy()
line_count=np.zeros(len(masks),dtype=np.uint8)
for line in line_masks:
    selected=(masks&line)==0
    line_count+=selected.astype(np.uint8)
    coverage|=np.where(selected,np.uint32(line),np.uint32(0))
valid=coverage==(1<<21)-1
pc16=np.array([x.bit_count() for x in range(1<<16)],dtype=np.uint8)
pcount=pc16[(masks&65535).astype(np.uint16)]+pc16[(masks>>16).astype(np.uint16)]
counts=np.bincount((pcount[valid].astype(np.int64)*32+line_count[valid].astype(np.int64)),minlength=32*32)
result={(i,j):int(counts[i*32+j]) for i in range(22) for j in range(22) if counts[i*32+j]}
assert len(result)==17,len(result)
expected={(4,4):105,(4,6):3360,(5,5):10080,(6,4):3360,
          (3,8):210,(4,7):2520,(7,4):2520,(8,3):210,
          (3,9):1120,(6,6):168,(9,3):1120,
          (2,12):210,(12,2):210,(1,16):21,(16,1):21,(0,21):1,(21,0):1}
assert result==expected,(result,expected)
assert sum(result.values())==25237
print('OK: independent affine-chart model, all 2^21 point selections; 21 lines; bivariate spectrum')
for pair in sorted(result):print(*pair,result[pair])
