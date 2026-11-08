"""Exact independent bit-matrix checks for cubelike edge-neighbor dynamics."""
from itertools import combinations
from random import Random


def rank(rows):
    basis = {}
    for row in rows:
        x=row
        while x:
            p=x.bit_length()-1
            if p in basis:
                x ^= basis[p]
            else:
                basis[p]=x
                break
    return len(basis)


def product(left, right):
    out=[]
    for row in left:
        v=0
        while row:
            low=row & -row
            v ^= right[low.bit_length()-1]
            row ^= low
        out.append(v)
    return out


def edge_matrix(r,S):
    n=1<<r
    edges=sorted((x,x^s) for x in range(n) for s in S if x<(x^s))
    incident=[0]*n
    for i,(a,b) in enumerate(edges):
        incident[a]|=1<<i
        incident[b]|=1<<i
    return [incident[a]^incident[b] for a,b in edges]


def span(S,r):
    v=0
    basis={}
    for s in S:
        x=s
        while x:
            p=x.bit_length()-1
            if p in basis:x^=basis[p]
            else:basis[p]=x;v+=1;break
    return v==r


def check(r,S):
    rows=edge_matrix(r,S)
    N=1<<r
    m=len(rows)
    B2=product(rows,rows)
    B3=product(B2,rows)
    assert not any(B3),(r,S,'cube')
    r1=rank(rows);r2=rank(B2)
    assert r1==N-2,(r,S,'rank1',r1,N-2)
    if __import__('functools').reduce(int.__xor__,S,0):
        assert r2==N//2-2,(r,S,'rank2',r2,N//2-2)
        a3=r2
        a2=r1-2*r2
        a1=m-2*a2-3*a3
        assert (a3,a2,a1)==(N//2-2,2,(len(S)-3)*N//2+2)
    return r1,r2

if __name__=='__main__':
    rng=Random(301126)
    allchecked=0
    eligible=0
    for r in (2,3):
        for bits in range(1,1<<((1<<r)-1)):
            S=[i for i in range(1,1<<r) if bits>>(i-1)&1]
            if not span(S,r):continue
            rr=check(r,S)
            allchecked+=1
            eligible+=int(bool(__import__('functools').reduce(int.__xor__,S,0)))
        print('complete r=',r,'tested=',allchecked,'xor_nonzero=',eligible)
    for r,count in ((4,150),(5,50)):
        tested=0
        for trial in range(count):
            S=set(1<<i for i in range(r))
            S.update(rng.sample(range(1,1<<r),rng.randrange(r, min((1<<r)-1, r+6)+1)))
            S=sorted(S)
            check(r,S)
            tested+=1
            eligible+=int(bool(__import__('functools').reduce(int.__xor__,S,0)))
        allchecked+=tested
        print('sampled r=',r,'tested=',tested)
    print('MATRIX_OK total_cases=',allchecked,'xor_nonzero=',eligible)
