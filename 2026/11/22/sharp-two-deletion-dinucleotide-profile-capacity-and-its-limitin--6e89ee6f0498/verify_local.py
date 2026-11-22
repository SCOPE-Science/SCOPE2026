#!/usr/bin/env python3
"""Exact finite local classification and parametric sharpness checks (stdlib)."""
from itertools import product, combinations

def edge(a,b):return 2*a+b

def vector(*signed_edges):
    v=[0]*4
    for sign,ab in signed_edges:v[ab]+=sign
    return tuple(v)

def plus(u,v):return tuple(x+y for x,y in zip(u,v))

def triple(a,b,c):return vector((1,edge(a,c)),(-1,edge(a,b)),(-1,edge(b,c)))

def adj(a,b,c,d):return vector((1,edge(a,d)),(-1,edge(a,b)),(-1,edge(b,c)),(-1,edge(c,d)))

T={triple(*x) for x in product((0,1),repeat=3)}
A={adj(*x) for x in product((0,1),repeat=4)}
assert len(T)==4 and len(A)==6

counts=[]
for l in product((0,1),repeat=2):
    line=[]
    for r in product((0,1),repeat=2):
        L=vector((-1,edge(*l)));R=vector((-1,edge(*r)))
        S={plus(x,y) for x in T for y in T}|A
        S|={plus(L,x) for x in T}|{plus(R,x) for x in T}|{plus(L,R)}
        S|={vector((-1,edge(*l)),(-1,edge(l[1],c))) for c in (0,1)}
        S|={vector((-1,edge(c,r[0])),(-1,edge(*r))) for c in (0,1)}
        line.append(len(S))
    counts.append(line)
assert counts==[[11,13,14,11],[14,14,17,13],[13,17,14,14],[11,14,13,11]],counts

def profile(w):
    h=[0]*4
    for x,y in zip(w,w[1:]):h[edge(x,y)]+=1
    return tuple(h)

def difference(w,i,j):
    a=profile(w)
    b=profile(w[:i]+w[i+1:j]+w[j+1:])
    return tuple(x-y for x,y in zip(b,a))

base='0100010101110'
assert len(base)==13
S={difference(tuple(map(int,base)),i,j) for i,j in combinations(range(13),2)}
assert len(S)==17
sharp_size=len(S)
chosen={}
for d in sorted(S):
    for i,j in combinations(range(13),2):
        if difference(tuple(map(int,base)),i,j)!=d:continue
        if all(difference(tuple(map(int,base[:4]+'0'*t+base[4:])),i+(t if i>=4 else 0),j+(t if j>=4 else 0))==d for t in (1,2,3,4,10)):
            chosen[d]=(i,j)
            break
    assert d in chosen
# The chosen configurations keep their local neighborhoods unchanged under an
# arbitrary number of inserted zeroes between the fourth and fifth positions.
for t in (0,1,2,3,5,10,30):
    w=tuple(map(int,base[:4]+'0'*t+base[4:]))
    assert len({difference(w,i,j) for i,j in combinations(range(len(w)),2)})==17
    assert all(difference(w,i+(t if i>=4 else 0),j+(t if j>=4 else 0))==d for d,(i,j) in chosen.items())

# Limiting profile-ball spectrum conditional on independent three-bit boundaries.
# Interior saturation occurs with exponentially high probability, since every
# binary length-four factor occurs many times in separated blocks.
from collections import Counter
limiting=Counter()
for pref in product((0,1),repeat=3):
    for suff in product((0,1),repeat=3):
        l=pref[:2];r=suff[1:]
        L=vector((-1,edge(*l)));R=vector((-1,edge(*r)))
        S={plus(x,y) for x in T for y in T}|A
        S|={plus(L,x) for x in T}|{plus(R,x) for x in T}|{plus(L,R)}
        S.add(vector((-1,edge(pref[0],pref[1])),(-1,edge(pref[1],pref[2]))))
        S.add(vector((-1,edge(suff[0],suff[1])),(-1,edge(suff[1],suff[2]))))
        limiting[len(S)]+=1
assert limiting=={9:4,10:8,11:4,13:24,14:16,17:8},limiting
print('limiting_spectrum_counts_out_of_64',dict(sorted(limiting.items())))
print('triple_change_types',len(T),'adjacent_change_types',len(A))
print('boundary_envelope_table')
for row in counts:print(' '.join(map(str,row)))
print('sharp_witness',base,'first_length',13,'profile_count',sharp_size)
print('witness_pairs_zero_indexed')
for d,pair in sorted(chosen.items()):print(' '.join(map(str,d))+' : '+str(pair[0])+','+str(pair[1]))
print('parameterized_witness_checks_passed')
