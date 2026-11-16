"""Checks for a three-node Szego-kernel determinant-design theorem.

Pure standard-library script. Finite checks support but do not replace proofs.
"""
import cmath
import math
import random
from fractions import Fraction


def rho2(a, b):
    return abs((a-b)/(1-a.conjugate()*b))**2


def determinant3(g):
    a,b,c=g[0]
    d,e,f=g[1]
    h,i,j=g[2]
    return (a*(e*j-f*i)-b*(d*j-f*h)+c*(d*i-e*h)).real


def gram_det(r,s,u,t):
    pts=[r*cmath.exp(1j*(u+t)),r*cmath.exp(1j*(u-t)),complex(s)]
    g=[[math.sqrt(1-abs(z)**2)*math.sqrt(1-abs(w)**2)/(1-z.conjugate()*w) for w in pts] for z in pts]
    return determinant3(g),math.prod(rho2(pts[i],pts[j]) for i in range(3) for j in range(i+1,3))


def scalars(r,s):
    return (r*r+s*s, 1+r*r*s*s, 2*r*s, (1-r*r)**2, 4*r*r)


def equation(r,s,c):
    A,C,b,h,q=scalars(r,s)
    return c*h*(A+b*c)*(C+b*c)-b*(C-A)*(1-c*c)*(h+q*(1-c*c))


def optimum(r,s):
    low,high=0.0,1.0
    assert equation(r,s,low)<0 and equation(r,s,high)>0
    for _ in range(80):
        mid=(low+high)/2
        if equation(r,s,mid)<0:low=mid
        else:high=mid
    c=(low+high)/2
    A,C,b,h,q=scalars(r,s)
    F=q*(1-c*c)/(h+q*(1-c*c))*((A+b*c)/(C+b*c))**2
    return c,F


def exact_reflection_identity():
    rng=random.Random(15)
    for _ in range(400):
        r=Fraction(rng.randrange(1,20),20)
        s=Fraction(rng.randrange(1,20),20)
        c=Fraction(rng.randrange(0,20),20)
        x=Fraction(rng.randrange(-20,21),20)
        A,C,b,h,q=scalars(r,s)
        def Q(L,y):return L*L-b*b*(1-c*c)-2*L*b*c*y+b*b*y*y
        diff=Q(A,-1)*Q(C,x)-Q(A,x)*Q(C,-1)
        fact=b*(A-C)*(x+1)*(b*(A+C)*(x-1)-2*A*C*c+2*b*b*c*(c*c+x-1))
        assert diff==fact and diff>=0
    return 400


def main():
    checks=exact_reflection_identity()
    rng=random.Random(25)
    for _ in range(150):
        r=rng.uniform(.08,.95);s=rng.uniform(.05,.94)
        c,F=optimum(r,s)
        assert 0<c<1
        u=math.pi;t=math.acos(c)
        direct,pair=gram_det(r,s,u,t)
        assert abs(F-direct)<5e-12 and abs(F-pair)<5e-12
        for _ in range(100):
            v=rng.random()*2*math.pi;w=rng.random()*math.pi/2
            observed,pair2=gram_det(r,s,v,w)
            assert abs(observed-pair2)<2e-11
            assert pair2<=F+2e-12
        checks+=102
    for r in [.15,.30,.45,.70,.91]:
        c,_=optimum(r,r)
        assert abs(c-.5)<1e-12
        checks+=1
    for s in [.2,.5,.8]:
        constant=((1+s)**4/(8*s*(1-s*s)))**.25
        for epsilon in [1e-5,1e-6,1e-7,1e-8]:
            c,F=optimum(math.sqrt(1-epsilon),s)
            ratio=math.acos(c)/(constant*epsilon**.25)
            assert abs(ratio-1)<0.025
            assert abs((1-F)/epsilon-2*(1-s)/(1+s))<.05
            checks+=2
    print('PASS:',checks,'finite checks')


if __name__=='__main__':main()
