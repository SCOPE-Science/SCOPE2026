"""Exact checks for perimeter-sampled triangle distance moment identities.
Requires Python 3; no external scientific packages.
"""
from fractions import Fraction as F
from math import sqrt
import random

def moments_by_sides(a,b,c):
    sides=(F(a),F(b),F(c)); P=sum(sides)
    m2_num=sum(x**4/F(6) for x in sides)
    m4_num=sum(x**6/F(15) for x in sides)
    for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
        x,y,z=(sides[t] for t in (i,j,k))
        X,Y=x*x,y*y; Z=X+Y-z*z
        eq2=(X+Y)/3-Z/4
        eq4=(X*X+Y*Y)/5+(Z*Z+2*X*Y)/9-Z*(X+Y)/4
        m2_num+=2*x*y*eq2
        m4_num+=2*x*y*eq4
    return m2_num/P**2,m4_num/P**2

def moments_by_formula(a,b,c):
    a,b,c=F(a),F(b),F(c)
    P=a+b+c; s=P/2
    A2=s*(s-a)*(s-b)*(s-c)
    u=(a*b+b*c+c*a)/P**2
    m2=P*P/24-2*A2/P**2
    m4=P**4/240-A2*(1-F(4,9)*u)
    return m2,m4

def isosceles_extrema(K):
    lo,hi=0.0,1/3
    for _ in range(85):
        mid=(lo+hi)/2
        if mid*mid*(1-2*mid)>K: hi=mid
        else: lo=mid
    alpha=(lo+hi)/2
    lo,hi=1/3,0.5
    for _ in range(85):
        mid=(lo+hi)/2
        if mid*mid*(1-2*mid)>K: lo=mid
        else: hi=mid
    beta=(lo+hi)/2
    e=lambda x:(1+2*x-3*x*x)/4
    return alpha,beta,e(alpha),e(beta)

rng=random.Random(39217)
checks=0
for tri in ((1,1,1),(3,4,5),(13,14,15),(5,5,8),(33,21,13),(1,1,F(1,5))):
    a,b,c=tri
    assert a+b>c and a+c>b and b+c>a
    q1=moments_by_sides(a,b,c)
    q2=moments_by_formula(a,b,c)
    assert q1==q2,(tri,q1,q2)
    P=F(a)+F(b)+F(c);m2,m4=q1
    A2=P**2*(P**2/F(24)-m2)/2
    e2=F(9,4)*(m4-P**4/F(240)+A2)/A2
    e3=m2/P**2-F(1,6)+e2/F(2)
    p=tuple(F(x)/P for x in tri)
    assert e2==sum(p[i]*p[j] for i in range(3) for j in range(i+1,3))
    assert e3==p[0]*p[1]*p[2]
    assert A2>0 and F(0)<m2/P**2<F(1,24)
    checks+=1

for _ in range(750):
    x=rng.random();y=rng.random();z=rng.random();S=x+y+z
    # slack triple gives an arbitrary nondegenerate triangle with perimeter one
    u,v,w=x/S,y/S,z/S
    sides=((1-u)/2,(1-v)/2,(1-w)/2)
    A2=(u*v*w)/16
    e2=sides[0]*sides[1]+sides[1]*sides[2]+sides[2]*sides[0]
    al,be,lower,upper=isosceles_extrema(u*v*w)
    assert lower-1e-12 <=e2<=upper+1e-12,(u,v,w,e2,lower,upper)
    assert al<1/3<be
    checks+=1

# independent Monte Carlo for a scalene triangle, random edge choices by length
sides=(4.0,3.0,5.0)
A=(0.0,0.0); B=(5.0,0.0)
Cx=(3**2+5**2-4**2)/(2*5); Cy=sqrt(3**2-Cx*Cx)
C=(Cx,Cy)
segments=((B,C),(C,A),(A,B))

def draw():
    z=rng.random()*sum(sides)
    idx=0 if z<sides[0] else 1 if z<sides[0]+sides[1] else 2
    t=rng.random()
    lo,hi=segments[idx]
    return (lo[0]+t*(hi[0]-lo[0]), lo[1]+t*(hi[1]-lo[1]))

N=170000
m2emp=m4emp=0
for _ in range(N):
    p=draw();q=draw();d2=(p[0]-q[0])**2+(p[1]-q[1])**2
    m2emp+=d2;m4emp+=d2*d2
m2emp/=N;m4emp/=N
m2,m4=moments_by_formula(*sides)
assert abs(m2emp-float(m2))/float(m2)<0.018
assert abs(m4emp-float(m4))/float(m4)<0.025
print('VERIFY_OK exact_triangle_cases=6 reconstruct_checks=6 sharp_envelope_samples=750 random_pair_trials=170000')
print('m2_true=',m2,'m2_mc=',m2emp,'m4_true=',m4,'m4_mc=',m4emp)
