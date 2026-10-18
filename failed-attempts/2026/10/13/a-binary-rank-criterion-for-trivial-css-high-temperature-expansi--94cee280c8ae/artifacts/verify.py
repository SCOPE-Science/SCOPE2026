#!/usr/bin/env python3
from itertools import product

def rank_f2(A):
    A=[row[:] for row in A]
    if not A:
        return 0
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]&1),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        for i in range(m):
            if i!=r and (A[i][c]&1):
                A[i]=[(x^y) for x,y in zip(A[i],A[r])]
        r+=1
        if r==m: break
    return r

def mul(A,x):
    return [sum(a*b for a,b in zip(row,x))%2 for row in A]

def check(A):
    n=len(A[0]) if A else 0
    ker=[x for x in product((0,1),repeat=n) if not any(mul(A,x))]
    nullity=n-rank_f2(A)
    assert len(ker)==2**nullity
    one=(1,)*n
    bone=mul(A,one)
    trivial = set(ker)==({(0,)*n} if any(bone) else {(0,)*n,one})
    criterion = (nullity==0) if any(bone) else (nullity==1)
    assert trivial==criterion
    return nullity,len(ker),trivial

witness=[[1,1,1],[1,0,0],[0,1,0]]
assert rank_f2(witness)==3
assert check(witness)==(0,1,True)

examples=[
 [[1]],
 [[0]],
 [[1,1],[1,0]],
 [[1,1],[1,1]],
 [[1,1,0],[0,1,1]],
 [[1,1,1],[1,0,1],[0,1,1]],
 witness,
]
for A in examples:
    check(A)
print('VERIFY_OK')
