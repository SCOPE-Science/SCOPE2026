#!/usr/bin/env python3
"""Exact finite certificate for threshold-two three-colour dynamics on K_{a,b,c}."""
from collections import Counter, defaultdict
from itertools import product
from math import lcm

BASE = [3**i for i in range(9)]
SIZE = 3**9

def decode(x):
    return tuple((x // BASE[j]) % 3 for j in range(9))

def successor_colour(s, shore, colour):
    next_colour = (colour + 1) % 3
    support = sum(s[3*j + next_colour] for j in range(3) if j != shore)
    return next_colour if support >= 2 else colour

def successor(s):
    out = [0] * 9
    for idx, count in enumerate(s):
        if count:
            k = 3*(idx//3) + successor_colour(s,idx//3,idx%3)
            out[k] = min(2,out[k] + count)
    return tuple(out)

def encode(s):
    return sum(BASE[i] * s[i] for i in range(9))

states=[decode(i) for i in range(SIZE)]
nxt=[encode(successor(s)) for s in states]
feasible=[i for i,s in enumerate(states) if all(any(s[3*a:3*a+3]) for a in range(3))]
assert len(feasible)==17576

# The colour trajectory of each originally occupied bucket determines every
# labelled vertex, regardless of the numbers represented by clipped value 2.
def lifted_trace(s, time):
    initial=s
    track=list(range(3))*3
    for t in range(time):
        moved=[successor_colour(s,j//3,track[j]) for j in range(9)]
        track=moved
        s=successor(s)
    return s,tuple(track[j] if initial[j] else -1 for j in range(9))

for i in feasible:
    assert lifted_trace(states[i],9)==lifted_trace(states[i],21)
# Sharpness: witness with exact counts (size 2,3,5), already sorted by shores.
witness=((0,1,1),(2,0,1),(2,2,1))
s0=tuple(x for part in witness for x in part)
assert lifted_trace(s0,8) != lifted_trace(s0,20)

# Every cycle of clipped counts, and the permutation of initially occupied
# colour buckets induced by a full lap around it.
visited=set();cycles=[]
for i in range(SIZE):
    if i in visited:continue
    path=[];where={};j=i
    while j not in visited and j not in where:
        where[j]=len(path);path.append(j);j=nxt[j]
    if j in where:
        cyc=path[where[j]:]
        if all(any(states[cyc[0]][3*a:3*a+3]) for a in range(3)):
            cycles.append(cyc)
    visited.update(path)
assert len(cycles)==826

# Each pattern (minimum part sizes, unrestricted-part flags) captures exactly
# the sizes that realize that clipped periodic cycle.
patterns=defaultdict(set)
cycle_types=Counter()
for cyc in cycles:
    s=states[cyc[0]]
    support=[j for j in range(9) if s[j]>0]
    after,trace=lifted_trace(s,len(cyc))
    assert after==s
    for a in range(3):
        initial={j%3 for j in support if j//3==a}
        image={trace[j] for j in support if j//3==a}
        assert initial==image
    mult=1
    for j in support:
        dest=j
        order=0
        while True:
            dest=3*(dest//3)+trace[dest]
            order+=1
            assert order<=3
            if dest==j:break
        mult=lcm(mult,order)
    period=len(cyc)*mult
    mins=tuple(sum(s[3*a:3*a+3]) for a in range(3))
    free=tuple(2 in s[3*a:3*a+3] for a in range(3))
    patterns[period].add((mins,free))
    cycle_types[period]+=1
assert set(patterns)=={1,3,4,6,12}
assert cycle_types=={1:174,3:614,4:9,6:2,12:27}

# Every minimum size is at most 6; values 7 and above are indistinguishable
# for these existential conditions. Testing 1..7 in each part is exhaustive.
def admits(sizes,p):
    return any(all((sizes[j]>=mins[j] if free[j] else sizes[j]==mins[j])
                   for j in range(3)) for mins,free in patterns[p])

def classified(sizes,p):
    a,b,c=sorted(sizes)
    if p==1:return True
    if p==3:return (a>=2 or (a==1 and ((b<=2 and c>=6) or b>=5)))
    if p==4:return (a==2 and b==2 and c>=4)
    if p==6:return (a,b,c)==(2,2,2)
    if p==12:return (a<=3 and b>=4)
    return False
for sizes in product(range(1,8),repeat=3):
    for p in (1,2,3,4,6,12):
        assert admits(sizes,p)==classified(sizes,p),(sizes,p)

assert max(max(m) for pats in patterns.values() for m,f in pats)<=6
print('CAPPED_STATES=19683 FEASIBLE=17576 CYCLES=826')
print('UNIVERSAL_IDENTITY=F^21=F^9 SHARP_FIRST_ENTRY=9')
print('PERIOD_COUNTS='+repr(dict(sorted(cycle_types.items()))))
print('EXACT_PERIOD_SET=(1,3,4,6,12)')
print('EXISTENCE_FORMULAS=PASS_ON_ALL_SIZE_CLASSES')
print('CERTIFICATE_OK')
