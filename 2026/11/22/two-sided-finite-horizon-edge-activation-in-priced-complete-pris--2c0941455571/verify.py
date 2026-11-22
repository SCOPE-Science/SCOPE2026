#!/usr/bin/env python3
"""Reproducibility checks for finite-horizon heat-trace allocation on a priced complete prism."""
import math
import numpy as np

def graph(m,a,b):
    L=np.zeros((2*m,2*m),dtype=float)
    for layer in range(2):
        for i in range(m):
            for j in range(i+1,m):
                u=layer*m+i;v=layer*m+j
                L[u,u]+=a;L[v,v]+=a;L[u,v]-=a;L[v,u]-=a
    for i in range(m):
        u=i;v=m+i
        L[u,u]+=b;L[v,v]+=b;L[u,v]-=b;L[v,u]-=b
    return L

def solution(m,r,B,t):
    if r>1 and t <= (m-1)/B*math.log1p(m*(r-1)):
        return B/(m*(m-1)),0.0
    if r<1 and t <= (m*r/(2*B))*math.log((2-r)/r):
        return 0.0,B/(m*r)
    def grad(b):
        a=(B/m-r*b)/(m-1)
        x=m*a*t;y=2*b*t
        return math.log(m*r/2)+np.logaddexp(y,0.0)-np.logaddexp(x,math.log(m-1))
    lo=0.;hi=B/(m*r)
    for _ in range(90):
        mid=(lo+hi)/2
        if grad(mid)>0:hi=mid
        else:lo=mid
    b=(lo+hi)/2
    a=(B/m-r*b)/(m-1)
    return a,b

def run():
    checks=0
    for m in (2,3,4,6,9,16):
        for r in (0.05,0.25,0.8,1,1.02,1.75,3,15):
            for B in (0.7,2.3):
                for t in (0.001,0.2,2.,20.,300.):
                    a,b=solution(m,r,B,t)
                    assert a>=-1e-12 and b>=-1e-12
                    assert abs(m*(m-1)*a+m*r*b-B)<1e-10
                    L=graph(m,max(a,0),max(b,0))
                    ev=np.linalg.eigvalsh(L)
                    theoretical=sorted([0.,2*b]+[m*a]*(m-1)+[m*a+2*b]*(m-1))
                    assert np.allclose(ev,theoretical,atol=1e-9,rtol=1e-9),(m,r,B,t,ev,theoretical)
                    H=np.exp(-t*ev).sum()
                    Hform=(1+(m-1)*math.exp(-m*a*t))*(1+math.exp(-2*b*t))
                    assert abs(H-Hform)<1e-8,(m,r,t,H,Hform)
                    bmax=B/(m*r)
                    for testb in np.linspace(0,bmax,31):
                        testa=(B/m-r*testb)/(m-1)
                        Htest=(1+(m-1)*math.exp(-m*testa*t))*(1+math.exp(-2*testb*t))
                        assert H<=Htest+2e-8,(m,r,B,t,a,b,testb,H,Htest)
                        checks+=1
    # Compare exact threshold side signs and large-horizon balances.
    for m in (2,3,9,40):
        for r in (0.15,0.9,1.1,2.,30.):
            B=1.7
            T=(m*r/(2*B))*math.log((2-r)/r) if r<1 else (m-1)/B*math.log1p(m*(r-1))
            a,b=solution(m,r,B,T/2)
            assert (abs(a)<1e-13 if r<1 else abs(b)<1e-13)
            a,b=solution(m,r,B,2*T)
            assert a>0 and b>0
            checks+=2
    rng=np.random.default_rng(271828)
    for m in (2,3,4,6):
        for r in (0.2,0.8,1.,1.5,4.):
            B=1.4
            for t in (0.15,2.,40.):
                a,b=solution(m,r,B,t)
                best=(1+(m-1)*math.exp(-m*a*t))*(1+math.exp(-2*b*t))
                edges=[]
                for layer in range(2):
                    for i in range(m):
                        for j in range(i+1,m):
                            edges.append((layer*m+i,layer*m+j,1.))
                for i in range(m):edges.append((i,m+i,r))
                for rep in range(10):
                    v=rng.uniform(0.05,1.,len(edges))
                    v*=B/np.dot(v,[e[2] for e in edges])
                    L=np.zeros((2*m,2*m))
                    for (u,w,c),weight in zip(edges,v):
                        L[u,u]+=weight;L[w,w]+=weight;L[u,w]-=weight;L[w,u]-=weight
                    value=sum(math.exp(-t*z) for z in np.linalg.eigvalsh(L))
                    assert value>=best-1e-9,(m,r,t,value,best)
                    checks+=1
    print('VERIFY_OK',checks)
if __name__=='__main__': run()
