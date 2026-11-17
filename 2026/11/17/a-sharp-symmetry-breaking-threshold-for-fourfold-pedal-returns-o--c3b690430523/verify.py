"""Reproduce exact inequalities and independent pedal-iteration checks.

Run with: python3 verify.py (standard library only).
All finite checks supplement, and do not establish, the all-parameter proof.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt, isclose
from random import Random


def sqdist_product(h, b, y):
    return (h*h+(b-y)**2)*(h*h+(b+y)**2)


def rho(a, b, x, y):
    N=(a*a-x*x)*(b*b-y*y)
    R=1.0
    for xx,yy in product((-a,a),(-b,b)):
        R*=sqrt((x-xx)**2+(y-yy)**2)
    return N/R


def exact_reduced(a,b,s):
    A=a*a; B=b*b
    return B*(A-s)/(s*s+2*(B-A)*s+(A+B)**2)


def foot(P,U,V):
    dx=V[0]-U[0]; dy=V[1]-U[1]
    t=((P[0]-U[0])*dx+(P[1]-U[1])*dy)/(dx*dx+dy*dy)
    return (U[0]+t*dx, U[1]+t*dy)


def four_pedal(a,b,x,y):
    P=(x,y)
    Z=[(-a,-b),(a,-b),(a,b),(-a,b)]
    for _ in range(4):
        Z=[foot(P,Z[i],Z[(i+1)%4]) for i in range(4)]
    return Z


def assert_close(lhs,rhs, tol=2e-10):
    assert isclose(lhs,rhs, rel_tol=tol,abs_tol=tol), (lhs,rhs)


def run():
    count=0
    for a,b in [(F(1),F(1)),(F(2),F(1)),(F(3),F(1)),(F(9),F(2))]:
        A=a*a; B=b*b
        for m in range(1,10):
            x=a*F(2*m-10,10)
            for j in range(1,10):
                y=b*F(2*j-10,10)
                if not (-a<x<a and -b<y<b):continue
                t=y*y/(b*b)
                for h in (a-x,a+x):
                    H=h*h/(b*b)
                    lhs=sqdist_product(h,b,y)-(1-t)**2*sqdist_product(h,b,F(0))
                    rhs=(b**4)*H*t*(2*H+6-(H+2)*t)
                    assert lhs==rhs and rhs>=0
                    count+=1
                lhs=(a*a-x*x)*(b*b-y*y)
                direct_prod=sqdist_product(a-x,b,y)*sqdist_product(a+x,b,y)
                assert lhs>=0 and direct_prod>0
                count+=1
        for j in range(1,30):
            s=A*F(j,30)
            D=s*s+2*(B-A)*s+(A+B)**2
            lhs= -D-(A-s)*(2*s+2*(B-A))
            rhs=(s-A)**2-B*(4*A+B)
            assert lhs==rhs
            count+=1
    for a,b in [(1,1), (1.5,1), (2,1),(sqrt(2+sqrt(5)),1), (2.1,1), (3,1), (6,1), (20,1)]:
        A=a*a; B=b*b
        U=b*sqrt(4*A+B)
        sstar=max(0.0,A-U)
        xstar=sqrt(sstar)
        max_formula=B*A/(A+B)**2 if sstar==0 else B/(2*(U-B))
        for xx in (-xstar,xstar):
            assert_close(rho(a,b,xx,0),max_formula)
            count+=1
            z=four_pedal(a,b,xx,0)
            q=[(-a,-b),(a,-b),(a,b),(-a,b)]
            w=[]
            for v0,v1 in zip(z,q):
                w.append(complex(v0[0]-xx,v0[1])/complex(v1[0]-xx,v1[1]))
            for wi in w[1:]:assert_close(abs(w[0]-wi),0)
            assert_close(abs(w[0]),max_formula)
            count+=4
    rng=Random(261101247)
    for _ in range(300):
        b=1.;a=rng.uniform(1,15)
        x=rng.uniform(-.98,.98)*a
        y=rng.uniform(-.98,.98)*b
        s=rho(a,b,x,y);s0=rho(a,b,x,0)
        assert s <= s0+1e-13
        assert_close(s0,exact_reduced(a,b,x*x))
        Z=four_pedal(a,b,x,y)
        Q=[(-a,-b),(a,-b),(a,b),(-a,b)]
        ratios=[complex(Z[i][0]-x,Z[i][1]-y)/complex(Q[i][0]-x,Q[i][1]-y) for i in range(4)]
        assert max(abs(u-ratios[0]) for u in ratios) <= 1e-9
        assert_close(abs(ratios[0]),s)
        count+=4
    print(f'PASS {count} deterministic exact/numeric assertions')

if __name__=='__main__':
    run()
