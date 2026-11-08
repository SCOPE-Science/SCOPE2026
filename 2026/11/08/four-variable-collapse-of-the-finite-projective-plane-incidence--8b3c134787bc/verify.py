#!/usr/bin/env python3
"""Exact finite-incidence checks for the four-variable projective-plane classification.
Only standard-library Python is used. Tests are finite corroboration, not the unrestricted proof.
"""
from itertools import product,combinations
from datetime import datetime

def field(q):
    if q == 4:
        add=lambda a,b:a^b
        def mul(a,b):
            aa,ab=a&1,a>>1; ba,bb=b&1,b>>1
            return (aa*ba ^ ab*bb) | ((aa*bb ^ ab*ba ^ ab*bb)<<1)
        inv={1:1,2:3,3:2}
    else:
        assert q in (2,3,5)
        add=lambda a,b:(a+b)%q
        mul=lambda a,b:a*b%q
        inv={a:pow(a,-1,q) for a in range(1,q)}
    return add,mul,inv

def plane(q):
    add,mul,inv=field(q)
    points=set()
    for t in product(range(q), repeat=3):
        if not any(t):continue
        p=next(a for a in t if a)
        points.add(tuple(mul(a,inv[p]) for a in t))
    vectors=sorted(points)
    N=len(vectors)
    assert N==q*q+q+1
    inc=set()
    for i,x in enumerate(vectors):
        for j,y in enumerate(vectors):
            dot=0
            for r in range(3):dot=add(dot,mul(x[r],y[r]))
            if dot==0:inc.add((i,N+j))
    assert len(inc)==N*(q+1)
    return N,inc

def signatures(q,exhaustive):
    N,inc=plane(q)
    U=range(2*N)
    hit=lambda a,b:((a,b) in inc or (b,a) in inc)
    def signature(z):
        sort=tuple(int(v>=N) for v in z)
        edges=tuple((int(z[i]==z[j]),int(hit(z[i],z[j])))
                    for i,j in combinations(range(len(z)),2))
        triples=[]
        for inds in combinations(range(len(z)),3):
            vals=[z[i] for i in inds]
            if len(set(vals))<3 or len({sort[i] for i in inds})>1:
                triples.append(0);continue
            other=range(N,2*N) if sort[inds[0]]==0 else range(N)
            triples.append(int(any(all(hit(v,a) for v in vals) for a in other)))
        return sort,edges,tuple(triples)
    ext={};seen={};checked=0
    for triple in product(U,repeat=3):
        typ=signature(triple)
        if exhaustive or typ not in ext or (sum((i+3)*a for i,a in enumerate(triple))%97==0):
            choices=frozenset(signature(triple+(x,)) for x in U)
            checked+=1
            if typ in ext:
                assert ext[typ]==choices,('nonuniform 3-type extension',q,triple)
            else:
                ext[typ]=choices;seen[typ]=triple
    assert len(ext)==48
    all_four=set.union(*(set(s) for s in ext.values()))
    print('q=%d points=%d 3types=%d 4types=%d checked_triples=%d' %(q,N,len(ext),len(all_four),checked))
    return ext

def formula(q):
    N,inc=plane(q); witnesses=0
    # Four variable names l,m,p,n; the final intersection witness reuses p.
    for l in range(N,2*N):
        for m in range(N,2*N):
            if l==m: continue
            centers=[x for x in range(N) if (x,l) in inc and (x,m) in inc]
            assert len(centers)==1
            c=centers[0]
            for p in range(N):
                if (p,l) in inc or (p,m) in inc:continue
                for n in range(N,2*N):
                    if n in (l,m) or (p,n) in inc or (c,n) not in inc:continue
                    witnesses+=1
    assert bool(witnesses)==(q>=3)
    print('q=%d exact_four_variable_sentence=%s witnesses=%d' %(q,bool(witnesses),witnesses))

def main():
    ext={q:signatures(q,exhaustive=(q in (2,3))) for q in (2,3,4,5)}
    for q in (3,4,5):
        assert ext[q]==ext[3]
    different=sum(ext[2][s]!=ext[3][s] for s in ext[2])
    assert different==8
    print('q>=3 common extension catalogue: PASS; q2 mismatching 3types:',different)
    for q in (2,3,4,5): formula(q)
    print('ALL CHECKS PASS')
if __name__=='__main__':main()
