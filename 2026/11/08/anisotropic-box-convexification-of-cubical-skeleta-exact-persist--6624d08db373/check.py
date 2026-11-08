"""Exact finite checks for anisotropic cubical-skeleton Minkowski offsets.
Run: python check.py   (standard-library only, no external data).
Finite checks corroborate the general proof; they are not its substitute.
"""
from itertools import product, combinations
from fractions import Fraction as F
from math import comb
import random

checks=0

def assert_equal(a,b,ctx=''):
    global checks
    checks+=1
    if a!=b: raise AssertionError((ctx,a,b))

def cells(s,k):
    return [c for c in product((0,1,2),repeat=s) if c.count(2)==k]

def rank_binary(columns):
    pivots={}
    for value in columns:
        x=value
        while x:
            pos=x.bit_length()-1
            if pos in pivots:x^=pivots[pos]
            else:
                pivots[pos]=x
                break
    return len(pivots)

def boundary_rank(s,k):
    if k==0:return 0
    rows=cells(s,k-1)
    index={v:i for i,v in enumerate(rows)}
    cols=[]
    for c in cells(s,k):
        bit=0
        for j,v in enumerate(c):
            if v==2:
                for w in (0,1):
                    b=c[:j]+(w,)+c[j+1:]
                    bit^=1<<index[b]
        cols.append(bit)
    return rank_binary(cols)

def beta(s,r):
    if s<=r:return 0
    return sum(2**(j-r-1)*comb(j-1,r) for j in range(r+1,s+1))

for s in range(1,7):
    for r in range(s):
        ranks=[boundary_rank(s,k) for k in range(0,r+2)]
        for k in range(r+1):
            actual=len(cells(s,k))-ranks[k]- (ranks[k+1] if k<r else 0)
            expected=beta(s,r)+(1 if k==0 and r==0 else 0) if k==r else (1 if k==0 else 0)
            # H_0 of a connected positive-dimensional skeleton is 1.
            if r==0 and k==0:expected=beta(s,0)+1
            assert_equal(actual,expected,('homology',s,r,k))
for s in range(2,80):
    for r in range(s):
        fchi=sum((-1)**j*2**(s-j)*comb(s,j) for j in range(r+1))
        assert_equal(beta(s,r),(-1)**r*(fchi-1),('Euler',s,r))
        assert_equal(beta(s,r)-beta(s-1,r),2**(s-r-1)*comb(s-1,r),('deaths',s,r))

def in_offset(x,a,lam,r):
    # x coordinate belongs to bounding Q and at least d-r endpoint intervals.
    d=len(x)
    if any(v < -lam*w or v > 1+lam*w for v,w in zip(x,a)):return False
    gap=sum(1 for v,w in zip(x,a) if lam*w < v < 1-lam*w)
    return gap<=r

def union_face_membership(x,a,lam,r):
    # Independent coordinatewise reconstruction: at least d-r coordinates
    # admit an endpoint of the cube within the corresponding dilation interval.
    good=0
    for v,w in zip(x,a):
        if v < -lam*w or v>1+lam*w:return False
        if abs(v)<=lam*w or abs(v-1)<=lam*w:good+=1
    return good>=len(x)-r

def missing_volume(a,lam,r):
    narrow=[i for i,w in enumerate(a) if 2*lam*w<1]
    wide=[i for i,w in enumerate(a) if 2*lam*w>=1]
    pref=F(1)
    for i in wide:pref*=1+2*lam*a[i]
    total=F(0)
    for mask in product((0,1),repeat=len(narrow)):
        if sum(mask)<=r:continue
        term=pref
        for bit,i in zip(mask,narrow):
            term*=1-2*lam*a[i] if bit else 4*lam*a[i]
        total+=term
    return total

rng=random.Random(190722)
for d in range(2,8):
    for r in range(d):
        for j in range(60):
            a=[F(rng.randint(1,7),rng.randint(1,5)) for _ in range(d)]
            lam=F(rng.randint(0,8),rng.randint(2,12))
            for z in range(25):
                x=[F(rng.randint(-10,20),rng.randint(4,12)) for _ in range(d)]
                assert_equal(in_offset(x,a,lam,r), union_face_membership(x,a,lam,r),('membership',d,r,j,z))
            narrow=sum(1 for w in a if 2*lam*w<1)
            assert_equal(missing_volume(a,lam,r)==0,narrow<=r,('convexity',d,r,j))
            a_sorted=sorted(a)
            threshold=1/(2*a_sorted[r])
            assert_equal(narrow<=r,lam>=threshold,('threshold',d,r,j))

print('PASS:',checks,'exact checks. Cubical homology ranks through dimension 6;')
print('Euler/death identities through dimension 79, all-rank;')
print('rational offset membership, volume and thresholds through dimension 7.')
