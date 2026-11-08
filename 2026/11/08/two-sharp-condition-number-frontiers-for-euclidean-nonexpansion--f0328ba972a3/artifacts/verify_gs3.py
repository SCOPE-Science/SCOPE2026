#!/usr/bin/env python3
"""Independent exact-polynomial and deterministic checks for a three-coordinate Gauss--Seidel benchmark."""
from fractions import Fraction as F
from math import sqrt
from random import Random

N = 0

def check(cond, message='assertion'):
    global N
    N += 1
    assert cond, message

def trim(p):
    p = tuple(p)
    while len(p)>1 and p[-1]==0:
        p=p[:-1]
    return p

def add(a,b):
    return trim([ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def neg(a): return tuple(-x for x in a)
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    v=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):v[i+j]+=x*y
    return trim(v)
def ev(a,r):return sum(x*r**i for i,x in enumerate(a))
def matmul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def transpose(a):return [list(t) for t in zip(*a)]
def gram(b):return matmul(transpose(b),b)

z=(0,);one=(1,);r=(0,1);rr=mul(r,r)
B=[[z,neg(r),neg(r)],
   [z,rr,mul(r,sub(r,one))],
   [z,mul(rr,sub(one,r)),mul(rr,sub((2,),r))]]
# Check B=-(D+L)^{-1}U by (D+L)B+U=0 as a polynomial identity.
L=[[one,z,z],[r,one,z],[r,r,one]]
U=[[z,r,r],[z,z,r],[z,z,z]]
for i in range(3):
    for j in range(3):
        lhs=U[i][j]
        for k in range(3): lhs=add(lhs,mul(L[i][k],B[k][j]))
        check(lhs==z,'sweep identity')
Gt=[[z]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        val=z
        for k in range(3): val=add(val,mul(B[k][i],B[k][j]))
        Gt[i][j]=val
trace=add(Gt[1][1],Gt[2][2])
det=sub(mul(Gt[1][1],Gt[2][2]),mul(Gt[1][2],Gt[2][1]))
S=(3,-2,7,-6,2)
expected_trace=mul(rr,S)
expected_det=mul(mul(rr,rr),(1,0,2))
P=(-1,-1,2,0,6)
expected_ide=mul(sub(r,one),P)
check(trace==expected_trace,'trace polynomial')
check(det==expected_det,'det polynomial')
check(sub(sub(one,trace),neg(det))==expected_ide,'det(I-G) polynomial')
# Nonzero characteristic polynomial: lambda^2 - trace(B) lambda + det(B22).
trb=add(B[1][1],B[2][2]); db=sub(mul(B[1][1],B[2][2]),mul(B[1][2],B[2][1]))
check(trb==(0,0,3,-1),'trace B')
check(db==(0,0,0,1),'det B')
# Derivative second derivative convexity and certified rational root intervals.
Pm=F(-4290,10000);Pmp=F(-4289,10000)
Pp=F(6150,10000);Ppp=F(6151,10000)
check(ev(P,Pm)>0 and ev(P,Pmp)<0,'negative root bracket')
check(ev(P,Pp)<0 and ev(P,Ppp)>0,'positive root bracket')
check(ev(P,F(-1,2))>0 and ev(P,F(0))<0 and ev(P,F(1))>0,'domain root signs')
check(ev(P,F(2,3))>0,'2/3 bound')
for k in range(-499,1000):
    x=F(k,1000)
    if x>=1:continue
    G=[[ev(Gt[i][j],x) for j in (1,2)] for i in (1,2)]
    T=G[0][0]+G[1][1]
    D=G[0][0]*G[1][1]-G[0][1]**2
    ID=(1-G[0][0])*(1-G[1][1])-G[0][1]**2
    check(T==ev(expected_trace,x) and D==ev(expected_det,x) and ID==ev(expected_ide,x),'exact Gram')
    try:
        norm2=float((T+sqrt(float(T*T-4*D)))/2)
    except ValueError:
        norm2=float(T/2)
    if x<Pm or x>Ppp:
        check(norm2>1 if (x<-.429 or x>.616) else True,'outer expansion')
    if Pmp<x<Pp:
        check(norm2<1+1e-12,'interior contraction')
# Direct independent forward coordinate updates and singular norm bounds.
rng=Random(20261101)
for _ in range(2500):
    x=F(rng.randint(-499,999),1000)
    vec=[F(rng.randint(-100,100),rng.randint(1,100)) for i in range(3)]
    A=[[F(1) if i==j else x for j in range(3)] for i in range(3)]
    u=vec[:]
    for i in range(3):
        u[i]=-sum(A[i][j]*u[j] for j in range(3) if j!=i)
    bx=[sum(ev(B[i][j],x)*vec[j] for j in range(3)) for i in range(3)]
    check(u==bx,'direct sweep')
# Numeric asymptotics near the identity, including phi limit.
phi=(1+sqrt(5))/2
for eps in (1e-4,1e-5,1e-6):
    for sig in (-1,1):
        x=sig*eps
        T=float(ev(expected_trace,x));D=float(ev(expected_det,x))
        g=(T+sqrt(max(0,T*T-4*D)))/2
        check(abs(sqrt(g)/eps-phi)<2e-4,'golden ratio first-order norm')
print('VERIFY_OK',N,'exact/independent checks')
