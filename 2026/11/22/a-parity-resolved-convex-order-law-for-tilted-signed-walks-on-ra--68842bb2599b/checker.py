#!/usr/bin/env python3
"""Exact-rational finite tests of signed-score parity laws; no external packages."""
from fractions import Fraction as Q
from math import comb

def binom(n,p):
    return {2*j-n:Q(comb(n,j))*p**j*(1-p)**(n-j) for j in range(n+1)}

def conv(a,b):
    out={}
    for x,px in a.items():
        for y,py in b.items():out[x+y]=out.get(x+y,Q(0))+px*py
    return out

def mix(a,b,weight):
    return {x:weight*a.get(x,0)+(1-weight)*b.get(x,0) for x in (a.keys()|b.keys())}

def moments(a):
    mean=sum(Q(x)*px for x,px in a.items())
    v=sum(Q(x*x)*px for x,px in a.items())-mean*mean
    return mean,v

def radial(d,t):
    x={0:Q(1)}
    for _ in range(t):
        y={}
        for j,p in x.items():
            if j==0:y[1]=y.get(1,Q(0))+p
            else:
                y[j-1]=y.get(j-1,Q(0))+p/d
                y[j+1]=y.get(j+1,Q(0))+p*Q(d-1,d)
        x=y
    return x

def cat(k):return comb(2*k,k)//(k+1)

def renewal(d,M):
    u=[Q(1)]
    for m in range(1,M+1):
        u.append(sum(Q(cat(j-1)*(d-1)**(j-1),d**(2*j-1))*u[m-j] for j in range(1,m+1)))
    return u

checks=0
for d in range(3,9):
    for p,q in [(Q(1,2),Q(1,9)),(Q(1,2),Q(1,3)),(Q(1,3),Q(1,5)),(Q(2,3),Q(1,3)),(Q(4,5),Q(3,5))]:
        assert 0<q<p<1
        delta=2*(q-p)
        base=binom(d,p)
        full=binom(d,q)
        one=conv(binom(d-1,p),binom(1,q))
        for m in range(1,10):
            u=radial(d,2*m)[0]
            v=radial(d,2*m-1)[1]
            assert v==d*u
            checks+=1
            assert u==renewal(d,m)[-1]
            checks+=1
            even=mix(full,base,u)
            odd=mix(one,base,v)
            assert sum(even.values())==sum(odd.values())==1
            checks+=1
            me,ve=moments(even);mo,vo=moments(odd)
            assert me==mo==d*(2*p-1)+d*u*delta
            checks+=1
            assert ve-vo==d*(d-1)*u*delta*delta and ve>vo
            checks+=1
            # Convex-order hinge test on every possible integer kink.
            for h in range(-d-1,d+2):
                he=sum(max(x-h,0)*p for x,p in even.items())
                ho=sum(max(x-h,0)*p for x,p in odd.items())
                assert he>=ho
                checks+=1
            # Equal mean and unequal second moments preclude either stochastic order.
            cume=cumo=Q(0)
            deltas=[]
            for z in sorted(even):
                cume+=even[z]; cumo+=odd[z]
                deltas.append(cume-cumo)
            assert min(deltas)<0<max(deltas)
            checks+=1
print('EXACT_CHECKS_PASSED',checks)
