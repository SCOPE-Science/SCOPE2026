"""Exact rational checks for the triangle-only two-community mean-field model.

Run: python3 verify.py
No third-party dependencies. These finite checks supplement the written proof.
"""
from fractions import Fraction as Q
from math import sqrt


def add(u, v):
    return u[0]+v[0], u[1]+v[1]


def neg(u):
    return -u[0], -u[1]


def sub(u, v):
    return add(u, neg(v))


def mul(u, v, r):
    return u[0]*v[0]+r*u[1]*v[1], u[0]*v[1]+u[1]*v[0]


def scalar(a):
    return Q(a), Q(0)


def polynomial_equilibrium(e, m):
    z2 = m*m*(2*e*(1-m)-1)/(e*(1-2*m))
    if not 0 < z2 < m*m or not m < Q(1,2):
        return False
    den = (1-m)**2-z2
    lam = 1/(2*e*m*den)
    x, y = (m,Q(1)), (m,Q(-1))
    one = scalar(1)
    def L(a, b):
        t = add(a,b)
        quad = sub(sub(mul(scalar(3),mul(a,a,z2),z2),mul(scalar(2),mul(a,b,z2),z2)),mul(b,b,z2))
        return mul(scalar(lam/4),add(mul(t,t,z2),mul(scalar(e),quad,z2)),z2)
    Lx,Ly=L(x,y),L(y,x)
    F1=add(neg(x),mul(sub(one,x),Lx,z2))
    F2=add(neg(y),mul(sub(one,y),Ly,z2))
    assert F1==(0,0) and F2==(0,0), (e,m,z2,F1,F2)
    def dxL(a,b):
        return mul(scalar(lam/4),add(mul(scalar(2),add(a,b),z2),mul(scalar(e),sub(mul(scalar(6),a,z2),mul(scalar(2),b,z2)),z2)),z2)
    def dyL(a,b):
        return mul(scalar(lam/2*(1-e)),add(a,b),z2)
    J11=add(sub(neg(one),Lx),mul(sub(one,x),dxL(x,y),z2))
    J12=mul(sub(one,x),dyL(x,y),z2)
    J21=mul(sub(one,y),dyL(y,x),z2)
    J22=add(sub(neg(one),Ly),mul(sub(one,y),dxL(y,x),z2))
    tr=add(J11,J22)
    det=sub(mul(J11,J22,z2),mul(J12,J21,z2))
    D=3*e*m*m-4*e*m+e+m*m
    T=e*(2*m*m-m-1)+2*m*m-m+1
    P=e*(12*m**3-17*m*m+8*m-1)+4*m**3-3*m*m
    assert tr==(T/D,0) and det==((2*e*(1-m)-1)*P/(D*D),0), (e,m,tr,det)
    return (lam,tr[0],det[0])


count=0
stable=0
saddle=0
for e_num in range(51,100,2):
    e=Q(e_num,100)
    for m_num in range(10,50):
        m=Q(m_num,100)
        if m>=Q(1,2): continue
        if 2*e*(1-m)<=1: continue
        ans=polynomial_equilibrium(e,m)
        if not ans: continue
        count+=1
        if ans[2]>0:
            stable+=1
            assert ans[1]<0
        else:
            saddle+=1
# A transparent rational interior stable witness.
lam,tr,det=polynomial_equilibrium(Q(9,10),Q(1,3))
assert (lam,tr,det)==(Q(9,2),Q(-1),Q(6,25))
# The exact threshold is f_*=(9+24sqrt(3))/61.
fstar=(9+24*sqrt(3))/61
assert 0.829003596 < fstar < 0.829003597
assert stable>0 and saddle>0 and count>100
print(f"PASS: {count} exactly evaluated interior asymmetric equilibria, {stable} stable, {saddle} saddle; exact witness lambda=9/2, trace=-1, determinant=6/25")
