#!/usr/bin/env python3
"""Independent graph-shape checks: evaluate full functional trajectories on cacti.
No use of data produced by other checks; compares exact product formula on its own.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb

def poly(n):
    d={0:1}
    for _ in range(n):
        z={}
        for k,v in d.items():
            for h in (-1,0,1):z[k+h]=z.get(k+h,0)+v
        d=z
    return d

def expected(lengths,b):
    hist={Fraction(0):3**(b+1)}
    for l in lengths:
        nxt={}
        for score,c in hist.items():
            for t,k in poly(l).items():
                if t%3:continue
                a=max(score,Fraction(abs(t),l))
                nxt[a]=nxt.get(a,0)+c*k
        hist=nxt
    return hist

def graph(edges):
    n=1+max(max(e) for e in edges)
    adj=[[] for _ in range(n)]
    for u,v in edges:
        assert v not in adj[u]
        adj[u].append(v);adj[v].append(u)
    return adj

def step(x,g,model):
    y=[]
    for i,a in enumerate(x):
        if model=='CCA':y.append((a+int((a+1)%3 in [x[j] for j in g[i]]))%3)
        elif a==0:y.append(int(any(x[j]==1 for j in g[i])))
        else:y.append((a+1)%3)
    return tuple(y)

def activity(state,g,model):
    path=[]; seen={}
    while state not in seen:
        assert len(path)<100
        seen[state]=len(path)
        path.append(state)
        state=step(state,g,model)
    j=seen[state];cycle=path[j:]
    changes=0
    for i,x in enumerate(cycle):
        y=cycle[(i+1)%len(cycle)]
        changes+=((y[0]-x[0])%3==1) if model=='CCA' else (x[0]==0 and y[0]==1)
    return Fraction(changes,len(cycle))*(3 if model=='GHM' else 1)

def main():
    cases=[
      ('two triangles joined by bridge',[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,3)],[3,3],1),
      ('chain of three triangles',[(0,1),(1,2),(2,0),(2,3),(3,4),(4,2),(4,5),(5,6),(6,4)],[3,3,3],0),
      ('triangle and square with pendant edge',[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,2),(1,6)],[3,4],1),
    ]
    for label,edges,lengths,b in cases:
        g=graph(edges)
        target=expected(lengths,b)
        for model in ('CCA','GHM'):
            actual=Counter(activity(x,g,model) for x in product(range(3),repeat=len(g)))
            assert actual==target,(label,model,actual,target)
        print('PASS',label,'states_per_model',3**len(g),'activity_counts',','.join(f'{k}:{v}' for k,v in sorted(target.items())))
    print('ALL_NONBOUQUET_CACTUS_CHECKS_PASS')

if __name__=='__main__':main()
