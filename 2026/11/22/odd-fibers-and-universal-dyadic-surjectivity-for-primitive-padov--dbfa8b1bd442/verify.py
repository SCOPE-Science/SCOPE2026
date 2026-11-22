#!/usr/bin/env python3
"""Exact integer-matrix and finite-instance checks for a Padovan residue-fiber theorem."""
from itertools import product

Q=((0,1,0),(0,0,1),(1,1,0))
I=((1,0,0),(0,1,0),(0,0,1))
B=((0,1,1),(1,1,1),(1,2,1))
D=((2,4,3),(3,5,4),(4,7,5))

def mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))

def power(a,n):
    r=I
    while n:
        if n&1:r=mul(r,a)
        a=mul(a,a);n>>=1
    return r

def det(a):
    return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])

def submodmatrix(a,b,p):
    return tuple(tuple((a[i][j]-b[i][j])%p for j in range(3)) for i in range(3))

def scalar_row(a,v):
    return sum(a[0][i]*v[i] for i in range(3))

assert power(Q,7)==tuple(tuple(I[i][j]+2*B[i][j] for j in range(3)) for i in range(3))
assert power(Q,14)==tuple(tuple(I[i][j]+4*D[i][j] for j in range(3)) for i in range(3))
assert det(Q)==1 and abs(det(B))==1 and abs(det(D))==1
assert all(submodmatrix(power(Q,i),I,2)!=((0,0,0),)*3 for i in range(1,7))
assert submodmatrix(power(Q,7),I,2)==((0,0,0),)*3
assert {(tuple(scalar_row(power(Q,j)[i:i+1]+((0,0,0),)*2,v)%2 for i in (0,))) for j in range(7) for v in [(1,0,0)]} == {(0,),(1,)}
expected={(1,0,0),(0,1,1),(0,1,0),(1,1,1),(0,0,1),(1,0,1),(1,1,0)}
for v in product(range(2),repeat=3):
    if v==(0,0,0):continue
    pattern=set()
    for j in range(7):
        a=power(Q,j)
        e=(scalar_row(a,v)%2,scalar_row(mul(B,a),v)%2,scalar_row(mul(D,a),v)%2)
        pattern.add(e)
    assert pattern==expected
    assert len([a for a in pattern if a[1:]==(1,1)])==2
    assert {a[0] for a in pattern if a[1:]==(1,1)}=={0,1}

# Exact 2-adic leading matrices at dyadic time shifts.
for s in range(10):
    h=7*(2**s)
    P=power(Q,h)
    M=tuple(tuple((P[i][j]-I[i][j])//(2**(s+1)) for j in range(3)) for i in range(3))
    assert P==tuple(tuple(I[i][j]+(2**(s+1))*M[i][j] for j in range(3)) for i in range(3))
    assert submodmatrix(M,B if s==0 else D,2)==((0,0,0),)*3

# All primitive states and all output residues, modulo 2,4,8,16,32.
for k in range(1,6):
    m=2**k; length=7*(2**(k-1))
    for a,b,c in product(range(m),repeat=3):
        if not (a|b|c)&1:continue
        x,y,z=a,b,c
        freq=[0]*m
        for _ in range(length):
            freq[x]+=1
            x,y,z=y,z,(x+y)%m
        assert (x,y,z)==(a,b,c)
        if k>=3:assert all(v%2==1 for v in freq),(k,(a,b,c),freq)
        elif k==2:assert all(v%2==0 for v in freq)
        else:assert sorted(freq)==[3,4]

# Larger levels for representative nontrivial states.
for k in range(6,13):
    m=1<<k; length=7*(1<<(k-1))
    for a,b,c in [(1,0,0),(1,1,1),(3,0,2),(2,3,4),(27,17,68)]:
        x,y,z=a%m,b%m,c%m
        freq=[0]*m
        for _ in range(length):
            freq[x]+=1
            x,y,z=y,z,(x+y)%m
        assert all(v&1 for v in freq),(k,(a,b,c))
print('VERIFY_OK')
