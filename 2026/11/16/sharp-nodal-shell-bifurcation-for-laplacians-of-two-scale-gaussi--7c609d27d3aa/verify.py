#!/usr/bin/env python3
"""Supplementary numerical and algebraic spot checks for Gaussian heat-mixture nodal shells.
All inputs and thresholds are specified here; no external data or libraries are needed.
These checks supplement, but do not replace, the theorem's proof.
"""
import math

def vc(d):
    b = math.sqrt(1 + 2/d) + math.sqrt(2/d)
    return b*b

def logq(y, d, v):
    return 0.5*(d+4)*math.log(v)+math.log(y-d)-math.log(d*v-y)-0.5*(1-1/v)*y

def logq_derivative(y,d,v):
    D=0.5*d*(v-1)
    h=y-0.5*d*(1+v)
    C=D*D-2*d*v
    return (v-1)*(h*h-C)/(2*v*(D*D-h*h))

def limits(d,v):
    C=(d*(v-1)/2)**2-2*d*v
    if C<=0: return None
    center=d*(1+v)/2
    lo,hi=center-math.sqrt(C),center+math.sqrt(C)
    return lo,hi,math.exp(logq(lo,d,v)),math.exp(logq(hi,d,v))

def target_roots(d,v,w):
    split=limits(d,v)
    lo=d;hi=d*v
    cuts=[lo]
    if split: cuts.extend(split[:2])
    cuts.append(hi)
    def h(y):return logq(y,d,v) - math.log((1-w)/w)
    ans=[]
    for a,b in zip(cuts[:-1],cuts[1:]):
        tiny=1e-10*(b-a)
        aa=max(a+tiny,d+1e-13)
        bb=min(b-tiny,d*v-1e-13)
        if h(aa)*h(bb)>0:continue
        left,right=aa,bb
        for _ in range(70):
            mid=(left+right)/2
            if h(left)*h(mid)<=0:right=mid
            else:left=mid
        ans.append((left+right)/2)
    return ans

def radial_delta(y,d,v,w):
    # a=1 and b=sqrt(v); common (2*pi)^(-d/2) removed.
    return (w*(y-d)*math.exp(-y/2)
           +(1-w)*v**(-(d+4)/2)*(y-d*v)*math.exp(-y/(2*v)))

def cusp_const(d):
    v=vc(d)
    qc=math.exp(0.5*(d+4)*math.log(v)-d*(v*v-1)/(4*v))
    gamma=d*math.sqrt(2*d+4)
    return qc/(1+qc)**2*(v-1)/(3*d*v*v)*gamma**1.5

checks=0
for d in (1,2,3,4,7,12,30):
    c=vc(d)
    assert abs(d*(c-1)**2-8*c)<1e-11
    checks+=1
    for v in (1.01,0.8*c,1.2*c,1.5*c,3*c):
        if v<=1: continue
        for fraction in (0.1,0.21,0.44,0.62,0.8,0.93):
            y=d+(d*v-d)*fraction
            h=1e-5*min(y-d,d*v-y)
            numeric=(logq(y+h,d,v)-logq(y-h,d,v))/(2*h)
            expected=logq_derivative(y,d,v)
            assert abs(numeric-expected)<1e-6*max(1,abs(expected)), (d,v,y,numeric,expected)
            checks+=1
    # Finite regimes: one shell both below threshold and above threshold outside window.
    for v in (1.1,0.95*c,1.2*c):
        if v<=1:continue
        for w in (0.002,0.99):
            roots=target_roots(d,v,w)
            assert len(roots)==1, (d,v,w,roots)
            for y in roots:
                assert abs(radial_delta(y,d,v,w))<1e-9
            checks+=1
    # Three-shell phase, including the exact boundaries as double roots.
    v=1.2*c
    a,b,Qmax,Qmin=limits(d,v)
    assert d<a<b<d*v and Qmax>Qmin>0
    wmin=1/(1+Qmax); wmax=1/(1+Qmin)
    for t in (0.2,0.5,0.8):
        w=wmin+t*(wmax-wmin)
        roots=target_roots(d,v,w)
        assert len(roots)==3,(d,v,w,roots)
        assert roots[0]<a<roots[1]<b<roots[2]
        for y in roots:
            assert abs(logq(y,d,v)-math.log((1-w)/w))<1e-11
        checks+=1
    # Analytic multiplicity: logQ_y vanishes at both critical radii,
    # and logQ has a strict maximum/minimum there.
    assert abs(logq_derivative(a,d,v))<1e-10
    assert abs(logq_derivative(b,d,v))<1e-10
    h=1e-4*min(a-d,b-a,d*v-b)
    assert logq(a,d,v)>logq(a-h,d,v) and logq(a,d,v)>logq(a+h,d,v)
    assert logq(b,d,v)<logq(b-h,d,v) and logq(b,d,v)<logq(b+h,d,v)
    checks+=1
    # Cusp leading coefficient at variance-ratio threshold.
    for eps in (0.01,0.003,0.0008):
        v=c+eps
        _,_,Qmax,Qmin=limits(d,v)
        width=1/(1+Qmin)-1/(1+Qmax)
        relative=width/(cusp_const(d)*eps**1.5)
        assert abs(relative-1)<0.025,(d,eps,relative)
        checks+=1
print('PASS: %d numerical/algebraic checks (including all seven dimension samples).' % checks)
