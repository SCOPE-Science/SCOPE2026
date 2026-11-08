"""Exact one-letter modal partition calculation over all finite complete multipartite graphs.
Requires only Python 3 standard library. Run: python3 abstract_checker.py.
"""
from itertools import product

CATEGORIES=('Z','O','M')
TRUTH={'Z':(0,),'O':(1,),'M':(0,1)}
states=[]
for counts in product(range(3),repeat=3):
    if sum(counts)<2: continue
    for j,category in enumerate(CATEGORIES):
        if counts[j]:
            for bit in TRUTH[category]:states.append((counts,category,bit))
states.sort()
index={s:i for i,s in enumerate(states)}
assert len(states)==68
edges=[]
for counts,own,bit in states:
    successors=set()
    for j,cat in enumerate(CATEGORIES):
        if counts[j]-(cat==own)>0:
            for value in TRUTH[cat]:successors.add(index[(counts,cat,value)])
    assert successors
    edges.append(tuple(sorted(successors)))

def compact(keys):
    lookup={k:i for i,k in enumerate(sorted(set(keys)))}
    return tuple(lookup[k] for k in keys)

def refine(labels,operator):
    keys=[]
    for i,old in enumerate(labels):
        support=tuple(sorted({labels[j] for j in edges[i]}))
        observation=support if operator=='box' or len(support)>1 else ()
        keys.append((old,observation))
    return compact(keys)

for op,target in [('delta',[2,4,10,10]),('box',[2,6,16,22,22])]:
    labels=compact([s[2] for s in states]); observed=[len(set(labels))]
    for depth in range(len(target)-1):
        new=refine(labels,op)
        observed.append(len(set(new)))
        labels=new
    assert observed==target,(op,observed,target)
    assert refine(labels,op)==labels,(op,'unstable')
    print(op,'pointed types by depth',observed,'formula classes',[2**x for x in observed])
print('PASS: 68 realizable abstract states, all successor supports, both sharp stable profiles')
