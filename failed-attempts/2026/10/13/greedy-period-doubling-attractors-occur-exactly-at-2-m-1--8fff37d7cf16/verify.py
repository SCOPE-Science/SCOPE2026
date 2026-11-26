#!/usr/bin/env python3
from pathlib import Path
import json

def tau(w):
    return ''.join('10' if c=='1' else '11' for c in w)

def P(m):
    w='1'
    for _ in range(m):
        w=tau(w)
    return w

def Q(m):
    w='0'
    for _ in range(m):
        w=tau(w)
    return w

def is_attractor(w,S):
    n=len(w); S=set(S)
    hit=[0]*(n+1)
    for i in range(n):
        hit[i+1]=hit[i]+(i in S)
    factors=set(); covered=set()
    for i in range(n):
        for j in range(i+1,n+1):
            f=w[i:j]
            factors.add(f)
            if hit[j]>hit[i]:
                covered.add(f)
    return factors<=covered

# Engine 1: replay the greedy definition exactly through 256 symbols.
w=P(8)
S=[]; additions=[]
for j in range(len(w)):
    if not is_attractor(w[:j+1],S):
        S.append(j); additions.append(j)
assert additions==[2**m-1 for m in range(9)]

# Engine 2: verify the morphic decomposition used by the infinite proof.
for m in range(1,11):
    pm,qm=P(m),Q(m)
    assert len(pm)==len(qm)==2**m
    assert pm[:-1]==qm[:-1] and pm[-1]!=qm[-1]
    hm=pm[:-1]
    assert P(m+1)[:-1]==pm+hm
    G=[2**i-1 for i in range(m)]
    assert is_attractor(hm,G)

# Engine 3: independently verify the occurrence lemma and the escaping
# unique suffixes that force every next greedy insertion.
for r in range(0,9):
    pr=P(r); big=P(r+2); q=2**r
    occ=[i for i in range(len(big)-len(pr)+1) if big.startswith(pr,i)]
    assert occ==[0,2*q,3*q],(r,occ)

for k in range(1,11):
    pk=P(k)
    previous=[2**i-1 for i in range(k)]
    assert not is_attractor(pk,previous)
    if k==1:
        F='0'; start=1
    else:
        r=k-2; q=2**r
        F=P(r)[-1]+P(r); start=3*q-1
    occ=[i for i in range(len(pk)-len(F)+1) if pk.startswith(F,i)]
    assert occ==[start],(k,F,occ,start)
    assert all(not(start<=s<start+len(F)) for s in previous)

cert=json.loads((Path(__file__).resolve().parent/'certificate.json').read_text(encoding='utf-8'))
assert cert['greedy_positions_first_nine']==additions
assert cert['exact_formula']=='{2^m-1:m>=0}'
print('VERIFY_OK direct_greedy_n=256 additions=0,1,3,7,15,31,63,127,255 '
      'recurrences_m<=10 occurrence_lemma_r<=8 unique_escape_k<=10 engines=3')
