#!/usr/bin/env python3
"""Independent GF(8) certificate for the named dimension-six toric code pair.
Coordinates of both polygons are explicitly in data below.
No third-party dependencies.
"""
from itertools import product

# GF(8)=GF(2)[a]/(a^3+a+1); elements are packed 3-bit polynomials.
MOD=0b1011

def mul(a,b):
    out=0
    while b:
        if b&1: out ^= a
        a <<= 1
        if a&8:a ^= MOD
        b >>= 1
    return out

def power(a,n):
    out=1
    for _ in range(n):out=mul(out,a)
    return out

def inv(a):
    if a==0:raise ZeroDivisionError
    return power(a,6)

# Luo--Yau--Zhang--Zuo (2014), Fig. 1.4; ordering only matters for matrix identity.
P4=((0,0),(1,0),(2,0),(3,0),(0,1),(0,-1))
P5=((0,0),(1,0),(2,0),(3,0),(0,1),(-1,-1))
field=tuple(range(1,8))
torus=tuple(product(field,repeat=2))
assert all(power(x,7)==1 for x in field)
assert all(mul(x,inv(x))==1 for x in field)

def ev(P,x,y):
    return tuple(mul(power(x,a%7),power(y,b%7)) for a,b in P)

# For P4-polynomial f, x^3*f(x^(-1),x^(-3)y) is a P5-polynomial.
# At a target point (x,y), P4 source (1/x,x^(-3)y), scalar x^3.
row_perm=[]
for x,y in torus:
    src_x=inv(x)
    src_y=mul(power(x,4),y)  # x^(-3)=x^4
    j=torus.index((src_x,src_y))
    row_perm.append(j)
    lhs=tuple(mul(power(x,3),z) for z in ev(P4,src_x,src_y))
    target=ev(P5,x,y)
    assert lhs==(target[3],target[2],target[1],target[0],target[4],target[5]),(x,y,lhs,target)
assert sorted(row_perm)==list(range(49))

def column_rank(columns):
    """Rank over GF(8), given a list of generator rows of equal length."""
    matrix=[list(col) for col in columns]
    pivot=0
    for j in range(len(matrix[0])):
        k=next((i for i in range(pivot,len(matrix)) if matrix[i][j]),None)
        if k is None:continue
        matrix[pivot],matrix[k]=matrix[k],matrix[pivot]
        z=inv(matrix[pivot][j])
        matrix[pivot]=[mul(z,a) for a in matrix[pivot]]
        for i in range(len(matrix)):
            if i==pivot:continue
            c=matrix[i][j]
            if c:
                matrix[i]=[a^mul(c,b) for a,b in zip(matrix[i],matrix[pivot])]
        pivot += 1
        if pivot==len(matrix):break
    return pivot

G4=[tuple(ev(P4,x,y)[i] for x,y in torus) for i in range(6)]
G5=[tuple(ev(P5,x,y)[i] for x,y in torus) for i in range(6)]
assert column_rank(G4)==column_rank(G5)==6
print('field=GF(8), |torus|=49, generators_both_rank=6, permutation_bijective=True')
print('source_coordinates: P4=(1,x,x^2,x^3,y,y^-1)')
print('target_coordinates: P5=(1,x,x^2,x^3,y,x^-1*y^-1)')
print('for every target (x,y): source=(x^-1,x^-3*y), scale=x^3')
print('row_identity: scaled P4 columns=(P5[3],P5[2],P5[1],P5[0],P5[4],P5[5])')
print('projective linear row transformation: reverse four polynomial coefficients, fix remaining two')
print('representative_point_permutation_first_12=',row_perm[:12])
print('VERIFY_OK')
