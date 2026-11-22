#!/usr/bin/env python3
"""Independently enumerate weighted 6^6 pair-count states of C12(1,5)."""
from collections import Counter
from math import factorial
PAIR_TYPES=((2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1))
ENC={q:i for i,q in enumerate(PAIR_TYPES)}
BASE=6
N=BASE**6
nextstate=[0]*N
weight=[0]*N
pows=[BASE**i for i in range(6)]
for s in range(N):
    t=s;qs=[];w=1
    for i in range(6):
        d=t%BASE;t//=BASE
        q=PAIR_TYPES[d];qs.append(q)
        w*=2//(factorial(q[0])*factorial(q[1])*factorial(q[2]))
    nxt=0
    for i,q in enumerate(qs):
        seen=qs[(i-1)%6][1]+qs[(i+1)%6][1]
        y=(q[2],q[0],q[1]) if seen>=2 else (q[0]+q[2],0,q[1])
        nxt+=pows[i]*ENC[y]
    nextstate[s]=nxt
    weight[s]=w
assert sum(weight)==3**12
known={}
for s in range(N):
    if s in known:continue
    route=[];positions={};u=s
    while u not in positions and u not in known:
        positions[u]=len(route);route.append(u);u=nextstate[u]
    if u in known:
        d,p=known[u]
    else:
        start=positions[u];p=len(route)-start;d=0
        for v in route[start:]:known[v]=(0,p)
        route=route[:start]
    for v in reversed(route):
        d+=1;known[v]=(d,p)
def transition(x):
    new=[]
    for i in range(6):
        exc=(x[2*((i-1)%6)]==1)+(x[2*((i-1)%6)+1]==1)+(x[2*((i+1)%6)]==1)+(x[2*((i+1)%6)+1]==1)
        for v in x[2*i:2*i+2]:
            new.append(2 if v==1 else 0 if v==2 else 1 if exc>=2 else 0)
    return tuple(new)

joint=Counter()
bridges=Counter()
for s in range(N):
    d,p=known[s]
    t=s; x=[]
    for i in range(6):
        a,b,c=PAIR_TYPES[t%BASE];t//=BASE
        x.extend([0]*a+[1]*b+[2]*c)
    x=tuple(x)
    for _ in range(d):x=transition(x)
    y=x
    for _ in range(p):y=transition(y)
    if y==x:P=p
    else:
        z=y
        for _ in range(p):z=transition(z)
        assert z==x
        P=2*p
    bridges[(p,P)]+=weight[s]
    joint[(d,P)]+=weight[s]
print('weighted total',sum(joint.values()))
print('quotient-to-labelled periods',sorted(bridges.items()))
print('weighted joint',sorted(joint.items()))
assert joint==Counter({(0,1):1,(0,3):6,(0,4):128,(0,6):12,(1,1):4095,(1,4):896,(1,6):756,(2,1):120103,(2,4):4736,(2,6):8448,(3,1):229514,(3,6):16356,(4,1):120152,(4,6):48,(5,1):17598,(6,1):8592})
print('PASS')
