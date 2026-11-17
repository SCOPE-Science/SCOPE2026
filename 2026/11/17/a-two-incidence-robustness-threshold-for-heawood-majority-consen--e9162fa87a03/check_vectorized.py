"""Independent exhaustive Fano-incidence majority-census checker.
Run with Python 3 and NumPy: python3 check_vectorized.py
"""
from itertools import combinations
from collections import defaultdict
import numpy as np

# Build Fano lines as 2-dimensional subspaces of F_2^3.
lines = sorted({tuple(sorted((a,b,a^b)))
                for a,b in combinations(range(1,8),2)})
assert len(lines)==7
edges=sorted((p-1,7+j) for j,ls in enumerate(lines) for p in ls)
assert len(edges)==21
size=1<<14
s=np.arange(size,dtype=np.uint16)
bits=[((s>>j)&1).astype(np.uint16) for j in range(14)]

def dynamics(deleted):
    nbr=[[] for _ in range(14)]
    for e in edges:
        if e not in deleted:
            i,j=e
            nbr[i].append(j)
            nbr[j].append(i)
    successor=np.zeros(size,dtype=np.uint16)
    for v, n in enumerate(nbr):
        count=np.zeros(size,dtype=np.uint16)
        for w in n: count+=bits[w]
        k=len(n)
        output=np.where(2*count>k,1,np.where(2*count<k,0,bits[v]))
        successor |= output.astype(np.uint16)<<v
    twice=successor[successor]
    fixed=successor==s
    periodic=twice==s
    dist=np.full(size,-1,dtype=np.int16)
    dist[periodic]=0
    for i in range(1,30):
        mask=(dist<0)&(dist[successor]>=0)
        dist[mask]=dist[successor[mask]]+1
        if np.all(dist>=0):break
    assert np.all(dist>=0), 'unexpected longer recurrence'
    limit=int(dist.max())
    image=s.copy()
    for j in range(limit):image=successor[image]
    assert np.all(successor[successor[image]]==image)
    consensus=(image==0)|(image==size-1)
    return (int(fixed.sum()),int((periodic&(~fixed)).sum()//2),
            int(consensus.sum()),limit,tuple(np.bincount(dist).tolist()),consensus)

def kind(a,b):
    if a[0]==b[0] or a[1]==b[1]:return 'adjacent'
    if (a[0],b[1]) in edges or (b[0],a[1]) in edges:return 'cross'
    return 'separated'

base=dynamics(set())
classes=defaultdict(set)
count=defaultdict(int)
rec={}
for delset in [tuple()] + [(e,) for e in edges] + list(combinations(edges,2)):
    typ='intact' if len(delset)==0 else ('single' if len(delset)==1 else kind(*delset))
    f,p2,basin,d,entry,mem=dynamics(set(delset))
    gained=int(np.count_nonzero(mem&(~base[-1])))
    lost=int(np.count_nonzero(base[-1]&(~mem)))
    value=(f,p2,basin,d,gained,lost,entry)
    classes[typ].add(value)
    count[typ]+=1
    rec[typ]=value

expected={
'intact':(1,(58,1653,2592,2,0,0,(3364,1820,11200))),
'single':(21,(66,777,3744,6,1152,0,(1620,1916,5872,2368,2240,1760,608))),
'adjacent':(42,(58,533,4960,11,2368,0,(1124,2348,4064,2304,3488,1536,640,112,192,192,320,64))),
'cross':(84,(90,376,4032,8,1736,296,(842,2742,4956,3204,2288,1672,576,72,32))),
'separated':(84,(86,427,4512,6,2048,128,(940,2794,4864,2954,2392,1808,632))),
}
for typ in expected:
    target_count,target_value=expected[typ]
    assert count[typ]==target_count
    assert classes[typ]=={target_value}
    print(typ, 'cases=',count[typ], 'result=',rec[typ])

# Independently trace two explicit configurations losing consensus after disjoint pair removal.
for pair,state in [(((0,7),(1,10)),130),(((0,7),(3,10)),265)]:
    orig=dynamics(set())[-1]
    defective=dynamics(set(pair))[-1]
    assert orig[state] and not defective[state]
    print('loss witness',pair,'initial_mask',state,'initial_ones', [k for k in range(14) if state>>k&1])
print('PASS: independent vectorized exhaustive 232-graph classification')
