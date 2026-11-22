#!/usr/bin/env python3
"""Verify the exceptional class's 56-, 576- and 288-object orbit structures."""
import re
from collections import Counter
from pathlib import Path

def cycles(p):
    seen=set(); out=Counter()
    assert sorted(p)==list(range(len(p)))
    for i in range(len(p)):
        if i not in seen:
            j=i; length=0
            while j not in seen:
                seen.add(j); length+=1; j=p[j]
            assert j==i
            out[length]+=1
    return dict(sorted(out.items()))

generated=Path('markings.txt').read_text().splitlines()
assert len(generated)==583
marks=[tuple(map(int,x.split())) for x in generated[7:]]
assert len(marks)==576 and all(len(x)==7 for x in marks)
loc={x:i for i,x in enumerate(marks)}
assert len(loc)==576
lines=Path('census.out').read_text().splitlines()
cls=[l for l in lines if re.search(r'\bmin=18\b',l)]
assert len(cls)==1
m=re.search(r'permutation=([0-9,]+)\s+cycle_lengths=',cls[0]);assert m
p=list(map(int,m.group(1).strip(',').split(',')))
assert cycles(p)=={2:1,18:3}
perm=[loc[tuple(sorted(p[k] for k in s))] for s in marks]
assert cycles(perm)=={18:32}
# Geiser of exceptional curves in the exact basis/order used by generation:
K=(-3,)+(1,)*7
C=[]
from itertools import combinations
for i in range(7):
    a=[0]*8;a[i+1]=1;C.append(tuple(a))
for i,j in combinations(range(7),2):
    a=[1]+[0]*7;a[i+1]=a[j+1]=-1;C.append(tuple(a))
for I in combinations(range(7),5):
    a=[2]+[0]*7
    for i in I:a[i+1]=-1
    C.append(tuple(a))
for i in range(7):
    a=[3]+[-1]*7;a[i+1]=-2;C.append(tuple(a))
idx={a:i for i,a in enumerate(C)}
geiser=[idx[tuple(-K[k]-a[k] for k in range(8))] for a in C]
mate=[loc[tuple(sorted(geiser[j] for j in s))] for s in marks]
assert all(mate[i]!=i and mate[mate[i]]==i for i in range(576))
assert all(mate[perm[i]]==perm[mate[i]] for i in range(576))
quot={tuple(sorted([i,mate[i]])) for i in range(576)}
assert len(quot)==288
QL=sorted(quot);qidx={x:i for i,x in enumerate(QL)}
qp=[qidx[tuple(sorted([perm[i],perm[j]]))] for i,j in QL]
assert cycles(qp)=={9:32}
print('56 exceptional-curve cycle lengths:',cycles(p))
print('576 contraction-set cycle lengths:',cycles(perm))
print('288 Aronhold-heptad cycle lengths:',cycles(qp))
print('Geiser pairs:',len(quot),'and commutes with representative')
