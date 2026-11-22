#!/usr/bin/env python3
"""Numerical checks for complete epicycloid hull formulas; Python 3 standard library only."""
import cmath, math

def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def hull(points):
    p=sorted(set(points))
    lower=[]
    for q in p:
        while len(lower)>=2 and cross(lower[-2],lower[-1],q)<=0: lower.pop()
        lower.append(q)
    upper=[]
    for q in p[::-1]:
        while len(upper)>=2 and cross(upper[-2],upper[-1],q)<=0: upper.pop()
        upper.append(q)
    return lower[:-1]+upper[:-1]

def area_perim(poly):
    area=0.; per=0.
    for a,b in zip(poly,poly[1:]+poly[:1]):
        area+=a[0]*b[1]-a[1]*b[0]
        per+=math.hypot(a[0]-b[0],a[1]-b[1])
    return abs(area)/2,per

def z(n,t):return (n+1)*cmath.exp(1j*t)-cmath.exp(1j*(n+1)*t)

for n in (1,2,3,4,5,8,13):
    count=1800*n
    pts=[(z(n,2*math.pi*j/count).real,z(n,2*math.pi*j/count).imag) for j in range(count)]
    A,P=area_perim(hull(pts))
    alpha=math.pi/(n+2)
    A_exact=2*math.pi*(n+1)+(n+2)*(n*n+2*n+2)*math.sin(2*alpha)/2
    P_exact=2*(n+2)**2*math.sin(alpha)
    assert 0<=A_exact-A<2e-4, (n,'area',A,A_exact)
    assert 0<=P_exact-P<2e-4, (n,'perimeter',P,P_exact)
    xmax=(n+2)*math.cos(alpha)
    assert max(q[0] for q in pts)<=xmax+1e-10
    for sign in (-1,1):
        w=z(n,sign*alpha)
        assert abs(w.real-xmax)<1e-10
        assert abs(w.imag-sign*n*math.sin(alpha))<1e-10
print('EPICYCLOID_CONVEX_HULL_CHECKS_OK 7')
