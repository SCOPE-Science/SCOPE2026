#!/usr/bin/env python3
import itertools, math, json
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/'artifacts'/'certificate.json').read_text(encoding='utf-8'))

q=5
points=list(range(q))
# RS[5,2,4]: all affine linear functions a+b*x over F5.
code=[]
for a in range(q):
    for b in range(q):
        word=tuple((a+b*x)%q for x in points)
        code.append(word)

assert len(set(code))==25
nonzero=[w for w in code if any(w)]
weights=[sum(v!=0 for v in w) for w in nonzero]
assert min(weights)==4

support_words=defaultdict(list)
for w in nonzero:
    supp=tuple(i for i,v in enumerate(w) if v!=0)
    support_words[supp].append(w)

all4=set(itertools.combinations(range(5),4))
weight4_supports={S for S in support_words if len(S)==4}
assert weight4_supports==all4
assert all(len(support_words[S])==q-1 for S in all4)

r=3
for i in range(5):
    helpers=[j for j in range(5) if j!=i]
    Rs=list(itertools.combinations(helpers,r))
    assert len(Rs)==math.comb(4,3)==4
    for R in Rs:
        S=tuple(sorted((i,)+R))
        assert S in support_words

# General incidence formulas and exact matching number.
for n in range(2,21):
    for d in range(2,n+1):
        r=n-d+1
        N=math.comb(n-1,r)
        assert N==math.comb(n-1,d-2)
        for t in range(r+1):
            assert math.comb(n-1-t,r-t)>=1
        if n<=10:
            V=tuple(range(n-1))
            edges=list(itertools.combinations(V,r))
            target=(n-1)//r
            # Existence by a canonical block partition.
            chosen=[tuple(V[j*r:(j+1)*r]) for j in range(target)]
            assert all(len(E)==r for E in chosen)
            assert len(set().union(*map(set,chosen)))==target*r
            # Upper bound is cardinality; exhaustive search confirms for tiny cases.
            best=0
            def dfs(pos,used,count):
                nonlocal_best[0]=max(nonlocal_best[0],count)
                if count+(len(V)-len(used))//r<=nonlocal_best[0]:
                    return
                for idx in range(pos,len(edges)):
                    E=edges[idx]
                    if not any(x in used for x in E):
                        dfs(idx+1, used|set(E), count+1)
            nonlocal_best=[0]
            dfs(0,set(),0)
            assert nonlocal_best[0]==target

ex=CERT['example']
assert ex['r']==3 and ex['recovery_sets_per_coordinate']==4 and ex['max_pairwise_disjoint']==1
print('VERIFY_OK')
