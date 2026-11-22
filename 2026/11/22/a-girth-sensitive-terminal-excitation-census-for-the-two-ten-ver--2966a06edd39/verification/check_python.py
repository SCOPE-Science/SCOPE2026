#!/usr/bin/env python3
"""Independent full-state vectorized census, NumPy required."""
from collections import Counter
import numpy as np

EXPECTED = {1: (1, 1023, 25415, 29230, 3380), 2: (1, 1023, 25205, 31300, 1520)}
MIN_SEEDS = {1: 3, 2: 4}
EXPECTED_POLY={1:{3:640,4:1240,5:1040,6:400,7:60},2:{4:420,5:720,6:320,7:60}}
EXPECTED_A2={1:{1:3340,2:40},2:{1:1460,2:60}}
TOTAL = 3 ** 10

def graph(k):
    edges = set()
    for i in range(5):
        for a, b in ((i, (i+1)%5), (i, i+5), (i+5, 5+(i+k)%5)):
            edges.add(tuple(sorted((a, b))))
    assert len(edges)==15
    return [tuple(j for j in range(10) if tuple(sorted((i,j))) in edges) for i in range(10)]

def examine(k):
    adj=graph(k)
    assert all(len(a)==3 for a in adj)
    z=np.arange(TOTAL,dtype=np.int64)
    a=(z[:,None]//(3**np.arange(10)))%3
    orig_ones=(a==1).sum(axis=1)
    first=np.full(TOTAL,-1,dtype=np.int16)
    late_excited=np.zeros(TOTAL,dtype=np.int16)
    for t in range(5):
        rest=(a==0).all(axis=1)
        first[(first<0)&rest]=t
        if t==2: late_excited=(a==1).sum(axis=1)
        if t==4:break
        excited=(a==1)
        contacts=np.stack([excited[:,nb].sum(axis=1) for nb in adj],axis=1)
        a=np.where(a==1,2,np.where(a==2,0,(contacts>=2).astype(np.int64)))
    assert (a==0).all(), 'the entire image under F^4 must be all-rest'
    assert (first>=0).all()
    hist=tuple(int((first==t).sum()) for t in range(5))
    assert hist==EXPECTED[k],(hist,EXPECTED[k])
    assert int((late_excited>0).sum())==hist[4]
    assert int(orig_ones[first==4].min())==MIN_SEEDS[k]
    by_seed={int(i):int(((orig_ones==i)&(first==4)).sum()) for i in range(11)}
    assert {i:n for i,n in by_seed.items() if n}==EXPECTED_POLY[k]
    a2=Counter(map(int,late_excited[first==4]))
    assert dict(a2)==EXPECTED_A2[k]
    return hist,by_seed,a2

if __name__=='__main__':
    for k in (1,2):
        hist,seeds,late=examine(k)
        print('GP(5,%s) first-hit 0..4 = %s; last-layer by initial excitation count = %s; second-generation excited vertices = %s'% (k,hist,seeds,dict(late)))
    print('PASS: two full state spaces, 118098 configurations, 4 transitions per configuration')
