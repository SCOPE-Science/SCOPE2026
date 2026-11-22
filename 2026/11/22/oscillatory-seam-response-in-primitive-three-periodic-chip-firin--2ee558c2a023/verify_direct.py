#!/usr/bin/env python3
"""Independent graph-level checks of primitive period-three chip-firing states."""
from itertools import product

def graph(n,twist):
    ed=set()
    for j in range(n):
        a=2*j;b=a+1
        ed.add(tuple(sorted((a,b))))
        if j+1<n:
            ed.add((a,2*j+2))
            ed.add((b,2*j+3))
        elif twist:
            ed.add(tuple(sorted((a,1))))
            ed.add(tuple(sorted((b,0))))
        else:
            ed.add(tuple(sorted((a,0))))
            ed.add(tuple(sorted((b,1))))
    nb=[set() for _ in range(2*n)]
    for a,b in ed:
        nb[a].add(b)
        nb[b].add(a)
    assert all(len(x)==3 for x in nb)
    return [sorted(x) for x in nb]

def phase_sum(nb):
    m=len(nb);total=0
    for phase in product(range(3),repeat=m):
        ways=1
        for i in range(m):
            ways*=sum(phase[j]==(phase[i]-1)%3 for j in nb[i])
            if ways==0:break
        total+=ways
    return total

def update(x,nb):
    fires=[int(t>=3) for t in x]
    return tuple(x[i]-3*fires[i]+sum(fires[j] for j in nb[i]) for i in range(len(x)))

def count_states(nb):
    m=len(nb);count=0
    for x in product(range(6),repeat=m):
        y=update(x,nb)
        if y==x:continue
        z=update(update(y,nb),nb)
        if z==x:count+=1
    return count

expected={3:((246,36),(164,24)),4:((792,192),(528,128)),
          5:((1530,4650),(1020,3100))}
for n in (3,4,5):
    for twist in (False,True):
        nb=graph(n,twist)
        z=phase_sum(nb)
        i=int(twist)
        assert z==expected[n][0][i]
        assert 2*z//3==expected[n][1][i]
        if n==3:
            states=count_states(nb)
            assert states==2*z
        print('n',n,'twist',twist,'phase_weight',z,'orbits',2*z//3)
print('INDEPENDENT_GRAPH_AND_CHIP_STATE_CHECKS_PASSED')
