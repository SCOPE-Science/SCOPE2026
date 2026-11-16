#!/usr/bin/env python3
"""Reproducible checks for exact local expansion of a three-tone evaluation kernel.
Uses only the Python standard library. Finite tests supplement an analytic proof.
"""
from fractions import Fraction as F
from math import factorial, sin, cos, pi, sqrt, isclose

def add(a,b):
    n=max(len(a),len(b));return [(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(n)]
def scale(a,c):return [z*c for z in a]
def mul(a,b,n=7):
    out=[F(0)]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<n:out[i+j]+=x*y
    return out

def div_power(num,den,p,degree=2):
    assert all(z==0 for z in den[:p]) and den[p]!=0
    if len(num)<p+degree+1:raise ValueError('insufficient numerator order')
    q=[]
    for i in range(degree+1):
        val=num[p+i]-sum(q[j]*den[p+i-j] for j in range(i))
        q.append(val/den[p])
    return q

def expected(y):
    p=175*y**3-115*y**2+9*y-5
    q=11025*y**4-12180*y**3-1530*y**2+2028*y+145
    return [F(9,4)*(5*y*y-2*y+1),-F(3,280)*p,q/F(78400)]

def actual(x):
    n=7
    s=[F((-1)**k,factorial(2*k+1)) for k in range(n)]
    s2=[F((-1)**k*2**(2*k),factorial(2*k+1)) for k in range(n)]
    c=[F((-1)**k, factorial(2*k))*x**(2*k) for k in range(n)]
    one=[F(1)]+[F(0)]*(n-1)
    a=scale(add(one,s2),F(1,2));b=scale(add(one,scale(s2,-1)),F(1,2))
    even_num=add(add(a,scale(mul(s,c,n),-2)),mul(c,c,n))
    even_den=add(a,scale(mul(s,s,n),-1))
    odd_num=add(one,scale(mul(c,c,n),-1))
    even=div_power(even_num,even_den,2)
    odd=div_power(odd_num,b,1)
    return [even[i]+odd[i] for i in range(3)]

def leverage(d,x):
    s=sin(d)/d;s2=sin(2*d)/(2*d)
    A=(1+s2)/2-s*s; B=(1-s2)/2
    assert A>0 and B>0
    return 1+(cos(d*x)-s)**2/A+sin(d*x)**2/B

def verify():
    sample_x=[F(0),F(1,10),F(1,4),F(1,2),F(3,5),F(4,5),F(7,8),F(1)]
    for x in sample_x:
        a=actual(x); e=expected(x*x)
        assert a==e,(x,a,e)
    # Exact polynomial root and fourth-order sign certificates at a rational bracket.
    P=lambda y:175*y**3-115*y**2+9*y-5
    Q=lambda y:11025*y**4-12180*y**3-1530*y**2+2028*y+145
    lo=F(645,1000);hi=F(646,1000)
    assert P(lo)<0<P(hi)
    assert Q(lo)<0 and Q(hi)<0
    for y in [lo,hi,F(3,5),F(1)]:
        R=6675*y*y-3246*y-5
        assert Q(y)==(63*y-F(141,5))*P(y)-F(4,5)*R
    assert P(F(3,5))<0 and (6675*F(3,5)**2-3246*F(3,5)-5)>0
    # Independent fixed-gap evaluation via orthogonal basis and a 3-by-3 Gram inverse.
    # Explicit inversion by direct Gaussian elimination on real (1,cos,sin) basis.
    checks=0
    def solve(mat,b):
        M=[list(map(float,mat[i]))+[float(b[i])] for i in range(3)]
        for j in range(3):
            k=max(range(j,3),key=lambda i:abs(M[i][j]));M[j],M[k]=M[k],M[j]
            u=M[j][j];assert abs(u)>1.e-12
            for l in range(j,4):M[j][l]/=u
            for i in range(3):
                if i!=j:
                    u=M[i][j]
                    for l in range(j,4):M[i][l]-=u*M[j][l]
        return [M[i][3] for i in range(3)]
    for d in [.2,.35,.5,.8,1,1.5,2,3,4.9,6,8,12]:
        s=sin(d)/d; s2=sin(2*d)/(2*d)
        G=[[1,s,0],[s,(1+s2)/2,0],[0,0,(1-s2)/2]]
        for x in [0,.1,.25,.5,.75,.803739,.9,1]:
            v=[1,cos(d*x),sin(d*x)]
            w=solve(G,v)
            independent=sum(v[i]*w[i] for i in range(3))
            assert isclose(independent,leverage(d,x),rel_tol=2.e-9,abs_tol=2.e-9),(d,x)
            checks+=1
    print('PASS',len(sample_x),'exact rational Taylor certificates;',checks,'independent Gram checks; rational root bracket')

if __name__=='__main__':verify()
