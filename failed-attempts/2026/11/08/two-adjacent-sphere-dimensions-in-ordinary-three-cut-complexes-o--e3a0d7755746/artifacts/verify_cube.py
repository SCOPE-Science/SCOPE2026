#!/usr/bin/env python3
"""Independent finite boundary/rank checks for ordinary three-cut Alexander duals of Boolean cubes.
The all-dimensional proof is mathematical; this program checks illustrative small dimensions.
"""
from itertools import combinations
from math import comb

def pop(x): return x.bit_count()

def gf2rank(columns):
    piv={}
    for a in columns:
        while a:
            k=a.bit_length()-1
            if k in piv: a^=piv[k]
            else:
                piv[k]=a;break
    return len(piv)

def dual_faces(d):
    n=1<<d
    edges=list(combinations(range(n),2))
    eidx={e:i for i,e in enumerate(edges)}
    paths=[]
    for a,b,c in combinations(range(n),3):
        e=(pop(a^b)==1)+(pop(a^c)==1)+(pop(b^c)==1)
        if e==2:paths.append((a,b,c))
    tidx={t:i for i,t in enumerate(paths)}
    squares=[]
    for b in range(n):
        for i in range(d):
            for j in range(i+1,d):
                t=tuple(sorted((b,b^(1<<i),b^(1<<j),b^(1<<i)^(1<<j))))
                if b==min(t):squares.append(t)
    squares=sorted(set(squares))
    b2=[sum(1<<eidx[e] for e in combinations(t,2)) for t in paths]
    b3=[sum(1<<tidx[t] for t in combinations(s,3)) for s in squares]
    r2=gf2rank(b2);r3=gf2rank(b3)
    longpairs=sum(pop(a^b)>=3 for a,b in edges)
    b2pred=2**(d-3)*(d*d-5*d+8)-1
    expected_r2=len(edges)-(n-1)-longpairs
    assert len(paths)==n*comb(d,2)
    assert len(squares)==2**(d-2)*comb(d,2)
    assert r2==expected_r2, (d,r2,expected_r2)
    assert r3==len(squares)
    assert len(paths)-r2-r3==b2pred
    # ∂2∂3=0 mod 2.
    assert all((__import__('functools').reduce(int.__xor__,(b2[tidx[t]] for t in combinations(s,3)),0))==0 for s in squares)
    if d<=4:
        # The Alexander dual has precisely those triples whose induced graphs are connected.
        for t in combinations(range(n),3):
            assert (t in tidx)==(sum(pop(x^y)==1 for x,y in combinations(t,2))>=2)
        for s in combinations(range(n),4):
            assert (s in set(squares))==all(sum(pop(x^y)==1 for x,y in combinations(t,2))>=2 for t in combinations(s,3))
        for t in combinations(range(n),5):
            assert not all(sum(pop(x^y)==1 for x,y in combinations(sub,2))>=2 for sub in combinations(t,3))
    return (d,n,len(edges),len(paths),len(squares),r2,r3,longpairs,b2pred)

if __name__=='__main__':
    for d in range(3,7):
        print('d,n,f1,f2,f3,rank_d2_mod2,rank_d3_mod2,beta1,beta2 =',dual_faces(d))
    print('all finite boundary and dual-face checks passed')
