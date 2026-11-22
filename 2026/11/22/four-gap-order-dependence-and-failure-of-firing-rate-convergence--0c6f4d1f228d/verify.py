#!/usr/bin/env python3
"""Exact finite consistency checks for the four-gap spiking result.

No randomness, external dependencies, or external data files are used.
"""
from fractions import Fraction
from itertools import product, permutations

A=(0,2,5,9)
B=(0,2,6,9)

def clock(word):
    ev=[14*k+u for k,z in enumerate(word) for u in (A if z=='A' else B)]
    ev.append(14*len(word))
    return ev

def greedy(events,c):
    accepted=[events[0]]
    for t in events[1:]:
        if Fraction(t-accepted[-1])>=c:
            accepted.append(t)
    return accepted

def expected(word,c):
    n=len(word)
    if c<=2:return 4*n
    if c<=3:return 3*n
    if c<=4:return 3*n-word.count('B')
    if c<=5:return 2*n
    raise ValueError('out of scope')

nwords=0
for n in range(1,9):
    for x in product('AB',repeat=n):
        word=''.join(x)
        ev=clock(word)
        assert len(ev)==4*n+1
        gaps=[v-u for u,v in zip(ev,ev[1:])]
        assert all(sorted(gaps[4*k:4*k+4])==[2,3,4,5] for k in range(n))
        for c in (Fraction(1,3),Fraction(2),Fraction(5,2),Fraction(3),
                  Fraction(7,2),Fraction(4),Fraction(9,2),Fraction(5)):
            shots=greedy(ev,c)
            assert len(shots)-1==expected(word,c), (word,c,shots)
            assert all(14*k in shots for k in range(n+1))
        nwords+=1

def best_subset_count(events,c):
    best=0
    for mask in range(1<<len(events)):
        s=[t for i,t in enumerate(events) if mask>>i&1]
        if all(b-a>=c for a,b in zip(s,s[1:])):
            best=max(best,len(s))
    return best

nmirror=0
for gaps in permutations((2,3,5)):
    P=sum(gaps)
    ev=[0,gaps[0],gaps[0]+gaps[1],P,
        P+gaps[0],P+gaps[0]+gaps[1],2*P]
    rev=sorted(2*P-t for t in ev)
    # Compare reflected finite arrangements via exact exhaustive optimum.
    for c in (1,2,3,4,5,6,8):
        assert len(greedy(ev,Fraction(c)))==best_subset_count(ev,c)
        assert best_subset_count(ev,c)==best_subset_count(rev,c)
        nmirror+=1

print(f'PASS: {nwords} binary words; {nwords*8} exact word/threshold projections; '
      f'{nmirror} reversal/greedy checks; fixed gap marginals.')
