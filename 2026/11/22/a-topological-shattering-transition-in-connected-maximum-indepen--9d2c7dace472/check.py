#!/usr/bin/env python3
"""Independent exhaustive verification of the extremal connected-clique shattering theorem.
Run: python3 check.py
"""
import itertools, collections
from functools import lru_cache

def graph_and_concepts(sizes):
    a=len(sizes)
    blocks=[]; idx=0
    for r in sizes:
        blocks.append(list(range(idx,idx+r))); idx+=r
    x=blocks[0][0]; connectors={i:blocks[i][0] for i in range(1,a)}
    edges=set()
    for B in blocks:
        edges.update(tuple(sorted(p)) for p in itertools.combinations(B,2))
    edges.update(tuple(sorted((x,y))) for y in connectors.values())
    concepts=[]
    for tup in itertools.product(*blocks):
        if x in tup and any(y in tup for y in connectors.values()): continue
        concepts.append(sum(1<<u for u in tup))
    # Cross-check the transversal enumeration against all independent vertex subsets.
    exhaustive=[]
    for mask in range(1<<idx):
        if all(not((mask>>u&1) and (mask>>v&1)) for u,v in edges):
            exhaustive.append(mask)
    alpha=max(s.bit_count() for s in exhaustive)
    assert alpha==a,(sizes,alpha)
    maximum={s for s in exhaustive if s.bit_count()==a}
    assert maximum==set(concepts),(sizes,len(maximum),len(concepts))
    return idx,blocks,edges,tuple(concepts)

def shattered(S,concepts):
    bits=tuple(u for u in range(S.bit_length()) if S>>u&1)
    masks={sum(1<<j for j,u in enumerate(bits) if c>>u&1) for c in concepts}
    return len(masks)==(1<<len(bits))

def predicted(S,blocks):
    if any((S & sum(1<<v for v in B)).bit_count()>1 for B in blocks): return False
    x=blocks[0][0];r0=len(blocks[0]);
    if r0==2:
        if (S&(1<<x)) or (S&(1<<blocks[0][1])):
            return S.bit_count()==1
        return True
    if S>>x&1:
        for i,B in enumerate(blocks[1:],1):
            if S>>B[0]&1: return False
            if len(B)==2 and S&sum(1<<v for v in B):return False
    return True

def predicted_poly(sizes):
    p=[1]
    def mul(p,q):
        o=[0]*(len(p)+len(q)-1)
        for i,a in enumerate(p):
            for j,b in enumerate(q):o[i+j]+=a*b
        return o
    r0=sizes[0]
    if r0==2:
        p=[1]
        for r in sizes[1:]:p=mul(p,[1,r])
        p[1]+=2
        return p
    p=[1,r0-1]
    for r in sizes[1:]:p=mul(p,[1,r])
    b=[0,1]
    for r in sizes[1:]:
        if r>=3:b=mul(b,[1,r-1])
    p += [0]*max(0,len(b)-len(p))
    for i,x in enumerate(b):p[i]+=x
    return p

def littlestone(concepts,n):
    @lru_cache(None)
    def f(v):
        if len(v)<=1:return 0
        best=0
        for u in range(n):
            z=tuple(c for c in v if not(c>>u&1))
            o=tuple(c for c in v if (c>>u&1))
            if z and o:best=max(best,1+min(f(z),f(o)))
        return best
    return f(tuple(sorted(concepts)))

def betti_mod2(faces,n):
    # Compute simplicial boundary ranks over GF(2) using integer XOR elimination
    by_dim=collections.defaultdict(list)
    for S in faces:by_dim[S.bit_count()-1].append(S)
    dims=range(0,max(by_dim)+1)
    ranks={}
    for d in dims:
        if d==0: ranks[d]=0;continue
        rows={x:i for i,x in enumerate(by_dim[d-1])}
        pivots={};rank=0
        for S in by_dim[d]:
            v=0
            for u in range(n):
                if S>>u&1: v ^= 1<<rows[S^(1<<u)]
            while v:
                pivot=v.bit_length()-1
                if pivot in pivots:v^=pivots[pivot]
                else:
                    pivots[pivot]=v;rank+=1;break
        ranks[d]=rank
    bettis={d:len(by_dim[d])-ranks[d]-ranks.get(d+1,0) for d in dims}
    bettis[0]-=1
    return {k:v for k,v in bettis.items() if v}

def predicted_betti(sizes):
    a=len(sizes);r0=sizes[0]
    if r0==2: return {0:2,a-2:1} if a>2 else {0:3}
    high=1
    for r in sizes[1:]:high*=r-1
    high*=r0-2
    large=[r for r in sizes[1:] if r>=3]
    if len(large):
        low=1
        for r in large:low*=r-2
        if len(large)==a-1:high+=low
        else:return {a-1:high,len(large):low}
    else:return {a-1:high,0:1}
    return {a-1:high}

def run(sizes,with_betti=False):
    n,blocks,edges,concepts=graph_and_concepts(sizes)
    assert all(c.bit_count()==len(sizes) for c in concepts)
    assert all(all(not(c>>u&1 and c>>v&1) for u,v in edges) for c in concepts)
    # exhaustive all supports; no sampling
    faces=[]; coefficients=collections.Counter()
    for S in range(1<<n):
        actual=shattered(S,concepts)
        expect=predicted(S,blocks)
        assert actual==expect, (sizes,S,actual,expect)
        if actual:faces.append(S);coefficients[S.bit_count()]+=1
    poly=[coefficients[i] for i in range(len(predicted_poly(sizes)))]
    assert poly==predicted_poly(sizes), (sizes,poly,predicted_poly(sizes))
    L=littlestone(concepts,n)
    assert L==(len(sizes)-1 if sizes[0]==2 else len(sizes)), (sizes,L)
    msg={'sizes':sizes,'n':n,'concepts':len(concepts),'shattered_polynomial':poly,'VC':max(i for i,c in enumerate(poly) if c),'Littlestone':L}
    if with_betti:
        b=betti_mod2(faces,n);be=predicted_betti(sizes)
        assert b==be, (sizes,b,be)
        msg['reduced_mod2_betti']=b
    print(msg,flush=True)

if __name__=='__main__':
    for sizes in ([2,2,2],[3,2,2],[3,3,2],[3,3,3],[3,3,2,2],[4,3,3], [4,4,3], [2,2,2,2]):
        run(sizes,with_betti=(sum(sizes)<=10))
    print('ALL CHECKS PASS')
