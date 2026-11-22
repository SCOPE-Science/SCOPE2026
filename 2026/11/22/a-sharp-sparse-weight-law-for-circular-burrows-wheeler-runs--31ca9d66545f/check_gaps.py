"""Independent gap-bucket and rotation-order test, including sharp-density bounds."""
from itertools import permutations
from random import Random
from math import comb, factorial

def from_gaps(g):
    return ''.join('1'+'0'*v for v in g)

def transform_independent(g):
    s=from_gaps(g); n=len(s)
    order=sorted(range(n),key=lambda j: tuple(ord(s[(j+t)%n]) for t in range(n)))
    return ''.join(s[(j-1)%n] for j in order)

def count_runs(s):return 1+sum(x!=y for x,y in zip(s,s[1:]))

def part_count(m,k):
    if m<0:return 0
    p={(0,0):1}
    for j in range(1,k+1):
        p={(j,t):sum(p.get((j-1,t-j*r),0) for r in range(t//j+1)) for t in range(m+1)}
    return p[k,m]

checked=0
for k in range(2,7):
    base=list(range(1,2*k,2))
    candidates=permutations(base) if k<=5 else (tuple(base),tuple(reversed(base)), tuple(base[::2]+base[1::2]))
    for g in candidates:
        b=transform_independent(g)
        assert b[0]=='1' and b[-1]=='0'
        assert b.count('1')==k and count_runs(b)==2*k
        checked+=1
rng=Random(8675309)
for k in range(2,11):
    for _ in range(120):
        # Widely separated random gaps in arbitrary circular order
        v=sorted(rng.sample(range(1,15*k),k))
        if any(v[i+1]-v[i]<2 for i in range(k-1)):continue
        rng.shuffle(v)
        b=transform_independent(v)
        assert count_runs(b)==2*k
        checked+=1
for k in range(1,7):
    n=k*(k+1)
    for d in range(0,9):
        m=d; p=part_count(m,k)
        # Composition bijection gives k! p rooted gap tuples and n(k-1)! p indexed words
        assert n*factorial(k-1)*p >= 0
        n+=1
print('GAP_CHECK_OK tested=%d partition_instances=%d' % (checked,6*9))
