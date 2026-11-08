#!/usr/bin/env python3
"""Standalone finite verification for power regularity constants."""
import cmath,math
from fractions import Fraction as Q

def coefficient(weights):
    weight=[Q(w) for w in weights]
    assert sum(weight)==1
    mu=sum(j*w for j,w in enumerate(weight))
    v=sum(w*(j-mu)**2 for j,w in enumerate(weight))
    assert mu>0 and v>0
    k3=sum(w*(j-mu)**3 for j,w in enumerate(weight))
    k4=sum(w*(j-mu)**4 for j,w in enumerate(weight))-3*v*v
    m2=mu*mu+v
    m3=mu**3+3*mu*v+k3
    return k4/(24*v*v)+m2*m2/(8*mu*mu*v)-m3/(6*mu*v)

def logobjective(weights,n,k,theta):
    w=sum(p*complex(math.cos(j*theta),math.sin(j*theta)) for j,p in enumerate(weights))
    if abs(w)<1e-300 or abs(1-w)<1e-300:
        return -1e300
    return n*math.log(abs(w))+k*math.log(abs(1-w))

def local_maximum(weights,n,k):
    mu=sum(j*p for j,p in enumerate(weights))
    v=sum(p*(j-mu)**2 for j,p in enumerate(weights))
    x0=math.sqrt(k/v)
    lo=max(1e-6,x0*.45)/math.sqrt(n)
    hi=min(math.pi,x0*1.6/math.sqrt(n))
    gr=(math.sqrt(5)-1)/2
    c=hi-gr*(hi-lo);d=lo+gr*(hi-lo)
    fc=logobjective(weights,n,k,c);fd=logobjective(weights,n,k,d)
    for _ in range(100):
        if fc<fd:
            lo=c;c=d;fc=fd;d=lo+gr*(hi-lo);fd=logobjective(weights,n,k,d)
        else:
            hi=d;d=c;fd=fc;c=hi-gr*(hi-lo);fc=logobjective(weights,n,k,c)
    return max(fc,fd)

assert coefficient([Q(1,2),Q(1,2)])==-Q(1,4)
assert coefficient([Q(1,4),Q(1,2),Q(1,4)])==-Q(5,16)
assert coefficient([Q(1,30),Q(14,15),0,0,Q(1,30)])==Q(145661,1401856)
checks=3
# Analytically derived exact optimization identity for a binary law.
for prob in [.2,.5,.8]:
    for stride in [1,3]:
        weights=[0.]*(stride+1);weights[0]=1-prob;weights[stride]=prob
        for k in [1,2,3]:
            for n in [50,200,1000]:
                exact=(prob/(1-prob))**(k/2)*(k/(n+k))**(k/2)*(n/(n+k))**(n/2)
                got=math.exp(local_maximum(weights,n,k))
                assert abs(got/exact-1)<2e-9,(prob,stride,n,k,got,exact)
                checks+=1
# The coefficient and the scaled finite maxima agree asymptotically.
for frac in [[Q(1,4),Q(1,2),Q(1,4)],
             [Q(1,30),Q(14,15),0,0,Q(1,30)]]:
    weights=[float(w) for w in frac]
    b=float(coefficient(frac))
    mu=sum(j*p for j,p in enumerate(weights))
    v=sum(p*(j-mu)**2 for j,p in enumerate(weights))
    for k in [1,2,3]:
        for n in [2000,5000,10000]:
            val=local_maximum(weights,n,k)
            lead=mu**k*(k/(math.e*v))**(k/2)
            observed=n*math.expm1(val+(k/2)*math.log(n)-math.log(lead))
            assert abs(observed-k*k*b)<.1,(frac,k,n,observed,b)
            checks+=1
print('POWER_REGULARITY_CHECK_OK',checks,'finite assertions')
