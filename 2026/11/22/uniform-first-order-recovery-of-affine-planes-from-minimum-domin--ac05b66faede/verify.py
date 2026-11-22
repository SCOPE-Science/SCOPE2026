#!/usr/bin/env python3
"""Exact small-plane checks for the stated affine domination/shattering theorem."""
from itertools import product, combinations
from functools import lru_cache
from math import comb

class Field:
    def __init__(self, q):
        self.q=q
        assert q in (2,3,4,5)
    def add(self,a,b):
        return (a^b) if self.q==4 else (a+b)%self.q
    def mul(self,a,b):
        if self.q!=4:return (a*b)%self.q
        t=0
        for i in range(2):
            for j in range(2):
                if ((a>>i)&1) and ((b>>j)&1):t^=1<<(i+j)
        if t&4:t^=7 # X^2=X+1
        return t

def plane(q):
    f=Field(q)
    pts=list(product(range(q),repeat=2))
    lines=[]
    for d in range(q+1):
        for b in range(q):
            lines.append(frozenset(i for i,(x,y) in enumerate(pts) if (x==b if d==q else f.add(y,f.mul(d,x))==b)))
    assert all(len(L)==q for L in lines)
    assert all(sum(i in L and j in L for L in lines)==1 for i,j in combinations(range(q*q),2))
    return pts,lines

def shattering_polynomial(concepts,n):
    result=[]
    for k in (0,1,2,3):
        count=0
        for T in combinations(range(n),k):
            traces=set()
            for H in concepts:
                t=sum(((H>>v)&1)<<i for i,v in enumerate(T))
                traces.add(t)
                if len(traces)==1<<k:break
            if len(traces)==1<<k:count+=1
        result.append(count)
    return result

def ld(concepts,n):
    pos=tuple(sum(1<<i for i,H in enumerate(concepts) if H>>v&1) for v in range(n))
    @lru_cache(None)
    def f(B):
        best=0
        for m in pos:
            a=B&m;b=B&~m
            if a and b:
                best=max(best,1+min(f(a),f(b)))
        return best
    return f((1<<len(concepts))-1)

def main():
    for q in (2,3,4,5):
        pts,lines=plane(q);v=q*q; n=v+len(lines)
        # Each chosen omitted line defines exactly one candidate minimum dominating set.
        H=[]
        for d in range(q+1):
            for b in range(q):
                omit=d*q+b
                pp=sum(1<<p for p in lines[omit]);ll=sum(1<<(v+d*q+j) for j in range(q) if j!=b)
                H.append(pp|ll)
        assert len(set(H))==q*(q+1)
        neighborhoods=[]
        for p in range(v):
            N=(1<<p)|sum(1<<(v+j) for j,L in enumerate(lines) if p in L)
            neighborhoods.append(N)
        for j,L in enumerate(lines):
            N=(1<<(v+j))|sum(1<<p for p in L)
            neighborhoods.append(N)
        U=(1<<n)-1
        assert all(__import__('functools').reduce(int.__or__,(neighborhoods[vx] for vx in range(n) if (h>>vx)&1),0)==U for h in H)
        if q in (2,3):
            cnt=0
            for k in range(1,2*q):
                for T in combinations(range(n),k):
                    cover=0
                    for vtx in T:cover|=neighborhoods[vtx]
                    if cover==U:cnt+=1
                if cnt:
                    assert k==2*q-1 and cnt==q*(q+1)
                    break
            print(f'minimum-exhaustive q={q}: cardinality={k}, count={cnt}')
        got=shattering_polynomial(H,n)
        expected=[1,n,(comb(v,2) if q==2 else q*(q*q-1)*(3*q+1)//2),0]
        assert got==expected,(q,got,expected)
        D=ld(H,n) if q<=3 else None
        if D is not None: assert D==2,(q,D)
        print(f'q={q}: concepts={len(H)}, shattering={got}, VC=2, exact online checked={D if D is not None else "not run"}')
        E=got[2]
        # Uniform first-order point predicate: nonneighbors induce an independent set.
        edge={(u,w) for u,w in combinations(range(n),2) if {0,1,2,3}=={((h>>u)&1)*2+((h>>w)&1) for h in H}}
        def adjacent(u,w):return (min(u,w),max(u,w)) in edge if u!=w else False
        for x in range(n):
            non=[y for y in range(n) if y!=x and not adjacent(x,y)]
            pred=all(not adjacent(y,z) for y,z in combinations(non,2))
            assert pred == (x<v)
        if q>=3:
            for p in range(v):
                for j,L in enumerate(lines):
                    assert adjacent(p,v+j)==(p not in L)
            assert E-n+1==(q+1)*(3*q**3-2*q**2-5*q+2)//2
            print(f'  first-order sort/incidence reconstruction PASS; H1 rank={E-n+1}')
        else:
            print('  q=2 boundary: only point-point pairs shattered')
if __name__=='__main__': main()
