#!/usr/bin/env python3
"""Graph-geometry independent census; Python standard library only."""
from itertools import combinations, product

def graphs():
    outer=[('o',i) for i in range(5)]
    inner=[('i',i) for i in range(5)]
    prism=outer+inner
    pairs=list(combinations(range(5),2))
    return (("prism",prism,lambda u,v: (u[0]==v[0] and (u[1]-v[1])%5 in (1,4)) or (u[0]!=v[0] and u[1]==v[1])),
            ("Petersen",pairs,lambda u,v: len(set(u)&set(v))==0))

expected_seed={'prism':(0,0,0,640,1240,1040,400,60,0,0,0), 'Petersen':(0,0,0,0,420,720,320,60,0,0,0)}
expected={'prism':(1,1023,25415,29230,3380),'Petersen':(1,1023,25205,31300,1520)}
for name,vertices,edge in graphs():
    adj=tuple(tuple(j for j in range(10) if i!=j and edge(u,vertices[j])) for i,u in enumerate(vertices))
    assert all(len(a)==3 for a in adj)
    hist=[0]*5;seed=[0]*11
    for initial in product((0,1,2),repeat=10):
        x=initial
        entry=None
        for t in range(5):
            if not any(x) and entry is None:
                entry=t
            if t<4:
                x=tuple(2 if x[i]==1 else 0 if x[i]==2 else int(sum(x[j]==1 for j in adj[i])>=2) for i in range(10))
        assert x==(0,)*10
        hist[entry]+=1
        if entry==4:seed[initial.count(1)]+=1
    assert tuple(hist)==expected[name]
    assert tuple(seed)==expected_seed[name]
    print(name,'first-hit',hist,'last-wave by initially excited sites',seed)
print('PASS independent graph constructions and 118098 complete trajectories')
