#!/usr/bin/env python3
"""Exact finite-state enumeration of binary one-deletion trigram-profile balls.
No third-party dependencies. Outputs are deterministic.
"""
from itertools import product

ALPHABET=(0,1)
def profile(word):
    v=[0]*8
    for a,b,c in zip(word,word[1:],word[2:]):
        v[4*a+2*b+c]+=1
    return tuple(v)
def difference(a,b):
    return tuple(x-y for x,y in zip(a,b))
def deletion_delta(word,i):
    return difference(profile(word[:i]+word[i+1:]),profile(word))

five_words=list(product(ALPHABET,repeat=5))
local={x:deletion_delta(x,2) for x in five_words}
features=tuple(sorted(set(local.values())))
assert len(features)==10
fid={v:i for i,v in enumerate(features)}
mask={x:1<<fid[local[x]] for x in five_words}
quadruples=list(product(ALPHABET,repeat=4))
left={q:(deletion_delta(q,0),deletion_delta(q,1)) for q in quadruples}
right={q:(deletion_delta(q,2),deletion_delta(q,3)) for q in quadruples}

# A deterministic automaton remembers its first four letters, last four,
# and exactly the distinct 5-neighborhood classes already observed.
# State merging is sound because the entire output statistic depends only
# on these three pieces of data.
max_by_n={}
first=[]
for prefix in quadruples:
    states={(prefix,0):''.join(map(str,prefix))}
    for n in range(4,21):
        for (suffix,seen),witness in states.items():
            actual={features[k] for k in range(10) if seen>>k&1}
            actual.update(left[prefix]);actual.update(right[suffix])
            count=len(actual)
            if count>max_by_n.get(n,0):max_by_n[n]=count
            if count==14 and (not first or n<first[0][0]):
                first=[(n,witness)]
        if n==20:break
        nxt={}
        for (suffix,seen),witness in states.items():
            for b in ALPHABET:
                q=suffix+(b,)
                ns=(q[1:],seen|mask[q])
                if ns not in nxt:nxt[ns]=witness+str(b)
        states=nxt
assert len(first)>0 and first[0][0]==20
assert all(max_by_n[n]<14 for n in range(4,20))
assert max_by_n[20]==14
print('interior_changes',len(features))
print('all_length_upper_bound',len(features)+4)
print('max_by_length_4_to_20',','.join(str(max_by_n[n]) for n in range(4,21)))
print('first_length_reaching_14',first[0][0])
print('one_20_letter_witness',first[0][1])

base='01'+'000'+'100101011011101'
assert len(base)==20
for t in range(25):
    w=tuple(map(int,'01'+'0'*(3+t)+'100101011011101'))
    sigs={deletion_delta(w,i) for i in range(len(w))}
    assert len(sigs)==14
print('explicit_family_verified_lengths','20..44')
