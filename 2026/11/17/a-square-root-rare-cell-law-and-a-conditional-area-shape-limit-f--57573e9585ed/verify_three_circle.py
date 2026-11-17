#!/usr/bin/env python3
"""Independent geometric and numerical checks for three random great circles."""
import math
import random

PI = math.pi

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def norm(x): return math.sqrt(dot(x,x))
def unit(x):
    a=norm(x)
    return tuple(y/a for y in x)
def rand_unit(rng):
    return unit(tuple(rng.gauss(0,1) for _ in range(3)))
def clamp(x): return min(1.0,max(-1.0,x))
def area_by_vertices(m):
    vertices=[]
    for i,j,k in [(0,1,2),(0,2,1),(1,2,0)]:
        v=unit(cross(m[i],m[j]))
        if dot(v,m[k])<0: v=tuple(-x for x in v)
        vertices.append(v)
    v0,v1,v2=vertices
    num=abs(dot(v0,cross(v1,v2)))
    den=1+dot(v0,v1)+dot(v1,v2)+dot(v2,v0)
    return 2*math.atan2(num,den)
def area_formula(m):
    angles=[math.acos(clamp(dot(m[i],m[j]))) for i,j in [(0,1),(0,2),(1,2)]]
    return 2*PI-sum(angles)

def J_midpoint(n):
    # dx dt with y=(1-x)t, z=(1-x)(1-t)
    out=0.0
    for i in range(n):
        x=(i+.5)/n
        sx=math.sin(PI*x)
        for j in range(n):
            y=(1-x)*(j+.5)/n
            z=1-x-y
            out+=(1-x)*math.sqrt(max(0,sx*math.sin(PI*y)*math.sin(PI*z)))
    return out/(n*n)

def main():
    rng=random.Random(271828)
    checked=0
    for _ in range(300):
        ns=[rand_unit(rng) for _ in range(3)]
        for s0,s1 in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            m=[tuple(s0*x for x in ns[0]),tuple(s1*x for x in ns[1]),ns[2]]
            a=area_formula(m)
            b=area_by_vertices(m)
            assert a>0 and abs(a-b)<1e-9,(a,b)
            checked+=1
    j300=J_midpoint(300)
    j600=J_midpoint(600)
    assert abs(j300-j600)<0.0002,(j300,j600)
    assert 0.2180<j600<0.2184
    coeff=2*PI**1.5*j600
    N=140000
    threshold=0.002
    count=0
    for _ in range(N):
        v=[rand_unit(rng) for _ in range(3)]
        a=math.acos(clamp(dot(v[0],v[1])))
        b=math.acos(clamp(dot(v[0],v[2])))
        c=math.acos(clamp(dot(v[1],v[2])))
        pmin=min(2*PI-a-b-c,b+c-a,a+c-b,a+b-c)/(2*PI)
        count+=pmin<threshold
    freq=count/N
    prediction=coeff*math.sqrt(threshold)
    assert abs(freq-prediction)<0.008,(freq,prediction)
    print('PASS: %d independently constructed spherical cells' % checked)
    print('PASS: J at 300/600 grid = %.10f / %.10f' % (j300,j600))
    print('PASS: small-cell event at %.4g: observed %.6f, leading %.6f, N=%d' % (threshold,freq,prediction,N))
    print('Note: Monte Carlo checks are not proofs; the integral and limit follow analytically.')

if __name__=='__main__':main()
