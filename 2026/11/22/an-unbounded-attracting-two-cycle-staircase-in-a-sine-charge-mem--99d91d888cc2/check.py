#!/usr/bin/env python3
"""Reproducibility diagnostics for two-cycle sink staircase in a sine-charge map.
These are finite checks; the analytical argument is in RESULT.md.
Requires sympy and mpmath.
"""
import math
import mpmath as mp
import sympy as sp

q=sp.symbols('q', real=True)
J=sp.Matrix([[-1,q],[1,1]])
assert sp.simplify(J**2-(1+q)*sp.eye(2))==sp.zeros(2)
Jrev=sp.Matrix([[-1,-q],[1,1]])
assert sp.simplify(Jrev*J-sp.Matrix([[1-q,-2*q],[0,1+q]]))==sp.zeros(2)

mp.mp.dps=65
K=mp.mpf('1.01'); h=K/2; gamma=mp.mpf(2); k=mp.mpf('0.1')
theta=mp.acos(1/K); t=mp.sqrt(K*K-1)
r=(1/t-theta)/mp.pi
num=0 if r<=0 else int(mp.ceil(r))
assert num==3, (r,num)
C=k/mp.log(3)

def f(x,y,z,mu):
    def g(v):return k*mp.cos(4*mu*gamma*mp.pi*v*(1-v))/mp.log(3-4*mu*v*(1-v))
    return (g(x)+h*mp.sin(z)*(x-y),g(y)-h*mp.sin(z)*(x-y),z+x-y)

def res(x,y,z,mu):
    a,b,c=f(x,y,z,mu)
    d,e,g=f(a,b,c,mu)
    return d-x,e-y,g-z

def mat(x,y,z,mu):
    def der(v):return mp.diff(lambda u: k*mp.cos(4*mu*gamma*mp.pi*u*(1-u))/mp.log(3-4*mu*u*(1-u)),v)
    s=h*mp.sin(z); d=h*mp.cos(z)*(x-y)
    return mp.matrix([[der(x)+s,-s,d],[-s,der(y)+s,-d],[1,-1,1]])

for n in range(num):
    z0=-mp.pi/2+theta
    L=2*(theta+mp.pi*n)
    d0=-L
    x0=C+d0/2; y0=C-d0/2
    residual=res(x0,y0,z0,mp.mpf('0'))
    assert max(map(abs,residual))<mp.mpf('1e-50')
    x1,y1,z1=f(x0,y0,z0,mp.mpf('0'))
    assert abs(z1-(-mp.pi/2-theta-2*mp.pi*n))<mp.mpf('1e-55')
    lam=1-2*t*(theta+mp.pi*n)
    M=mat(x1,y1,z1,mp.mpf('0'))*mat(x0,y0,z0,mp.mpf('0'))
    # Trace and determinant are basis-invariant; the full 3D characteristic polynomial is lambda*(lambda-lam)**2.
    charval=[mp.det(M-u*mp.eye(3)) for u in [mp.mpf('0'),mp.mpf('0.2'),mp.mpf('1')]]
    for u,v in zip([mp.mpf('0'),mp.mpf('0.2'),mp.mpf('1')],charval):
        assert abs(v-(-u*(lam-u)**2))<mp.mpf('1e-55')
    assert abs(lam)<1
    mu=mp.mpf('0.000001')
    root=mp.findroot(lambda x,y,z:res(x,y,z,mu),(x0,y0,z0),tol=mp.mpf('1e-45'),maxsteps=70)
    xr,yr,zr=root
    a,b,c=f(xr,yr,zr,mu)
    Mpos=mat(a,b,c,mu)*mat(xr,yr,zr,mu)
    ev=mp.eig(Mpos,left=False,right=False)
    assert max(abs(e) for e in ev)<1, (n,ev)
    assert abs(a-xr)+abs(b-yr)+abs(c-zr)>mp.mpf('0.01')
    print('n=',n,'lam0=',mp.nstr(lam,15),'mu=',mp.nstr(mu),'max_|eig|=',mp.nstr(max(abs(e) for e in ev),14),'norm_res=',mp.nstr(max(abs(v) for v in res(xr,yr,zr,mu)),4))

for Kvalue in ['1.00005','1.001','1.01','1.1','1.5','2.0']:
 Kx=mp.mpf(Kvalue); ax=mp.acos(1/Kx);tx=mp.sqrt(Kx*Kx-1)
 n=max(0,int(mp.ceil((1/tx-ax)/mp.pi)))
 sinks=sum(1 for j in range(n+3) if tx*(ax+mp.pi*j)<1)
 assert n==sinks
 print('K',Kvalue,'sink_count',n)
print('PASS: exact symbolic blocks, 3 hyperbolic sinks and positive-input continuations, staircase counts')
