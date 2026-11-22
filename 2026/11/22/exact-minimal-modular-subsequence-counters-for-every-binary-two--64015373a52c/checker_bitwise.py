#!/usr/bin/env python3
"""Independent finite orbit and distinguishability checks for two-run subsequence parity."""
from collections import deque
from itertools import product
from math import comb


def transition(a,b,state,letter):
    t=a.bit_length(); mask=(1<<t)-1; ym=(1<<b)-1
    r,y=state
    if letter=='0': return ((r+1)&mask,y)
    B=int((r&a)==a)
    return r,(y^((y<<1)&ym)^B)

def seq_state(a,b,w):
    s=[0]*(a+b+1);s[0]=1
    pattern='0'*a+'1'*b
    for c in w:
        for j in range(a+b,0,-1):
            if pattern[j-1]==c:s[j]^=s[j-1]
    return s

def full_signature(a,b,state):
    r,y=state;p='0'*a+'1'*b
    s=[1]+[comb(r,j)%2 for j in range(1,a+1)]+[(y>>j)&1 for j in range(b)]
    sig=[]
    for j in range(a+b+1):
        v=s.copy()
        for c in p[j:]:
            for i in range(a+b,0,-1):
                if p[i-1]==c:v[i]^=v[i-1]
        sig.append(v[-1])
    return tuple(sig)

cases=0;states_total=0;all_word_checks=0
for a in range(1,9):
 for b in range(1,9):
    if a+b>12:continue
    initial=(0,0);seen={initial};queue=[initial]
    for s in queue:
        for ch in '01':
            t=transition(a,b,s,ch)
            if t not in seen:seen.add(t);queue.append(t)
    expected=1<<(a.bit_length()+b)
    assert len(seen)==expected,(a,b,len(seen),expected)
    sigs={full_signature(a,b,s) for s in seen}
    assert len(sigs)==len(seen),(a,b,'not distinguishable')
    for w_len in range(0,min(9,a+b+3)):
        for chars in product('01',repeat=w_len):
            w=''.join(chars)
            state=initial
            for c in w:state=transition(a,b,state,c)
            s=seq_state(a,b,w)
            r,y=state
            assert r==w.count('0')%(1<<a.bit_length())
            assert y==sum(s[a+j]<< (j-1) for j in range(1,b+1)),(a,b,w)
            all_word_checks+=1
    states_total+=len(seen)
    cases+=1
print('PASS cases=%d reachable_states=%d signature_states=%d literal_words=%d'% (cases,states_total,states_total,all_word_checks))
