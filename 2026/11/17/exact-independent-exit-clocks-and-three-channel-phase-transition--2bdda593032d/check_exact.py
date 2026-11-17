#!/usr/bin/env python3
"""Exact rational verification for exit channels of a planar absolute-value map.

No external packages.  Tests rational parameters spanning every polygon regime,
then checks complete original-coordinate iterates and centered branch formulas.
Finite samples corroborate, but do not replace, the universal polygon proof.
"""
from fractions import Fraction as F
from itertools import product

def area(poly):
    if len(poly)<3: return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])))/2

def clip(poly,a,b,c):
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp=a*p[0]+b*p[1]-c
        fq=a*q[0]+b*q[1]-c
        if fp<=0: out.append(p)
        if fp*fq<0:
            out.append(tuple((fq*p[k]-fp*q[k])/(fq-fp) for k in range(2)))
    result=[]
    for p in out:
        if p not in result: result.append(p)
    return result

def matmul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

A=((-1,-1),(1,-1))

def survivors(n,t):
    M=((1,0),(0,1))
    poly=[(F(-100000),F(-100000)),(F(100000),F(-100000)),(F(100000),F(100000)),(F(-100000),F(100000))]
    for _ in range(n):
        poly=clip(poly,M[0][0],M[0][1],F(1))
        poly=clip(poly,-M[1][0],-M[1][1],t)
        M=matmul(A,M)
    return poly

def inv(p): return tuple(((-p[0]+p[1])/2,(-p[0]-p[1])/2))

def cval(t):
    if t<=F(1,3): return 25*t*t/8
    if t<2: return (-2*t*t+18*t-3)/8
    return F(25,8)

def dval(t):
    if t<=F(1,3): return 25*t*t/16
    if t<2: return (2-t)*(11*t-2)/16
    return F(0)

def eval_(t):
    if t<=F(1,3) or t>=2:return F(0)
    if t<=F(3,4):return (3*t-1)**2/16
    return (2-t)*(7*t-4)/16

def mapped(poly): return sorted(map(inv,poly))

def original_map(z,a,b):
    x,y=z
    return abs(x)-y+a,x-abs(y)+b

cases=sorted(set([F(x,30) for x in range(1,91)]+[F(1,3),F(3,4),F(2),F(1,100),F(99,10),F(100,1)]))
for t in cases:
    p=survivors(3,t)
    d=clip(p,F(1),F(1),-t/2)
    e=clip(d,F(-1),F(1),-F(1,2))
    r=clip(p,F(-1),F(1),-F(1,2))
    assert area(p)==cval(t),(t,'c',area(p),cval(t))
    assert area(d)==dval(t),(t,'d',area(d),dval(t))
    assert area(e)==eval_(t),(t,'e',area(e),eval_(t))
    assert area(r)==cval(t)/2-dval(t)+eval_(t)
    assert area(d)-area(e)>=0 and area(r)-area(e)>=0
    assert area(d)+area(r)-area(e)==area(p)/2
    for n in range(3,12):
        p_n=survivors(n,t)
        p_next=survivors(n+1,t)
        assert sorted(p_next)==mapped(p_n),(t,n,p_next,mapped(p_n))
        assert area(p_n)==area(p)/2**(n-3)
# At the exceptional ratio t=2 the inverse similarity starts one visit earlier.
assert sorted(survivors(3,F(2)))==mapped(survivors(2,F(2)))
for t in [F(1,2),F(19,10),F(201,100),F(5)]:
    assert sorted(survivors(3,t))!=mapped(survivors(2,t))
# Separately check the actual nonlinear F_{a,b} on exact orbits that stay in Q2.
for a,b in [(-F(1),F(1)),(-F(1),F(2)),(-F(1),F(3)),(F(0),F(2)),(F(1),F(3)),(F(2),F(7))]:
    alpha=(b-2*a)/5; beta=(a+2*b)/5
    assert alpha>0 and beta>0
    q=(-alpha,beta)
    for u,v in product([F(-1,20),F(0),F(1,20)],repeat=2):
        x,y=q[0]+u*alpha,q[1]+v*alpha
        assert x<0<y
        p=original_map((x,y),a,b)
        assert p==(q[0]-alpha*(u+v),q[1]+alpha*(u-v))
print('THREE_CHANNEL_EXACT_RATIONAL_CHECK_OK cases=%d polygon_steps=9 original_branch_cases=54'%len(cases))
