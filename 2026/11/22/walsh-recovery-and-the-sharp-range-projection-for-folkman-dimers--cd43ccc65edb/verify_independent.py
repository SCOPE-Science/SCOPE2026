#!/usr/bin/env python3
"""Independent exact-integer Folkman dimer Walsh census; requires NumPy."""
import math
import numpy as np
from collections import Counter, deque
from fractions import Fraction

pairs = [(i,j) for i in range(5) for j in range(i+1,5)]
# This implementation explicitly labels each left clone as 2*i+copy, and right vertex as 10+k.
edges = [(2*i+c, 10+k) for k,(i,j) in enumerate(pairs) for i in (i,j) for c in (0,1)]
assert len(edges)==40 and len(set(edges))==40
neighbors = [[] for _ in range(20)]
for t,(a,b) in enumerate(edges):
    neighbors[a].append((b,t)); neighbors[b].append((a,t))
assert all(len(a)==4 for a in neighbors)
seen={0}; q=deque([0]); tree=set()
while q:
    u=q.popleft()
    for v,e in neighbors[u]:
        if v not in seen: seen.add(v);tree.add(e);q.append(v)
assert len(tree)==19 and len(seen)==20
chords={e:i for i,e in enumerate(e for e in range(40) if e not in tree)}
assert len(chords)==21
freq = np.zeros(1<<21, dtype=np.int64)
orientations=0
for orient in range(1024):
    incoming=[[] for _ in range(5)]
    for k,(i,j) in enumerate(pairs):
        incoming[i if ((orient>>k)&1) else j].append(k)
    if any(len(a)!=2 for a in incoming):continue
    orientations+=1
    for assignment in range(32):
        mask=0
        for i in range(5):
            for t,k in enumerate(incoming[i]):
                copy=t ^ ((assignment>>i)&1)
                edge=4*k + (copy if pairs[k][0]==i else 2+copy)
                if edge in chords:mask^=1<<chords[edge]
        freq[mask]+=1
assert orientations==24 and int(freq.sum())==768 and int(np.count_nonzero(freq))==768

def wht(arr):
    n=arr.size
    h=1
    while h<n:
        for start in range(0,n,2*h):
            a=arr[start:start+h].copy()
            b=arr[start+h:start+2*h].copy()
            arr[start:start+h]=a+b
            arr[start+h:start+2*h]=a-b
        h*=2

trans=freq.copy();wht(trans)
# Direct character sums for a fixed deterministic selection, independent of the transform.
frequencies=[0,1,3,5,21,53,256,511,1025,4095,45678,123456,999999,2097151]
match_masks=np.flatnonzero(freq).tolist()
for S in frequencies:
    expected=sum(-1 if (int(S & m).bit_count() & 1) else 1 for m in match_masks)
    assert int(trans[S]) == expected, (S,expected,int(trans[S]))
assert int(np.dot(trans,trans))==(1<<21)*768
hist=Counter(map(int,trans))
assert hist[0]==1262164 and sum(hist.values())==2097152
assert min(abs(k) for k in hist if k) == 32
assert trans[0]==768
proj=np.asarray(trans!=0,dtype=np.int64)
wht(proj)
numer=int(np.abs(proj).sum());endnorm=Fraction(numer,2097152)
assert numer==452160984 and endnorm==Fraction(56520123,262144)
print('INDEPENDENT_FOLKMAN_WALSH_PASS')
print('orientation_count',orientations,'matchings',int(freq.sum()))
print('nullity_reduced',hist[0],'rank_reduced',2097152-hist[0])
print('projector_norm',endnorm)
print('multiplier_histogram',sorted(hist.items()))
