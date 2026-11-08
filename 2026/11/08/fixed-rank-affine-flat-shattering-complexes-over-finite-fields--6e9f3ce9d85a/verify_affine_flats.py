#!/usr/bin/env python3
"""Independent finite incidence checks of fixed-rank affine-flat shattering."""
from itertools import product, combinations
from functools import lru_cache
from math import factorial

def fld(q):
    assert q in (2,3,4)
    def add(a,b):return (a^b) if q==4 else (a+b)%q
    def mul(a,b):
        if q!=4:return (a*b)%q
        poly=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1:poly ^=1<<(i+j)
        if poly&4:poly^=7
        return poly
    return add,mul

def generate(q,d,k):
    add,mul=fld(q)
    P=list(product(range(q),repeat=d)); idx={a:i for i,a in enumerate(P)}
    zero=(0,)*d
    def plus(a,b):return tuple(add(x,y) for x,y in zip(a,b))
    def scale(t,a):return tuple(mul(t,x) for x in a)
    spans={frozenset([zero])}
    for j in range(k):
        new=set()
        for old in spans:
            for v in P:
                if v in old: continue
                new.add(frozenset(plus(w,scale(t,v)) for w in old for t in range(q)))
        spans=new
    flats={frozenset(idx[plus(w,v)] for w in space) for space in spans for v in P}
    return P,flats

def rank_affine(q,points):
    add,mul=fld(q)
    if not points:return 0
    v0=points[0]
    A=[[add(x,y) if q==4 else (x-y)%q for x,y in zip(v,v0)] for v in points[1:]]
    r=0; d=len(v0)
    for c in range(d):
        j=next((j for j in range(r,len(A)) if A[j][c]),None)
        if j is None:continue
        A[r],A[j]=A[j],A[r]
        r+=1
        if r==len(A):break
        for row in range(r,len(A)):
            if A[row][c]:
                # eliminate using division-free two-row combination
                a,b=A[r-1][c],A[row][c]
                A[row]=[add(mul(a,y),mul(b,x)) if q==4 else (a*y-b*x)%q
                        for x,y in zip(A[r-1],A[row])]
    return r

def dimension(masks, count):
    @lru_cache(None)
    def rec(A):
        if not A:return -1
        best=0
        for M in masks:
            pos=A&M;neg=A&~M
            if pos and neg: best=max(best,1+min(rec(pos),rec(neg)))
        return best
    return rec((1<<count)-1)

def check(q,d,k,full_higher=True,do_ldim=False):
    points,flats=generate(q,d,k)
    n=len(points); masks=list(set(sum(1<<i for i in flat) for flat in flats))
    assert len(masks)==len(flats)
    expected=[]
    for m in range(k+2):
        val=n
        for j in range(m-1):val*=n-q**j
        expected.append(val//factorial(m) if m else 1)
    observed=[0]*(k+3)
    for m in range(k+3):
        if m>k+1 and not full_higher:continue
        for ids in combinations(range(n),m):
            traces=set()
            for h in masks:
                a=0
                for j,i in enumerate(ids):a|=((h>>i)&1)<<j
                traces.add(a)
                if len(traces)==1<<m:break
            actual=len(traces)==1<<m
            pred=(m<=k+1 and rank_affine(q,[points[i] for i in ids])==m-1) if m else True
            assert actual==pred,(q,d,k,ids,actual,pred)
            observed[m]+=actual
    assert observed[:k+2]==expected,(q,d,k,observed,expected)
    if do_ldim:
        queries=[sum(1<<j for j,M in enumerate(masks) if (M>>i)&1) for i in range(n)]
        L=dimension(queries,len(masks))
        assert L==k+1,(q,d,k,L)
    print('AFFINE_FLAT_CASE_PASS',q,d,k,len(flats),'supports',observed[:k+3], 'ldim_exact',do_ldim)

def main():
    for args in [(2,1,0),(2,2,0),(2,2,1),(3,2,0),(3,2,1),
                 (2,3,0),(2,3,1),(2,3,2),(3,3,1),(3,3,2),
                 (2,4,1),(2,4,2),(2,4,3),(4,2,1)]:
        q,d,k=args
        check(q,d,k,full_higher=(q**d<=27),do_ldim=(q**d<=9 and k<d))
    print('ALL_AFFINE_FLAT_TRACES_PASS')
if __name__=='__main__':main()
