#!/usr/bin/env python3
"""Exact arithmetic checks for Radau-IIA star heat-step identities.

Run with Python 3 standard library: python3 verify.py
The universal argument is in RESULT.md; these tests are finite validations.
"""
from fractions import Fraction as F
from math import isqrt

checks = 0

def require(test, name):
    global checks
    if not test:
        raise AssertionError(name)
    checks += 1

# A bivariate integer polynomial has keys (degree_in_m, degree_in_h).
def poly(c=0):
    return {(0, 0): c} if c else {}
def mono(a, b, c=1):
    return {(a, b): c} if c else {}
def add(*args):
    out = {}
    for p in args:
        for k, v in p.items(): out[k] = out.get(k, 0) + v
    return {k:v for k,v in out.items() if v}
def neg(p): return {k:-v for k,v in p.items()}
def sub(a,b): return add(a,neg(b))
def mul(*args):
    out=poly(1)
    for p in args:
        nxt={}
        for (a,b),x in out.items():
            for (c,d),y in p.items():
                key=(a+c,b+d)
                nxt[key]=nxt.get(key,0)+x*y
        out={k:v for k,v in nxt.items() if v}
    return out
def scale(p,k): return {i:v*k for i,v in p.items() if v*k}

o=poly(1); m=mono(1,0); h=mono(0,1)
N=add(m,o)
Da=add(mul(h,h),scale(h,4),poly(6))
Db=add(mul(N,N,h,h),scale(mul(N,h),4),poly(6))
An=add(poly(6),neg(scale(h,2)))
Bn=add(poly(6),neg(scale(mul(N,h),2)))
Q=add(mul(N,h,h),scale(mul(h,sub(poly(2),m)),2),poly(6))
P=add(mul(N,h,h,h,h),
      mul(add(neg(scale(mul(m,m),2)),scale(m,2),poly(10)),h,h,h),
      mul(add(scale(mul(m,m),6),scale(m,4),poly(16)),h,h),
      mul(add(scale(m,24),poly(12)),h),poly(36))
S=add(mul(N,h,h),scale(mul(add(m,poly(2)),h),6),poly(18))
require(not sub(add(Db,mul(m,Bn)),mul(N,Q)), 'hub polynomial identity')
require(not sub(add(mul(m,Da,Db),mul(Bn,Da),mul(sub(m,o),N,An,Db)),mul(m,N,P)), 'leaf polynomial identity')
require(not sub(sub(add(mul(m,Da,Db),mul(Bn,Da)),mul(N,An,Db)),mul(m,N,h,h,S)), 'leaf-to-leaf numerator')
require(not sub(sub(Db,Bn),mul(N,h,add(mul(N,h),poly(6)))), 'hub-to-leaf numerator')

# Exact rational confirmation of the positive quartic certificate at m=10.
#  P_10(h) = h (h - 39/5)^2(11h+8/5)
#              +293/25*h^2+19332/125*h+36.
def polyeval(p, mm, hh):
    return sum(v*mm**a*hh**b for (a,b),v in p.items())
# Univariate coefficient comparison in exact rational arithmetic.
def pu_add(a,b):
    return {i:a.get(i,F(0))+b.get(i,F(0)) for i in set(a)|set(b) if a.get(i,F(0))+b.get(i,F(0))}
def pu_mul(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items(): out[i+j]=out.get(i+j,F(0))+x*y
    return {i:x for i,x in out.items() if x}
def pu_scale(a,k):return {i:k*x for i,x in a.items() if k*x}
X={1:F(1)}
Qshift={1:F(1),0:-F(39,5)}
cert=pu_add(pu_add(pu_mul(pu_mul(X,pu_mul(Qshift,Qshift)),{1:F(11),0:F(8,5)}),
                       {2:F(293,25),1:F(19332,125)}),{0:F(36)})
actual={i:polyeval(P,10,F(0)) if i==0 else sum(v*10**a for (a,j),v in P.items() if j==i) for i in range(5)}
require(cert == actual, 'exact SOS coefficient identity for P10')
# Exact threshold witness and discriminant values.
for mm in range(2,61):
    val=polyeval(P,mm,8)
    require(val == -4*(160*mm*mm-1392*mm-2593), 'm-dependent sign witness')
    require((val<0)==(mm>=11), 'leaf threshold at h=8')
    require(((mm-2)**2-6*(mm+1)>0)==(mm>=11), 'hub discriminant threshold')

# Rational projector and full matrix equation. No numerical eigensolvers required.
def matrix_product(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def matrix_add(A,B): return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
def matrix_scale(A,z): return [[z*x for x in row] for row in A]
def step(m,h):
    n=m+1
    r=lambda z:(6-2*z)/(z*z+4*z+6)
    a=r(h);b=r(n*h)
    zero=F(0);one=F(1)
    E0=[[F(1,n) for j in range(n)] for i in range(n)]
    v=[m]+[-1]*m
    En=[[F(v[i]*v[j],m*n) for j in range(n)] for i in range(n)]
    I=[[one if i==j else zero for j in range(n)] for i in range(n)]
    E1=matrix_add(matrix_add(I,matrix_scale(E0,-1)),matrix_scale(En,-1))
    return matrix_add(matrix_add(E0,matrix_scale(E1,a)),matrix_scale(En,b))
def lap(m):
    n=m+1
    return [[F(m if i==j==0 else 1 if i==j else -1 if i==0 or j==0 else 0)
             for j in range(n)] for i in range(n)]
for mm in range(2,33):
    n=mm+1
    L=lap(mm); L2=matrix_product(L,L)
    I=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    for hh in [F(1,17),F(1,2),F(1),F(2),F(3),F(4),F(6),F(8),F(12),F(24),F(80)]:
        T=step(mm,hh)
        M=matrix_add(matrix_add(matrix_scale(L2,hh*hh),matrix_scale(L,4*hh)),matrix_scale(I,6))
        RHS=matrix_add(matrix_scale(I,6),matrix_scale(L,-2*hh))
        require(matrix_product(T,M)==RHS,'Radau exact rational matrix equation')
        require(all(sum(row)==1 for row in T),'mass conservation')
        require(all(T[i][j]==T[j][i] for i in range(n) for j in range(n)), 'symmetry')
        q=polyeval(Q,mm,hh)
        p=polyeval(P,mm,hh)
        Da0=hh*hh+4*hh+6;Db0=(n*hh)**2+4*n*hh+6
        require(T[0][0]==q/Db0 and T[1][1]==p/(Da0*Db0),'diagonal closed forms')
        require(all(T[i][j]>0 for i in range(n) for j in range(i+1,n)), 'off diagonal positive')
        require((min(x for row in T for x in row)>=0)==(q>=0 and p>=0), 'positivity iff polynomial signs')
print('VERIFY_OK',checks)
