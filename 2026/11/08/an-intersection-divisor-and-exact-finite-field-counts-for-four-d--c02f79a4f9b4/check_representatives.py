#!/usr/bin/env python3
"""Direct odd/even prime-field computations for canonical rank-one/two X."""
from itertools import product

def mult(A,B,q):
    return [[sum(A[i][k]*B[k][j] for k in range(4))%q for j in range(4)] for i in range(4)]
def zero(A): return all(x==0 for row in A for x in row)

def valid(X,Y,q):
    YY=mult(Y,Y,q)
    XY=mult(X,Y,q);YX=mult(Y,X,q)
    return zero(YY) and all((XY[i][j]+YX[i][j])%q==0 for i in range(4) for j in range(4))
for q in (2,3):
    X1=[[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    X2=[[0,0,1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]]
    c1=0
    for d00,d01,d10,d11,b0,b1,e0,e1,c in product(range(q),repeat=9):
        Y=[[0,b0,b1,c],[0,d00,d01,e0],[0,d10,d11,e1],[0,0,0,0]]
        if valid(X1,Y,q): c1+=1
    c2=nonzero=0
    for a00,a01,a10,a11,b00,b01,b10,b11 in product(range(q),repeat=8):
        Y=[[a00,a01,b00,b01],[a10,a11,b10,b11],
           [0,0,(-a00)%q,(-a01)%q],[0,0,(-a10)%q,(-a11)%q]]
        if valid(X2,Y,q):
            c2+=1
            if not zero(mult(X2,Y,q)):nonzero+=1
    assert c1==q**5+q**4-q**2,(q,c1)
    assert c2==2*q**4-q**2,(q,c2)
    assert nonzero==q**2*(q**2-1),(q,nonzero)
    print(f'field F_{q}: rank-one fiber={c1}; rank-two fiber={c2}; nonzero-product fiber={nonzero}')
print('ALL_CANONICAL_PAIR_FIBERS_PASS')
