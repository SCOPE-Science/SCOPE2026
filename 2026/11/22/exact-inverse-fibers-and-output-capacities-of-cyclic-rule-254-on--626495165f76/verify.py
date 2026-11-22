#!/usr/bin/env python3
"""Exact checks for a radius-one Boolean OR map on cyclic independent binary configurations.
Only standard-library arithmetic; the infinite assertions rest on the written proof.
"""
from collections import Counter
from itertools import product
from math import isclose

P=[1,-2,1,0,-1,1,-1]
Q=[1,-1,0,0,-1,0,-1,-1,-1]

def trace_coeffs(poly,stop):
    coefficients=[0]*(stop+1)
    for n in range(1,stop+1):
        coefficients[n]=-(n*poly[n] if n<len(poly) else 0)
        coefficients[n]-=sum(poly[j]*coefficients[n-j] for j in range(1,min(n,len(poly)-1)+1))
    return coefficients

def compositions23(t):
    if t<0:return 0
    c=[0]*(t+1)
    c[0]=1
    for j in range(1,t+1):
        c[j]=(c[j-2] if j>=2 else 0)+(c[j-3] if j>=3 else 0)
    return c[t]

def perrin(n):
    a=[3,0,2]
    while len(a)<=n:a.append(a[-2]+a[-3])
    return a[n]

def predicted_fiber(y):
    n=len(y)
    if sum(y)==0:return 1
    if sum(y)==n:return perrin(n)
    starts=[i for i in range(n) if y[i] and not y[(i-1)%n]]
    ans=1
    for i in starts:
        length=0
        while y[(i+length)%n]:length+=1
        ans*=compositions23(length-3)
    return ans

def observed(n):
    obs=Counter()
    for x in product((0,1), repeat=n):
        if any(x[i] and x[(i+1)%n] for i in range(n)):continue
        y=tuple(int(x[(i-1)%n] or x[i] or x[(i+1)%n]) for i in range(n))
        obs[y]+=1
    return obs

def main():
    image=trace_coeffs(P,20)
    uniq=trace_coeffs(Q,20)
    image[1]-=1
    for n in range(1,19):
        actual=observed(n)
        assert len(actual)==image[n],(n,len(actual),image[n])
        assert sum(c==1 for c in actual.values())==uniq[n],(n,uniq[n])
        for y in product((0,1),repeat=n):
            p=predicted_fiber(y)
            assert actual[y]==p, (n,y,actual[y],p)
            forbidden=any(tuple(y[(i+j)%n] for j in range(k))==pat
                for pat in ((0,1,0),(0,1,1,0),(0,1,1,1,1,0))
                for k in (len(pat),) for i in range(n))
            assert (p>0)==(not forbidden and (n>1 or y!=(1,))), (n,y,p,forbidden)
    print('VERIFY_OK: direct all-output fibers, forbidden factors, image and singleton counts for n=1..18')
    print('I(1..12):',image[1:13]);print('U(1..12):',uniq[1:13])
if __name__=='__main__':main()
