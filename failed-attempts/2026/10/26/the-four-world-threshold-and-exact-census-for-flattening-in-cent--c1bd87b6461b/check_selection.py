#!/usr/bin/env python3
"""Complete four-world centered-functional selection-frame census."""
from itertools import product, permutations
N=4
W=range(N)
FULL=(1<<N)-1
options={}
for w in W:
    masks=[a for a in range(1,1<<N) if not (a>>w)&1]
    options[w]=[dict(zip(masks, vals)) for vals in product(*[tuple(v for v in W if a>>v&1) for a in masks])]
assert [len(options[w]) for w in W]==[24]*N

def choose(rows,w,a):
    if a==0:return None
    return w if (a>>w)&1 else rows[w][a]

def valid(rows,n=N):
    for w in range(n):
        for a in range(1,1<<n):
            for x in range(1,1<<n):
                if x&a != x:continue
                if choose(rows,choose(rows,w,a),x)!=choose(rows,w,x):
                    return False
    return True

allvalid=[]
for rows in product(*(options[w] for w in W)):
    if valid(rows):allvalid.append(rows)
assert len(allvalid)==138
orders={w:list(permutations(v for v in W if v!=w)) for w in W}
rankvalid=[]
for code in product(range(6),repeat=N):
    ranks=tuple(orders[w][code[w]] for w in W)
    if all(ranks[ranks[w][0]].index(ranks[w][1])<ranks[ranks[w][0]].index(ranks[w][2]) for w in W):
        rankvalid.append(ranks)
assert len(rankvalid)==138

def from_rows(rows):
    result=[]
    for w in W:
        v=rows[w][FULL^(1<<w)]
        a,b=(x for x in W if x!=w and x!=v)
        if rows[w][(1<<a)|(1<<b)]==a:result.append((v,a,b))
        else:result.append((v,b,a))
    return tuple(result)
assert set(map(from_rows,allvalid))==set(rankvalid)

perms=list(permutations(W))
def transformed(profile,p):
    return tuple(tuple(p[v] for v in profile[p.index(i)]) for i in W)
unseen=set(rankvalid)
orbits=[]
while unseen:
    profile=min(unseen)
    orbit={transformed(profile,p) for p in perms}
    assert orbit<=set(rankvalid)
    unseen-=orbit
    orbits.append(len(orbit))
assert sorted(orbits)==[6,12,24,24,24,24,24]

for n in (1,2,3):
    small={}
    for w in range(n):
        ms=[a for a in range(1,1<<n) if not a>>w&1]
        small[w]=[dict(zip(ms,vals)) for vals in product(*[tuple(v for v in range(n) if a>>v&1) for a in ms])]
    total=good=0
    for rows in product(*(small[w] for w in range(n))):
        total+=1
        if valid(rows,n):good+=1
    assert total==good
    assert total==[1,1,8][n-1]
print('CENTRED_SELECTION_FLATTENING_OK total=331776 valid=138 invalid=331638 orbits=7')
