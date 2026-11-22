#!/usr/bin/env python3
"""Exact checks for ternary digit-set boundary ambiguity; stdlib only."""
from fractions import Fraction
from collections import deque
from itertools import product

STATES=(-2,-1,0)
DIGITS=(0,1,2)
REP={0:0,1:1,2:5}
def h(a,c):
    n=a+c
    return (n-REP[n%3])//3
assert {h(a,c) for a in DIGITS for c in STATES}==set(STATES)

def step(B,a):
    return frozenset(c for c in STATES if h(a,c) in B)
START=frozenset((0,))
FULL=frozenset(STATES)
EMPTY=frozenset()
mixed=(START,frozenset((-1,0)),frozenset((-2,-1)),frozenset((-2,0)),frozenset((-2,)),frozenset((-1,)))
assert len(mixed)==6 and len(set(mixed))==6
assert {step(B,a) for B in mixed for a in DIGITS}==set(mixed)|{FULL,EMPTY}
T=[[sum(step(B,a)==C for a in DIGITS) for C in mixed] for B in mixed]
EXPECTED=[[1,1,1,0,0,0],[0,1,0,1,0,0],[1,0,1,0,1,0],[0,1,1,0,0,0],[0,0,0,0,1,1],[1,0,0,0,1,0]]
assert T==EXPECTED,(T,EXPECTED)

def dests(B):
    words={B:''}
    q=deque([B])
    while q:
        curr=q.popleft()
        for a in DIGITS:
            after=step(curr,a)
            if after not in words:
                words[after]=words[curr]+str(a)
                q.append(after)
    return words
for B in mixed:
    words=dests(B)
    assert FULL in words and EMPTY in words and all(step(B,int(c)) in set(mixed)|{FULL,EMPTY} for c in '012')

# Every reachable negative carry can be attained from zero by low-order digits.
reach={0}
for i in range(1,4):
    reach|={h(a,c) for c in reach for a in DIGITS}
assert reach==set(STATES)

# Independently evaluate all ternary prefix words directly via carry compositions.
def direct_B(word):
    return frozenset(c for c in STATES if fold_carry(c,reversed(word))==0)
def fold_carry(c,word):
    for a in word:
        c=h(a,c)
    return c
v=[1 if i==0 else 0 for i in range(6)]
counts=[]
for n in range(10):
    count=sum(v)
    counts.append(count)
    if n<=7:
        brute=0
        for word in product(DIGITS,repeat=n):
            if direct_B(word) in mixed: brute+=1
        assert brute==count,(n,brute,count)
    v=[sum(v[i]*T[i][j] for i in range(6)) for j in range(6)]
assert counts==[1,3,8,20,49,119,288,696,1681,4059],counts
# (1-z)(1-2z-z^2)=1-3z+z^2+z^3.
for n in range(3,len(counts)):
    assert counts[n]==3*counts[n-1]-counts[n-2]-counts[n-3]
# Check recurrence beyond sample by 100 further exact matrix steps.
for n in range(10,111):
    nxt=sum(v)
    assert nxt==3*counts[-1]-counts[-2]-counts[-3]
    counts.append(nxt)
    v=[sum(v[i]*T[i][j] for i in range(6)) for j in range(6)]
# Direct graph strong connectivity.
for initial in mixed:
    assert set(mixed).issubset(dests(initial))
print('TERNARY_BOUNDARY_CERTIFICATE_OK; mixed=6; brute_levels=0..7; recurrence_levels=0..110; prefixes='+str(counts[:10]))
