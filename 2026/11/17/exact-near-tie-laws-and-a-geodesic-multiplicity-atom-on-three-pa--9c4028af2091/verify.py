#!/usr/bin/env python3
"""Independent numerical route-order integration for three-arm metric networks.
Run: python verify.py (requires numpy and scipy).
"""
from itertools import combinations
from math import isclose
import numpy as np
from scipy.integrate import quad

def pair_area(u,v,w,e):
    slopes=np.array([1.,-1.,-1.,1.])
    def row_width(x):
        bases=np.array([x,u+v-x,x+v+w,u-x+w])
        cuts=[0.,v]
        for i in range(4):
            for j in range(i):
                if slopes[i]==slopes[j]: continue
                for offset in (-e,0.,e):
                    y=(bases[j]-bases[i]+offset)/(slopes[i]-slopes[j])
                    if 0<y<v: cuts.append(y)
        cuts=np.array(sorted(cuts))
        mid=(cuts[1:]+cuts[:-1])/2
        route=np.sort(bases[:,None]+slopes[:,None]*mid[None,:],axis=0)
        return float(np.sum((cuts[1:]-cuts[:-1])*(route[1]-route[0]<e)))
    points=[u/2, max(0.,(u-v)/2),min(u,(u+v)/2),
            max(0.,(u-v+w)/2),min(u,(u+v-w)/2),
            max(0.,u/2-w/2),min(u,u/2+w/2),
            max(0.,u/2-e/2),min(u,u/2+e/2),
            max(0.,u/2-w/2-e/2),min(u,u/2-w/2+e/2),
            max(0.,u/2+w/2-e/2),min(u,u/2+w/2+e/2)]
    return quad(row_width,0,u,epsabs=1e-8,limit=170,points=points)[0]

def same_area(u,v,w,e):
    z=sorted((v,w))
    def f(d):
        q=sorted((d,u-d+z[0],u-d+z[1])); return q[1]-q[0]
    cuts={0.,u}
    for t in [(u+z[0])/2,(u+z[1])/2,abs(z[1]-z[0])/2]:
        for offset in (-e/2,0.,e/2):
            v0=t+offset
            if 0<v0<u: cuts.add(v0)
    grid=sorted(cuts)
    area=0.
    for lo,hi in zip(grid,grid[1:]):
        m=(lo+hi)/2
        if f(m)<e: area+=2*u*(hi-lo)-(hi*hi-lo*lo)
    return area

def predicted(a,b,c,e):
    L=a+b+c
    if a<b: n=3*(b+c)*e-1.5*e*e
    elif b<c: n=(c-a)**2/4+(7*a+5*c)*e/2-.75*e*e
    else: n=6*a*e-.75*e*e
    return n/L**2

def integrated(a,b,c,e):
    arms=(a,b,c)
    same=sum(same_area(arms[i],arms[(i+1)%3],arms[(i+2)%3],e)
             for i in range(3))
    pairs=sum(pair_area(arms[i],arms[j],arms[3-i-j],e)
              for i,j in combinations(range(3),2))
    return (same+2*pairs)/(a+b+c)**2

if __name__=='__main__':
    tests=[(.7,1.1,1.8),(.3,.9,2.4),(1.,1.5,1.9),
           (1.,1.,2.),(.7,.7,1.6),(1.,1.,1.)]
    n=0
    for a,b,c in tests:
        threshold=(min(a,b-a) if a<b else min(a,c-a) if b<c else a)/4
        for eps in (threshold/6,threshold/3):
            got=integrated(a,b,c,eps); need=predicted(a,b,c,eps)
            assert abs(got-need)<2e-7,(a,b,c,eps,got,need)
            n+=1
    print('THETA_SIMPLE_ROUTE_GAP_OK cases=',n)
