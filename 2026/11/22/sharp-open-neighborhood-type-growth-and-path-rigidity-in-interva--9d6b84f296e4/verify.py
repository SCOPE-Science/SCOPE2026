#!/usr/bin/env python3
"""Standalone finite check of interval-intersection trace bounds.
Mathematical proof (not this finite test) establishes statements for all sizes.
"""
from collections import Counter

def matchings(points):
    if not points:
        yield ()
        return
    a=points[0]
    for j in range(1,len(points)):
        b=points[j]
        for tail in matchings(points[1:j]+points[j+1:]):
            yield ((a,b),)+tail

def external_traces(intervals):
    n=len(intervals)
    traces=set()
    # 2n distinct endpoints at integer positions 1,...,2n. All closed query
    # intervals can be shifted to gap endpoints, where relations are constant.
    for lo in range(2*n+1):
        for hi in range(lo,2*n+1):
            mask=0
            for k,(l,r) in enumerate(intervals):
                if l<=hi and r>lo:
                    mask |=1<<k
            traces.add(mask)
    return traces

def open_traces(intervals):
    traces=external_traces(intervals)
    for k,(l,r) in enumerate(intervals):
        traces.add(sum(1<<j for j,(a,b) in enumerate(intervals)
                       if j!=k and a<r and b>l))
    return traces

def is_unique_path_overlap(intervals):
    n=len(intervals)
    order=sorted(range(n),key=lambda i:intervals[i][0])
    for a in range(n):
        for b in range(a+1,n):
            x,y=order[a],order[b]
            touching=intervals[x][1]>intervals[y][0]
            if touching != (b==a+1):return False
    return True

for m in range(1,7):
    hist=Counter(); maximal=[]; total=0
    for arrangement in matchings(tuple(range(1,2*m+1))):
        total+=1
        v=len(open_traces(arrangement))
        hist[v]+=1
        if m>=3 and v==1+m*(m+1)//2+(m-2):
            assert is_unique_path_overlap(arrangement), arrangement
            maximal.append(arrangement)
    predicted=2 if m==1 else 4 if m==2 else 1+m*(m+1)//2+(m-2)
    assert max(hist)==predicted,(m,hist)
    if m>=3: assert len(maximal)==1, (m,len(maximal))
    print('m',m,'matchings',total,'max',max(hist),'argmax',hist[predicted])

# Explicit optimizers for arbitrary m, and sharp minimum graph orders.
for m in range(1,11):
    A=[(4*i,4*i+6) for i in range(m)]
    # Generic half-integer sampling of query endpoints covers all possible
    # distinct external intersection patterns for these marked intervals.
    samples=[-4]+[x+0.5 for a,b in A for x in (a,b)]+[4*m+8]
    samples=sorted(set(samples))
    q={}
    for u in samples:
        for v in samples:
            if u>v:continue
            mask=sum(1<<i for i,(l,r) in enumerate(A) if l<=v and r>=u)
            q.setdefault(mask,(u,v))
    if m==1:
        wanted={1}
    elif m==2:
        wanted={0,3}
    else:
        B={0}
        for i in range(m):
            for j in range(i,m):
                B.add(sum(1<<h for h in range(i,j+1)))
        endpoint_singletons={1<<1,1<<(m-2)}
        wanted=B-endpoint_singletons
    assert wanted.issubset(q), (m,wanted-set(q))
    N=len(A)+len(wanted)
    mark_profiles=[]
    for i,(a,b) in enumerate(A):
        mark_profiles.append(sum(1<<j for j,(c,d) in enumerate(A)
                                 if i!=j and c<=b and a<=d))
    all_profiles=set(wanted)|set(mark_profiles)
    predicted=2 if m==1 else 4 if m==2 else 1+m*(m+1)//2+(m-2)
    min_order=2 if m==1 else 4 if m==2 else 9 if m==3 else predicted
    assert len(all_profiles)==predicted and N==min_order,(m,N,predicted,len(all_profiles))
    print('construction',m,'order',N,'traces',len(all_profiles))
print('VERIFY_OK')
