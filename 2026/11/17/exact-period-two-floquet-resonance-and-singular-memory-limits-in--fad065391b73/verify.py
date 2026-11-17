#!/usr/bin/env python3
"""Finite reproducibility tests for an explicit fractional-logistic Floquet resonance."""
import math

def coefficients(q, m):
    out=[1.0]
    for j in range(1,m+1):
        out.append(out[-1]*(j-1-q)/j)
    return out

def resonance(q,m):
    g=coefficients(q,m)
    s=sum(g)
    t=sum(v*(-1)**j for j,v in enumerate(g))
    p=sum(v*(-1j)**j for j,v in enumerate(g))
    k=abs(t+1j*p)**2
    r1=1+2*s+t
    r2=1+s+math.sqrt((s+t)**2+k)
    return g,s,t,p,k,r1,r2

def check(q,m):
    g,s,t,p,k,r1,r=resonance(q,m)
    assert r>r1>1
    u=(r-1+t)/(2*r)
    v=math.sqrt((r-1+t)*(r-r1))/(2*r)
    x=[u+v,u-v]
    assert all(0<a<1 for a in x)
    for n in range(2):
        lhs=sum(gg*x[(n+1-j)%2] for j,gg in enumerate(g))
        rhs=r*x[n]*(1-x[n])-x[n]
        assert abs(lhs-rhs)<1e-10,(q,m,n,lhs-rhs)
    c=(1j*p).real
    d=(1j*p).imag
    y=[d,-(c+t+2*r*v),-d,c+t+2*r*v]
    assert math.hypot(y[0],y[1])>.01
    for n in range(4):
        lhs=sum(gg*y[(n+1-j)%4] for j,gg in enumerate(g))
        rhs=(r-1-2*r*x[n%2])*y[n]
        assert abs(lhs-rhs)<1e-8,(q,m,n,lhs-rhs)
    for offset in [-1e-3,1e-3]:
        rr=r+offset
        det=k-(rr-1+t)*(rr-r1)
        assert (det>0)==(offset<0)

cases=0
for q in [.2,.5,.8,1.0]:
    for m in [2,3,4,5,10,40]:
        check(q,m)
        cases+=1
for q in [.2,.5,.8]:
    T=2**q
    Z=(1+1j)**q
    R=1+math.sqrt(T*T+abs(T+1j*Z)**2)
    A=(1+T/(R-1))/math.gamma(1-q)
    for m in [300,3000,10000]:
        r=resonance(q,m)[-1]
        err=abs((r-R)*m**q-A)
        assert err < .3,(q,m,err)
    print('MEMORY_LIMIT',q,'R',format(R,'.12f'),'A',format(A,'.12f'))
assert abs(resonance(1,2)[-1]-(1+math.sqrt(6)))<1e-12
print('VERIFY_OK', 'four_phase_cases='+str(cases), 'asymptotic_orders=3', 'memory_lengths=3', 'endpoint_q1=1')
