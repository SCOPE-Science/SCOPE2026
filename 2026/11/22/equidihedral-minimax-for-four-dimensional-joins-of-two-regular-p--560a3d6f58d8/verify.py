#!/usr/bin/env python3
"""Numerical structural checks of a geometric identity (not an infinite proof)."""
import math

def dot(x,y):return sum(a*b for a,b in zip(x,y))
def unit(x):
    h=math.sqrt(dot(x,x));return [a/h for a in x]
def normals(m,n,a,b):
    cm,cn=math.cos(math.pi/m),math.cos(math.pi/n)
    def N(i,j):
        x=2*math.pi*(i+0.5)/m;y=2*math.pi*(j+0.5)/n
        return unit([math.cos(x)/(a*cm), math.sin(x)/(a*cm),
                     math.cos(y)/(b*cn),math.sin(y)/(b*cn)])
    return N
for m,n in [(3,4),(4,5),(5,5),(7,11),(13,6)]:
    a0=math.tan(math.pi/m);b0=math.tan(math.pi/n)
    ua,ub=math.sin(math.pi/m)**2,math.sin(math.pi/n)**2
    target=1-2*ua*ub/(ua+ub)
    for factor in [0.6,1.0,1.5]:
        a,b=a0*factor,b0
        N=normals(m,n,a,b)
        U=1/(a*a*math.cos(math.pi/m)**2)
        V=1/(b*b*math.cos(math.pi/n)**2)
        CA=1-2*U*ua/(U+V); CB=1-2*V*ub/(U+V)
        # Each j has m ridges changing i; each i has n ridges changing j.
        types=[]
        for i in range(m):
            for j in range(n):
                xa=dot(N(i,j),N((i+1)%m,j))
                xb=dot(N(i,j),N(i,(j+1)%n))
                assert abs(xa-CA)<1e-12
                assert abs(xb-CB)<1e-12
                types.extend([xa,xb])
        assert len(types)==2*m*n
        if factor==1.0:
            assert abs(CA-CB)<1e-12
            assert abs(CA-target)<1e-12
        else:
            assert max(CA,CB)>target+1e-6
print('PASS: 5 polygon-order pairs, 3 radius ratios each; every ridge tested')
