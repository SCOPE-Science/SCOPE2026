#!/usr/bin/env python3
"""Reproducible exact finite verification of a rooted food-web example.

No external libraries, network access or random sampling are required.
"""
from itertools import combinations
from math import comb

N = 5
# Species -1 is an undeletable nutrient root. 0,...,4 are subject to
# primary removals; 5,6 are monitored consumers, not primary-removal targets.
EDGES = (
    (-1,0), (-1,1), (-1,2),
    (0,4), (0,6), (1,3), (2,4), (2,5),
    (3,4), (4,5), (4,6),
)

def reachable(mask):
    """Return reachability of consumers 5,6 after primary removals."""
    seen = {-1}
    for v in range(N):
        if mask & (1 << v) and any(u in seen for u,w in EDGES if w == v):
            seen.add(v)
    return tuple(any(u in seen for u,w in EDGES if w == target)
                 for target in (5,6))

def algebraic(mask):
    s = [bool(mask & (1<<j)) for j in range(N)]
    x = s[2] or (s[4] and (s[0] or (s[1] and s[3])))
    y = s[0] or (s[4] and (s[2] or (s[1] and s[3])))
    return x,y

for m in range(1<<N):
    assert reachable(m) == algebraic(m), (m,reachable(m),algebraic(m))
# Every deletable vertex makes a difference to at least one focal consumer.
assert all(any(reachable(mask) != reachable(mask ^ (1<<i))
               for mask in range(1<<N) if mask & (1<<i))
           for i in range(N))

witness = []
for k in range(N+1):
    layer = [reachable(m) for m in range(1<<N) if m.bit_count()==k]
    size = len(layer)
    a = sum(x for x,_ in layer)
    b = sum(y for _,y in layer)
    both = sum(x and y for x,y in layer)
    covariance_num = size * both - a*b
    witness.append((size,a,b,both,covariance_num))
assert witness == [
    (1,0,0,0,0), (5,1,1,0,-1), (10,5,5,3,5),
    (10,9,9,8,-1), (5,5,5,5,0), (1,1,1,1,0)]

# Every increasing Boolean function on four coordinates is uniquely
# represented by a sixteen-bit truth table (one bit for each subset).
# Checking the 32 Boolean-cube cover relations suffices for monotonicity.
M = 4
cover = [(s,s|(1<<i)) for s in range(1<<M)
         for i in range(M) if not (s&(1<<i))]
assert len(cover) == 32
all_increasing = []
for truth in range(1<<(1<<M)):
    if all(not ((truth>>s)&1) or ((truth>>t)&1) for s,t in cover):
        all_increasing.append(truth)
assert len(all_increasing)==168  # Includes constants 0 and 1.

# An independent antichain construction yields the identical set of functions.
# Any monotone function is an OR of AND terms from its incomparable minimal
# true input subsets (the empty family produces the constant-zero function).
all_masks = list(range(1<<M))
from_antichains = set()
for family_bits in range(1<<(1<<M)):
    family = [all_masks[j] for j in range(1<<M)
              if family_bits & (1<<j)]
    if any((s&t)==s for s in family for t in family if s!=t):
        continue
    truth = sum((1<<state) for state in range(1<<M)
                if any((state&minimal)==minimal for minimal in family))
    from_antichains.add(truth)
assert from_antichains==set(all_increasing)

layers = [[s for s in range(1<<M) if s.bit_count()==k] for k in (1,2,3)]
assert [len(z) for z in layers] == [4,6,4]
counts = []
for truth in all_increasing:
    counts.append(tuple(sum((truth>>s)&1 for s in layer) for layer in layers))

def score(a,b,layer,count_a,count_b):
    joint = sum(((a>>s)&1) & ((b>>s)&1) for s in layer)
    return len(layer)*joint-count_a*count_b

pairs_checked = 0
for i,a in enumerate(all_increasing):
    for j,b in enumerate(all_increasing):
        numerators = [score(a,b,layers[k],counts[i][k],counts[j][k])
                      for k in range(3)]
        signs = [1 if z>0 else -1 for z in numerators if z]
        assert not (len(signs)==3 and signs[0]!=signs[1] and signs[1]!=signs[2]), (i,j,numerators)
        pairs_checked+=1
assert pairs_checked==168**2
print('PASS 32 cover relations, 168 monotone functions by two enumerations, 28,224 ordered pairs')
print('PASS 32 rooted-web configurations, covariance numerators:')
for k,(size,a,b,both,num) in enumerate(witness):
    print(k,size,a,b,both,num)
