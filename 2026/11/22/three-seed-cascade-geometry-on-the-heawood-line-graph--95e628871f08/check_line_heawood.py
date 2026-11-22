#!/usr/bin/env python3
"""Exact independent three-seed census for the Fano-incidence line graph."""
from itertools import combinations
from collections import Counter

# A different Fano-plane model: nonzero vectors of F_2^3 and line kernels.
def parity(x): return x.bit_count() % 2
flags = [(point,normal) for point in range(1,8)
         for normal in range(1,8) if parity(point & normal)==0]
assert len(flags)==21
adj = [sum(1<<j for j,f in enumerate(flags)
           if i!=j and (e[0]==f[0] or e[1]==f[1]))
       for i,e in enumerate(flags)]
assert all(a.bit_count()==4 for a in adj)
FULL=(1<<21)-1

def spread(seed):
    active=seed
    rounds=0
    while True:
        additions=0
        for i,near in enumerate(adj):
            if ((active>>i)&1)==0 and (near&active).bit_count()>=2:
                additions|=1<<i
        if not additions: return active==FULL,rounds
        active|=additions
        rounds+=1

def motif(indices):
    chosen=[flags[i] for i in indices]
    if any(a[0]==b[0] or a[1]==b[1] for a,b in combinations(chosen,2)):
        return 'nonmatching'
    cross=[]
    for i,j in combinations(range(3),2):
        a,A=chosen[i]; b,B=chosen[j]
        if parity(a&B)==0: cross.append((i,j,('point',a),('line',B)))
        if parity(b&A)==0: cross.append((i,j,('line',A),('point',b)))
    n=len(cross)
    if n==0:return 'zero_cross'
    if n==1:return 'one_cross'
    if n==3:return 'triangle_cross'
    assert n==2
    center=list(set(cross[0][:2])&set(cross[1][:2]))
    assert len(center)==1
    c=center[0]
    def endpoint(t):
        return t[2] if ((t[2][0]=='point' and chosen[c][0]==t[2][1]) or (t[2][0]=='line' and chosen[c][1]==t[2][1])) else t[3]
    return 'path_shared_end' if endpoint(cross[0])==endpoint(cross[1]) else 'path_opposite_ends'

c=Counter()
for ids in combinations(range(21),3):
    name=motif(ids)
    success,t=spread(sum(1<<i for i in ids))
    c[(name, t if success else 'blocked')]+=1
expected={('nonmatching','blocked'):686,
          ('zero_cross','blocked'):84,
          ('one_cross',6):168,
          ('triangle_cross',4):56,
          ('path_shared_end','blocked'):168,
          ('path_opposite_ends',5):168}
assert dict(c)==expected,(c,expected)
assert sum(v for (name,t),v in c.items() if t!='blocked')==392
print('PASS: independent algebraic model, 1330 triples, six motif classes:')
for key in sorted(c): print(key,c[key])
