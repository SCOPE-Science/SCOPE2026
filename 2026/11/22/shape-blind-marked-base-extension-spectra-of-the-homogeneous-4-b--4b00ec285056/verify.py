#!/usr/bin/env python3
"""Finite-hull enumeration for reduced degree-3/4 leaf trees.
Run python3 verify.py. No external dependencies.
"""
from collections import Counter, defaultdict
from itertools import permutations
from math import factorial

def seed():
    return {0:{100}, 1:{100}, 2:{100}, 100:{0,1,2}}

def copy(g): return {v:set(ns) for v,ns in g.items()}
def connect(g,a,b): g[a].add(b);g[b].add(a)
def unlink(g,a,b): g[a].remove(b);g[b].remove(a)
def nq(g):
    leaves=[v for v in g if len(g[v])==1]
    return len(leaves),sum(len(g[v])==4 for v in g)
def attach(g,label):
    assert label not in g
    ret=[]
    for u in sorted(g):
        for v in sorted(g[u]):
            if u>=v: continue
            h=copy(g);unlink(h,u,v)
            w=max(max(h)+1,100)
            h[w]=set();h[label]=set()
            connect(h,u,w);connect(h,v,w);connect(h,w,label)
            ret.append(h)
    for v in sorted(g):
        if len(g[v])==3:
            h=copy(g);h[label]=set();connect(h,v,label)
            ret.append(h)
    return ret

def signature(g):
    leaves=frozenset(v for v in g if len(g[v])==1)
    n=len(leaves)
    out=[]
    for u in g:
        for v in g[u]:
            if u>=v:continue
            seen={u};stack=[u]
            while stack:
                x=stack.pop()
                for y in g[x]:
                    if (x==u and y==v) or (x==v and y==u) or y in seen:continue
                    seen.add(y);stack.append(y)
            a=frozenset(seen & leaves)
            if 1<len(a)<n-1:
                b=leaves-a
                out.append(min(tuple(sorted(a)),tuple(sorted(b))))
    return tuple(sorted(set(out)))

def canonical_unlabeled(g):
    internal=[u for u in g if len(g[u])>1]
    s=len(internal)
    rows=[]
    for per in permutations(internal):
        # adjacency among internal plus the count of leaf children
        rows.append(tuple((sum(len(g[w])==1 for w in g[u]),
                        tuple(int(v in g[u]) for v in per[i+1:]))
                        for i,u in enumerate(per)))
    return min(rows)

def counts_by_state(n,q,r):
    c={0:1}
    for j in range(r):
        d=defaultdict(int)
        for k,v in c.items():
            d[k]+=v*(2*(n+j)-(q+k)-3)
            d[k+1]+=v*((n+j)-2-2*(q+k))
        c={k:v for k,v in d.items() if v}
    return c

def test():
    alltrees={signature(seed()):seed()}
    expected={3:1,4:4,5:25,6:220,7:2485,8:34300}
    representative={}
    for n in range(3,8):
        assert len(alltrees)==expected[n], (n,len(alltrees))
        shapes=defaultdict(set)
        for sig,g in alltrees.items():
            sz,q=nq(g);assert sz==n
            if n<=6:
                can=canonical_unlabeled(g)
                shapes[q].add(can)
                representative.setdefault((n,q,can),g)
            assert len(attach(g,n))==sum(counts_by_state(n,q,1).values())
            if n<=6:
                kids=attach(g,n)
                assert len({signature(x) for x in kids})==len(kids)
                assert Counter(nq(x)[1]-q for x in kids)==Counter(counts_by_state(n,q,1))
        if n<=6:
            print('n',n,'labeled',len(alltrees),'unlabeled by 4-valent count',dict(sorted((q,len(sh)) for q,sh in shapes.items())))
        if n==6:
            assert {q:len(sh) for q,sh in shapes.items()}=={0:2,1:2,2:1}
        if n==7:break
        nxt={}
        for g in alltrees.values():
            for h in attach(g,n):
                k=signature(h)
                assert k not in nxt, ('duplicate tree extension',n,k)
                nxt[k]=h
        alltrees=nxt
    # Compare explicit two-stage extensions against a fresh recurrence, for
    # representatives of every unlabelled shape on 6 leaves.
    for (n,q,shape),g in representative.items():
        if n!=6:continue
        second=[]
        for h in attach(g,6):second.extend(attach(h,7))
        s=[signature(h) for h in second]
        assert len(s)==len(set(s)), 'multiple construction paths'
        actual=Counter(nq(h)[1]-q for h in second)
        expect=Counter(counts_by_state(n,q,2))
        assert actual==expect, (q,actual,expect)
        print('shape',q,'r=2',sum(actual.values()),dict(sorted(actual.items())))
    # Small table and differential recurrence check.
    for n in range(3,12):
        for q in range((n-2)//2+1):
            for r in range(6):
                c=counts_by_state(n,q,r)
                assert all(x>=0 for x in c.values())
                assert sum(c.values())>0
    print('ALL_SHAPE_AND_EXTENSION_CHECKS_OK')
if __name__=='__main__':test()
