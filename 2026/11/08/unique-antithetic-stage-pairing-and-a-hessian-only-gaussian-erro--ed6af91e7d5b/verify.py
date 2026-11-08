#!/usr/bin/env python3
"""Self-contained algebra and numerical checks for antithetically paired randomized RK2.
Requires only Python's standard library. Finite checks illustrate, but do not prove, the asymptotic theorem.
"""
from fractions import Fraction as Q
from math import sin, cos, atan, tan, exp, isclose
import random

# Work with truncated power series of step h, keeping powers 0..4.
D=4
Z=Q(0)
def poly(*coeff): return tuple(list(map(Q, coeff))[:D+1]+[Z]*max(0,D+1-len(coeff)))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def mul(a,b): return tuple(sum((a[j]*b[i-j] for j in range(i+1)),Z) for i in range(D+1))
def scale(a,q): return tuple(q*x for x in a)
H=poly(0,1)
ONE=poly(1)

def rk_square(x,u):
    # f(x)=x^2; RK2(x,u)=x+h*(x+h*u*x^2)^2.
    stage=add(x,scale(mul(H,mul(x,x)),u))
    return add(x,mul(H,mul(stage,stage)))

def rk_linear(x,u,lam):
    # f(x)=lambda*x, polynomial exact.
    return mul(x,add(add(ONE,scale(H,lam)),scale(mul(H,H),u*lam*lam)))

checks=0
for x in [Q(1),Q(-2),Q(3,2)]:
    for u in [Q(0),Q(1,7),Q(1,2),Q(5,6),Q(1)]:
        z=rk_square(rk_square(poly(x),u),1-u)
        # f=x^2: Jf=2*x^3, A=4*x^4, H[f,f]=2*x^4;
        # exact flow at time 2h has coefficient (2h)^3*x^4=8h^3*x^4.
        xi=(1-u)**2-Q(1,3)
        expected=x**4*(Q(8)+Q(-4,3)+2*xi)
        assert z[0]==x and z[1]==2*x*x and z[2]==4*x**3
        assert z[3]==expected
        checks+=4
for lam in [Q(-2),Q(-1),Q(1,3),Q(2)]:
    for u in [Q(0),Q(1,7),Q(1,2),Q(1)]:
        z=rk_linear(rk_linear(ONE,u,lam),1-u,lam)
        assert z[0]==1
        assert z[1]==2*lam
        assert z[2]==2*lam**2
        assert z[3]==lam**3
        assert z[4]==u*(1-u)*lam**4
        checks+=5
# Exact uniform moments and continuum variance.
assert Q(1,5)-Q(1,9)==Q(4,45)
assert Q(1,30)-Q(1,36)==Q(1,180)  # E[U^2(1-U)^2]-E[U(1-U)]^2
assert Q(4,45)/2==Q(2,45)
assert Q(1,12)*2==Q(1,6)
checks+=4

y0=1.0; T=0.5
def sol(t): return 2*atan(exp(t)*tan(y0/2))
yT=sol(T)
def phi(t): return sin(yT)/sin(sol(t))
def A(t):
    y=sol(t)
    return cos(y)**2*sin(y)
def HH(t):
    y=sol(t)
    return -(sin(y)**3)
def simpson(fun, m=10000):
    assert m%2==0
    step=T/m
    return (fun(0.0)+fun(T)+4*sum(fun(j*step) for j in range(1,m,2))+2*sum(fun(j*step) for j in range(2,m,2)))*step/3
B=-simpson(lambda t:phi(t)*A(t))/6.0
sig2=2*simpson(lambda t:(phi(t)*HH(t))**2)/45
assert 0.015<sig2<0.019 and -0.014<B<-0.008
checks+=2
# Reproducible, bounded computational illustration, not evidence for an infinite limit.
rng=random.Random(20261107)
n=160; m=3000; h=T/(2*n)
values=[]
for rep in range(m):
    x=y0
    for k in range(n):
        u=rng.random()
        x=x+h*sin(x+h*u*sin(x))
        v=1-u
        x=x+h*sin(x+h*v*sin(x))
    values.append((x-yT-h*h*B)/h**2.5)
mean=sum(values)/m
variance=sum((z-mean)**2 for z in values)/(m-1)
assert abs(variance/sig2-1)<0.11, (variance,sig2)
checks+=1
# Nonlinear vector-field consistency check for the noncommutative Jacobian/Hessian terms.
# A fourth-order reference flow is stepped on a finer grid; this tests, but cannot prove,
# the leading vector local defect coefficient.
def vector_field(p):
    return (sin(p[0])+p[1], cos(p[1])-p[0])
def vec_add(a,b,scale=1.0):
    return (a[0]+scale*b[0],a[1]+scale*b[1])
def vector_rk2(p,h,u):
    return vec_add(p,vector_field(vec_add(p,vector_field(p),h*u)),h)
def vector_rk4(p,h):
    k1=vector_field(p)
    k2=vector_field(vec_add(p,k1,h/2))
    k3=vector_field(vec_add(p,k2,h/2))
    k4=vector_field(vec_add(p,k3,h))
    return (p[0]+h*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6,
            p[1]+h*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6)
p0=(0.2,-0.4); u=0.13
f0=vector_field(p0)
x,y=p0
jf=(cos(x)*f0[0]+f0[1], -f0[0]-sin(y)*f0[1])
A2=(cos(x)*jf[0]+jf[1],-jf[0]-sin(y)*jf[1])
H2=(-sin(x)*f0[0]**2,-cos(y)*f0[1]**2)
xi=(1-u)**2-1/3
prediction=tuple(-a/3+xi*b for a,b in zip(A2,H2))
for hh in (0.02,0.01,0.005):
    approx=vector_rk2(vector_rk2(p0,hh,u),hh,1-u)
    exact=p0
    for _ in range(50):
        exact=vector_rk4(exact,2*hh/50)
    measured=tuple((a-b)/hh**3 for a,b in zip(approx,exact))
    assert max(abs(a-b) for a,b in zip(prediction,measured))<hh*8
    checks+=1

print('PASS',checks,'exact algebra/moment and numerical diagnostic checks')
print(f'scalar sine benchmark: y(T)={yT:.15f}, B={B:.15f}, Sigma={sig2:.15f}')
print(f'monte carlo: n={n}, samples={m}, normalized mean={mean:.6f}, variance={variance:.6f}')
