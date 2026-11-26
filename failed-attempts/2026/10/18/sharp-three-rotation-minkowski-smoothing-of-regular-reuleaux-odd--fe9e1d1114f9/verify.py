"""Reproduce numerical and symbolic-consistency checks for triple rotational Minkowski means.
Run with Python 3.10+; no nonstandard dependencies. The analytic proof is in RESULT.md.
Finite checks here are regressions, not substitutes for quantified proofs.
"""
from math import pi, sin, cos, tan, hypot, atan2
import random


def area_R(n):
    assert n>=3 and n%2
    return pi/2 - n/2*tan(pi/(2*n))


def area_two(n, angle):
    a=pi/n; b=a/2
    s=angle%(2*a)
    d=min(s,2*a-s)
    return pi/2 - (n/4)*(d+(sin(b)+sin(b-d))/cos(b))


def deficit_two(n, angle):
    return pi/4-area_two(n,angle)


def deficit_fourier(n, angle, cutoff=15001):
    x=n*angle
    return sum((1+cos(k*x))/(k*k*(n*n*k*k-1)) for k in range(1,cutoff,2))/pi


def area_three(n, angles):
    d0=deficit_two(n,0)
    dsum=sum(deficit_two(n,angles[i]-angles[j]) for i,j in [(0,1),(0,2),(1,2)])
    return pi/4-(4/9)*dsum+(1/3)*d0


def optimal_area(n):
    return 5*pi/18 - n/6*tan(pi/(6*n))


def intersect_circles(a,b,r=1.0):
    dx=b[0]-a[0];dy=b[1]-a[1];d=hypot(dx,dy)
    if d>2*r+1e-12 or d<1e-10:return []
    x=(a[0]+b[0])/2;y=(a[1]+b[1])/2
    hh=(r*r-d*d/4)**.5
    u=(-dy/d,dx/d)
    return [(x+hh*u[0],y+hh*u[1]),(x-hh*u[0],y-hh*u[1])]


def support_model(n):
    R=1/(2*cos(pi/(2*n)))
    centers=[(R*cos(2*pi*j/n),R*sin(2*pi*j/n)) for j in range(n)]
    corner=[]
    for i in range(n):
        for j in range(i+1,n):
            for q in intersect_circles(centers[i],centers[j]):
                if all(hypot(q[0]-c[0],q[1]-c[1]) <1+1e-8 for c in centers):
                    if all(hypot(q[0]-p[0],q[1]-p[1])>1e-7 for p in corner):corner.append(q)
    assert len(corner)==n, (n,len(corner))
    return centers,corner


def support_point(model,theta):
    centers,corners=model
    u=(cos(theta),sin(theta))
    eligible=corners.copy()
    for c in centers:
        q=(c[0]+u[0],c[1]+u[1])
        if all(hypot(q[0]-v[0],q[1]-v[1])<=1+1e-9 for v in centers):eligible.append(q)
    assert eligible
    return max(eligible,key=lambda p:p[0]*u[0]+p[1]*u[1])


def numerical_boundary_area(n,angles,N=4096):
    model=support_model(n)
    out=[]
    for j in range(N):
        a=2*pi*(j+0.231)/N
        x=y=0
        for d in angles:
            p=support_point(model,a-d)
            x+=(p[0]*cos(d)-p[1]*sin(d))/len(angles)
            y+=(p[0]*sin(d)+p[1]*cos(d))/len(angles)
        out.append((x,y))
    return abs(sum(out[j][0]*out[(j+1)%N][1]-out[j][1]*out[(j+1)%N][0]
                   for j in range(N)))/2


def main():
    rng=random.Random(314159)
    for n in [3,5,7,11,21,51]:
        L=2*pi/n
        for u in [0,1/7,1/3,0.5,2/3,0.9,1]:
            d=L*u/2
            err=abs(deficit_two(n,d)-deficit_fourier(n,d))
            assert err<2e-10,(n,u,err)
        o=optimal_area(n)
        assert abs(area_three(n,[0,L/3,2*L/3])-o)<1e-12
        assert abs(pi/4-o-(pi/4-area_R(3*n))/9)<1e-12
        assert o<pi/4
        for j in range(5000):
            a,b=rng.random()*L,rng.random()*L
            assert area_three(n,[0,a,b])<=o+1e-12, (n,a,b)
        if n>3:
            assert optimal_area(n)>optimal_area(n-2)
    for n in [3,5,7]:
        L=2*pi/n
        for angles in [[0,0,0],[0,L/3,2*L/3],[0,L/5,L*3/5]]:
            numerical=numerical_boundary_area(n,angles,3072)
            exact=area_three(n,angles)
            assert abs(numerical-exact)<2e-4,(n,angles,numerical,exact)
    print('VERIFY_OK Fourier=42 triple_random=30000 boundary=9 asymptotic_and_hierarchy=6')

if __name__=='__main__':main()
