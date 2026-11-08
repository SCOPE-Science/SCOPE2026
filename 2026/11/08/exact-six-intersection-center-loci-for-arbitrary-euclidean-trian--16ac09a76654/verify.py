"""Reproducibility checks for the exact six-intersection-center intervals on a triangle.
Run with Python 3.9+; standard library only. Numerical checks supplement the analytic proof.
"""
from math import acos, cos, sin, hypot, pi, sqrt, isclose
from random import Random


def dist(p, q):
    return hypot(p[0]-q[0], p[1]-q[1])


def dot(u, v):
    return u[0]*v[0]+u[1]*v[1]


def sub(u, v):
    return (u[0]-v[0],u[1]-v[1])


def bounds(T,i):
    A,B,C=T[i],T[(i+1)%3],T[(i+2)%3]
    c,b,a=dist(A,B),dist(A,C),dist(B,C)
    alpha=acos(max(-1,min(1,dot(sub(B,A),sub(C,A))/(c*b))))
    beta=acos(max(-1,min(1,dot(sub(A,B),sub(C,B))/(c*a))))
    if alpha>=pi/2 or beta>=pi/2: return None
    low=max(c*sin(beta)/(1+sin(beta)),c-a/cos(beta))
    high=min(c/(1+sin(alpha)), b/cos(alpha))
    return low,high


def point(T,i,x):
    A,B=T[i],T[(i+1)%3];c=dist(A,B)
    return A[0]+x*(B[0]-A[0])/c, A[1]+x*(B[1]-A[1])/c


def rootcount(T,p,r):
    roots=[]
    for i in range(3):
        A,B=T[i],T[(i+1)%3];v=sub(B,A);w=sub(A,p)
        aa=dot(v,v);bb=2*dot(v,w);cc=dot(w,w)-r*r;dd=bb*bb-4*aa*cc
        if dd<0:continue
        tvals=[(-bb-sqrt(max(0,dd)))/(2*aa),(-bb+sqrt(max(0,dd)))/(2*aa)]
        for t in tvals:
            if 0<=t<=1:
                q=(A[0]+t*v[0],A[1]+t*v[1])
                if all(dist(q,z)>1e-8 for z in roots):roots.append(q)
    return len(roots)


def maxcount(T,p):
    critical={0.0}
    for i in range(3):
        A,B=T[i],T[(i+1)%3];u=sub(B,A);w=sub(p,A)
        critical.add(dist(p,A)); t=dot(w,u)/dot(u,u)
        if 0<t<1:
            foot=(A[0]+t*u[0],A[1]+t*u[1]);critical.add(dist(p,foot))
    ss=sorted(critical);checks=[]
    for u,v in zip(ss,ss[1:]):
        if v-u>1e-10:checks.append((u+v)*0.5)
    checks.extend(ss[1:])
    return max(rootcount(T,p,r) for r in checks) if checks else 0


def main():
    T=[(0,0),(1,0),(0.5,sqrt(3)/2)]
    eq=7-4*sqrt(3)
    intervals=[bounds(T,i) for i in range(3)]
    assert all(abs(hi-lo-eq)<1e-12 for lo,hi in intervals)
    assert abs(eq-4*(1-sqrt(3)/2)**2)<1e-12
    T=[(0,0),(3,0),(0,4)]
    b=bounds(T,1)
    # For the hypotenuse oriented (3,0)->(0,4), the interval length is 65/72.
    assert abs((b[1]-b[0])-65/72)<1e-12,(b,65/72)
    assert bounds(T,0) is None and bounds(T,2) is None
    rng=Random(20261101)
    checked=0
    for j in range(270):
        T=[(0.,0.),(1.,0.),(rng.uniform(-0.5,1.5),10**rng.uniform(-1.7,0.6))]
        for i in range(3):
            c=dist(T[i],T[(i+1)%3]);iv=bounds(T,i)
            samples=[0.08*c,0.29*c,0.52*c,0.78*c,0.93*c]
            if iv is not None:
                lo,hi=iv
                assert 0<=lo<hi<=c,(T,i,iv)
                samples += [(lo+hi)/2,lo*0.4+(lo+hi)/2*0.6,(lo+hi)/2*0.6+hi*0.4]
            for x in samples:
                if not 0<x<c:continue
                predicted=bool(iv and iv[0]+1e-7<x<iv[1]-1e-7)
                if iv and min(abs(x-iv[0]),abs(x-iv[1]))<2e-5:continue
                observed=maxcount(T,point(T,i,x))==6
                assert observed==predicted,(T,i,x,iv,observed)
                checked+=1
    print('VERIFY_OK equilateral_fraction=7-4sqrt3 right_3_4_5=65/864 random_interior_centers=',checked)

if __name__=='__main__':main()
