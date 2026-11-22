#!/usr/bin/env python3
"""Supplementary finite checks for a two-scale Poisson covariance frontier.
These checks do not replace the analytic infinite-dimensional argument.
"""
from math import cos, pi, sqrt
import numpy as np
from scipy.linalg import eigh_tridiagonal

def block(r,s,N,parity):
    ids=np.arange(-N,N+1,dtype=int)
    ids=ids[ids%2==parity]
    d=np.array([(s**abs(int(n)-1)+s**abs(int(n)+1))/(4*r**abs(int(n))) for n in ids])
    b=np.array([s**abs(int(n)+1)/(4*r**((abs(int(n))+abs(int(n)+2))/2)) for n in ids[:-1]])
    return ids,d,b

def norm(r,s,N):
    return max(float(eigh_tridiagonal(*block(r,s,N,p)[1:],eigvals_only=True,select='i',select_range=(len(block(r,s,N,p)[0])-1,len(block(r,s,N,p)[0])-1))[0]) for p in (0,1))

def P(r,t):return (1-r*r)/(1-2*r*cos(t)+r*r)

def K(r,s,g,x,y):return P(r,x-y)-g*cos(x)*cos(y)*P(s,x-y)

def gram(r,s,g,x):return np.array([[K(r,s,g,a,b) for b in x] for a in x])

def run():
    count=0
    for r in (.2,.47,.7,.9):
        for s in (0,.01*r,.2*r,.6*r,.9*r):
            N=70;v=norm(r,s,N)
            q=s/r
            err=((1+s*s)/(4*r)+.5)*(q**N)
            assert v>0
            assert 1/(2*r)-1e-12<=v<=(r+1/r)/2+1e-10
            if s==0:assert abs(v-1/(2*r))<1e-12
            if s>0:
                a=norm(r,s,N//2)
                C=((1+s*s)/(4*r)+.5)*q**(N//2)
                assert a<=v+1e-10 and v<=a+C+1e-10,(r,s,a,v,C)
            count+=4
        for t in (.01,.04):
            s=t*r
            v=norm(r,s,35)
            approx=1/(2*r)+s*s/(4*r)
            assert abs(v-approx)<10*s**4/r**3+1e-11,(r,s,v,approx)
            count+=1
        assert abs(norm(r,r,65)-(r+1/r)/2)<2e-4
        count+=1
        for s in (0,.4*r,.8*r,r):
            g=1/norm(r,s,65) if s<r else 2*r/(1+r*r)
            x=np.linspace(0,2*pi,18,endpoint=False)
            m=gram(r,s,g*(1-1e-4),x)
            assert np.linalg.eigvalsh(m)[0]>-3e-9,(r,s)
            count+=1
        g=2*r/(1+r*r)
        mat=gram(r,r,g,[0,pi])
        assert np.max(abs(mat@np.array([1.,-1.])))<1e-11
        assert np.linalg.eigvalsh(gram(r,r,g*(1+1e-5),[0,pi]))[0]<-1e-10
        count+=2
    print(f"PASS: {count} supplementary assertions across spectral truncation, endpoint limits, small-scale expansion, and Gram tests.")
if __name__=='__main__':run()
