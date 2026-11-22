#!/usr/bin/env python3
"""Exact finite checks of the algebra and independent geometric samples.
The accompanying analytic argument, not this finite script, proves universality.
Python 3 standard library only.
"""
from fractions import Fraction as F
from math import sqrt, isclose

COUNT=0

def confirm(ok, label):
    global COUNT
    assert ok, label
    COUNT+=1

# Polynomial arithmetic in u=a^2 and v=delta^2; every coefficient is exact.
def add(P,Q):
    R=dict(P)
    for k,val in Q.items():
        R[k]=R.get(k,0)+val
    return {k:v for k,v in R.items() if v}
def neg(P): return {k:-v for k,v in P.items()}
def sub(P,Q): return add(P,neg(Q))
def mul(P,Q):
    R={}
    for (i,j),a in P.items():
        for (k,l),b in Q.items():
            key=(i+k,j+l)
            R[key]=R.get(key,0)+a*b
    return {k:v for k,v in R.items() if v}
def sq(P): return mul(P,P)
U={(1,0):1}
V={(0,1):1}
ONE={(0,0):1}
TWO={(0,0):2}
FOUR={(0,0):4}
THREE_U={(1,0):3}
lhs=sub(mul(sub(FOUR,U),sq(sub(U,mul(TWO,V)))),mul(mul(U,sub(U,V)),sq(sub(TWO,U))))
rhs=mul(sub(sq(U),mul(FOUR,V)),sub(sub(THREE_U,sq(U)),mul(sub(FOUR,U),V)))
confirm(lhs==rhs,'exact polynomial factorization')

for a_num in range(1,21):
    a=F(a_num,20)
    u=a*a
    s2=1-u/4
    for k in range(21):
        delta=u*F(k,40)
        v=delta*delta
        h2=u-v
        confirm(h2>0 and 4*v<=u*u,'geometric domain')
        nonnegative_1=u*u-4*v
        positive_2=3*u-u*u-(4-u)*v
        confirm(nonnegative_1>=0 and positive_2>0,'certificate signs')
        confirm(s2>0,'unit-circle half chord')
        # Signed, exact check of the inequality F_a(delta)>=2-a^2
        compare=(4-u)*(u-2*v)**2-u*(u-v)*(2-u)**2
        confirm(compare>=0,'squared endpoint inequality')
        confirm((compare==0)==(delta==u/2),'equality location')
        # Exact construction: for the minimal fixed-leg trapezoid p=1, q=1-a^2.
    p=F(1)
    q=1-u
    h2=u*(1-u/4)
    diag2=((p+q)/2)**2+h2
    confirm(diag2==1,'unit diagonals in equality model')
    confirm(q>=0,'positive short base except degenerate a=1')
    perim=p+q+2*a
    confirm(perim==2+2*a-u,'profile formula')
    if a>=F(1,2):
        confirm(perim>=F(11,4),'universal 11/4 bound within model')

# Independently implement inside-polygon test as half-plane cross products.
def inside(point, polygon, eps=1e-9):
    for A,B in zip(polygon,polygon[1:]+polygon[:1]):
        cross=(B[0]-A[0])*(point[1]-A[1])-(B[1]-A[1])*(point[0]-A[0])
        if cross < -eps: return False
    return True

def calc(a,delta,base_sum):
    p=base_sum/2+delta
    q=base_sum/2-delta
    h=sqrt(a*a-delta*delta)
    s=sqrt(1-a*a/4)
    poly=[(-p/2,0),(p/2,0),(q/2,h),(-q/2,h)]
    right=((p+q)/4 - s*h/a,h/2-s*delta/a)
    left=(-right[0],right[1])
    return poly,right,left

for a_num in range(2,20):
    a=a_num/20
    for j in range(0,21):
        delta=a*a*j/40
        h=sqrt(a*a-delta*delta)
        s=sqrt(1-a*a/4)
        Fbound=2*s*(a*a-2*delta*delta)/(a*h)
        for ds in (0,0.03,0.4):
            S=max(Fbound,2*delta)+ds
            if S<=2*delta: S+=0.1
            P,X,Y=calc(a,delta,S)
            confirm(inside(X,P) and inside(Y,P),'constructed witnesses are contained')
            B=P[1]
            C=P[2]
            A=P[0]
            D=P[3]
            confirm(isclose(sum((X[i]-B[i])**2 for i in range(2)),1,abs_tol=1e-10),'right witness B distance')
            confirm(isclose(sum((X[i]-C[i])**2 for i in range(2)),1,abs_tol=1e-10),'right witness C distance')
            confirm(isclose(sum((Y[i]-A[i])**2 for i in range(2)),1,abs_tol=1e-10),'left witness A distance')
            confirm(isclose(sum((Y[i]-D[i])**2 for i in range(2)),1,abs_tol=1e-10),'left witness D distance')
        if delta>0.0:
            # Narrow the base sum on purpose: the candidate must leave the left boundary.
            S=max(Fbound*0.99,2*delta+1e-5)
            if S<Fbound:
                P,X,Y=calc(a,delta,S)
                confirm(not inside(X,P) and not inside(Y,P),'sharp base-sum containment threshold')

# A direct exact witness at the unique global minimizer.
a=F(1,2);p=F(1);q=F(3,4);h2=F(15,64)
confirm(((p+q)/2)**2+h2==1,'sharp diagonal length exactly one')
confirm((p+q+2*a)==F(11,4),'sharp perimeter exactly 11/4')
print(f'PASS: {COUNT} exact polynomial/rational and independent geometric assertions')
