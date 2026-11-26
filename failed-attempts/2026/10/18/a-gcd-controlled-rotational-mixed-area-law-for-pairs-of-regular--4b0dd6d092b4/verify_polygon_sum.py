#!/usr/bin/env python3
"""Numerical cross-checks for rotation-dependent areas of regular polygon sums.

Independent brute-force convex hull of all pairwise vertex sums; the proof
of the universal statement is analytical and does not rely on these tests.
Only Python's standard library is required.
"""
from math import cos, sin, pi, gcd, atan2, sqrt, isclose


def hull(points):
    ps = sorted(points)
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    low=[]
    for p in ps:
        while len(low)>=2 and cross(low[-2],low[-1],p)<=1.e-10:
            low.pop()
        low.append(p)
    high=[]
    for p in reversed(ps):
        while len(high)>=2 and cross(high[-2],high[-1],p)<=1.e-10:
            high.pop()
        high.append(p)
    return low[:-1]+high[:-1]


def polygon_sum(n,m,theta,R,S):
    A=[(R*cos(2*pi*i/n),R*sin(2*pi*i/n)) for i in range(n)]
    B=[(S*cos(theta+2*pi*j/m),S*sin(theta+2*pi*j/m)) for j in range(m)]
    boundary=hull([(x+u,y+v) for x,y in A for u,v in B])
    area=abs(sum(x*v-y*u for (x,y),(u,v) in zip(boundary,boundary[1:]+boundary[:1]))/2)
    return area,len(boundary)


def closed_form(n,m,theta,R,S):
    d=gcd(n,m)
    N=n//d
    delta=pi*d/(n*m)
    phase=pi/n-theta+(N-1)*delta
    x=(phase+delta)%(2*delta)-delta
    C=d*R*S*sin(pi/n)*sin(pi/m)/sin(delta)
    B=n*R*R*sin(2*pi/n)/2+m*S*S*sin(2*pi/m)/2
    return B+2*C*cos(x), x, B, C, delta


tests=0
for n in range(3,19):
    for m in range(3,19):
        d=gcd(n,m)
        delta=pi*d/(n*m)
        max_angle=pi/n+(n//d-1)*delta
        for theta in [max_angle,max_angle+delta]:
            brute,verts=polygon_sum(n,m,theta,1.1,.73)
            exact,*_=closed_form(n,m,theta,1.1,.73)
            expected=n+m if theta==max_angle else n+m-d
            assert abs(brute-exact)<1.e-9,(n,m,theta,brute,exact)
            assert verts==expected,(n,m,theta,verts,expected)
            tests+=1
        for j in range(15):
            theta=(j+.137)*pi/(n*m)
            brute,verts=polygon_sum(n,m,theta,1.1,.73)
            exact,*_=closed_form(n,m,theta,1.1,.73)
            assert abs(brute-exact)<1.e-9,(n,m,theta,brute,exact)
            tests+=1
print('VERIFY_OK pair_counts=',16*16,'cases=',tests)
