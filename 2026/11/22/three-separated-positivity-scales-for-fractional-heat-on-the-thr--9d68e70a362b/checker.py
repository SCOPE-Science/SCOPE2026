"""Reproducibility checks for the fractional graph heat kernel on the three-cube."""
import itertools
import math
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import brentq
from scipy.special import lambertw

vertices=list(itertools.product((0,1),repeat=3))
A=np.zeros((8,8))
for i,u in enumerate(vertices):
    for j,v in enumerate(vertices):
        if sum(x!=y for x,y in zip(u,v))==1: A[i,j]=1
L=3*np.eye(8)-A
vals, vec=eigh(L)

def entries(alpha,t):
    a=2**alpha; b=4**alpha; c=6**alpha
    x=math.exp(-a*t); y=math.exp(-b*t); z=math.exp(-c*t)
    return np.array([1+3*x+3*y+z, 1+x-y-z, 1-x-y+z, 1-3*x+3*y-z])/8

def scalar(alpha,t,r):return entries(alpha,t)[r]

def cross(alpha,r,bracket):
    return brentq(lambda t:scalar(alpha,t,r),*bracket,xtol=1e-15)

tests=0
for alpha in (0.25,0.7,1.,1.01,1.25,1.5,1.99,2.,2.01,2.1,2.5,3.,4.,6.,10.):
    rates=np.where(vals<1e-10,0,np.maximum(vals,0)**alpha)
    for t in (1e-4,0.001,0.01,0.05,0.1,0.2,0.5,1.,2.):
        M=(vec*np.exp(-t*rates))@vec.T
        e=entries(alpha,t)
        for i,u in enumerate(vertices):
            for j,v in enumerate(vertices):
                d=sum(x!=y for x,y in zip(u,v))
                assert abs(M[i,j]-e[d])<8e-13,(alpha,t,i,j,M[i,j],e[d])
                tests+=1
        assert abs(M.sum(axis=1).max()-1)<5e-13

root_tests=0
for alpha in (1.1,1.5,1.9,2.,2.01,2.1,3.,4.,6.,10.,15.):
    a=2**alpha; b=4**alpha
    d2=cross(alpha,2,(1e-10,10/a))
    assert scalar(alpha,d2*0.8,2)<0 and scalar(alpha,d2*1.2,2)>0
    if alpha<=2:
        d3=cross(alpha,3,(1e-3/a,10/a))
        assert scalar(alpha,d3*0.8,3)<0 and scalar(alpha,d3*1.2,3)>0
    else:
        d3lo=cross(alpha,3,(1e-4/b,math.log(2)/b))
        d3hi=cross(alpha,3,(math.log(2)/a,4/a))
        assert d3lo<math.log(2)/b<d2<math.log(2)/a<d3hi
        assert scalar(alpha,d3lo*0.5,3)>0
        assert scalar(alpha,(d3lo+d3hi)/2,3)<0
        assert scalar(alpha,d3hi*1.2,3)>0
    root_tests+=1

for alpha in (6.,8.,10.,12.,15.):
    a=2**alpha;b=4**alpha; p=2**alpha
    low=cross(alpha,3,(1e-4/b,math.log(2)/b))
    high=cross(alpha,3,(math.log(2)/a,4/a))
    m=cross(alpha,2,(1e-10,10/a))
    print('alpha',alpha,'b*t_minus',b*low,'b*t2',b*m,'W(p)',float(lambertw(p).real),'a*t_plus',a*high)
print('CHECK_OK',tests,'matrix entries and',root_tests,'root-family checks')
