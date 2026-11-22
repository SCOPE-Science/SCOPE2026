"""Exact finite tests for capacity-constrained single-item recolouring.

A state is an n-tuple of named colours; each colour can occur at most q times.
The tests are independent of the article's asymptotic or spectral background.
"""
from collections import deque, Counter, defaultdict
from itertools import product
import random


def legal(a,q):
    return max(Counter(a).values(), default=0) <= q


def lower_witness(n,q,k):
    t,rem=divmod(n,2*q)
    a=[];b=[]
    for j in range(t):
        x,y=2*j,2*j+1
        a.extend([x]*q+[y]*q)
        b.extend([y]*q+[x]*q)
    if rem==1:
        a.append(2*t)
        b.append(2*t+1)
    if rem>=2:
        a.extend(range(2*t,2*t+rem))
        b.extend(2*t+(j+1)%rem for j in range(rem))
    assert len(a)==n and len(b)==n and all(x!=y for x,y in zip(a,b))
    assert max(a+b,default=-1)<k and legal(a,q) and legal(b,q)
    return tuple(a),tuple(b)


def strongly_connected_components(vertices,edges):
    out=defaultdict(list);rev=defaultdict(list)
    for s,t,_ in edges:
        out[s].append(t);rev[t].append(s)
    used=set();order=[]
    def dfs(v):
        used.add(v)
        for w in out[v]:
            if w not in used:dfs(w)
        order.append(v)
    for v in vertices:
        if v not in used:dfs(v)
    used.clear();cs=[]
    def backward(v,res):
        used.add(v);res.add(v)
        for w in rev[v]:
            if w not in used:backward(w,res)
    for v in reversed(order):
        if v not in used:
            component=set();backward(v,component);cs.append(component)
    return cs


def route(initial,target,q,k):
    n=len(initial);now=list(initial);target=tuple(target)
    assert legal(now,q) and legal(target,q) and max(initial+target,default=-1)<k
    states=[tuple(now)]
    def move(i,c):
        assert now[i]!=c
        assert now.count(c)<q
        now[i]=c
        assert legal(now,q)
        states.append(tuple(now))
    while tuple(now)!=target:
        movable=next((i for i in range(n) if now[i]!=target[i] and now.count(target[i])<q),None)
        if movable is not None:
            move(movable,target[movable]);continue
        edges=[(now[i],target[i],i) for i in range(n) if now[i]!=target[i]]
        vertices={s for s,t,i in edges}|{t for s,t,i in edges}
        cs=strongly_connected_components(vertices,edges)
        # No directly recolourable vertex: some sink SCC is a closed Eulerian piece.
        selected=None
        for C in cs:
            if len(C)>=2 and not any(s in C and t not in C for s,t,i in edges):
                assert not any(s not in C and t in C for s,t,i in edges)
                selected=C;break
        assert selected is not None,('no SCC',now,target,edges)
        sub=[(s,t,i) for s,t,i in edges if s in selected]
        adj=defaultdict(list)
        for e in sub:adj[e[0]].append(e)
        # Hierholzer's algorithm returns a directed closed Euler tour.
        start=sub[0][0];verts=[start];arcstack=[];tour=[]
        while verts:
            v=verts[-1]
            if adj[v]:
                e=adj[v].pop();verts.append(e[1]);arcstack.append(e)
            else:
                verts.pop()
                if arcstack:tour.append(arcstack.pop())
        tour=tour[::-1]
        assert len(tour)==len(sub) and tour[0][0]==tour[-1][1]
        assert all(tour[j][1]==tour[j+1][0] for j in range(len(tour)-1))
        spare=next(c for c in range(k) if c not in now)
        first=tour[0]
        move(first[2],spare)
        for s,t,i in tour[:0:-1]:move(i,t)
        move(first[2],first[1])
        assert all(now[i]==target[i] for i in range(n) if target[i] in selected)
    assert len(states)-1<=n+n//(2*q)
    return states


def brute_diam(n,q,k):
    states=[x for x in product(range(k),repeat=n) if legal(x,q)]
    ix={a:i for i,a in enumerate(states)}
    # Permuting vertices and colour labels preserves distances. Starting states
    # are classified by the partition of n into nonzero colour-class sizes.
    patterns={}
    for a in states:
        pat=tuple(sorted(Counter(a).values()))
        patterns.setdefault(pat,a)
    dia=0
    for a in patterns.values():
        dst=[-1]*len(states);dst[ix[a]]=0;queue=deque([ix[a]])
        while queue:
            j=queue.popleft();v=states[j];d=dst[j]
            counts=Counter(v)
            for i in range(n):
                for c in range(k):
                    if c==v[i] or counts[c]>=q:continue
                    w=v[:i]+(c,)+v[i+1:];index=ix[w]
                    if dst[index]<0:dst[index]=d+1;queue.append(index)
        assert min(dst)>=0,('disconnected',n,q,k,a)
        dia=max(dia,max(dst))
    assert dia==n+n//(2*q),(n,q,k,dia,n+n//(2*q))
    return len(states),len(patterns),dia


def main():
    checked=0;work=0
    for n in range(1,7):
        for q in range(1,4):
            k=n+1
            if (n,q) in ((6,3),):continue
            size,patterns,dia=brute_diam(n,q,k)
            checked+=1;work+=size*patterns
    print('EXACT_ORBIT_REDUCED_ALL_PAIR_BFS_PASS cases=',checked,'source_state_pairs=',work)
    rng=random.Random(526091)
    cases=0;steps=0
    for q in range(1,6):
        for n in range(1,16):
            k=n+1
            a,b=lower_witness(n,q,k)
            path=route(a,b,q,k)
            assert len(path)-1==n+n//(2*q)
            for _ in range(20):
                a=tuple(rng.randrange(k) for _ in range(n))
                b=tuple(rng.randrange(k) for _ in range(n))
                if not legal(a,q) or not legal(b,q):continue
                states=route(a,b,q,k)
                assert states[0]==a and states[-1]==b
                assert all(sum(x!=y for x,y in zip(s,t))==1 for s,t in zip(states,states[1:]))
                cases+=1;steps+=len(states)-1
    print('CONSTRUCTIVE_ROUTING_AND_SHARP_WITNESS_PASS cases=',cases,'path_steps=',steps)
    print('VERIFY_OK')

if __name__=='__main__': main()
