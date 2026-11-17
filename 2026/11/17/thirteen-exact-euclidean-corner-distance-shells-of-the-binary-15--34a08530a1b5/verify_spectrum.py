#!/usr/bin/env python3
"""Exact cubic-corner to [15,4,8] binary simplex-code polytope spectrum.
Run: python verify_spectrum.py
Only Python standard library. Every one of the 32768 cube corners is visited.
"""
from fractions import Fraction
from collections import Counter, defaultdict
N=16
n=15
codewords=[sum(((((a & v).bit_count() & 1) << (v-1))) for v in range(1,N)) for a in range(N)]
expected={
'49/15':16, '18/7':240, '12/5':448, '25/11':1680,
'27/13':560, '29/14':6720, '2':6720, '5/3':7168,
'3/2':6720, '4/3':560, '6/5':1680, '7/9':240, '0':16}
expected_active={
'49/15':15, '18/7':7, '12/5':10, '25/11':11,
'27/13':13, '29/14':7, '2':4, '5/3':6,
'3/2':3, '4/3':3, '6/5':5, '7/9':9, '0':1}
assert len(set(codewords))==N
assert all((codewords[a]^codewords[b]).bit_count()==8 for a in range(N) for b in range(a))
count=Counter();active=defaultdict(Counter);by_distance=defaultdict(set)
for x in range(1<<n):
    wt=x.bit_count()
    b=[N-2*(c.bit_count()+wt)+4*(c&x).bit_count() for c in codewords]
    assert sum(b)==N and sum(t*t for t in b)==N*N
    ordered=sorted(b,reverse=True)
    threshold=None
    for k in range(1,N+1):
        t=Fraction(sum(ordered[:k])-N,k)
        if ordered[k-1]>t and (k==N or ordered[k]<=t):
            threshold=t;support=k;break
    assert threshold is not None
    y=[max(Fraction(0),Fraction(z)-threshold) for z in b]
    assert sum(y)==N
    # KKT: each y_a >= 0, y_a=b_a-threshold on its support,
    # and b_a <= threshold elsewhere.
    assert all((y[a]>0 and y[a]==b[a]-threshold) or
               (y[a]==0 and b[a]<=threshold) for a in range(N))
    d=sum((y[a]-b[a])**2 for a in range(N))/(4*N)
    label=str(d)
    count[label]+=1;active[label][support]+=1
    by_distance[label].add(x)
assert count==expected,(count,expected)
assert all(active[level]==Counter({expected_active[level]:frequency})
           for level,frequency in expected.items()),active
assert sum(count.values())==32768
full=(1<<n)-1
maxima={full^c for c in codewords}
assert by_distance['49/15']==maxima
neighbors={x^(1<<i) for x in maxima for i in range(n)}
assert len(neighbors)==240 and by_distance['18/7']==neighbors
print('SIMPLEX15_EXACT_PASS inputs=32768 shells=13 max=16 next=240')
