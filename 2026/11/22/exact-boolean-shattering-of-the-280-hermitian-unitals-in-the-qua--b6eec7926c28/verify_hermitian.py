#!/usr/bin/env python3
"""Independent GF(4) Hermitian-form realization and shattering checker."""
from itertools import product, combinations
from collections import Counter

def mul(a,b):
    z=0
    for i in range(2):
        if b>>i&1: z^=a<<i
    if z&8:z^=14
    if z&4:z^=7
    return z

def power(a): return mul(a,a)
def det(m):
    s=0
    for p in ((0,1,2),(1,2,0),(2,0,1),(0,2,1),(2,1,0),(1,0,2)):
        s ^= mul(mul(m[0][p[0]],m[1][p[1]]),m[2][p[2]])
    return s

points=set()
for v in product(range(4),repeat=3):
    if not any(v):continue
    first=next(x for x in v if x)
    inv=next(x for x in (1,2,3) if mul(x,first)==1)
    points.add(tuple(mul(inv,x) for x in v))
points=sorted(points)
assert len(points)==21

unitals=set()
for bits in range(512):
    dia=[(bits>>i)&1 for i in range(3)]
    off=[(bits>>(3+2*j))&3 for j in range(3)]
    H=[[0]*3 for _ in range(3)]
    for i in range(3):H[i][i]=dia[i]
    for (i,j),a in zip(((0,1),(0,2),(1,2)),off):
        H[i][j]=a;H[j][i]=power(a)
    if not det(H):continue
    mask=0
    for i,v in enumerate(points):
        z=0
        for a in range(3):
            for b in range(3):z^=mul(mul(power(v[a]),H[a][b]),v[b])
        if not z:mask|=1<<i
    assert mask.bit_count()==9
    unitals.add(mask)
assert len(unitals)==280, len(unitals)
# Compare to an independent line-incidence (three nonconcurrent lines) description.
def determinant(a,b,c):
    return (mul(a[0],mul(b[1],c[2])^mul(b[2],c[1]))^
            mul(a[1],mul(b[0],c[2])^mul(b[2],c[0]))^
            mul(a[2],mul(b[0],c[1])^mul(b[1],c[0])))
lines=set()
for i,j in combinations(range(21),2):
    lines.add(sum(1<<k for k in range(21) if determinant(points[i],points[j],points[k])==0))
assert len(lines)==21
triangle_unitals=set()
for a,b,c in combinations(sorted(lines),3):
    if (a&b)==(a&c):continue
    triangle_unitals.add((a|b|c)^((a&b)|(a&c)|(b&c)))
assert triangle_unitals==unitals

subsets=[Counter() for _ in range(10)]
for u in unitals:
    ix=[i for i in range(21) if u>>i&1]
    for k in range(1,10):
        for C in combinations(ix,k):
            m=sum(1<<i for i in C)
            subsets[k][m]+=1
assert [len(subsets[k]) for k in range(1,10)] == [21,210,1330,5880,17640,23520,10080,2520,280]
assert set(subsets[6].values())=={1}
assert set(subsets[5].values())=={2}
assert set(subsets[4].values())=={6}

# Check that every 6-point subset within a unital is shattered.
min_traces=64
trace_distribution=Counter()
for S in subsets[6]:
    bits=[1<<i for i in range(21) if S>>i&1]
    flags=0
    for u in unitals:
        signature=sum(1<<j for j,b in enumerate(bits) if u&b)
        flags|=1<<signature
    n=flags.bit_count()
    min_traces=min(min_traces,n)
    trace_distribution[n]+=1
assert trace_distribution==Counter({64:23520}),trace_distribution
print('HERM: 21 points; 280 nonsingular Hermitian unitals; six-set traces',dict(trace_distribution))
print('HERM: contained-support census', [len(subsets[k]) for k in range(1,10)])
print('HERM: five-set multiplicity',Counter(subsets[5].values()))
print('HERM: six-set multiplicity',Counter(subsets[6].values()))
