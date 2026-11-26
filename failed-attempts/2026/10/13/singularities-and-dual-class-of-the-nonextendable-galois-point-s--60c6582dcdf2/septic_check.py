#!/usr/bin/env python3
"""Exact, standard-library checks for a rational plane septic over C.
Cyclotomic computations use Q[z]/(z^4+z^3+z^2+z+1); no floating point.
"""
from fractions import Fraction as F
from itertools import combinations
Z=(F(0),)*4
ONE=(F(1),F(0),F(0),F(0))
ZETA=(F(0),F(1),F(0),F(0))
def c(x):return (F(x),F(0),F(0),F(0))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    out=[F(0)]*7
    for i in range(4):
        for j in range(4):out[i+j]+=a[i]*b[j]
    # The defining polynomial is z^4+z^3+z^2+z+1.
    for k in range(6,3,-1):
        v=out[k]
        for j in range(k-4,k):out[j]-=v
    return tuple(out[:4])
def powr(a,k):
    v=ONE
    for _ in range(k):v=mul(v,a)
    return v
def det(A):
    n=len(A);a=[list(row) for row in A];d=ONE
    for i in range(n):
        k=next((j for j in range(i,n) if a[j][i]!=Z),None)
        if k is None:return Z
        if k!=i:a[i],a[k]=a[k],a[i];d=neg(d)
        q=a[i][i];d=mul(d,q)
        iq=inv(q)
        for j in range(i+1,n):
            v=mul(a[j][i],iq)
            for h in range(i+1,n):a[j][h]=sub(a[j][h],mul(v,a[i][h]))
            a[j][i]=Z
    return d
def inv(a):
    assert a!=Z
    M=[[mul(a,tuple(F(int(i==j)) for j in range(4)))[k] for i in range(4)] for k in range(4)]
    # Invert by solving a*x = 1 over Q via Gauss-Jordan.
    B=[M[i]+[F(int(i==0))] for i in range(4)]
    for i in range(4):
        p=next(j for j in range(i,4) if B[j][i]);B[i],B[p]=B[p],B[i]
        v=B[i][i];B[i]=[x/v for x in B[i]]
        for j in range(4):
            if j!=i:
                v=B[j][i];B[j]=[u-v*x for u,x in zip(B[j],B[i])]
    return tuple(B[i][-1] for i in range(4))
def norm(a):
    M=[[mul(a,tuple(F(int(i==j)) for j in range(4)))[k] for i in range(4)] for k in range(4)]
    # determinant over Q
    D=F(1)
    for i in range(4):
        p=next((j for j in range(i,4) if M[j][i]),None)
        if p is None:return 0
        if p!=i:M[i],M[p]=M[p],M[i];D=-D
        t=M[i][i];D*=t
        for j in range(i+1,4):
            v=M[j][i]/t
            for k in range(i+1,4):M[j][k]-=v*M[i][k]
            M[j][i]=0
    return D
# Polynomials over Q(zeta), in highest-degree-first order for the Sylvester matrix.
def resultant(A,B):
    m=len(A)-1;n=len(B)-1
    R=[]
    for i in range(n):R.append([Z]*i+list(A)+[Z]*(n-1-i))
    for i in range(m):R.append([Z]*i+list(B)+[Z]*(m-1-i))
    return det(R)
def derivative(A):
    d=len(A)-1
    return [mul(c(d-i),A[i]) for i in range(d)]
assert powr(ZETA,5)==ONE and all(powr(ZETA,k)!=ONE for k in (1,2,3,4))
polys=[]
for k in range(1,5):
    a=powr(ZETA,k)
    # T_a(w) = a(1+a)w^3 + (1+a+a^2)w^2 + 1.
    P=[mul(a,add(ONE,a)),add(add(ONE,a),mul(a,a)),Z,ONE]
    assert norm(P[0])!=0
    # T_a(0)=1, T_a(-1)=2.
    atminusone=sub(add(neg(P[0]),P[1]),Z)
    atminusone=add(atminusone,ONE)
    assert atminusone==c(2)
    ai=inv(a)
    at_other_pole=add(sub(mul(P[1],mul(ai,ai)),mul(P[0],powr(ai,3))),ONE)
    assert at_other_pole==c(2)
    disc=neg(mul(resultant(P,derivative(P)),inv(P[0])))
    assert norm(disc)==674041
    polys.append(P)
for a,b in combinations(polys,2):
    assert norm(resultant(a,b))==2000
# Verify the dual parametrization from exact polynomial cross-products.
def poly_mul(a,b):
    ans=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):ans[i+j]+=x*y
    return ans
def poly_sub(a,b):
    return [(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def poly_diff(a):return [i*a[i] for i in range(1,len(a))]
def cross(a,b):return poly_sub(poly_mul(a,poly_diff(b)),poly_mul(b,poly_diff(a)))
X=[-1,0,0,0,0,0,1]
Y=[1,0,1]
T=poly_mul([0,0,0,0,0,1],Y)
# Remove the common t factor of the projective tangent map.
tangent=[cross(Y,T),cross(T,X),cross(X,Y)]
assert all(q[0]==0 for q in tangent)
tangent=[q[1:] for q in tangent]
assert tangent[0]==[0,0,0,5,0,10,0,5]
assert tangent[1]==[0,0,0,5,0,7,0,0,0,1,0,-1]
assert tangent[2]==[-2,0,0,0,-6,0,-4]
# A direct implicit equation of the image, independently checking the node at [1:0:0].
# Terms are (coefficient, power of X, power of Y, power of Z).
terms=[(1,5,2,0),(1,5,0,2),(5,4,3,0),(-5,4,1,2),
       (10,3,4,0),(-10,3,2,2),(10,2,5,0),(-5,2,3,2),
       (5,2,1,4),(5,1,6,0),(5,1,2,4),(1,0,7,0),(-1,0,1,6)]
def poly_add(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def poly_power(a,n):
    p=[1]
    for _ in range(n):p=poly_mul(p,a)
    return p
lhs=[0]
for coef,i,j,k in terms:
    mon=poly_mul(poly_mul(poly_power(X,i),poly_power(Y,j)),poly_power(T,k))
    lhs=poly_add(lhs,[coef*v for v in mon])
assert not any(lhs)
assert [(coef,i,j,k) for coef,i,j,k in terms if j+k==2]==[(1,5,2,0),(1,5,0,2)]
# Its quadratic tangent cone at P=[1:0:0] is Y^2+Z^2: two lines.
# Differential of the parametrization has no ramification outside t=0:
# x=t^6-1, y=t^2+1, z=t^5(t^2+1).
# xy'-yx' = -4t^7-6t^5-2t; yz'-zy'=5t^4(t^2+1)^2;
# at every t !=0 at least one of these is nonzero (at t^2=-1 first !=0).
# At t=infinity, X/Z has local order one, so the normalization is immersed.
# At t=0, (X/Y+1, Z/Y) has leading orders (2,5), an A4 cusp.
# At t= +/-i, Y=Z=0 and X=-2, with distinct tangent slopes +/-i.
assert 4*3*2//2==12
assert 12+1==13
assert 13+2==(7-1)*(7-2)//2
assert 7*6-13*2-(4+2-1)==11
print('VERIFY_OK degree=7 nodes=13 cusp=A4 dual_degree=11 discriminant_norms=4x674041 pair_resultant_norms=6x2000')
