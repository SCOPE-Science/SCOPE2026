"""Independent finite diagnostics for an exact Hardy-space q-Berezin power law.

Finite samples supplement but do not certify asymptotic or universal statements.
Dependencies: Python standard library plus NumPy and SciPy.
"""
import math
import numpy as np
from scipy.optimize import brentq

count = 0

def check(condition, label):
    global count
    if not condition:
        raise AssertionError(label)
    count += 1


def poly(m, a, k, s):
    return (m-(m-1)*(1-a)*k*s-(m+2+a*(m-2))*s*s
            +(m+1)*(1-a)*k*s**3+m*a*s**4)


def F(m, a, q, s):
    k = math.sqrt(max(0.,1-q*q))
    return q*s**m*(1-s*s)/(1-(1-a)*k*s-a*s*s)


def root(m,a,q):
    k=math.sqrt(max(0.,1-q*q))
    h=k/(1+q)
    return brentq(lambda x:poly(m,a,k,x),h,1,xtol=3e-15)


def direct(m,a,q,s):
    k=math.sqrt(max(0.,1-q*q))
    r=(s-k)/(1-k*s)
    return q*s**m*(1-r*s)/(1-a*r*s)

for m in range(1,34):
    for a in (0.,.03,.2,.5,.89,.995):
        for q in (.08,.2,.5,.8,.999,1.):
            k=math.sqrt(max(0.,1-q*q))
            h=k/(1+q)
            x=root(m,a,q)
            check(h<x<1,'root location')
            check(abs(poly(m,a,k,x))<5e-9,'polynomial residual')
            check(abs(F(m,a,q,x)-direct(m,a,q,x))<4e-10,'kernel-value identity')
            samples=np.linspace(h,1-1e-9,350)
            check(F(m,a,q,x)>=max(F(m,a,q,float(z)) for z in samples)-5e-10,'sample global peak')
            phase=q*q-(1-a)/(m+1-a)
            if abs(phase)>1e-7:
                check((x-k)*phase>0,'phase threshold sign')
            eps=min(1e-6,(1-x)/30,(x-h)/30)
            check(F(m,a,q,x)>=F(m,a,q,x-eps)-1e-9,'left extremal')
            check(F(m,a,q,x)>=F(m,a,q,x+eps)-1e-9,'right extremal')

for beta in (.05,.25,.5,.8):
    for q in (.3,.5,.8,1.):
        k=math.sqrt(max(0.,1-q*q))
        C=2*q/(math.e*(1-k))
        for m in (30,60,120,240,480):
            a=beta**m
            u=root(m,a,q)
            ratio=m*F(m,a,q,u)/C
            check(.5<ratio<1.1,'asymptotic radius broad')
            check(.6<m*(1-u)<1.1,'asymptotic boundary width broad')
        check(abs(480*F(480,beta**480,q,root(480,beta**480,q))/C-1)<.09,'high-power ratio')

for beta in (.1,.3,.6,.9):
    val=[]
    for m in range(1,55):
        val.append((1-beta**m)/(m+1-beta**m))
    check(all(val[i]>val[i+1] for i in range(53)),'one-way power transition')

print('Finite diagnostic assertions passed:',count)
