#!/usr/bin/env python3
"""Independent bit-vector enumeration of cyclic elementary CA rule 3.
Checks the proved fixed-point and entry-time formulas on all states in tested rings.
"""
from math import gcd

def trace_power(M, n):
    sz=len(M)
    A=[[int(i==j) for j in range(sz)] for i in range(sz)]
    for _ in range(n):
        A=[[sum(A[i][k]*M[k][j] for k in range(sz)) for j in range(sz)] for i in range(sz)]
    return sum(A[i][i] for i in range(sz))

U=[[1,1,0,0],[0,0,1,1],[1,0,0,0],[0,0,1,1]]
V=[[0,1,0,0],[0,0,1,0],[1,1,0,0],[0,0,0,0]]

def image(x,n):
    mask=(1<<n)-1
    prior=((x<<1)&mask)|(x>>(n-1))
    return (~(prior|x))&mask

def predicted(n,m):
    return trace_power(U,gcd(n,m//2)) if m%2==0 else trace_power(V,gcd(n,m))

case_count=0
for n in range(3,15):
    size=1<<n
    S={image(x,n) for x in range(size)}
    forbidden={x for x in range(size) if all(not (((x>>i)&1) and not((x>>((i+1)%n))&1) and ((x>>((i+2)%n))&1)) for i in range(n))}
    assert S==forbidden, ('image mismatch',n)
    assert len(S)==trace_power(U,n),('recurrent count',n)
    # Iterates are generated without assuming the formula.
    X=list(range(size))
    for m in range(1,2*n+1):
        X=[image(x,n) for x in X]
        actual=sum(x==y for x,y in enumerate(X))
        expect=predicted(n,m)
        assert actual==expect,(n,m,actual,expect)
        case_count+=1
    assert all(image(image(image(x,n),n),n)==(((image(x,n)<<1)&(size-1)) | (image(x,n)>>(n-1))) for x in range(size)),('cubic shift',n)
    print(f'n={n:2d}: {size:6d} states, {len(S):5d} recurrent, {2*n:2d} temporal fixed-point checks OK')
print(f'PASS: {case_count} independently computed fixed-point counts, all image/subshift and cubic-shift checks.')
