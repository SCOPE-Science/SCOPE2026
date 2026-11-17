#!/usr/bin/env python3
"""Independent exhaustive labelled-vertex replay (no capped populations)."""
from collections import Counter
from itertools import product

def update(x,sizes):
    cuts=[0]
    for a in sizes:cuts.append(cuts[-1]+a)
    y=list(x)
    for i in range(len(x)):
        own=next(j for j in range(3) if cuts[j]<=i<cuts[j+1])
        succ=(x[i]+1)%3
        cnt=sum(x[k]==succ for k in range(len(x))
                if not(cuts[own]<=k<cuts[own+1]))
        if cnt>=2:y[i]=succ
    return tuple(y)

def census(sizes):
    all_states=list(product(range(3),repeat=sum(sizes)))
    ids={x:i for i,x in enumerate(all_states)}
    nxt=[ids[update(x,sizes)] for x in all_states]
    per=[0]*len(all_states);depth=[-1]*len(all_states)
    for i in range(len(all_states)):
        if depth[i]>=0:continue
        path=[];where={};j=i
        while depth[j]<0 and j not in where:
            where[j]=len(path);path.append(j);j=nxt[j]
        if depth[j]>=0:
            period=per[j];d=depth[j]
            for x in reversed(path):
                d+=1;depth[x]=d;per[x]=period
        else:
            begin=where[j];period=len(path)-begin
            for x in path[begin:]:per[x]=period;depth[x]=0
            d=0
            for x in reversed(path[:begin]):
                d+=1;depth[x]=d;per[x]=period
    assert all(x<=9 for x in depth)
    assert set(per)<=set((1,3,4,6,12))
    return Counter(per),max(depth),next((all_states[i] for i in range(len(per)) if depth[i]==9),None)

sizes_to_check=[(1,1,6),(1,4,4),(1,4,5),(2,2,2),(2,2,4),(2,3,5),(3,3,3)]
for sizes in sizes_to_check:
    periods,d,w=census(sizes)
    print('sizes=%s states=%d maxentry=%d periods=%s' %
          (sizes,3**sum(sizes),d,dict(sorted(periods.items()))))
    if w is not None:print('sharp_witness='+repr(w))
print('LABELLED_EXHAUSTIVE_OK')
