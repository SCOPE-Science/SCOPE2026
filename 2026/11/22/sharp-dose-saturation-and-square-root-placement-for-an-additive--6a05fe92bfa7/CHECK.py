"""Numerical diagnostic for fixed-absolute-dose river oxygen-deficit theorem.

Standard-library only. All general assertions are proved in RESULT.md;
finite checks test the derived formulas and independently sample placement risks.
"""
import math
import random

checks=0

def check(test):
    global checks
    assert test
    checks+=1

def bisect(f,l,r,n=110):
    for _ in range(n):
        m=(l+r)/2
        if f(m)>0:r=m
        else:l=m
    return (l+r)/2

def setup(a,b,L):
    K=a*L/(b-a); tc=math.log(b/a)/(b-a)
    def g(t): return K*(math.exp(-a*t)-math.exp(-b*t))
    M=g(tc); ss=-math.log1p(-M/K)/(b-a); ds=g(ss)
    return K,tc,g,M,ss,ds

def downstream_peak(a,b,L,delta,s):
    K,tc,g,M,ss,ds=setup(a,b,L)
    applied=min(delta,g(s))
    P=K*math.exp(-a*s)
    Q=K*math.exp(-b*s)+applied
    y=max(0.0, math.log(b*Q/(a*P))/(b-a))
    return P*math.exp(-a*y)-Q*math.exp(-b*y)

def location(a,b,L,delta):
    K,tc,g,M,ss,ds=setup(a,b,L)
    if delta>=ds:return ss
    def diff(s):return g(s)-downstream_peak(a,b,L,delta,s)
    return bisect(diff,ss,tc)

def risk(a,b,L,delta,s):
    K,tc,g,M,ss,ds=setup(a,b,L)
    before=g(s) if s<=tc else M
    return max(before,downstream_peak(a,b,L,delta,s))

K,tc,g,M,ss,ds=setup(1,2,1)
check(abs(K-1)<1e-13);check(abs(tc-math.log(2))<1e-13)
check(abs(M-.25)<1e-13);check(abs(ss-math.log(4/3))<1e-13)
check(abs(ds-3/16)<1e-13)
for delta in [0.01,0.05,0.1,3/16,0.2,0.6]:
    s=location(1,2,1,delta)
    check(s>0 and s<tc)
    check(abs(risk(1,2,1,delta,s)-g(s))<1e-11)
    for x in range(1,401):
        candidate=2*tc*x/400
        check(risk(1,2,1,delta,candidate)>=g(s)-2e-12)
check(abs(location(1,2,1,0.1)-0.34997783284302425)<1e-12)
check(abs(risk(1,2,1,0.1,location(1,2,1,.1))-.20809639077514855)<1e-12)
for d in [1e-4,1e-5,1e-6]:
    diff=tc-location(1,2,1,d)
    scale=math.sqrt(2*d/(1*2*M))
    check(abs(diff/scale-1)<4*math.sqrt(d))

rng=random.Random(290721)
for _ in range(150):
    a=0.25+rng.random()*2.5
    b=a*(1.1+3.0*rng.random())
    L=0.2+rng.random()*12
    K,tc,g,M,ss,ds=setup(a,b,L)
    check(0<ss<tc and 0<ds<M)
    d=ds*(0.05+2*rng.random())
    s=location(a,b,L,d)
    check(0<s<tc)
    check(abs(risk(a,b,L,d,s)-g(s))<1e-9*max(1,M))
    for j in range(301):
        t=tc*j/150
        check(risk(a,b,L,d,t)>=risk(a,b,L,d,s)-2e-10*max(1,M))

print('PASS',checks,'diagnostic assertions')
