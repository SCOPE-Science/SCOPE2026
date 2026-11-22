#!/usr/bin/env python3
"""Exact independent small-case verifier for rooted-tree poset type-depth claim.

Canonical unlabelled rooted trees use sorted multisets of child trees.  All
one-point extension signatures are independently enumerated as (L,U) subsets.
"""
from functools import lru_cache
from itertools import combinations
from collections import defaultdict, Counter

@lru_cache(None)
def nodes(t):
    return 1 + sum(nodes(c) for c in t)

@lru_cache(None)
def trees(n):
    if n==1: return ((),)
    palette = [t for k in range(1,n) for t in trees(k)]
    out=[]
    def rec(left,start,selected):
        if left==0:
            out.append(tuple(selected))
            return
        for j in range(start,len(palette)):
            t=palette[j]
            if nodes(t)>left:break
            rec(left-nodes(t),j,selected+[t])
    rec(n-1,0,[])
    return tuple(out)

def poly_mul(a,b):
    out=defaultdict(int)
    for i,x in a.items():
        for j,y in b.items():out[i+j]+=x*y
    return dict(out)

@lru_cache(None)
def ideals(t):
    product={0:1}
    for c in t:product=poly_mul(product,ideals(c))
    return {0:1, **{k+1:v for k,v in product.items()}}

def flatten(t):
    parents=[]; depths=[]
    def walk(u,par,d):
        i=len(parents);parents.append(par);depths.append(d)
        for ch in u:walk(ch,i,d+1)
    walk(t,-1,0)
    return parents,depths

def direct_types(t):
    p,depths=flatten(t);n=len(p)
    ancestor=[]
    for i in range(n):
        cur=p[i];mask=0
        while cur!=-1:
            mask|=1<<cur;cur=p[cur]
        ancestor.append(mask)
    descendant=[0]*n
    for i in range(n):
        for j in range(n):
            if ancestor[j]>>i &1:descendant[i]|=1<<j
    poly=defaultdict(int)
    for L in range(1<<n):
        if any((L>>i &1) and (ancestor[i] &L)!=ancestor[i] for i in range(n)):
            continue
        for U in range(1<<n):
            if any((U>>i &1) and (descendant[i]&U)!=descendant[i] for i in range(n)):
                continue
            if L&U:continue
            if any((L>>i&1) and (U &~descendant[i]) for i in range(n)):
                continue
            poly[L.bit_count(),U.bit_count()]+=1
    return dict(poly)

def leaves_depth(t):
    p,d=flatten(t)
    nonleaves=set(x for x in p if x>=0)
    return Counter(d[i] for i in range(len(p)) if i not in nonleaves)

def main():
    counts=[];collisions=[];direct_checks=0
    for n in range(1,8):
        shapes=trees(n);counts.append(len(shapes))
        seen={}
        for t in shapes:
            key=tuple(sorted(ideals(t).items()))
            if key in seen:collisions.append((n,seen[key],t,key))
            else:seen[key]=t
            B=direct_types(t)
            assert {k:v for k,v in B.items() if k[1]==0}=={(i,0):v for i,v in ideals(t).items()}
            leaf=leaves_depth(t)
            for d in range(n+1):
                expected=sum(v for depth,v in leaf.items() if depth>=d)
                assert B.get((d,1),0)==expected,(t,d,expected,B.get((d,1),0))
            direct_checks+=1
    assert counts==[1,1,2,4,9,20,48],counts
    assert len(collisions)==1 and collisions[0][0]==7,collisions
    _,x,y,key=collisions[0]
    expected={0:1,1:1,2:2,3:3,4:4,5:4,6:3,7:1}
    assert dict(key)==expected
    assert x==((),((),(((),),)))
    assert y==(((),),(((),()),))
    assert leaves_depth(x)==Counter({1:1,2:1,4:1})
    assert leaves_depth(y)==Counter({2:1,3:2})
    assert direct_types(x).get((2,1))==2
    assert direct_types(y).get((2,1))==3
    print('PASS canonical rooted-tree counts at sizes 1..7:',counts)
    print('PASS independent ideal/upset extension-diagram enumerations:',direct_checks)
    print('PASS all leaf-depth extraction identities at all sizes 1..7')
    print('PASS unique first collision at seven rooted vertices')
    print('PASS common ideal polynomial: 1 + z + 2z² + 3z³ + 4z⁴ + 4z⁵ + 3z⁶ + z⁷')
    print('PASS witness A leaf depths {1,2,4}, witness B {2,3,3}')
    print('PASS mixed coefficient [u²v] is 2 versus 3')
    print('Finite checks establish the finite cutoff, not the infinite reconstruction identity.')

if __name__=='__main__':main()
