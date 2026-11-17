#!/usr/bin/env python3
"""Exact 3375-state support certificate for four-state excitation on tripartite graphs.
All loops use finite ranges and integer arithmetic; no graph-size cutoff is assumed.
"""
from collections import Counter
from itertools import product, permutations

COLORS=range(4)
MASKS=range(1,16)
STATES=list(product(MASKS, repeat=3))

def bitset(mask):
    return tuple(a for a in COLORS if mask & (1<<a))

def indicators(s):
    return tuple(any(s[j]&2 for j in range(3) if i!=j) for i in range(3))

def local(x,exc):
    if x==0: return int(exc)
    return (x+1)%4

def step(s):
    e=indicators(s)
    out=[]
    for i in range(3):
        mask=0
        for a in bitset(s[i]):
            mask |= 1<<local(a,e[i])
        out.append(mask)
    return tuple(out)

def iterate(s,t):
    for _ in range(t): s=step(s)
    return s

def transport(s,t):
    """Return target color of each initially occupied color in each part."""
    maps=[{a:a for a in bitset(m)} for m in s]
    for _ in range(t):
        e=indicators(s)
        for i in range(3):
            maps[i]={a:local(b,e[i]) for a,b in maps[i].items()}
        s=step(s)
    return maps

def identity(s,t):
    return iterate(s,t)==s and all(
        all(a==b for a,b in f.items()) for f in transport(s,t))

# This is a complete exhaustive identity over the size-independent 15^3 quotient.
assert len(STATES)==3375 and len(set(STATES))==3375
count_by_t=Counter()
period4_coeff=Counter()
count_by_period=Counter()
for s in STATES:
    assert iterate(s,10)==iterate(s,6)
    assert identity(iterate(s,6),4)
    recurrent=[t for t in range(7) if identity(iterate(s,t),4)]
    assert recurrent
    t=min(recurrent)
    count_by_t[t]+=1
    if t==0:
        if identity(s,1):
            assert s==(1,1,1)
            count_by_period[1]+=1
        else:
            assert not identity(s,2)
            count_by_period[4]+=1
            period4_coeff[tuple(mask.bit_count() for mask in s)]+=1
assert [count_by_t[t] for t in range(7)]==[620,248,658,739,641,391,78]
assert count_by_period=={1:1,4:619}
assert sum(period4_coeff.values())==619

# The numerical coefficient of a symmetrized surjection product is independent
# of how three sizes are assigned to the three labelled parts.
ordered_coeff={}
for i in range(1,5):
 for j in range(i,5):
  for k in range(j,5):
   v={period4_coeff.get(p,0) for p in set(permutations((i,j,k)))}
   assert len(v)==1
   c=v.pop()
   if c: ordered_coeff[(i,j,k)]=c
assert len(ordered_coeff)==16
expected={
 (1,1,2):4,(1,2,2):16,(1,2,3):8,(1,3,3):12,
 (1,3,4):4,(1,4,4):4,(2,2,2):42,(2,2,3):32,
 (2,2,4):6,(2,3,3):36,(2,3,4):12,(2,4,4):6,
 (3,3,3):36,(3,3,4):12,(3,4,4):4,(4,4,4):1}
assert ordered_coeff==expected
print('SUPPORT_STATES',len(STATES))
print('ENTRY_COUNTS',*(count_by_t[t] for t in range(7)))
print('CYCLIC_SUPPORTS_PERIOD1',count_by_period[1])
print('CYCLIC_SUPPORTS_FULL_PERIOD4',count_by_period[4])
for k,v in sorted(ordered_coeff.items()):
    print('COEFF',*k,v)
print('EXACT_SUPPORT_CERTIFICATE_PASS')
