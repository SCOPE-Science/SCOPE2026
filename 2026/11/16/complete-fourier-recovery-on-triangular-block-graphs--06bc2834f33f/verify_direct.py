#!/usr/bin/env python3
"""Exact cyclic-character Fourier check on two nonisomorphic triangular cacti.
All arithmetic uses integer residue histograms, no floating-point comparison."""
from itertools import product
from collections import Counter

def edges_for_blocks(blocks):
    e=set()
    for block in blocks:
        for i in range(len(block)):
            for j in range(i):e.add(tuple(sorted((block[i],block[j]))))
    n=max(v for b in blocks for v in b)+1
    return n,sorted(e)

def attach(blocks):
    seen={0}; out=[]
    rest=list(blocks)
    while rest:
        candidates=[(i,b) for i,b in enumerate(rest) if len(set(b)&seen)==1]
        assert candidates, (blocks,rest,seen)
        i,b=candidates[0]
        a=next(iter(set(b)&seen)); new=[v for v in b if v!=a]
        out.append((len(b),a,new));seen.update(new);rest.pop(i)
    return out

def predicted(freq,q,blocks):
    n=max(v for b in blocks for v in b)+1
    if sum(freq)%q:return 0
    child=[[] for _ in range(n)]
    for kind,parent,new in attach(blocks):
        for v in new:child[parent].append(v)
    eta=[None]*n
    def visit(v):
        for u in child[v]:visit(u)
        eta[v]=(freq[v]+sum(eta[u] for u in child[v]))%q
    visit(0)
    def S(k):return q-1 if k%q==0 else -1
    z=q
    for kind,parent,new in attach(blocks):
        if kind==2:z*=S(eta[new[0]])
        else:z*=S(eta[new[0]])*S(eta[new[1]])-S(eta[new[0]]+eta[new[1]])
    return z

def cycle_int(hist,q):
    if q==3:
        assert hist[1]==hist[2]
        return hist[0]-hist[1]
    if q==4:
        assert hist[1]==hist[3]
        return hist[0]-hist[2]
    if q==5:
        assert len(set(hist[1:]))==1
        return hist[0]-hist[1]
    raise ValueError(q)

def run(q,blocks):
    n,edges=edges_for_blocks(blocks)
    good=[c for c in product(range(q),repeat=n) if all(c[i]!=c[j] for i,j in edges)]
    assert len(good)==q*(q-1)**sum(len(b)==2 for b in blocks)*((q-1)*(q-2))**sum(len(b)==3 for b in blocks)
    cf=Counter()
    for xi in product(range(q),repeat=n):
        hist=[0]*q
        for c in good:
            hist[sum(a*b for a,b in zip(xi,c))%q]+=1
        v=cycle_int(hist,q)
        p=predicted(xi,q,blocks)
        assert v==p,(q,blocks,xi,v,p,hist)
        cf[v]+=1
    e=sum(len(b)==2 for b in blocks);t=sum(len(b)==3 for b in blocks)
    assert sum(m for val,m in cf.items() if val!=0)==q**(n-1)
    print('PASS',{'q':q,'n':n,'edges':e,'triangles':t,'proper':len(good),'balanced_rank':q**(n-1),'distinct_multipliers':len(cf)})

if __name__=='__main__':
    cases=[(3,[(0,1,2),(0,3,4)]),(4,[(0,1,2),(0,3,4)]),
           (3,[(0,1,2),(2,3,4),(4,5)]),
           (3,[(0,1,2),(2,5),(5,3,4)]),
           (4,[(0,1,2),(2,3)]),
           (5,[(0,1,2)]),
           (5,[(0,1,2),(0,3,4)]),
           (4,[(0,1),(1,2),(1,3)])]
    for c in cases:run(*c)
