"""Exact rational checks for the planar dissipative-skew parallel-sum formulas.

This is a supplemental finite check of the displayed algebra, not a proof of
any universal assertion. The analytic argument is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt


def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def tr(A):
    return A[0][0]+A[1][1]

def det(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def adj(A):
    return ((A[1][1],-A[0][1]),(-A[1][0],A[0][0]))

def trans(A):
    return ((A[0][0],A[1][0]),(A[0][1],A[1][1]))

def sym(A):
    return tuple(tuple((A[i][j]+A[j][i])/2 for j in range(2)) for i in range(2))

def scalar(A,c):
    return tuple(tuple(c*A[i][j] for j in range(2)) for i in range(2))

def add(A,B):
    return tuple(tuple(A[i][j]+B[i][j] for j in range(2)) for i in range(2))

def inv(A):
    return scalar(adj(A),1/det(A))

I=((F(1),F(0)),(F(0),F(1)))
J=((F(0),F(-1)),(F(1),F(0)))

def P(v):
    return ((v[0]*v[0],v[0]*v[1]),(v[0]*v[1],v[1]*v[1]))

def v(z):
    return ((1-z*z)/(1+z*z),2*z/(1+z*z))

cases=0
for a,b,z,s1,s2 in product([F(1,2),F(1),F(3)], [F(1),F(2)],
                               [F(0),F(1,4),F(2,3)],
                               [F(-2),F(1,2)], [F(-1,2),F(3,2)]):
    e=(F(1),F(0)); u=v(z)
    M1=add(scalar(P(e),a),scalar(J,s1))
    M2=add(scalar(P(u),b),scalar(J,s2))
    assert det(M1)==s1*s1 and det(M2)==s2*s2
    A1=inv(M1); A2=inv(M2)
    for A in (A1,A2):
        assert det(sym(A))==0 and tr(sym(A))>0
    H=add(M1,M2)
    ss=s1+s2
    sin2=1-(u[0]*u[0])
    d=a*b*sin2+ss*ss
    assert det(H)==d
    S=add(scalar(P(e),a),scalar(P(u),b))
    assert sym(H)==S
    if d>0:
        Q=inv(H)
        assert mm(H,Q)==I and mm(Q,H)==I
        assert sym(Q)==scalar(adj(S),1/d)
        assert tr(mm(trans(H),H))==(a+b)**2-2*a*b*sin2+2*ss*ss
        # Analytic singular-value identity checked after squaring:
        # (sigma_max + sigma_min)^2 = tr(H^T H)+2det H,
        # (sigma_max - sigma_min)^2 = tr(H^T H)-2det H.
        assert tr(mm(trans(H),H))+2*d==(a+b)**2+4*ss*ss
        assert tr(mm(trans(H),H))-2*d==(a-b)**2+4*a*b*(u[0]**2)
        resolvent=mm(H,inv(add(I,H)))
        assert resolvent==add(I,scalar(inv(add(I,H)),F(-1)))
    else:
        assert z==0 and ss==0
        assert H==scalar(P(e),a+b)
    cases+=1

# Probe the sharp norm and resolvent asymptotics along two paths.
for h in (1e-2, 1e-3, 1e-4):
    a,b,s0=1.5,2.5,1.0
    from math import cos,sin
    theta=h; s=h
    C=cos(theta); D=sin(theta)
    S=((a+b*C*C,b*C*D),(b*C*D,b*D*D))
    H=((S[0][0],S[0][1]-s),(S[1][0]+s,S[1][1]))
    delta=a*b*D*D+s*s
    norm=(sqrt((a+b)**2+4*s*s)+sqrt((a-b)**2+4*a*b*C*C))/(2*delta)
    assert abs(norm*delta/(a+b)-1)<20*h*h
    from numpy.linalg import norm as npnorm
    import numpy as np
    H0=np.diag([a+b,0.0]); N=np.array(H)
    R=N@np.linalg.inv(np.eye(2)+N)
    R0=H0@np.linalg.inv(np.eye(2)+H0)
    expected=(b*abs(theta)+abs(s))/(1+a+b)
    assert abs(npnorm(R-R0,2)/expected-1)<10*h

print('OK: %d exact-rational cases and 3 asymptotic probes' % cases)
