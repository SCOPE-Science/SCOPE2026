#!/usr/bin/env python3
"""Verify cyclic marked-arc descriptions by a second direct bit simulator (stdlib only)."""
from itertools import combinations, product
from math import cos, pi
from collections import deque

def state_graph(n, marks):
    marks=tuple(marks); N=n+len(marks)
    nb=[[((v-1)%n),((v+1)%n)] for v in range(n)] + [[] for _ in marks]
    for i,v in enumerate(marks):
        nb[v].append(n+i);nb[n+i]=[v]
    return nb

def update(s,v,nb):
    val=(s>>v)&1
    same=sum(1 for w in nb[v] if ((s>>w)&1)==val)
    if same*2>=len(nb[v]):
        # Flip only if self-inclusive strict minority demands it:
        # 2*(same+1) > deg+1  => 2*same >= deg.
        return s^(1<<v)
    return s

def predicted(n,marks):
    marks=tuple(sorted(marks));k=len(marks)
    arcs=[(marks[(i+1)%k]-marks[i])%n or n for i in range(k)]
    classes=[]
    for mask in range(1<<k):
        ix=[i for i in range(k) if mask&(1<<i)]
        if len(ix)%2!=n%2 or (k>1 and any((i+1)%k in ix for i in ix)):continue
        for seed in [0,1]:
            cls=[]
            choices=[list(range(arcs[i])) if i in ix else [-1] for i in range(k)]
            for pos in product(*choices):
                bits=[None]*n
                b=seed
                for i,mark in enumerate(marks):
                    assert bits[mark] is None or bits[mark]==b
                    bits[mark]=b
                    for j in range(arcs[i]):
                        u=(mark+j)%n;w=(u+1)%n
                        # edge is same iff it carries a particle
                        b=b if j==pos[i] else 1-b
                        if bits[w] is None: bits[w]=b
                        else:assert bits[w]==b
                state=sum(c<<i for i,c in enumerate(bits))
                state+=sum((1-bits[v])<<(n+i) for i,v in enumerate(marks))
                cls.append(state)
            assert len(cls)==len(set(cls))
            classes.append(set(cls))
    return classes,arcs

def test():
    checks=0;states=0;edges=0
    for n in range(3,10):
        samples=[(0,),tuple(range(0,n,2)),tuple(range(n))]
        if n>=5:samples.extend([(0,2),(0,1,n-1)])
        if n>=7:samples.append((0,2,4,6))
        for marks in set(samples):
            nb=state_graph(n,marks)
            classes,arcs=predicted(n,marks)
            for C in classes:
                start=next(iter(C));seen={start};queue=deque([start])
                while queue:
                    x=queue.popleft()
                    for v in range(len(nb)):
                        y=update(x,v,nb)
                        assert y in C,(n,marks,x,v,y)
                        if y!=x:edges+=1
                        if y not in seen:
                            seen.add(y);queue.append(y)
                assert seen==C,(n,marks,len(seen),len(C))
                # All changes are reversible in the recurrent class.
                for x in C:
                    for v in range(len(nb)):
                        y=update(x,v,nb)
                        if y!=x:assert update(y,v,nb)==x
            assert len(set.union(*classes))==sum(map(len,classes))
            checks+=1;states+=sum(map(len,classes))
        print('n',n,'checks',checks,'recurrent states checked',states,flush=True)
    # Neumann path Laplacian formula: sum of elementary frequencies.
    for ell in range(1,21):
        u=[cos((j+0.5)*r*pi/ell) for j in range(ell) for r in []] # no work needed
        for r in range(ell):
            v=[cos((j+0.5)*r*pi/ell) for j in range(ell)]
            for j in range(ell):
                L=(v[j]-v[j-1] if j else 0)+(v[j]-v[j+1] if j+1<ell else 0)
                target=2*(1-cos(r*pi/ell))*v[j]
                assert abs(L-target)<1e-10
    print('PASS', checks, states,edges,'reflecting-path eigenvectors verified ell<=20')
if __name__=='__main__':test()
