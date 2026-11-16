"""Exact exhaustive check of non-cancelling unordered threefold dyadic sums."""
from itertools import combinations_with_replacement
from collections import defaultdict
B=4096
# Any representation of nonzero D has largest absolute term at most 4|D|.
E=(4*B).bit_length()-1
S=[0]+[t for j in range(E+1) for t in (-2**j,2**j)]
buckets=defaultdict(int)
for a,b,c in combinations_with_replacement(S,3):
    if a==-b or a==-c or b==-c:continue
    d=a+b+c
    if 0<abs(d)<=B:buckets[d]+=1
assert all(buckets[d]==buckets[-d] for d in range(1,B+1))
assert all(buckets[d] in range(0,7) or buckets[d]==8 for d in range(1,B+1))
assert {d for d in range(1,B+1) if buckets[d]==8}=={3*2**k for k in range(1,12) if 3*2**k<=B}
print('PASS exhaustive',B, 'all nonzero integers; positive max',max(buckets[d] for d in range(1,B+1)), 'exception_count',sum(buckets[d]==8 for d in range(1,B+1)))
