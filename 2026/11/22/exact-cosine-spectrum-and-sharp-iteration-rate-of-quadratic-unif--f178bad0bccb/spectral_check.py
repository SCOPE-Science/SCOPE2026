"""Reproducible checks of the quadratic Schoenberg–Greville spectral formula.
No external Python dependencies. Run: python spectral_check.py.
Finite checks supplement, not replace, the analytical proof.
"""
from fractions import Fraction as F
from math import pi, sin, cos, isclose
from random import Random


def knots(n):
    return [F(0)]*3 + [F(i,n) for i in range(1,n)] + [F(1)]*3

def greville(t):
    return [(t[i+1]+t[i+2])/2 for i in range(len(t)-3)]

def basis(t,x):
    p0=[F(1) if t[i]<=x<t[i+1] else F(0) for i in range(len(t)-1)]
    if x==1:
        return [F(0)]*(len(t)-4)+[F(1)]
    for deg in (1,2):
        out=[]
        for i in range(len(p0)-1):
            l=F(0) if t[i+deg]==t[i] else (x-t[i])/(t[i+deg]-t[i])*p0[i]
            r=F(0) if t[i+deg+1]==t[i+1] else (t[i+deg+1]-x)/(t[i+deg+1]-t[i+1])*p0[i+1]
            out.append(l+r)
        p0=out
    return p0

def matrix(n):
    t=knots(n); nodes=greville(t)
    return [[a for a in basis(t,x)] for x in nodes],nodes

def multiply(a,b):
    return [sum(aij*bj for aij,bj in zip(row,b)) for row in a]

def check(n):
    M,nodes=matrix(n)
    assert len(M)==n+2
    for i,row in enumerate(M):
        assert sum(row)==1 and all(x>=0 for x in row)
        assert sum(row[j]*nodes[j] for j in range(n+2))==nodes[i]
        expect=[F(0)]*(n+2)
        if i==0 or i==n+1: expect[i]=1
        else:
            expect[i]=F(5,8) if i==1 or i==n else F(3,4)
            expect[i-1]=F(1,4) if i==1 else F(1,8)
            expect[i+1]=F(1,4) if i==n else F(1,8)
        assert row==expect, (n,i,row,expect)
    T=[row[1:n+1] for row in M[1:n+1]]
    for j in range(1,n+1):
        theta=j*pi/n
        v=[sin((i-F(1,2))*theta) for i in range(1,n+1)]
        lam=(3+cos(theta))/4
        Tv=[sum(float(tij)*vj for tij,vj in zip(row,v)) for row in T]
        assert all(isclose(a,lam*b,abs_tol=4e-13,rel_tol=5e-13) for a,b in zip(Tv,v)),(n,j,Tv)
        vnorm=sum(vi*vi for vi in v)
        target=n if j==n else n/2
        assert isclose(vnorm,target,rel_tol=4e-13,abs_tol=4e-13)
    rng=Random(21821+n)
    for _ in range(4):
        y=[F(rng.randint(-9,9),rng.randint(1,12)) for _ in range(n+2)]
        d=[float(y[i]-(1-nodes[i])*y[0]-nodes[i]*y[-1]) for i in range(1,n+1)]
        td=d[:]
        for m in range(1,8):
            if m>1: td=[sum(float(a)*u for a,u in zip(row,td)) for row in T]
            coefficients=[0.]*n
            for j in range(1,n+1):
                theta=j*pi/n;v=[sin((i-.5)*theta) for i in range(1,n+1)]
                lam=(3+cos(theta))/4
                proj=sum(a*b for a,b in zip(d,v))/(n if j==n else n/2)
                coefficients=[ci+lam**(m-1)*proj*vi for ci,vi in zip(coefficients,v)]
            assert all(isclose(a,b,rel_tol=3e-11,abs_tol=3e-11) for a,b in zip(coefficients,td)),(n,m)
    return True

if __name__=='__main__':
    for n in range(2,49): check(n)
    print('PASS: n=2..48; 47 exact-rational collocation/affine checks, 1175 eigenmodes, 1316 power-expansion checks.')
