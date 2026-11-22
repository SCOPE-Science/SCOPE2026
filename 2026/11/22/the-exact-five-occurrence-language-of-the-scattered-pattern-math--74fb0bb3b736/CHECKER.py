#!/usr/bin/env python3
"""Finite-state certificate for a fixed subsequence-frequency language.

The program verifies, for every binary input word, that the exact-five
subsequence counter for 001100 recognizes precisely
    1* 0 1* 0 (1011|1101) 0 1* 0 1*.

Usage: python CHECKER.py
       python CHECKER.py --emit > CERTIFICATE.tsv
Standard-library Python only.
"""
from collections import deque
from functools import lru_cache
from itertools import product
from math import comb
from pathlib import Path
import sys

PATTERN='001100'
SATURATION=6
WORDS=('1011','1101')
TOKENS=tuple(tuple(('1*','0','1*','0')+tuple(v)+('0','1*','0','1*')) for v in WORDS)


def epsilon_close(bits, k):
    t=TOKENS[k]
    while True:
        nextbits=bits
        for i,token in enumerate(t):
            if token=='1*' and (bits>>i)&1:
                nextbits |= 1<<(i+1)
        if nextbits==bits:
            return bits
        bits=nextbits

@lru_cache(maxsize=None)
def regex_transition(bits,k,letter):
    t=TOKENS[k]; newbits=0
    for i, token in enumerate(t):
        if not ((bits>>i)&1) or i==len(t):
            continue
        if token=='1*':
            if letter==1: newbits |= 1<<i
        elif token==str(letter):
            newbits |= 1<<(i+1)
    return epsilon_close(newbits,k)

def count_transition(counts, letter):
    # Prefix-subsequence recurrence, saturated at 6.
    d=list(counts)
    for j in range(5,-1,-1):
        if int(PATTERN[j])==letter:
            d[j]=min(SATURATION, d[j]+(1 if j==0 else d[j-1]))
    return tuple(d)

def next_state(st,letter):
    d,s,t=st
    return (count_transition(d,letter),
            regex_transition(s,0,letter),regex_transition(t,1,letter))

def start():
    return ((0,)*6,epsilon_close(1,0),epsilon_close(1,1))

def row_ok(st):
    d,s,t=st
    is_five=(d[5]==5)
    is_regex=bool((s>>len(TOKENS[0]))&1 or (t>>len(TOKENS[1]))&1)
    return is_five==is_regex

def enumerate_reachable():
    states=[start()]; index={states[0]:0}; queue=deque([0]); edges=[]
    while queue:
        j=queue.popleft(); st=states[j]
        if not row_ok(st):
            raise AssertionError(('language disagreement',j,st))
        nxt=[]
        for c in (0,1):
            v=next_state(st,c)
            if v not in index:
                index[v]=len(states); states.append(v);queue.append(index[v])
            nxt.append(index[v])
        edges.append((j,*nxt))
    edges.sort()
    return states,edges

def serialize(states,edges):
    return ''.join(f'{i}\t{",".join(map(str,states[i][0]))}\t{states[i][1]}\t{states[i][2]}\t{e0}\t{e1}\n' for i,e0,e1 in edges)

def read_certificate(filename):
    rows=[]
    for l in filename.read_text('utf-8').splitlines():
        pieces=l.split('\t')
        assert len(pieces)==6,l
        i=int(pieces[0]);d=tuple(int(x) for x in pieces[1].split(','));s,t,e0,e1=map(int,pieces[2:])
        assert len(d)==6 and all(0<=x<=SATURATION for x in d)
        rows.append((i,(d,s,t),(e0,e1)))
    return rows

def direct_counter(w):
    # A second implementation, with unbounded integer counters.
    dp=[1,0,0,0,0,0,0]
    for c in w:
        for j in range(6,0,-1):
            if c==PATTERN[j-1]:dp[j]+=dp[j-1]
    return dp[-1]

def verify(path):
    rows=read_certificate(path)
    assert len(rows)==126
    states=[st for i,st,e in rows]
    assert [i for i,st,e in rows]==list(range(len(rows)))
    assert len(set(states))==len(states) and states[0]==start()
    reach={0};Q=deque([0]);allowed_edges=[]
    for i,st,ed in rows:
        assert row_ok(st),('bad terminal',i)
        assert all(0<=j<len(rows) for j in ed)
        assert all(states[ed[c]]==next_state(st,c) for c in (0,1)),('bad edge',i)
        allowed_edges.append(ed)
    while Q:
        q=Q.popleft()
        for h in allowed_edges[q]:
            if h not in reach:reach.add(h);Q.append(h)
    assert len(reach)==len(rows),'certificate includes unreachable states'
    print('PASS complete finite-state certificate:',len(rows),'reachable product states; 252 verified transitions')
    print('PASS terminal equivalence holds at every reachable state')

    # An independent short-word check of the exact length enumeration.
    for n in range(6,17):
        observed=sum(direct_counter(''.join(w))==5 for w in product('01',repeat=n))
        predicted=2*comb(n-5,3) if n>=8 else 0
        assert observed==predicted,(n,observed,predicted)
    print('PASS direct count for every binary word of lengths 6 through 16')
    print('PASS coefficient formula: 2*z^8/(1-z)^4')

if __name__=='__main__':
    if len(sys.argv)==2 and sys.argv[1]=='--emit':
        states,edges=enumerate_reachable()
        sys.stdout.write(serialize(states,edges))
    elif len(sys.argv)==1:
        verify(Path(__file__).with_name('CERTIFICATE.tsv'))
    else:
        raise SystemExit('usage: CHECKER.py [--emit]')
